"""Paired warning-blind explicit rewiring Phase H runner."""
from __future__ import annotations

import importlib
import json
from collections import defaultdict
from contextlib import contextmanager
from dataclasses import replace
from pathlib import Path
from typing import Any, Iterator, Sequence

from .explicit_rewiring_phase_h import (
    PHASE_H_AREA_REFERENCE,
    PHASE_H_BARRIER_INCREASE,
    PHASE_H_HOLD_GENERATIONS,
    PHASE_H_INTERACTION_KAPPA,
    PHASE_H_MASTER_SEEDS,
    PHASE_H_MIGRATION_RATE,
    PHASE_H_MIN_BASELINE_ELIGIBLE_PER_SEED,
    PHASE_H_RAMP_GENERATIONS,
    PHASE_H_REPLICATES_PER_SEED,
    lost_primary_partner_index,
    network_schedule,
    phase_h_conditions,
    phase_h_coordinate,
    phase_h_manifest,
    post_loss_edges,
)
from .protocol002_calibration import assert_protocol002_blind_calibration_columns
from .protocol002_condition_map import classify_seed_rates
from .protocol002_source_grid import SOURCE_HOLD_GENERATIONS, SOURCE_NESTED_BARRIER_GRIDS, SOURCE_STAGE_GENERATIONS
from .protocol002_stage0 import UPSTREAM_COMMIT, UPSTREAM_REPOSITORY
from .protocol002_stage1_projection_pilot import UPSTREAM_CHAIN_RUNTIME_MODULE
from .protocol002_stage2_smoke import UPSTREAM_CALIBRATION_MODULE, UPSTREAM_DYNAMICS_MODULE
from .protocol002_upstream_h1_asym_smoke import (
    UPSTREAM_EXPERIMENT_MODULE,
    UPSTREAM_H1_MODULE,
    UPSTREAM_MUTATION_MODULE,
    _upstream_import_path,
    patched_protocol002_mutation_runner,
)


def _assert_blind(value: Any) -> None:
    if isinstance(value, dict):
        assert_protocol002_blind_calibration_columns(value.keys())
        for child in value.values():
            _assert_blind(child)
    elif isinstance(value, (list, tuple)):
        for child in value:
            _assert_blind(child)


@contextmanager
def patched_interaction_support_schedule(
    mutation_module: Any,
    multipliers: Sequence[float],
    *,
    patch_count: int,
) -> Iterator[dict[str, int]]:
    """Apply one prospective network-derived support multiplier per generation."""
    values = tuple(float(value) for value in multipliers)
    if not values:
        raise ValueError("support multiplier schedule must be nonempty")
    if patch_count < 1:
        raise ValueError("patch_count must be positive")
    if any(value < 0.0 or value > 1.0 for value in values):
        raise ValueError("support multiplier schedule must lie in [0, 1]")

    original = mutation_module.interaction_support_signal
    state = {"calls": 0}

    def scheduled_signal(interaction: float, realised_high_trait_mass: float, high_allele_frequency: float, parameters: Any) -> float:
        generation_index = state["calls"] // patch_count
        if generation_index >= len(values):
            raise RuntimeError("interaction support schedule exhausted before simulation completed")
        factor = values[generation_index]
        state["calls"] += 1
        return factor * original(interaction, realised_high_trait_mass, high_allele_frequency, parameters)

    mutation_module.interaction_support_signal = scheduled_signal
    try:
        yield state
    finally:
        mutation_module.interaction_support_signal = original


