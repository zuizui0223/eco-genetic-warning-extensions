"""Paired high-precision runner for dynamic partner architecture Phase T."""
from __future__ import annotations

import importlib
import json
from collections import defaultdict
from contextlib import contextmanager
from dataclasses import replace
from math import comb, exp, factorial
from pathlib import Path
from random import Random
from typing import Any, Iterable, Iterator, Sequence

from .dynamic_partner_architecture_phase_t import (
    PHASE_T_ARCHITECTURES,
    PHASE_T_CONDITIONS,
    PHASE_T_CONSTANT_SUPPORT,
    PHASE_T_MIN_BASELINE_ELIGIBLE_PER_SEED,
    PHASE_T_NETWORK_SEED_OFFSET,
    PHASE_T_PARTNER_AVAILABILITY,
    PHASE_T_PARTNER_COUNT,
    PHASE_T_PHASE_G_PREFIX_COUNTS,
    PHASE_T_PHASE_N_CONSTANT_BLOCKS,
    PHASE_T_REPLICATES_PER_SEED,
    phase_t_manifest,
    support_from_availability,
)
from .mutation_coordinates import MutationCoordinates
from .partner_redundancy_phase_g import (
    PHASE_G_AREA_REFERENCE,
    PHASE_G_BARRIER_INCREASE,
    PHASE_G_HOLD_GENERATIONS,
    PHASE_G_INTERACTION_KAPPA,
    PHASE_G_KAPPA_MU,
    PHASE_G_MASTER_SEEDS,
    PHASE_G_MIGRATION_RATE,
    PHASE_G_P_STAR,
    PHASE_G_RAMP_GENERATIONS,
)
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
    pooled = sum(losses for losses, _ in blocks) / sum(eligible for _, eligible in blocks)
    if not 0.0 < pooled < 1.0:
        raise ValueError("pooled rate must lie in (0,1)")
    statistic = 0.0
    for losses, eligible in blocks:
        expected_loss = eligible * pooled
        expected_nonloss = eligible * (1.0 - pooled)
        statistic += ((losses - expected_loss) ** 2) / expected_loss
        statistic += (((eligible - losses) - expected_nonloss) ** 2) / expected_nonloss
    df = len(blocks) - 1
    return statistic, df, _chi_square_sf_even_df(statistic, df)


def _exact_mcnemar_two_sided(a: int, b: int) -> float:
    n = int(a) + int(b)
    if n == 0:
        return 1.0
    k = min(int(a), int(b))
    tail = sum(comb(n, i) for i in range(k + 1)) / (2**n)
    return min(1.0, 2.0 * tail)


def _screen(rates: tuple[float, ...]) -> str:
    if all(rate < 0.30 for rate in rates):
        return "R1_highrep"
    if all(rate > 0.70 for rate in rates):
        return "R2_highrep"
    if all(0.30 <= rate <= 0.70 for rate in rates):
        return "R4_highrep"
    return "R3_highrep"


@contextmanager
def patched_support_schedule(
    mutation_module: Any,
    multipliers: Sequence[float],
    *,
    patch_count: int,
) -> Iterator[dict[str, int]]:
    values = tuple(float(value) for value in multipliers)
    if not values or any(value < 0.0 or value > 1.0 for value in values):
        raise ValueError("support schedule must be nonempty and lie in [0,1]")
    original = mutation_module.interaction_support_signal
    state = {"calls": 0}

    def scheduled_signal(interaction: float, realised_high_trait_mass: float, high_allele_frequency: float, parameters: Any) -> float:
        generation_index = state["calls"] // patch_count
        if generation_index >= len(values):
            raise RuntimeError("Phase-T support schedule exhausted")
        multiplier = values[generation_index]
        state["calls"] += 1
        return multiplier * original(interaction, realised_high_trait_mass, high_allele_frequency, parameters)

    mutation_module.interaction_support_signal = scheduled_signal
    try:
        yield state
    finally:
        mutation_module.interaction_support_signal = original


def availability_schedule(seed: int, generations: int) -> tuple[tuple[bool, ...], ...]:
    if generations < 1:
        raise ValueError("generations must be positive")
    rng = Random(int(seed) + PHASE_T_NETWORK_SEED_OFFSET)
    return tuple(
        tuple(rng.random() < PHASE_T_PARTNER_AVAILABILITY for _ in range(PHASE_T_PARTNER_COUNT))
        for _ in range(generations)
    )


def architecture_support_schedule(architecture: Any, availability: tuple[tuple[bool, ...], ...]) -> tuple[float, ...]:
    return tuple(support_from_availability(architecture.weights, row) for row in availability)


