"""Per-seed runner and aggregator for process-resolved movement Phase R."""
from __future__ import annotations

import importlib
import json
from dataclasses import replace
from math import comb, exp, factorial
from pathlib import Path
from typing import Any, Iterable

from .migration_condition_phase_e import (
    PHASE_E_AREA_REFERENCE,
    PHASE_E_BARRIER_INCREASE,
    PHASE_E_HOLD_GENERATIONS,
    PHASE_E_INTERACTION_KAPPA,
    PHASE_E_KAPPA_MU,
    PHASE_E_MASTER_SEEDS,
    PHASE_E_P_STAR,
    PHASE_E_RAMP_GENERATIONS,
)
from .mutation_coordinates import MutationCoordinates
from .process_resolved_movement import simulate_with_process_resolved_dispersal
from .process_resolved_movement_phase_r import (
    PHASE_R_CONDITIONS,
    PHASE_R_INDIVIDUAL_DISPERSAL_RATE,
    PHASE_R_LEGACY_MIGRATION_RATE,
    PHASE_R_MIN_BASELINE_ELIGIBLE_PER_SEED,
    PHASE_R_PHASE_M_BLOCKS,
    PHASE_R_PREFIX_COUNTS,
    PHASE_R_REPLICATES_PER_SEED,
    phase_r_manifest,
)
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


def _regime(rates: tuple[float, ...]) -> str:
    return {
        "warning_evaluable": "R4_highrep",
        "rapid_loss": "R2_highrep",
        "persistence": "R1_highrep",
        "seed_heterogeneous": "R3_highrep",
    }[classify_seed_rates(rates)]


def _pooled_rate(blocks: tuple[tuple[int, int], ...]) -> float:
    losses = sum(losses for losses, _ in blocks)
    eligible = sum(eligible for _, eligible in blocks)
    if eligible < 1:
        raise ValueError("pooled eligible count must be positive")
    return losses / eligible


