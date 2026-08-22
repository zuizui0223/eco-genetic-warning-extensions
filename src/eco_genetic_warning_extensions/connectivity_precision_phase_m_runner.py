"""Per-seed runner and aggregator for high-precision Phase-M connectivity validation."""
from __future__ import annotations

import importlib
import json
from dataclasses import replace
from math import comb
from pathlib import Path
from typing import Any, Iterable

from .connectivity_precision_phase_m import (
    PHASE_M_MIN_BASELINE_ELIGIBLE_PER_SEED,
    PHASE_M_PREFIX_REPLICATES,
    PHASE_M_REPLICATES_PER_SEED,
    expected_prefix,
    phase_m_manifest,
)
from .migration_condition_phase_e import (
    PHASE_E_AREA_REFERENCE,
    PHASE_E_BARRIER_INCREASE,
    PHASE_E_HOLD_GENERATIONS,
    PHASE_E_INTERACTION_KAPPA,
    PHASE_E_KAPPA_MU,
    PHASE_E_MASTER_SEEDS,
    PHASE_E_MIGRATION_RATES,
    PHASE_E_P_STAR,
    PHASE_E_RAMP_GENERATIONS,
)
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


def _exact_mcnemar_two_sided(discordant_a: int, discordant_b: int) -> float:
    n = int(discordant_a) + int(discordant_b)
    if n == 0:
        return 1.0
    k = min(int(discordant_a), int(discordant_b))
    tail = sum(comb(n, i) for i in range(0, k + 1)) / (2**n)
    return min(1.0, 2.0 * tail)


def _regime(rates: tuple[float, ...]) -> str:
    return {
        "warning_evaluable": "R4_highrep",
        "rapid_loss": "R2_highrep",
        "persistence": "R1_highrep",
        "seed_heterogeneous": "R3_highrep",
    }[classify_seed_rates(rates)]