def _support_diagnostics(schedule: tuple[float, ...]) -> dict[str, float]:
    mean = sum(schedule) / len(schedule)
    variance = sum((value - mean) ** 2 for value in schedule) / len(schedule)
    return {
        "realised_support_mean": mean,
        "realised_support_variance": variance,
        "zero_support_generation_fraction": sum(value <= 1e-12 for value in schedule) / len(schedule),
        "support_min": min(schedule),
        "support_max": max(schedule),
    }


def _outcome_row(base: dict[str, Any], condition: str, result: Any, dynamics: Any, diagnostics: dict[str, Any]) -> dict[str, Any]:
    baseline_present = any(item.realised_high_trait_occupied for item in result.snapshots[0].trait_occupancy)
    raw_loss_time = dynamics.tau_trait_realised(result)
    loss_time = None if raw_loss_time is None or raw_loss_time == 0 else raw_loss_time
    return {
        **base,
        "condition": condition,
        **diagnostics,
        "source_prepared": True,
        "projection_supported": True,
        "baseline_realised_high_trait_present": baseline_present,
        "eligible_for_trait_loss_denominator": bool(baseline_present),
        "trait_loss_time_post_baseline": loss_time,
        "trait_loss_observed_post_baseline": None if not baseline_present else loss_time is not None,
    }