def _network_diagnostics(condition: Any, replicate_index: int, generations: int) -> tuple[tuple[float, ...], dict[str, Any]]:
    schedule = network_schedule(condition, replicate_index, generations)
    multipliers = tuple(float(row["support_multiplier"]) for row in schedule)
    final = schedule[-1]
    final_edges = tuple(float(value) for value in final["edge_strengths"])
    lost_index = None if not condition.remove_primary_partner else lost_primary_partner_index(replicate_index)
    base_sum = sum(post_loss_edges(replicate_index)) if condition.remove_primary_partner else sum(final_edges)
    latent_active = sum(final_edges[index] > 1e-12 for index in range(4, len(final_edges)))
    diagnostics = {
        "network_condition": condition.name,
        "rewiring_rule": condition.rewiring_rule,
        "lost_primary_partner_index": lost_index,
        "support_multiplier_first": multipliers[0],
        "support_multiplier_final": multipliers[-1],
        "support_multiplier_mean": sum(multipliers) / len(multipliers),
        "support_multiplier_min": min(multipliers),
        "support_multiplier_max": max(multipliers),
        "final_edge_strengths": list(final_edges),
        "final_active_edge_count": int(final["active_edge_count"]),
        "final_realised_connectance": float(final["realised_connectance"]),
        "final_functional_support": float(final["functional_support"]),
        "final_latent_partner_edges_activated": latent_active,
        "final_rewired_edge_effort": max(0.0, sum(final_edges) - base_sum),
    }
    return multipliers, diagnostics