def run_phase_m_seed(upstream_checkout: str | Path, master_seed: int) -> dict[str, Any]:
    if master_seed not in PHASE_E_MASTER_SEEDS:
        raise ValueError("master seed is not one of the locked Phase-E seeds")
    checkout = Path(upstream_checkout)
    if not checkout.exists():
        raise FileNotFoundError(f"upstream checkout does not exist: {checkout}")

    coordinate = MutationCoordinates(kappa_mu=PHASE_E_KAPPA_MU, p_star=PHASE_E_P_STAR)
    driver_rate = coordinate.kappa_mu / 2.0
    total_generations = PHASE_E_RAMP_GENERATIONS + PHASE_E_HOLD_GENERATIONS
    attempts: list[dict[str, Any]] = []

    with _upstream_import_path(checkout):
        audit = importlib.import_module(UPSTREAM_H1_MODULE)
        experiments = importlib.import_module(UPSTREAM_EXPERIMENT_MODULE)
        mutation = importlib.import_module(UPSTREAM_MUTATION_MODULE)
        runtime = importlib.import_module(UPSTREAM_CHAIN_RUNTIME_MODULE)
        calibration = importlib.import_module(UPSTREAM_CALIBRATION_MODULE)
        dynamics = importlib.import_module(UPSTREAM_DYNAMICS_MODULE)
        chain = runtime.chain

        schedule = calibration.RampHoldSchedule(
            PHASE_E_RAMP_GENERATIONS,
            PHASE_E_HOLD_GENERATIONS,
            PHASE_E_BARRIER_INCREASE,
        )
        spec = replace(
            experiments.standard_profile(),
            experiment_id="connectivity_precision_phase_m",
            generations=1,
            replicates=PHASE_M_REPLICATES_PER_SEED,
            master_seed=master_seed,
            area_reference_values=(PHASE_E_AREA_REFERENCE,),
            interaction_feedback_values=(PHASE_E_INTERACTION_KAPPA,),
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
                raise RuntimeError("Phase M requires exactly one H1 cell per master seed")
            cell = cells[0]
            isolated = experiments.scenario_equal_isolated(spec)

            for record in cell.replicates:
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
                base = {
                    "master_seed": master_seed,
                    "replicate": record.replicate_index,
                    "calibration_seed": record.seed,
                    "source_support": record.resolution_stable_h1_loop_mechanism_supported,
                }
                if prepared is None:
                    for migration_rate in PHASE_E_MIGRATION_RATES:
                        attempts.append({
                            **base,
                            "migration_rate": migration_rate,
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
                    raise RuntimeError("Phase-M source requires positive canonical interval")
                barriers = calibration.ramp_and_hold_barrier_schedule(
                    anchor_barrier=anchor_barrier,
                    canonical_interval_width=interval[1] - interval[0],
                    schedule=schedule,
                )

                for migration_rate in PHASE_E_MIGRATION_RATES:
                    scenario = experiments.LandscapeScenario(
                        scenario_id=f"phase_m_m_{migration_rate:.3f}",
                        patch_areas=isolated.patch_areas,
                        migration_rate=migration_rate,
                    )
                    template = chain.parameters_for_cell(
                        spec,
                        scenario,
                        replace(cell.parameters, interaction_barrier=anchor_barrier),
                        seed=record.seed,
                    )
                    projected, invariants = chain.project_full_state(source, template)
                    if not invariants.projection_supported:
                        attempts.append({
                            **base,
                            "migration_rate": migration_rate,
                            "source_prepared": True,
                            "projection_supported": False,
                            "baseline_realised_high_trait_present": None,
                            "eligible_for_trait_loss_denominator": False,
                            "trait_loss_observed_post_baseline": None,
                        })
                        continue
                    result = mutation.simulate_with_symmetric_allele_mutation(
                        replace(projected, generations=total_generations, random_seed=record.seed),
                        mutation_rate=driver_rate,
                        interaction_barrier_schedule=barriers,
                    )
                    baseline_present = any(
                        item.realised_high_trait_occupied for item in result.snapshots[0].trait_occupancy
                    )
                    raw_loss_time = dynamics.tau_trait_realised(result)
                    loss_time = None if raw_loss_time is None or raw_loss_time == 0 else raw_loss_time
                    attempts.append({
                        **base,
                        "migration_rate": migration_rate,
                        "source_prepared": True,
                        "projection_supported": True,
                        "baseline_realised_high_trait_present": baseline_present,
                        "eligible_for_trait_loss_denominator": bool(baseline_present),
                        "trait_loss_observed_post_baseline": None if not baseline_present else loss_time is not None,
                    })

    summaries = []
    prefix_ok = True
    for migration_rate in PHASE_E_MIGRATION_RATES:
        rows = [row for row in attempts if row["migration_rate"] == migration_rate]
        prefix = [row for row in rows if row["replicate"] < PHASE_M_PREFIX_REPLICATES]
        prefix_eligible = [row for row in prefix if row["eligible_for_trait_loss_denominator"]]
        prefix_losses = [row for row in prefix_eligible if row["trait_loss_observed_post_baseline"] is True]
        expected_eligible, expected_losses = expected_prefix(master_seed, migration_rate)
        this_prefix_ok = len(prefix_eligible) == expected_eligible and len(prefix_losses) == expected_losses
        prefix_ok = prefix_ok and this_prefix_ok
        eligible = [row for row in rows if row["eligible_for_trait_loss_denominator"]]
        losses = [row for row in eligible if row["trait_loss_observed_post_baseline"] is True]
        summaries.append({
            "migration_rate": migration_rate,
            "attempted": len(rows),
            "source_prepared": sum(row["source_prepared"] is True for row in rows),
            "projection_supported": sum(row["projection_supported"] is True for row in rows),
            "baseline_eligible": len(eligible),
            "trait_loss": len(losses),
            "trait_loss_rate": None if not eligible else len(losses) / len(eligible),
            "precision_sufficient": len(eligible) >= PHASE_M_MIN_BASELINE_ELIGIBLE_PER_SEED,
            "prefix": {
                "observed_eligible": len(prefix_eligible),
                "observed_losses": len(prefix_losses),
                "expected_eligible": expected_eligible,
                "expected_losses": expected_losses,
                "matches_historical": this_prefix_ok,
            },
        })

    return {
        "stage": "warning-blind connectivity precision validation Phase M",
        "master_seed": master_seed,
        "prefix_audit_passed": prefix_ok,
        "condition_summaries": summaries,
        "attempts": attempts,
    }


def aggregate_phase_m(seed_payloads: Iterable[dict[str, Any]]) -> dict[str, Any]:
    payloads = tuple(seed_payloads)
    if sorted(payload["master_seed"] for payload in payloads) != sorted(PHASE_E_MASTER_SEEDS):
        raise RuntimeError("Phase M aggregate requires exactly the five locked Phase-E master seeds")
    prefix_ok = all(payload["prefix_audit_passed"] for payload in payloads)

    summaries = []
    regime_by_rate: dict[str, str] = {}
    for migration_rate in PHASE_E_MIGRATION_RATES:
        blocks = []
        for payload in sorted(payloads, key=lambda item: item["master_seed"]):
            row = next(item for item in payload["condition_summaries"] if item["migration_rate"] == migration_rate)
            blocks.append((int(row["trait_loss"]), int(row["baseline_eligible"])))
        sufficient = all(eligible >= PHASE_M_MIN_BASELINE_ELIGIBLE_PER_SEED for _, eligible in blocks)
        rates = tuple(losses / eligible for losses, eligible in blocks)
        regime = "insufficient_precision" if not sufficient else _regime(rates)
        pooled_losses = sum(losses for losses, _ in blocks)
        pooled_eligible = sum(eligible for _, eligible in blocks)
        pooled = pooled_losses / pooled_eligible
        statistic, df, p_value = pearson_equal_rate_test(tuple(blocks))
        reference_pass = ensemble_gate_pass_probability(tuple(eligible for _, eligible in blocks), pooled)
        key = f"{migration_rate:.3f}"
        regime_by_rate[key] = regime
        summaries.append({
            "migration_rate": migration_rate,
            "blocks": [
                {"master_seed": seed, "losses": losses, "eligible": eligible, "rate": losses / eligible}
                for seed, (losses, eligible) in zip(PHASE_E_MASTER_SEEDS, blocks, strict=True)
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

    # Aggregate paired switches across all five historical master seeds using per-trajectory rows.
    paired = []
    by_seed_rep_rate: dict[tuple[int, int, float], dict[str, Any]] = {}
    for payload in payloads:
        for row in payload["attempts"]:
            by_seed_rep_rate[(row["master_seed"], row["replicate"], float(row["migration_rate"]))] = row
    for migration_rate in PHASE_E_MIGRATION_RATES[1:]:
        counts = {"comparable_pair_count": 0, "loss_to_no_loss": 0, "no_loss_to_loss": 0, "same_loss": 0, "same_no_loss": 0}
        for master_seed in PHASE_E_MASTER_SEEDS:
            for replicate in range(PHASE_M_REPLICATES_PER_SEED):
                ref = by_seed_rep_rate[(master_seed, replicate, 0.0)]
                row = by_seed_rep_rate[(master_seed, replicate, migration_rate)]
                if not (ref["eligible_for_trait_loss_denominator"] and row["eligible_for_trait_loss_denominator"]):
                    continue
                counts["comparable_pair_count"] += 1
                ref_loss = ref["trait_loss_observed_post_baseline"] is True
                new_loss = row["trait_loss_observed_post_baseline"] is True
                if ref_loss and not new_loss:
                    counts["loss_to_no_loss"] += 1
                elif not ref_loss and new_loss:
                    counts["no_loss_to_loss"] += 1
                elif ref_loss and new_loss:
                    counts["same_loss"] += 1
                else:
                    counts["same_no_loss"] += 1
        p_mcnemar = _exact_mcnemar_two_sided(counts["loss_to_no_loss"], counts["no_loss_to_loss"])
        paired.append({
            "migration_rate": migration_rate,
            "reference_migration_rate": 0.0,
            **counts,
            "exact_mcnemar_two_sided_p": p_mcnemar,
            "paired_loss_probability_direction": (
                "higher_at_migration" if counts["no_loss_to_loss"] > counts["loss_to_no_loss"] else
                "lower_at_migration" if counts["no_loss_to_loss"] < counts["loss_to_no_loss"] else "balanced"
            ),
        })

    historical_r3_persists = any(regime_by_rate[key] == "R3_highrep" for key in ("0.100", "0.200"))
    if not prefix_ok:
        decision = "prefix_reproducibility_failed"
    elif any(value == "insufficient_precision" for value in regime_by_rate.values()):
        decision = "insufficient_precision"
    elif historical_r3_persists:
        decision = "historical_r3_persists_at_high_precision"
    else:
        decision = "historical_r3_disappears_at_high_precision"

    return {
        "stage": "warning-blind connectivity precision validation Phase M",
        "manifest": phase_m_manifest(),
        "prefix_audit_passed": prefix_ok,
        "decision": decision,
        "regime_by_migration_rate": regime_by_rate,
        "migration_condition_summaries": summaries,
        "paired_loss_status_vs_isolation": paired,
        "per_seed_payloads": list(payloads),
    }


def load_and_aggregate_phase_m(paths: Iterable[str | Path]) -> dict[str, Any]:
    payloads = [json.loads(Path(path).read_text(encoding="utf-8")) for path in paths]
    return aggregate_phase_m(payloads)