def _chi_square_sf_even_df(statistic: float, df: int) -> float:
    if statistic < 0.0 or df < 2 or df % 2:
        raise ValueError("requires nonnegative statistic and positive even df")
    x = statistic / 2.0
    return exp(-x) * sum((x**j) / factorial(j) for j in range(df // 2))


def pearson_equal_rate_test(blocks: tuple[tuple[int, int], ...]) -> tuple[float, int, float]:
    if len(blocks) < 2:
        raise ValueError("at least two blocks are required")
    pooled = _pooled_rate(blocks)
    if pooled <= 0.0 or pooled >= 1.0:
        raise ValueError("pooled rate must lie inside (0,1)")
    statistic = 0.0
    for losses, eligible in blocks:
        nonlosses = eligible - losses
        expected_loss = eligible * pooled
        expected_nonloss = eligible * (1.0 - pooled)
        statistic += ((losses - expected_loss) ** 2) / expected_loss
        statistic += ((nonlosses - expected_nonloss) ** 2) / expected_nonloss
    df = len(blocks) - 1
    return statistic, df, _chi_square_sf_even_df(statistic, df)


def _exact_mcnemar_two_sided(a: int, b: int) -> float:
    n = int(a) + int(b)
    if n == 0:
        return 1.0
    k = min(int(a), int(b))
    tail = sum(comb(n, i) for i in range(k + 1)) / (2**n)
    return min(1.0, 2.0 * tail)


def _outcome_row(base: dict[str, Any], condition: str, result: Any, dynamics: Any, **extra: Any) -> dict[str, Any]:
    baseline_present = any(item.realised_high_trait_occupied for item in result.snapshots[0].trait_occupancy)
    raw_loss_time = dynamics.tau_trait_realised(result)
    loss_time = None if raw_loss_time is None or raw_loss_time == 0 else raw_loss_time
    return {
        **base,
        "condition": condition,
        "source_prepared": True,
        "projection_supported": True,
        "baseline_realised_high_trait_present": baseline_present,
        "eligible_for_trait_loss_denominator": bool(baseline_present),
        "trait_loss_time_post_baseline": loss_time,
        "trait_loss_observed_post_baseline": None if not baseline_present else loss_time is not None,
        **extra,
    }


def run_phase_r_seed(upstream_checkout: str | Path, master_seed: int) -> dict[str, Any]:
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
            experiment_id="process_resolved_movement_phase_r",
            generations=1,
            replicates=PHASE_R_REPLICATES_PER_SEED,
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
                raise RuntimeError("Phase R requires exactly one H1 cell per master seed")
            cell = cells[0]
            isolated = experiments.scenario_equal_isolated(spec)

            for record in cell.replicates:
                base = {
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
                    for condition in PHASE_R_CONDITIONS:
                        attempts.append({
                            **base,
                            "condition": condition,
                            "source_prepared": False,
                            "projection_supported": None,
                            "baseline_realised_high_trait_present": None,
                            "eligible_for_trait_loss_denominator": False,
                            "trait_loss_time_post_baseline": None,
                            "trait_loss_observed_post_baseline": None,
                        })
                    continue

                source, anchor_barrier = prepared
                interval = cell.canonical_bistable_barrier_interval
                if interval is None or interval[1] <= interval[0]:
                    raise RuntimeError("Phase-R source requires a positive canonical interval")
                barriers = calibration.ramp_and_hold_barrier_schedule(
                    anchor_barrier=anchor_barrier,
                    canonical_interval_width=interval[1] - interval[0],
                    schedule=schedule,
                )

                scenarios = {
                    "no_connectivity": experiments.LandscapeScenario(
                        scenario_id="phase_r_no_connectivity",
                        patch_areas=isolated.patch_areas,
                        migration_rate=0.0,
                    ),
                    "allele_only_m010": experiments.LandscapeScenario(
                        scenario_id="phase_r_allele_only_m010",
                        patch_areas=isolated.patch_areas,
                        migration_rate=PHASE_R_LEGACY_MIGRATION_RATE,
                    ),
                }
                projected_by_condition: dict[str, Any] = {}
                projection_ok = True
                for condition, scenario in scenarios.items():
                    template = chain.parameters_for_cell(
                        spec,
                        scenario,
                        replace(cell.parameters, interaction_barrier=anchor_barrier),
                        seed=record.seed,
                    )
                    projected, invariants = chain.project_full_state(source, template)
                    if not invariants.projection_supported:
                        projection_ok = False
                    projected_by_condition[condition] = projected

                if not projection_ok:
                    for condition in PHASE_R_CONDITIONS:
                        attempts.append({
                            **base,
                            "condition": condition,
                            "source_prepared": True,
                            "projection_supported": False,
                            "baseline_realised_high_trait_present": None,
                            "eligible_for_trait_loss_denominator": False,
                            "trait_loss_time_post_baseline": None,
                            "trait_loss_observed_post_baseline": None,
                        })
                    continue

                no_parameters = replace(
                    projected_by_condition["no_connectivity"],
                    generations=total_generations,
                    random_seed=record.seed,
                )
                legacy_parameters = replace(
                    projected_by_condition["allele_only_m010"],
                    generations=total_generations,
                    random_seed=record.seed,
                )

                no_result = mutation.simulate_with_symmetric_allele_mutation(
                    no_parameters,
                    mutation_rate=driver_rate,
                    interaction_barrier_schedule=barriers,
                )
                legacy_result = mutation.simulate_with_symmetric_allele_mutation(
                    legacy_parameters,
                    mutation_rate=driver_rate,
                    interaction_barrier_schedule=barriers,
                )
                process = simulate_with_process_resolved_dispersal(
                    dynamics,
                    mutation,
                    no_parameters,
                    coordinate,
                    dispersal_rate=PHASE_R_INDIVIDUAL_DISPERSAL_RATE,
                    interaction_barrier_schedule=barriers,
                    movement_seed=record.seed,
                )

                attempts.append(_outcome_row(base, "no_connectivity", no_result, dynamics))
                attempts.append(_outcome_row(base, "allele_only_m010", legacy_result, dynamics))
                attempts.append(_outcome_row(
                    base,
                    "individual_dispersal_d010",
                    process.simulation,
                    dynamics,
                    total_movers=process.diagnostics.total_movers,
                    realised_movement_fraction=process.diagnostics.realised_movement_fraction,
                ))

    prefix_ok = True
    baseline_pairing_ok = True
    condition_summaries = []
    by_key = {(row["replicate"], row["condition"]): row for row in attempts}
    for replicate in range(PHASE_R_REPLICATES_PER_SEED):
        no = by_key[(replicate, "no_connectivity")]
        process = by_key[(replicate, "individual_dispersal_d010")]
        if no["eligible_for_trait_loss_denominator"] != process["eligible_for_trait_loss_denominator"]:
            baseline_pairing_ok = False

    for condition in PHASE_R_CONDITIONS:
        rows = [row for row in attempts if row["condition"] == condition]
        eligible = [row for row in rows if row["eligible_for_trait_loss_denominator"]]
        losses = [row for row in eligible if row["trait_loss_observed_post_baseline"] is True]
        summary = {
            "condition": condition,
            "attempted": len(rows),
            "source_prepared": sum(row["source_prepared"] is True for row in rows),
            "projection_supported": sum(row["projection_supported"] is True for row in rows),
            "baseline_eligible": len(eligible),
            "trait_loss": len(losses),
            "trait_loss_rate": None if not eligible else len(losses) / len(eligible),
            "precision_sufficient": len(eligible) >= PHASE_R_MIN_BASELINE_ELIGIBLE_PER_SEED,
        }
        if condition in PHASE_R_PREFIX_COUNTS[master_seed]:
            prefix = [row for row in rows if row["replicate"] < 20]
            pe = [row for row in prefix if row["eligible_for_trait_loss_denominator"]]
            pl = [row for row in pe if row["trait_loss_observed_post_baseline"] is True]
            expected_eligible, expected_losses = PHASE_R_PREFIX_COUNTS[master_seed][condition]
            match = len(pe) == expected_eligible and len(pl) == expected_losses
            prefix_ok = prefix_ok and match
            summary["prefix"] = {
                "observed_eligible": len(pe),
                "observed_losses": len(pl),
                "expected_eligible": expected_eligible,
                "expected_losses": expected_losses,
                "matches_historical": match,
            }
        if condition == "individual_dispersal_d010":
            moved = [row for row in rows if row.get("total_movers") is not None]
            summary["movement"] = {
                "mean_total_movers": None if not moved else sum(row["total_movers"] for row in moved) / len(moved),
                "mean_realised_movement_fraction": None if not moved else sum(row["realised_movement_fraction"] for row in moved) / len(moved),
            }
        condition_summaries.append(summary)

    return {
        "stage": "process-resolved movement validation Phase R",
        "master_seed": master_seed,
        "prefix_audit_passed": prefix_ok,
        "process_baseline_pairing_passed": baseline_pairing_ok,
        "condition_summaries": condition_summaries,
        "attempts": attempts,
    }


def _paired_counts(payloads: tuple[dict[str, Any], ...], reference: str, comparison: str) -> dict[str, Any]:
    counts = {"comparable_pair_count": 0, "loss_to_no_loss": 0, "no_loss_to_loss": 0, "same_loss": 0, "same_no_loss": 0}
    rows = {}
    for payload in payloads:
        for row in payload["attempts"]:
            rows[(row["master_seed"], row["replicate"], row["condition"])] = row
    for seed in PHASE_E_MASTER_SEEDS:
        for replicate in range(PHASE_R_REPLICATES_PER_SEED):
            ref = rows[(seed, replicate, reference)]
            alt = rows[(seed, replicate, comparison)]
            if not (ref["eligible_for_trait_loss_denominator"] and alt["eligible_for_trait_loss_denominator"]):
                continue
            counts["comparable_pair_count"] += 1
            ref_loss = ref["trait_loss_observed_post_baseline"] is True
            alt_loss = alt["trait_loss_observed_post_baseline"] is True
            if ref_loss and not alt_loss:
                counts["loss_to_no_loss"] += 1
            elif not ref_loss and alt_loss:
                counts["no_loss_to_loss"] += 1
            elif ref_loss:
                counts["same_loss"] += 1
            else:
                counts["same_no_loss"] += 1
    return {
        "reference": reference,
        "comparison": comparison,
        **counts,
        "exact_mcnemar_two_sided_p": _exact_mcnemar_two_sided(counts["loss_to_no_loss"], counts["no_loss_to_loss"]),
    }


def aggregate_phase_r(seed_payloads: Iterable[dict[str, Any]]) -> dict[str, Any]:
    payloads = tuple(seed_payloads)
    if sorted(payload["master_seed"] for payload in payloads) != sorted(PHASE_E_MASTER_SEEDS):
        raise RuntimeError("Phase R requires exactly the five locked Phase-E master seeds")

    prefix_ok = all(payload["prefix_audit_passed"] for payload in payloads)
    baseline_pairing_ok = all(payload["process_baseline_pairing_passed"] for payload in payloads)
    summaries = []
    regime_by_condition = {}
    blocks_by_condition: dict[str, tuple[tuple[int, int], ...]] = {}

    for condition in PHASE_R_CONDITIONS:
        blocks = []
        movement_rows = []
        for payload in sorted(payloads, key=lambda item: item["master_seed"]):
            row = next(item for item in payload["condition_summaries"] if item["condition"] == condition)
            blocks.append((int(row["trait_loss"]), int(row["baseline_eligible"])))
            if "movement" in row:
                movement_rows.append(row["movement"])
        block_tuple = tuple(blocks)
        blocks_by_condition[condition] = block_tuple
        sufficient = all(eligible >= PHASE_R_MIN_BASELINE_ELIGIBLE_PER_SEED for _, eligible in block_tuple)
        rates = tuple(losses / eligible for losses, eligible in block_tuple)
        regime = "insufficient_precision" if not sufficient else _regime(rates)
        statistic, df, p_value = pearson_equal_rate_test(block_tuple)
        summary = {
            "condition": condition,
            "blocks": [
                {"master_seed": seed, "losses": losses, "eligible": eligible, "rate": losses / eligible}
                for seed, (losses, eligible) in zip(PHASE_E_MASTER_SEEDS, block_tuple, strict=True)
            ],
            "pooled_loss_rate": _pooled_rate(block_tuple),
            "historical_screen_at_full_precision": regime,
            "pearson_equal_rate_statistic": statistic,
            "pearson_equal_rate_df": df,
            "pearson_equal_rate_p_value": p_value,
            "precision_sufficient": sufficient,
        }
        if movement_rows:
            summary["movement"] = {
                "mean_total_movers_across_seed_blocks": sum(row["mean_total_movers"] for row in movement_rows) / len(movement_rows),
                "mean_realised_movement_fraction_across_seed_blocks": sum(row["mean_realised_movement_fraction"] for row in movement_rows) / len(movement_rows),
            }
        summaries.append(summary)
        regime_by_condition[condition] = regime

    legacy_full_replay_ok = (
        blocks_by_condition["no_connectivity"] == PHASE_R_PHASE_M_BLOCKS["no_connectivity"]
        and blocks_by_condition["allele_only_m010"] == PHASE_R_PHASE_M_BLOCKS["allele_only_m010"]
    )
    opening_passed = prefix_ok and baseline_pairing_ok and legacy_full_replay_ok
    process_summary = next(row for row in summaries if row["condition"] == "individual_dispersal_d010")

    paired_vs_no = _paired_counts(payloads, "no_connectivity", "individual_dispersal_d010")
    paired_vs_legacy = _paired_counts(payloads, "allele_only_m010", "individual_dispersal_d010")

    if not opening_passed:
        decision = "opening_replay_failed"
    elif process_summary["pearson_equal_rate_p_value"] < 0.05:
        decision = "process_resolved_dispersal_shows_between_block_heterogeneity"
    else:
        decision = "legacy_m010_heterogeneity_not_reproduced_by_process_resolved_dispersal"

    return {
        "stage": "process-resolved movement validation Phase R",
        "manifest": phase_r_manifest(),
        "opening": {
            "prefix_audit_passed": prefix_ok,
            "process_baseline_pairing_passed": baseline_pairing_ok,
            "legacy_full_phase_m_replay_passed": legacy_full_replay_ok,
            "opening_passed": opening_passed,
        },
        "decision": decision,
        "condition_summaries": summaries,
        "regime_by_condition": regime_by_condition,
        "paired_process_vs_no_connectivity": paired_vs_no,
        "paired_process_vs_allele_only_m010": paired_vs_legacy,
        "interpretation": {
            "process_marginal_effect_detected": paired_vs_no["exact_mcnemar_two_sided_p"] < 0.05,
            "process_differs_from_allele_only_m010": paired_vs_legacy["exact_mcnemar_two_sided_p"] < 0.05,
            "process_between_block_heterogeneity_detected": process_summary["pearson_equal_rate_p_value"] < 0.05,
        },
        "per_seed_payloads": list(payloads),
    }


def load_and_aggregate_phase_r(paths: Iterable[str | Path]) -> dict[str, Any]:
    payloads = [json.loads(Path(path).read_text(encoding="utf-8")) for path in paths]
    return aggregate_phase_r(payloads)