def run_phase_t_seed(upstream_checkout: str | Path, master_seed: int) -> dict[str, Any]:
    if master_seed not in PHASE_G_MASTER_SEEDS:
        raise ValueError("master seed is not one of the locked Phase-G seeds")
    checkout = Path(upstream_checkout)
    if not checkout.exists():
        raise FileNotFoundError(f"upstream checkout does not exist: {checkout}")

    coordinate = MutationCoordinates(kappa_mu=PHASE_G_KAPPA_MU, p_star=PHASE_G_P_STAR)
    driver_rate = coordinate.kappa_mu / 2.0
    total_generations = PHASE_G_RAMP_GENERATIONS + PHASE_G_HOLD_GENERATIONS
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
            PHASE_G_RAMP_GENERATIONS,
            PHASE_G_HOLD_GENERATIONS,
            PHASE_G_BARRIER_INCREASE,
        )
        spec = replace(
            experiments.standard_profile(),
            experiment_id="dynamic_partner_architecture_phase_t",
            generations=1,
            replicates=PHASE_T_REPLICATES_PER_SEED,
            master_seed=master_seed,
            area_reference_values=(PHASE_G_AREA_REFERENCE,),
            interaction_feedback_values=(PHASE_G_INTERACTION_KAPPA,),
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
                raise RuntimeError("Phase T requires exactly one H1 cell per master seed")
            cell = cells[0]
            isolated = experiments.scenario_equal_isolated(spec)
            scenario = experiments.LandscapeScenario(
                scenario_id="equal_fragmented_dynamic_partner_phase_t",
                patch_areas=isolated.patch_areas,
                migration_rate=PHASE_G_MIGRATION_RATE,
            )

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
                    for condition in PHASE_T_CONDITIONS:
                        attempts.append({
                            **base,
                            "condition": condition,
                            "source_prepared": False,
                            "projection_supported": None,
                            "eligible_for_trait_loss_denominator": False,
                            "trait_loss_observed_post_baseline": None,
                        })
                    continue

                source, anchor_barrier = prepared
                interval = cell.canonical_bistable_barrier_interval
                if interval is None or interval[1] <= interval[0]:
                    raise RuntimeError("Phase-T source requires a positive canonical interval")
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
                if not invariants.projection_supported:
                    for condition in PHASE_T_CONDITIONS:
                        attempts.append({
                            **base,
                            "condition": condition,
                            "source_prepared": True,
                            "projection_supported": False,
                            "eligible_for_trait_loss_denominator": False,
                            "trait_loss_observed_post_baseline": None,
                        })
                    continue

                common_availability = availability_schedule(record.seed, total_generations)
                schedules = {
                    "constant_support_075": tuple(PHASE_T_CONSTANT_SUPPORT for _ in range(total_generations)),
                }
                for architecture in PHASE_T_ARCHITECTURES:
                    schedules[architecture.name] = architecture_support_schedule(architecture, common_availability)

                for condition in PHASE_T_CONDITIONS:
                    schedule = schedules[condition]
                    diagnostics = _support_diagnostics(schedule)
                    if condition == "constant_support_075":
                        diagnostics.update({
                            "partner_weights": None,
                            "theoretical_expected_support": PHASE_T_CONSTANT_SUPPORT,
                            "theoretical_support_variance": 0.0,
                        })
                    else:
                        architecture = next(item for item in PHASE_T_ARCHITECTURES if item.name == condition)
                        diagnostics.update({
                            "partner_weights": list(architecture.weights),
                            "theoretical_expected_support": architecture.expected_support,
                            "theoretical_support_variance": architecture.support_variance,
                            "contribution_cv": architecture.contribution_cv,
                        })
                    with patched_support_schedule(mutation, schedule, patch_count=len(projected.patch_areas)) as state:
                        result = mutation.simulate_with_symmetric_allele_mutation(
                            replace(projected, generations=total_generations, random_seed=record.seed),
                            mutation_rate=driver_rate,
                            interaction_barrier_schedule=barriers,
                        )
                    expected_calls = total_generations * len(projected.patch_areas)
                    if state["calls"] != expected_calls:
                        raise RuntimeError("Phase-T support schedule call count mismatch")
                    attempts.append(_outcome_row(base, condition, result, dynamics, diagnostics))

    constant_rows = [row for row in attempts if row["condition"] == "constant_support_075"]
    dynamic_rows = [row for row in attempts if row["condition"] != "constant_support_075"]
    baseline_pairing_ok = True
    constant_by_rep = {row["replicate"]: row for row in constant_rows}
    for row in dynamic_rows:
        if row["eligible_for_trait_loss_denominator"] != constant_by_rep[row["replicate"]]["eligible_for_trait_loss_denominator"]:
            baseline_pairing_ok = False

    prefix = [row for row in constant_rows if row["replicate"] < 20]
    prefix_eligible = [row for row in prefix if row["eligible_for_trait_loss_denominator"]]
    prefix_losses = [row for row in prefix_eligible if row["trait_loss_observed_post_baseline"] is True]
    expected_eligible, expected_losses = PHASE_T_PHASE_G_PREFIX_COUNTS[master_seed]
    prefix_ok = len(prefix_eligible) == expected_eligible and len(prefix_losses) == expected_losses

    condition_summaries = []
    for condition in PHASE_T_CONDITIONS:
        rows = [row for row in attempts if row["condition"] == condition]
        eligible = [row for row in rows if row["eligible_for_trait_loss_denominator"]]
        losses = [row for row in eligible if row["trait_loss_observed_post_baseline"] is True]
        diagnostics_rows = [row for row in rows if row.get("realised_support_mean") is not None]
        condition_summaries.append({
            "condition": condition,
            "attempted": len(rows),
            "baseline_eligible": len(eligible),
            "trait_loss": len(losses),
            "trait_loss_rate": None if not eligible else len(losses) / len(eligible),
            "precision_sufficient": len(eligible) >= PHASE_T_MIN_BASELINE_ELIGIBLE_PER_SEED,
            "mean_realised_support": None if not diagnostics_rows else sum(row["realised_support_mean"] for row in diagnostics_rows) / len(diagnostics_rows),
            "mean_realised_support_variance": None if not diagnostics_rows else sum(row["realised_support_variance"] for row in diagnostics_rows) / len(diagnostics_rows),
            "mean_zero_support_generation_fraction": None if not diagnostics_rows else sum(row["zero_support_generation_fraction"] for row in diagnostics_rows) / len(diagnostics_rows),
        })

    return {
        "stage": "dynamic partner architecture Phase T",
        "master_seed": master_seed,
        "constant_prefix_audit_passed": prefix_ok,
        "dynamic_baseline_pairing_passed": baseline_pairing_ok,
        "constant_prefix": {
            "observed_eligible": len(prefix_eligible),
            "observed_losses": len(prefix_losses),
            "expected_eligible": expected_eligible,
            "expected_losses": expected_losses,
        },
        "condition_summaries": condition_summaries,
        "attempts": attempts,
    }


def _paired_counts(payloads: tuple[dict[str, Any], ...], reference: str, comparison: str) -> dict[str, Any]:
    rows = {
        (row["master_seed"], row["replicate"], row["condition"]): row
        for payload in payloads for row in payload["attempts"]
    }
    counts = {"comparable": 0, "loss_to_no_loss": 0, "no_loss_to_loss": 0, "same_loss": 0, "same_no_loss": 0}
    for seed in PHASE_G_MASTER_SEEDS:
        for replicate in range(PHASE_T_REPLICATES_PER_SEED):
            ref = rows[(seed, replicate, reference)]
            alt = rows[(seed, replicate, comparison)]
            if not (ref["eligible_for_trait_loss_denominator"] and alt["eligible_for_trait_loss_denominator"]):
                continue
            counts["comparable"] += 1
            a = ref["trait_loss_observed_post_baseline"] is True
            b = alt["trait_loss_observed_post_baseline"] is True
            if a and not b:
                counts["loss_to_no_loss"] += 1
            elif not a and b:
                counts["no_loss_to_loss"] += 1
            elif a:
                counts["same_loss"] += 1
            else:
                counts["same_no_loss"] += 1
    return {
        "reference": reference,
        "comparison": comparison,
        **counts,
        "exact_mcnemar_p": _exact_mcnemar_two_sided(counts["loss_to_no_loss"], counts["no_loss_to_loss"]),
    }


def aggregate_phase_t(seed_payloads: Iterable[dict[str, Any]]) -> dict[str, Any]:
    payloads = tuple(seed_payloads)
    if sorted(payload["master_seed"] for payload in payloads) != sorted(PHASE_G_MASTER_SEEDS):
        raise RuntimeError("Phase T requires exactly the five locked Phase-G master seeds")

    prefix_ok = all(payload["constant_prefix_audit_passed"] for payload in payloads)
    baseline_pairing_ok = all(payload["dynamic_baseline_pairing_passed"] for payload in payloads)
    summaries = []
    blocks_by_condition: dict[str, tuple[tuple[int, int], ...]] = {}

    for condition in PHASE_T_CONDITIONS:
        blocks = []
        support_rows = []
        for payload in sorted(payloads, key=lambda item: item["master_seed"]):
            row = next(item for item in payload["condition_summaries"] if item["condition"] == condition)
            blocks.append((int(row["trait_loss"]), int(row["baseline_eligible"])))
            support_rows.append(row)
        block_tuple = tuple(blocks)
        blocks_by_condition[condition] = block_tuple
        rates = tuple(losses / eligible for losses, eligible in block_tuple)
        sufficient = all(eligible >= PHASE_T_MIN_BASELINE_ELIGIBLE_PER_SEED for _, eligible in block_tuple)
        statistic, df, equal_p = pearson_equal_rate_test(block_tuple)
        summaries.append({
            "condition": condition,
            "blocks": [
                {"master_seed": seed, "losses": losses, "eligible": eligible, "rate": losses / eligible}
                for seed, (losses, eligible) in zip(PHASE_G_MASTER_SEEDS, block_tuple, strict=True)
            ],
            "pooled_loss_rate": sum(losses for losses, _ in block_tuple) / sum(eligible for _, eligible in block_tuple),
            "historical_screen": "insufficient_precision" if not sufficient else _screen(rates),
            "pearson_equal_rate_statistic": statistic,
            "pearson_equal_rate_df": df,
            "pearson_equal_rate_p": equal_p,
            "precision_sufficient": sufficient,
            "mean_realised_support": sum(row["mean_realised_support"] for row in support_rows) / len(support_rows),
            "mean_realised_support_variance": sum(row["mean_realised_support_variance"] for row in support_rows) / len(support_rows),
            "mean_zero_support_generation_fraction": sum(row["mean_zero_support_generation_fraction"] for row in support_rows) / len(support_rows),
        })

    legacy_full_replay_ok = blocks_by_condition["constant_support_075"] == PHASE_T_PHASE_N_CONSTANT_BLOCKS
    opening_passed = prefix_ok and baseline_pairing_ok and legacy_full_replay_ok
    paired_even_constant = _paired_counts(payloads, "constant_support_075", "even_dynamic")
    paired_dominant_constant = _paired_counts(payloads, "constant_support_075", "dominant_dynamic")
    paired_dominant_even = _paired_counts(payloads, "even_dynamic", "dominant_dynamic")

    dynamic_summaries = {row["condition"]: row for row in summaries}
    effect_flags = {
        "even_vs_constant_marginal": paired_even_constant["exact_mcnemar_p"] < 0.05,
        "dominant_vs_constant_marginal": paired_dominant_constant["exact_mcnemar_p"] < 0.05,
        "dominant_vs_even_marginal": paired_dominant_even["exact_mcnemar_p"] < 0.05,
        "even_block_heterogeneity": dynamic_summaries["even_dynamic"]["pearson_equal_rate_p"] < 0.05,
        "dominant_block_heterogeneity": dynamic_summaries["dominant_dynamic"]["pearson_equal_rate_p"] < 0.05,
    }
    if not opening_passed:
        decision = "opening_replay_failed"
    elif any(effect_flags.values()):
        decision = "dynamic_partner_architecture_changes_functional_loss_process"
    else:
        decision = "no_detected_dynamic_partner_architecture_effect_at_matched_expected_support"

    return {
        "stage": "dynamic partner architecture Phase T",
        "manifest": phase_t_manifest(),
        "opening": {
            "constant_prefix_audit_passed": prefix_ok,
            "dynamic_baseline_pairing_passed": baseline_pairing_ok,
            "constant_full_phase_n_replay_passed": legacy_full_replay_ok,
            "opening_passed": opening_passed,
        },
        "decision": decision,
        "condition_summaries": summaries,
        "paired_even_vs_constant": paired_even_constant,
        "paired_dominant_vs_constant": paired_dominant_constant,
        "paired_dominant_vs_even": paired_dominant_even,
        "effect_flags": effect_flags,
        "per_seed_payloads": list(payloads),
    }


def load_and_aggregate_phase_t(paths: Iterable[str | Path]) -> dict[str, Any]:
    return aggregate_phase_t([json.loads(Path(path).read_text(encoding="utf-8")) for path in paths])
