"""Per-seed runner and aggregate inference for fresh connectivity replication Phase U."""
from __future__ import annotations

import importlib
import json
from dataclasses import replace
from math import comb, exp, factorial
from pathlib import Path
from typing import Any, Iterable

from .fresh_connectivity_replication_phase_u import (
    PHASE_U_ALPHA,
    PHASE_U_MASTER_SEEDS,
    PHASE_U_MIGRATION_RATES,
    PHASE_U_MIN_BASELINE_ELIGIBLE_PER_SEED,
    PHASE_U_REPLICATES_PER_SEED,
    phase_u_manifest,
)
from .migration_condition_phase_e import (
    PHASE_E_AREA_REFERENCE,
    PHASE_E_BARRIER_INCREASE,
    PHASE_E_HOLD_GENERATIONS,
    PHASE_E_INTERACTION_KAPPA,
    PHASE_E_KAPPA_MU,
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


def _chi_square_sf_even_df(statistic: float, df: int) -> float:
    if statistic < 0.0 or df < 2 or df % 2:
        raise ValueError("requires nonnegative statistic and positive even df")
    x = statistic / 2.0
    return exp(-x) * sum((x**j) / factorial(j) for j in range(df // 2))


def pearson_equal_rate_test(blocks: tuple[tuple[int, int], ...]) -> tuple[float, int, float]:
    if len(blocks) < 2:
        raise ValueError("at least two blocks are required")
    total_eligible = sum(eligible for _, eligible in blocks)
    total_losses = sum(losses for losses, _ in blocks)
    if total_eligible < 1:
        raise ValueError("positive eligible total is required")
    pooled = total_losses / total_eligible
    if not 0.0 < pooled < 1.0:
        raise ValueError("pooled rate must lie inside (0, 1)")
    statistic = 0.0
    for losses, eligible in blocks:
        expected_loss = eligible * pooled
        expected_nonloss = eligible * (1.0 - pooled)
        statistic += ((losses - expected_loss) ** 2) / expected_loss
        statistic += (((eligible - losses) - expected_nonloss) ** 2) / expected_nonloss
    df = len(blocks) - 1
    return statistic, df, _chi_square_sf_even_df(statistic, df)


def _exact_mcnemar_two_sided(loss_to_no_loss: int, no_loss_to_loss: int) -> float:
    n = int(loss_to_no_loss) + int(no_loss_to_loss)
    if n == 0:
        return 1.0
    k = min(int(loss_to_no_loss), int(no_loss_to_loss))
    tail = sum(comb(n, index) for index in range(k + 1)) / (2**n)
    return min(1.0, 2.0 * tail)


def _historical_screen(rates: tuple[float, ...]) -> str:
    return {
        "warning_evaluable": "R4_highrep",
        "rapid_loss": "R2_highrep",
        "persistence": "R1_highrep",
        "seed_heterogeneous": "R3_highrep",
    }[classify_seed_rates(rates)]


def run_phase_u_seed(upstream_checkout: str | Path, master_seed: int) -> dict[str, Any]:
    if master_seed not in PHASE_U_MASTER_SEEDS:
        raise ValueError("master_seed is not one of the preregistered fresh Phase-U seeds")
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
            experiment_id="fresh_connectivity_replication_phase_u",
            generations=1,
            replicates=PHASE_U_REPLICATES_PER_SEED,
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
                raise RuntimeError("Phase U requires exactly one H1 cell per fresh master seed")
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
                    for migration_rate in PHASE_U_MIGRATION_RATES:
                        attempts.append({
                            **base,
                            "migration_rate": migration_rate,
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
                    raise RuntimeError("Phase-U source requires a positive canonical interval")
                barriers = calibration.ramp_and_hold_barrier_schedule(
                    anchor_barrier=anchor_barrier,
                    canonical_interval_width=interval[1] - interval[0],
                    schedule=schedule,
                )

                for migration_rate in PHASE_U_MIGRATION_RATES:
                    scenario = experiments.LandscapeScenario(
                        scenario_id=f"phase_u_m_{migration_rate:.2f}",
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
                            "trait_loss_time_post_baseline": None,
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
                        "trait_loss_time_post_baseline": loss_time,
                        "trait_loss_observed_post_baseline": None if not baseline_present else loss_time is not None,
                    })

    by_key = {(row["replicate"], float(row["migration_rate"])): row for row in attempts}
    baseline_pairing_ok = all(
        by_key[(replicate, 0.0)]["eligible_for_trait_loss_denominator"]
        == by_key[(replicate, 0.10)]["eligible_for_trait_loss_denominator"]
        for replicate in range(PHASE_U_REPLICATES_PER_SEED)
    )

    condition_summaries = []
    for migration_rate in PHASE_U_MIGRATION_RATES:
        rows = [row for row in attempts if float(row["migration_rate"]) == migration_rate]
        eligible = [row for row in rows if row["eligible_for_trait_loss_denominator"]]
        losses = [row for row in eligible if row["trait_loss_observed_post_baseline"] is True]
        condition_summaries.append({
            "migration_rate": migration_rate,
            "attempted": len(rows),
            "source_prepared": sum(row["source_prepared"] is True for row in rows),
            "projection_supported": sum(row["projection_supported"] is True for row in rows),
            "baseline_eligible": len(eligible),
            "trait_loss": len(losses),
            "trait_loss_rate": None if not eligible else len(losses) / len(eligible),
            "precision_sufficient": len(eligible) >= PHASE_U_MIN_BASELINE_ELIGIBLE_PER_SEED,
        })

    return {
        "stage": "fresh connectivity replication Phase U",
        "master_seed": master_seed,
        "baseline_pairing_passed": baseline_pairing_ok,
        "condition_summaries": condition_summaries,
        "attempts": attempts,
    }


def aggregate_phase_u(seed_payloads: Iterable[dict[str, Any]]) -> dict[str, Any]:
    payloads = tuple(seed_payloads)
    if sorted(payload["master_seed"] for payload in payloads) != sorted(PHASE_U_MASTER_SEEDS):
        raise RuntimeError("Phase U requires exactly the five preregistered fresh master seeds")

    baseline_pairing_ok = all(payload["baseline_pairing_passed"] for payload in payloads)
    condition_summaries = []
    blocks_by_rate: dict[float, tuple[tuple[int, int], ...]] = {}
    precision_sufficient = baseline_pairing_ok

    for migration_rate in PHASE_U_MIGRATION_RATES:
        blocks = []
        for payload in sorted(payloads, key=lambda item: item["master_seed"]):
            row = next(
                item for item in payload["condition_summaries"]
                if float(item["migration_rate"]) == migration_rate
            )
            blocks.append((int(row["trait_loss"]), int(row["baseline_eligible"])))
        block_tuple = tuple(blocks)
        blocks_by_rate[migration_rate] = block_tuple
        sufficient = all(eligible >= PHASE_U_MIN_BASELINE_ELIGIBLE_PER_SEED for _, eligible in block_tuple)
        precision_sufficient = precision_sufficient and sufficient
        rates = tuple(losses / eligible for losses, eligible in block_tuple if eligible > 0)
        pooled = sum(losses for losses, _ in block_tuple) / sum(eligible for _, eligible in block_tuple)
        if sufficient:
            statistic, df, p_value = pearson_equal_rate_test(block_tuple)
            screen = _historical_screen(rates)
        else:
            statistic, df, p_value, screen = None, None, None, "insufficient_precision"
        condition_summaries.append({
            "migration_rate": migration_rate,
            "blocks": [
                {"master_seed": seed, "losses": losses, "eligible": eligible, "rate": None if eligible == 0 else losses / eligible}
                for seed, (losses, eligible) in zip(PHASE_U_MASTER_SEEDS, block_tuple, strict=True)
            ],
            "pooled_loss_rate": pooled,
            "historical_screen": screen,
            "pearson_equal_rate_statistic": statistic,
            "pearson_equal_rate_df": df,
            "pearson_equal_rate_p": p_value,
            "precision_sufficient": sufficient,
        })

    rows = {
        (row["master_seed"], row["replicate"], float(row["migration_rate"])): row
        for payload in payloads for row in payload["attempts"]
    }
    counts = {
        "comparable": 0,
        "loss_to_no_loss": 0,
        "no_loss_to_loss": 0,
        "same_loss": 0,
        "same_no_loss": 0,
    }
    for seed in PHASE_U_MASTER_SEEDS:
        for replicate in range(PHASE_U_REPLICATES_PER_SEED):
            reference = rows[(seed, replicate, 0.0)]
            comparison = rows[(seed, replicate, 0.10)]
            if not (reference["eligible_for_trait_loss_denominator"] and comparison["eligible_for_trait_loss_denominator"]):
                continue
            counts["comparable"] += 1
            ref_loss = reference["trait_loss_observed_post_baseline"] is True
            cmp_loss = comparison["trait_loss_observed_post_baseline"] is True
            if ref_loss and not cmp_loss:
                counts["loss_to_no_loss"] += 1
            elif not ref_loss and cmp_loss:
                counts["no_loss_to_loss"] += 1
            elif ref_loss:
                counts["same_loss"] += 1
            else:
                counts["same_no_loss"] += 1

    paired = {
        "reference_migration_rate": 0.0,
        "comparison_migration_rate": 0.10,
        **counts,
        "exact_mcnemar_p": _exact_mcnemar_two_sided(counts["loss_to_no_loss"], counts["no_loss_to_loss"]),
    }

    by_rate = {float(row["migration_rate"]): row for row in condition_summaries}
    if not precision_sufficient:
        decision = "insufficient_fresh_precision"
    else:
        p_zero = float(by_rate[0.0]["pearson_equal_rate_p"])
        p_m010 = float(by_rate[0.10]["pearson_equal_rate_p"])
        if p_m010 < PHASE_U_ALPHA and p_zero >= PHASE_U_ALPHA:
            decision = "specific_m010_heterogeneity_replicated"
        elif p_m010 < PHASE_U_ALPHA and p_zero < PHASE_U_ALPHA:
            decision = "fresh_ensemble_heterogeneity_not_specific_to_m010"
        else:
            decision = "historical_m010_heterogeneity_not_freshly_replicated"

    return {
        "stage": "fresh connectivity replication Phase U",
        "manifest": phase_u_manifest(),
        "opening": {
            "baseline_pairing_passed": baseline_pairing_ok,
            "all_blocks_precision_sufficient": precision_sufficient,
        },
        "decision": decision,
        "condition_summaries": condition_summaries,
        "paired_m010_vs_zero": paired,
        "per_seed_payloads": list(payloads),
    }


def load_and_aggregate_phase_u(paths: Iterable[str | Path]) -> dict[str, Any]:
    return aggregate_phase_u([json.loads(Path(path).read_text(encoding="utf-8")) for path in paths])
