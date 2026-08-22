"""High-precision per-seed runner and aggregator for Phase K."""
from __future__ import annotations

import importlib
import json
from dataclasses import replace
from pathlib import Path
from typing import Any, Iterable

from .explicit_rewiring_phase_h import (
    PHASE_H_AREA_REFERENCE,
    PHASE_H_BARRIER_INCREASE,
    PHASE_H_HOLD_GENERATIONS,
    PHASE_H_INTERACTION_KAPPA,
    PHASE_H_KAPPA_MU,
    PHASE_H_MIGRATION_RATE,
    PHASE_H_P_STAR,
    PHASE_H_RAMP_GENERATIONS,
    post_loss_edges,
    support_multiplier,
)
from .explicit_rewiring_phase_h_runner import patched_interaction_support_schedule
from .mutation_coordinates import MutationCoordinates
from .protocol002_condition_map import classify_seed_rates
from .protocol002_source_grid import SOURCE_HOLD_GENERATIONS, SOURCE_NESTED_BARRIER_GRIDS, SOURCE_STAGE_GENERATIONS
from .protocol002_stage1_projection_pilot import UPSTREAM_CHAIN_RUNTIME_MODULE
from .protocol002_stage2_smoke import UPSTREAM_CALIBRATION_MODULE, UPSTREAM_DYNAMICS_MODULE
from .protocol002_upstream_h1_asym_smoke import (
    UPSTREAM_EXPERIMENT_MODULE,
    UPSTREAM_H1_MODULE,
    UPSTREAM_MUTATION_MODULE,
    _upstream_import_path,
    patched_protocol002_mutation_runner,
)
from .r4_gate_validity_phase_j import ensemble_gate_pass_probability, pearson_equal_rate_test
from .r4_precision_phase_k import (
    PHASE_K_MIN_BASELINE_ELIGIBLE_PER_SEED,
    PHASE_K_PREFIX_REPLICATES,
    PHASE_K_REPLICATES_PER_SEED,
    expected_prefix,
    phase_k_manifest,
    phase_k_seed_families,
)

CONDITIONS = ("intact_control", "partner_loss_no_rescue")


def _family_for_seed(master_seed: int) -> str:
    for family, seeds in phase_k_seed_families().items():
        if master_seed in seeds:
            return family
    raise ValueError("master seed is not in Phase K")


def _support_schedule(condition: str, replicate_index: int, generations: int) -> tuple[float, ...]:
    """Replay the exact Phase-H / Phase-I effective-support closure.

    The historical partner-loss condition does not use a constant 0.75 support
    multiplier.  Losing primary partner ``replicate_index mod 4`` yields one of
    four trait-match-weighted support levels.  Those four levels are balanced
    across each 20-replicate prefix and average to 0.75, but individual
    trajectories must retain their exact replicate-specific multiplier.
    """
    if condition == "intact_control":
        value = 1.0
    elif condition == "partner_loss_no_rescue":
        value = support_multiplier(post_loss_edges(replicate_index))
    else:
        raise ValueError("unknown Phase-K condition")
    return tuple(value for _ in range(generations))