def run_phase_h(upstream_checkout: str | Path) -> dict[str, Any]:
    checkout = Path(upstream_checkout)
    if not checkout.exists():
        raise FileNotFoundError(f"upstream checkout does not exist: {checkout}")

    coordinate = phase_h_coordinate()
    conditions = phase_h_conditions()
    driver_rate = coordinate.kappa_mu / 2.0
    attempts: list[dict[str, Any]] = []
    source_preparation_count = 0
    total_generations = PHASE_H_RAMP_GENERATIONS + PHASE_H_HOLD_GENERATIONS

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

        for master_seed in PHASE_H_MASTER_SEEDS:
            spec = replace(
                experiments.standard_profile(),
                experiment_id="explicit_rewiring_phase_h",
                generations=1,
                replicates=PHASE_H_REPLICATES_PER_SEED,
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
                    raise RuntimeError("Phase H must return exactly one H1 cell per master seed")
                cell = cells[0]
                isolated = experiments.scenario_equal_isolated(spec)
                scenario = experiments.LandscapeScenario(
                    scenario_id="equal_fragmented_explicit_rewiring_phase_h",
                    patch_areas=isolated.patch_areas,
                    migration_rate=PHASE_H_MIGRATION_RATE,
                )

                for record in cell.replicates:
                    source_preparation_count += 1
                    source_base: dict[str, Any] = {
                        "kappa_mu": coordinate.kappa_mu,
                        "p_star": coordinate.p_star,
                        "area_reference": PHASE_H_AREA_REFERENCE,
                        "kappa": PHASE_H_INTERACTION_KAPPA,
                        "migration_rate": PHASE_H_MIGRATION_RATE,
                        "ramp_generations": PHASE_H_RAMP_GENERATIONS,
                        "hold_generations": PHASE_H_HOLD_GENERATIONS,
                        "horizon": total_generations,
                        "normalised_barrier_increase": PHASE_H_BARRIER_INCREASE,
                        "master_seed": master_seed,
                        "replicate": record.replicate_index,
                        "calibration_seed": record.seed,
                        "source_support": record.resolution_stable_h1_loop_mechanism_supported,
                    }
                    condition_schedules = {
                        condition.name: _network_diagnostics(condition, record.replicate_index, total_generations)
                        for condition in conditions
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
                        for condition in conditions:
                            _, diagnostics = condition_schedules[condition.name]
                            attempts.append({
                                **source_base,
                                **diagnostics,
                                "status": "source_preparation_failed",
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
                        raise RuntimeError("prepared Phase-H source requires a positive canonical interval")
                    interval_width = interval[1] - interval[0]
                    barriers = calibration.ramp_and_hold_barrier_schedule(
                        anchor_barrier=anchor_barrier,
                        canonical_interval_width=interval_width,
                        schedule=deterioration,
                    )
                    template = chain.parameters_for_cell(
                        spec,
                        scenario,
                        replace(cell.parameters, interaction_barrier=anchor_barrier),
                        seed=record.seed,
                    )
                    projected, invariants = chain.project_full_state(source, template)

                    for condition in conditions:
                        multipliers, diagnostics = condition_schedules[condition.name]
                        base = {**source_base, **diagnostics}
                        if not invariants.projection_supported:
                            base.update({
                                "status": "projection_failed",
                                "source_prepared": True,
                                "projection_supported": False,
                                "baseline_realised_high_trait_present": None,
                                "eligible_for_trait_loss_denominator": False,
                                "trait_loss_time_post_baseline": None,
                                "trait_loss_observed_post_baseline": None,
                            })
                            attempts.append(base)
                            continue

                        with patched_interaction_support_schedule(
                            mutation,
                            multipliers,
                            patch_count=len(projected.patch_areas),
                        ) as schedule_state:
                            result = mutation.simulate_with_symmetric_allele_mutation(
                                replace(projected, generations=total_generations, random_seed=record.seed),
                                mutation_rate=driver_rate,
                                interaction_barrier_schedule=barriers,
                            )
                        expected_calls = total_generations * len(projected.patch_areas)
                        if schedule_state["calls"] != expected_calls:
                            raise RuntimeError(
                                f"Phase-H network schedule consumed {schedule_state['calls']} support calls; expected {expected_calls}"
                            )
                        baseline_present = any(
                            item.realised_high_trait_occupied for item in result.snapshots[0].trait_occupancy
                        )
                        raw_loss_time = dynamics.tau_trait_realised(result)
                        loss_time = None if raw_loss_time is None or raw_loss_time == 0 else raw_loss_time
                        base.update({
                            "status": "completed",
                            "source_prepared": True,
                            "projection_supported": True,
                            "baseline_realised_high_trait_present": baseline_present,
                            "eligible_for_trait_loss_denominator": bool(baseline_present),
                            "trait_loss_time_post_baseline": loss_time,
                            "trait_loss_observed_post_baseline": None if not baseline_present else loss_time is not None,
                        })
                        attempts.append(base)

    artifact = _build_artifact(attempts, source_preparation_count)
    _assert_blind(artifact)
    return artifact


def _regime_for_rows(rows: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], float | None, bool, str]:
    seed_blocks: list[dict[str, Any]] = []
    rates: list[float] = []
    sufficient = True
    for seed in PHASE_H_MASTER_SEEDS:
        seed_rows = [row for row in rows if row["master_seed"] == seed and row["eligible_for_trait_loss_denominator"]]
        seed_losses = [row for row in seed_rows if row["trait_loss_observed_post_baseline"] is True]
        if len(seed_rows) < PHASE_H_MIN_BASELINE_ELIGIBLE_PER_SEED:
            sufficient = False
        rate = None if not seed_rows else len(seed_losses) / len(seed_rows)
        seed_blocks.append({
            "master_seed": seed,
            "baseline_eligible_count": len(seed_rows),
            "trait_loss_count": len(seed_losses),
            "trait_loss_rate": rate,
        })
        if rate is not None:
            rates.append(rate)
    eligible = [row for row in rows if row["eligible_for_trait_loss_denominator"]]
    losses = [row for row in eligible if row["trait_loss_observed_post_baseline"] is True]
    pooled = None if not eligible else len(losses) / len(eligible)
    if not sufficient or len(rates) != len(PHASE_H_MASTER_SEEDS):
        regime = "insufficient_highrep_support"
    else:
        base_regime = classify_seed_rates(tuple(rates))
        regime = {
            "warning_evaluable": "R4_highrep",
            "rapid_loss": "R2_highrep",
            "persistence": "R1_highrep",
            "seed_heterogeneous": "R3_highrep",
        }[base_regime]
    return seed_blocks, pooled, sufficient, regime


def _paired_switches(
    reference_rows: list[dict[str, Any]],
    comparison_rows: list[dict[str, Any]],
    *,
    reference_name: str,
    comparison_name: str,
) -> dict[str, Any]:
    reference = {(row["master_seed"], row["replicate"]): row for row in reference_rows}
    counts = {
        "comparable_pair_count": 0,
        "loss_to_no_loss": 0,
        "no_loss_to_loss": 0,
        "same_loss": 0,
        "same_no_loss": 0,
    }
    for row in comparison_rows:
        ref = reference[(row["master_seed"], row["replicate"])]
        if not (row["eligible_for_trait_loss_denominator"] and ref["eligible_for_trait_loss_denominator"]):
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
    return {
        "reference": reference_name,
        "comparison": comparison_name,
        **counts,
    }


def _build_artifact(attempts: list[dict[str, Any]], source_preparation_count: int) -> dict[str, Any]:
    expected_sources = len(PHASE_H_MASTER_SEEDS) * PHASE_H_REPLICATES_PER_SEED
    expected_rows = expected_sources * len(phase_h_conditions())
    if source_preparation_count != expected_sources:
        raise RuntimeError(f"Phase H must attempt {expected_sources} source preparations")
    if len(attempts) != expected_rows:
        raise RuntimeError(f"Phase H must retain {expected_rows} network-condition rows")

    by_condition: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in attempts:
        by_condition[str(row["network_condition"])].append(row)

    summaries: list[dict[str, Any]] = []
    for condition in phase_h_conditions():
        rows = by_condition[condition.name]
        eligible = [row for row in rows if row["eligible_for_trait_loss_denominator"]]
        losses = [row for row in eligible if row["trait_loss_observed_post_baseline"] is True]
        seed_blocks, pooled, sufficient, regime = _regime_for_rows(rows)
        summaries.append({
            "network_condition": condition.name,
            "rewiring_rule": condition.rewiring_rule,
            "status_counts": {
                "attempted": len(rows),
                "source_prepared": sum(row["source_prepared"] is True for row in rows),
                "projection_supported": sum(row["projection_supported"] is True for row in rows),
                "baseline_eligible": len(eligible),
                "trait_loss": len(losses),
            },
            "seed_blocks": seed_blocks,
            "pooled_trait_loss_rate": pooled,
            "highrep_support_sufficient": sufficient,
            "regime": regime,
            "network_diagnostics": {
                "mean_final_support_multiplier": sum(float(row["support_multiplier_final"]) for row in rows) / len(rows),
                "mean_support_multiplier_over_time": sum(float(row["support_multiplier_mean"]) for row in rows) / len(rows),
                "mean_final_active_edge_count": sum(int(row["final_active_edge_count"]) for row in rows) / len(rows),
                "mean_final_realised_connectance": sum(float(row["final_realised_connectance"]) for row in rows) / len(rows),
                "mean_final_rewired_edge_effort": sum(float(row["final_rewired_edge_effort"]) for row in rows) / len(rows),
                "mean_final_latent_edges_activated": sum(int(row["final_latent_partner_edges_activated"]) for row in rows) / len(rows),
            },
        })

    summary_by_name = {row["network_condition"]: row for row in summaries}
    intact = summary_by_name["intact_control"]
    no_rewiring = summary_by_name["partner_loss_no_rewiring"]
    rewiring = summary_by_name["partner_loss_trait_capacity_rewiring"]
    opening_rule_satisfied = bool(
        intact["highrep_support_sufficient"]
        and intact["regime"] == "R4_highrep"
        and no_rewiring["highrep_support_sufficient"]
        and no_rewiring["regime"] == "R3_highrep"
    )
    if not opening_rule_satisfied:
        rescue_classification = "not_opened"
    elif rewiring["regime"] == "R4_highrep":
        rescue_classification = "rescued_to_R4"
    else:
        rescue_classification = "not_rescued"

    paired = [
        _paired_switches(
            by_condition["intact_control"],
            by_condition["partner_loss_no_rewiring"],
            reference_name="intact_control",
            comparison_name="partner_loss_no_rewiring",
        ),
        _paired_switches(
            by_condition["partner_loss_no_rewiring"],
            by_condition["partner_loss_trait_capacity_rewiring"],
            reference_name="partner_loss_no_rewiring",
            comparison_name="partner_loss_trait_capacity_rewiring",
        ),
    ]

    return {
        "stage": "warning-blind explicit rewiring Phase H",
        "calibration_scope": "source_network_and_trait_loss_only",
        "manifest": phase_h_manifest(),
        "upstream": {"repository": UPSTREAM_REPOSITORY, "commit": UPSTREAM_COMMIT},
        "source_preparation_count": source_preparation_count,
        "opening_rule_satisfied": opening_rule_satisfied,
        "rescue_classification": rescue_classification,
        "network_condition_summaries": summaries,
        "paired_loss_status": paired,
        "attempts": attempts,
    }


def write_phase_h(upstream_checkout: str | Path, output: str | Path) -> Path:
    destination = Path(output)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(run_phase_h(upstream_checkout), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return destination