def run_phase_k_seed(upstream_checkout: str | Path, master_seed: int) -> dict[str, Any]:
    checkout = Path(upstream_checkout)
    if not checkout.exists():
        raise FileNotFoundError(f"upstream checkout does not exist: {checkout}")
    family = _family_for_seed(master_seed)
    coordinate = MutationCoordinates(kappa_mu=PHASE_H_KAPPA_MU, p_star=PHASE_H_P_STAR)
    driver_rate = coordinate.kappa_mu / 2.0
    total_generations = PHASE_H_RAMP_GENERATIONS + PHASE_H_HOLD_GENERATIONS
    attempts: list[dict[str, Any]] = []

    with _upstream_import_path(checkout):
        audit = importlib.import_module(UPSTREAM_H1_MODULE)
        experiments = importlib.import_module(UPSTREAM_EXPERIMENT_MODULE)
        mutation = importlib.import_module(UPSTREAM_MUTATION_MODULE)
        runtime = importlib.import_module(UPSTREAM_CHAIN_RUNTIME_MODULE)
        calibration = importlib.import_module(UPSTREAM_CALIBRATION_MODULE)
        dynamics = importlib.import_module(UPSTREAM_DYNAMICS_MODULE)
        chain = runtime.chain

        deterioration = calibration.RampHoldSchedule(
            PHASE_H_RAMP_GENERATIONS,
            PHASE_H_HOLD_GENERATIONS,
            PHASE_H_BARRIER_INCREASE,
        )
        spec = replace(
            experiments.standard_profile(),
            experiment_id="r4_precision_phase_k",
            generations=1,
            replicates=PHASE_K_REPLICATES_PER_SEED,
            master_seed=master_seed,
            area_reference_values=(PHASE_H_AREA_REFERENCE,),
            interaction_feedback_values=(PHASE_H_INTERACTION_KAPPA,),
            interaction_barrier_values=(0.5,),
        )

        with patched_protocol002_mutation_runner(mutation, coordinate):
            cells = audit.run_finite_h1_boundary_resolution_audit(
                spec,
                endpoint_padding_fraction=0.5,
                stage_generations=SOURCE_STAGE_GENERATIONS,
                nested_barrier_points=SOURCE_NESTED_BARRIER_GRIDS,
                interaction_separation_threshold=0.05,
                maximum_normalized_bracket_width=0.03,
            )
            if len(cells) != 1:
                raise RuntimeError("Phase K requires exactly one H1 cell per master seed")
            cell = cells[0]
            isolated = experiments.scenario_equal_isolated(spec)
            scenario = experiments.LandscapeScenario(
                scenario_id="equal_fragmented_r4_precision_phase_k",
                patch_areas=isolated.patch_areas,
                migration_rate=PHASE_H_MIGRATION_RATE,
            )

            for record in cell.replicates:
                base = {
                    "seed_family": family,
                    "master_seed": master_seed,
                    "replicate": record.replicate_index,
                    "calibration_seed": record.seed,
                    "source_support": record.resolution_stable_h1_loop_mechanism_supported,
                }
                prepared = chain._prepare_mutation_high_state(
                    driver_rate,
                    spec,
                    cell,
                    record,
                    endpoint_padding_fraction=0.5,
                    stage_generations=SOURCE_STAGE_GENERATIONS,
                    hold_generations=SOURCE_HOLD_GENERATIONS,
                    interaction_separation_threshold=0.05,
                )
                if prepared is None:
                    for condition in CONDITIONS:
                        attempts.append({
                            **base,
                            "condition": condition,
                            "effective_support_multiplier": _support_schedule(condition, record.replicate_index, 1)[0],
                            "source_prepared": False,
                            "projection_supported": None,
                            "baseline_realised_high_trait_present": None,
                            "eligible_for_trait_loss_denominator": False,
                            "trait_loss_observed_post_baseline": None,
                        })
                    continue

                source, anchor_barrier = prepared
                interval = cell.canonical_bistable_barrier_interval
                if interval is None or interval[1] <= interval[0]:
                    raise RuntimeError("Phase-K source requires positive canonical interval")
                barriers = calibration.ramp_and_hold_barrier_schedule(
                    anchor_barrier=anchor_barrier,
                    canonical_interval_width=interval[1] - interval[0],
                    schedule=deterioration,
                )
                template = chain.parameters_for_cell(
                    spec,
                    scenario,
                    replace(cell.parameters, interaction_barrier=anchor_barrier),
                    seed=record.seed,
                )
                projected, invariants = chain.project_full_state(source, template)

                for condition in CONDITIONS:
                    multipliers = _support_schedule(condition, record.replicate_index, total_generations)
                    support_value = multipliers[0]
                    if not invariants.projection_supported:
                        attempts.append({
                            **base,
                            "condition": condition,
                            "effective_support_multiplier": support_value,
                            "source_prepared": True,
                            "projection_supported": False,
                            "baseline_realised_high_trait_present": None,
                            "eligible_for_trait_loss_denominator": False,
                            "trait_loss_observed_post_baseline": None,
                        })
                        continue
                    with patched_interaction_support_schedule(
                        mutation,
                        multipliers,
                        patch_count=len(projected.patch_areas),
                    ) as state:
                        result = mutation.simulate_with_symmetric_allele_mutation(
                            replace(projected, generations=total_generations, random_seed=record.seed),
                            mutation_rate=driver_rate,
                            interaction_barrier_schedule=barriers,
                        )
                    if state["calls"] != total_generations * len(projected.patch_areas):
                        raise RuntimeError("Phase-K support schedule call count mismatch")
                    baseline_present = any(
                        item.realised_high_trait_occupied for item in result.snapshots[0].trait_occupancy
                    )
                    raw_loss_time = dynamics.tau_trait_realised(result)
                    loss_time = None if raw_loss_time is None or raw_loss_time == 0 else raw_loss_time
                    attempts.append({
                        **base,
                        "condition": condition,
                        "effective_support_multiplier": support_value,
                        "source_prepared": True,
                        "projection_supported": True,
                        "baseline_realised_high_trait_present": baseline_present,
                        "eligible_for_trait_loss_denominator": bool(baseline_present),
                        "trait_loss_observed_post_baseline": None if not baseline_present else loss_time is not None,
                    })

    summaries = []
    prefix_ok = True
    for condition in CONDITIONS:
        rows = [row for row in attempts if row["condition"] == condition]
        if len(rows) != PHASE_K_REPLICATES_PER_SEED:
            raise RuntimeError("Phase-K condition row count mismatch")
        prefix = [row for row in rows if row["replicate"] < PHASE_K_PREFIX_REPLICATES]
        prefix_eligible = [row for row in prefix if row["eligible_for_trait_loss_denominator"]]
        prefix_losses = [row for row in prefix_eligible if row["trait_loss_observed_post_baseline"] is True]
        expected_eligible, expected_losses = expected_prefix(master_seed, condition)
        this_prefix_ok = len(prefix_eligible) == expected_eligible and len(prefix_losses) == expected_losses
        prefix_ok = prefix_ok and this_prefix_ok

        eligible = [row for row in rows if row["eligible_for_trait_loss_denominator"]]
        losses = [row for row in eligible if row["trait_loss_observed_post_baseline"] is True]
        support_levels = sorted({round(float(row["effective_support_multiplier"]), 15) for row in rows})
        summaries.append({
            "condition": condition,
            "attempted": len(rows),
            "source_prepared": sum(row["source_prepared"] is True for row in rows),
            "projection_supported": sum(row["projection_supported"] is True for row in rows),
            "baseline_eligible": len(eligible),
            "trait_loss": len(losses),
            "trait_loss_rate": None if not eligible else len(losses) / len(eligible),
            "precision_sufficient": len(eligible) >= PHASE_K_MIN_BASELINE_ELIGIBLE_PER_SEED,
            "effective_support_levels": support_levels,
            "prefix": {
                "observed_eligible": len(prefix_eligible),
                "observed_losses": len(prefix_losses),
                "expected_eligible": expected_eligible,
                "expected_losses": expected_losses,
                "matches_historical": this_prefix_ok,
            },
        })

    return {
        "stage": "warning-blind R4 precision validation Phase K",
        "master_seed": master_seed,
        "seed_family": family,
        "replicates_per_seed": PHASE_K_REPLICATES_PER_SEED,
        "prefix_audit_passed": prefix_ok,
        "condition_summaries": summaries,
    }


def _historical_regime_from_rates(rates: tuple[float, ...]) -> str:
    return {
        "warning_evaluable": "R4_highrep",
        "rapid_loss": "R2_highrep",
        "persistence": "R1_highrep",
        "seed_heterogeneous": "R3_highrep",
    }[classify_seed_rates(rates)]


def aggregate_phase_k(seed_payloads: Iterable[dict[str, Any]]) -> dict[str, Any]:
    payloads = tuple(seed_payloads)
    expected_seeds = tuple(seed for family in phase_k_seed_families().values() for seed in family)
    if sorted(payload["master_seed"] for payload in payloads) != sorted(expected_seeds):
        raise RuntimeError("Phase-K aggregate must contain exactly the ten locked master seeds")
    prefix_audit_passed = all(payload["prefix_audit_passed"] for payload in payloads)

    family_summaries = []
    family_loss_regimes = {}
    for family, seeds in phase_k_seed_families().items():
        family_payloads = [payload for payload in payloads if payload["master_seed"] in seeds]
        for condition in CONDITIONS:
            blocks = []
            for payload in sorted(family_payloads, key=lambda item: item["master_seed"]):
                row = next(item for item in payload["condition_summaries"] if item["condition"] == condition)
                blocks.append((int(row["trait_loss"]), int(row["baseline_eligible"])))
            sufficient = all(eligible >= PHASE_K_MIN_BASELINE_ELIGIBLE_PER_SEED for _, eligible in blocks)
            rates = tuple(losses / eligible for losses, eligible in blocks)
            regime = "insufficient_precision" if not sufficient else _historical_regime_from_rates(rates)
            pooled_losses = sum(losses for losses, _ in blocks)
            pooled_eligible = sum(eligible for _, eligible in blocks)
            pooled = pooled_losses / pooled_eligible
            statistic, df, p_value = pearson_equal_rate_test(tuple(blocks))
            reference_pass = ensemble_gate_pass_probability(tuple(eligible for _, eligible in blocks), pooled)
            family_summaries.append({
                "seed_family": family,
                "condition": condition,
                "blocks": [
                    {"master_seed": seed, "losses": losses, "eligible": eligible, "rate": losses / eligible}
                    for seed, (losses, eligible) in zip(sorted(seeds), blocks, strict=True)
                ],
                "pooled_loss_rate": pooled,
                "historical_gate_regime_at_full_precision": regime,
                "precision_sufficient": sufficient,
                "pearson_equal_rate_statistic": statistic,
                "pearson_equal_rate_df": df,
                "pearson_equal_rate_p_value": p_value,
                "homogeneous_reference_gate_pass_probability": reference_pass,
                "homogeneous_reference_gate_fail_probability": 1.0 - reference_pass,
            })
            if condition == "partner_loss_no_rescue":
                family_loss_regimes[family] = regime

    if not prefix_audit_passed:
        decision = "prefix_reproducibility_failed"
    elif any(regime == "insufficient_precision" for regime in family_loss_regimes.values()):
        decision = "insufficient_precision"
    elif len(set(family_loss_regimes.values())) == 1:
        decision = f"precision_convergence:{next(iter(family_loss_regimes.values()))}"
    else:
        decision = "between_ensemble_instability_persists"

    return {
        "stage": "warning-blind R4 precision validation Phase K",
        "manifest": phase_k_manifest(),
        "prefix_audit_passed": prefix_audit_passed,
        "decision": decision,
        "partner_loss_regime_by_seed_family": family_loss_regimes,
        "family_condition_summaries": family_summaries,
        "per_seed_payloads": list(payloads),
    }


def load_and_aggregate_phase_k(paths: Iterable[str | Path]) -> dict[str, Any]:
    payloads = [json.loads(Path(path).read_text(encoding="utf-8")) for path in paths]
    return aggregate_phase_k(payloads)
