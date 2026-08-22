"""Paired warning-blind support/timing decomposition Phase I runner."""
from __future__ import annotations

import importlib
from collections import defaultdict
from dataclasses import replace
from pathlib import Path
from typing import Any

from .explicit_rewiring_phase_h import (
    PHASE_H_AREA_REFERENCE,
    PHASE_H_BARRIER_INCREASE,
    PHASE_H_HOLD_GENERATIONS,
    PHASE_H_INTERACTION_KAPPA,
    PHASE_H_MIGRATION_RATE,
    PHASE_H_RAMP_GENERATIONS,
)
from .explicit_rewiring_phase_h_runner import patched_interaction_support_schedule
from .protocol002_calibration import assert_protocol002_blind_calibration_columns
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
from .support_timing_phase_i import (
    PHASE_I_MASTER_SEEDS,
    PHASE_I_MIN_BASELINE_ELIGIBLE_PER_SEED,
    PHASE_I_REPLICATES_PER_SEED,
    phase_i_conditions,
    phase_i_coordinate,
    phase_i_manifest,
    phase_i_schedule,
)


def _assert_blind(value: Any) -> None:
    if isinstance(value, dict):
        assert_protocol002_blind_calibration_columns(value.keys())
        for child in value.values():
            _assert_blind(child)
    elif isinstance(value, (list, tuple)):
        for child in value:
            _assert_blind(child)


def _condition_schedule(condition: Any, replicate_index: int, generations: int) -> tuple[tuple[float, ...], dict[str, Any]]:
    schedule = phase_i_schedule(condition, replicate_index, generations)
    effective = tuple(float(row["effective_support_multiplier"]) for row in schedule)
    raw = tuple(float(row["raw_topology_support_multiplier"]) for row in schedule)
    final = schedule[-1]
    final_edges = tuple(float(value) for value in final["edge_strengths"])
    diagnostics = {
        "network_condition": condition.name,
        "topology_rule": condition.topology_rule,
        "effective_support_rule": condition.effective_support_rule,
        "effective_support_first": effective[0],
        "effective_support_final": effective[-1],
        "effective_support_mean": sum(effective) / len(effective),
        "effective_support_min": min(effective),
        "effective_support_max": max(effective),
        "raw_topology_support_first": raw[0],
        "raw_topology_support_final": raw[-1],
        "raw_topology_support_mean": sum(raw) / len(raw),
        "final_edge_strengths": list(final_edges),
        "final_active_edge_count": int(final["active_edge_count"]),
        "final_realised_connectance": float(final["realised_connectance"]),
    }
    return effective, diagnostics


def _regime_for_rows(rows: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], float | None, bool, str]:
    seed_blocks: list[dict[str, Any]] = []
    rates: list[float] = []
    sufficient = True
    for seed in PHASE_I_MASTER_SEEDS:
        seed_rows = [row for row in rows if row["master_seed"] == seed and row["eligible_for_trait_loss_denominator"]]
        seed_losses = [row for row in seed_rows if row["trait_loss_observed_post_baseline"] is True]
        if len(seed_rows) < PHASE_I_MIN_BASELINE_ELIGIBLE_PER_SEED:
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
    if not sufficient or len(rates) != len(PHASE_I_MASTER_SEEDS):
        regime = "insufficient_highrep_support"
    else:
        regime = {
            "warning_evaluable": "R4_highrep",
            "rapid_loss": "R2_highrep",
            "persistence": "R1_highrep",
            "seed_heterogeneous": "R3_highrep",
        }[classify_seed_rates(tuple(rates))]
    return seed_blocks, pooled, sufficient, regime


def _paired_switches(reference_rows: list[dict[str, Any]], comparison_rows: list[dict[str, Any]], reference_name: str, comparison_name: str) -> dict[str, Any]:
    reference = {(row["master_seed"], row["replicate"]): row for row in reference_rows}
    counts = {"comparable_pair_count": 0, "loss_to_no_loss": 0, "no_loss_to_loss": 0, "same_loss": 0, "same_no_loss": 0}
    eligibility_mismatch = 0
    for row in comparison_rows:
        ref = reference[(row["master_seed"], row["replicate"])]
        if row["eligible_for_trait_loss_denominator"] != ref["eligible_for_trait_loss_denominator"]:
            eligibility_mismatch += 1
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
    return {"reference": reference_name, "comparison": comparison_name, "eligibility_mismatch_count": eligibility_mismatch, **counts}


def _biological_identity(pair: dict[str, Any]) -> bool:
    return (
        pair["eligibility_mismatch_count"] == 0
        and pair["loss_to_no_loss"] == 0
        and pair["no_loss_to_loss"] == 0
    )


def run_phase_i(upstream_checkout: str | Path) -> dict[str, Any]:
    checkout = Path(upstream_checkout)
    if not checkout.exists():
        raise FileNotFoundError(f"upstream checkout does not exist: {checkout}")

    coordinate = phase_i_coordinate()
    conditions = phase_i_conditions()
    driver_rate = coordinate.kappa_mu / 2.0
    total_generations = PHASE_H_RAMP_GENERATIONS + PHASE_H_HOLD_GENERATIONS
    attempts: list[dict[str, Any]] = []
    source_preparation_count = 0

    with _upstream_import_path(checkout):
        audit = importlib.import_module(UPSTREAM_H1_MODULE)
        experiments = importlib.import_module(UPSTREAM_EXPERIMENT_MODULE)
        mutation = importlib.import_module(UPSTREAM_MUTATION_MODULE)
        runtime = importlib.import_module(UPSTREAM_CHAIN_RUNTIME_MODULE)
        calibration = importlib.import_module(UPSTREAM_CALIBRATION_MODULE)
        dynamics = importlib.import_module(UPSTREAM_DYNAMICS_MODULE)
        chain = runtime.chain

        deterioration = calibration.RampHoldSchedule(PHASE_H_RAMP_GENERATIONS, PHASE_H_HOLD_GENERATIONS, PHASE_H_BARRIER_INCREASE)

        for master_seed in PHASE_I_MASTER_SEEDS:
            spec = replace(
                experiments.standard_profile(),
                experiment_id="support_timing_phase_i",
                generations=1,
                replicates=PHASE_I_REPLICATES_PER_SEED,
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
                    raise RuntimeError("Phase I must return exactly one H1 cell per master seed")
                cell = cells[0]
                isolated = experiments.scenario_equal_isolated(spec)
                scenario = experiments.LandscapeScenario(
                    scenario_id="equal_fragmented_support_timing_phase_i",
                    patch_areas=isolated.patch_areas,
                    migration_rate=PHASE_H_MIGRATION_RATE,
                )

                for record in cell.replicates:
                    source_preparation_count += 1
                    source_base = {
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
                    schedules = {condition.name: _condition_schedule(condition, record.replicate_index, total_generations) for condition in conditions}
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
                            _, diagnostics = schedules[condition.name]
                            attempts.append({**source_base, **diagnostics, "status": "source_preparation_failed", "source_prepared": False, "projection_supported": None, "baseline_realised_high_trait_present": None, "eligible_for_trait_loss_denominator": False, "trait_loss_time_post_baseline": None, "trait_loss_observed_post_baseline": None})
                        continue

                    source, anchor_barrier = prepared
                    interval = cell.canonical_bistable_barrier_interval
                    if interval is None or interval[1] <= interval[0]:
                        raise RuntimeError("prepared Phase-I source requires a positive canonical interval")
                    barriers = calibration.ramp_and_hold_barrier_schedule(
                        anchor_barrier=anchor_barrier,
                        canonical_interval_width=interval[1] - interval[0],
                        schedule=deterioration,
                    )
                    template = chain.parameters_for_cell(spec, scenario, replace(cell.parameters, interaction_barrier=anchor_barrier), seed=record.seed)
                    projected, invariants = chain.project_full_state(source, template)

                    for condition in conditions:
                        multipliers, diagnostics = schedules[condition.name]
                        base = {**source_base, **diagnostics}
                        if not invariants.projection_supported:
                            attempts.append({**base, "status": "projection_failed", "source_prepared": True, "projection_supported": False, "baseline_realised_high_trait_present": None, "eligible_for_trait_loss_denominator": False, "trait_loss_time_post_baseline": None, "trait_loss_observed_post_baseline": None})
                            continue
                        with patched_interaction_support_schedule(mutation, multipliers, patch_count=len(projected.patch_areas)) as state:
                            result = mutation.simulate_with_symmetric_allele_mutation(
                                replace(projected, generations=total_generations, random_seed=record.seed),
                                mutation_rate=driver_rate,
                                interaction_barrier_schedule=barriers,
                            )
                        if state["calls"] != total_generations * len(projected.patch_areas):
                            raise RuntimeError("Phase-I support schedule call count mismatch")
                        baseline_present = any(item.realised_high_trait_occupied for item in result.snapshots[0].trait_occupancy)
                        raw_loss_time = dynamics.tau_trait_realised(result)
                        loss_time = None if raw_loss_time is None or raw_loss_time == 0 else raw_loss_time
                        attempts.append({
                            **base,
                            "status": "completed",
                            "source_prepared": True,
                            "projection_supported": True,
                            "baseline_realised_high_trait_present": baseline_present,
                            "eligible_for_trait_loss_denominator": bool(baseline_present),
                            "trait_loss_time_post_baseline": loss_time,
                            "trait_loss_observed_post_baseline": None if not baseline_present else loss_time is not None,
                        })

    artifact = _build_artifact(attempts, source_preparation_count)
    _assert_blind(artifact)
    return artifact


def _build_artifact(attempts: list[dict[str, Any]], source_preparation_count: int) -> dict[str, Any]:
    expected_sources = len(PHASE_I_MASTER_SEEDS) * PHASE_I_REPLICATES_PER_SEED
    expected_rows = expected_sources * len(phase_i_conditions())
    if source_preparation_count != expected_sources or len(attempts) != expected_rows:
        raise RuntimeError("Phase-I attempted row count does not match preregistration")

    by_condition: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in attempts:
        by_condition[str(row["network_condition"])].append(row)

    summaries = []
    regimes = {}
    for condition in phase_i_conditions():
        rows = by_condition[condition.name]
        eligible = [row for row in rows if row["eligible_for_trait_loss_denominator"]]
        losses = [row for row in eligible if row["trait_loss_observed_post_baseline"] is True]
        seed_blocks, pooled, sufficient, regime = _regime_for_rows(rows)
        regimes[condition.name] = regime
        summaries.append({
            "network_condition": condition.name,
            "topology_rule": condition.topology_rule,
            "effective_support_rule": condition.effective_support_rule,
            "status_counts": {"attempted": len(rows), "source_prepared": sum(row["source_prepared"] is True for row in rows), "projection_supported": sum(row["projection_supported"] is True for row in rows), "baseline_eligible": len(eligible), "trait_loss": len(losses)},
            "seed_blocks": seed_blocks,
            "pooled_trait_loss_rate": pooled,
            "highrep_support_sufficient": sufficient,
            "regime": regime,
            "diagnostics": {
                "mean_final_active_edge_count": sum(float(row["final_active_edge_count"]) for row in rows) / len(rows),
                "mean_final_realised_connectance": sum(float(row["final_realised_connectance"]) for row in rows) / len(rows),
                "mean_effective_support_first": sum(float(row["effective_support_first"]) for row in rows) / len(rows),
                "mean_effective_support_final": sum(float(row["effective_support_final"]) for row in rows) / len(rows),
                "mean_effective_support_over_time": sum(float(row["effective_support_mean"]) for row in rows) / len(rows),
                "mean_raw_topology_support_final": sum(float(row["raw_topology_support_final"]) for row in rows) / len(rows),
            },
        })

    pairs = [
        _paired_switches(by_condition["partner_loss_no_rescue"], by_condition["topology_only_null"], "partner_loss_no_rescue", "topology_only_null"),
        _paired_switches(by_condition["partial_support_only"], by_condition["coupled_rewiring_replay"], "partial_support_only", "coupled_rewiring_replay"),
        _paired_switches(by_condition["intact_control"], by_condition["full_support_immediate"], "intact_control", "full_support_immediate"),
        _paired_switches(by_condition["partner_loss_no_rescue"], by_condition["partial_support_only"], "partner_loss_no_rescue", "partial_support_only"),
        _paired_switches(by_condition["partner_loss_no_rescue"], by_condition["full_support_delayed"], "partner_loss_no_rescue", "full_support_delayed"),
    ]
    representation_audit = {
        "topology_only_null_matches_no_rescue": _biological_identity(pairs[0]),
        "partial_support_only_matches_coupled_rewiring": _biological_identity(pairs[1]),
        "full_support_immediate_matches_intact": _biological_identity(pairs[2]),
    }
    opening = regimes["intact_control"] == "R4_highrep" and regimes["partner_loss_no_rescue"] == "R3_highrep"
    if not opening:
        classification = "not_opened"
    elif not all(representation_audit.values()):
        classification = "representation_audit_failed"
    elif regimes["partial_support_only"] == "R4_highrep":
        classification = "partial_support_sufficient"
    elif regimes["full_support_delayed"] == "R4_highrep":
        classification = "support_magnitude_limiting"
    elif regimes["full_support_immediate"] == "R4_highrep":
        classification = "recovery_timing_path_dependence"
    else:
        classification = "positive_control_failed"

    return {
        "stage": "warning-blind support/timing decomposition Phase I",
        "calibration_scope": "source_network_and_trait_loss_only",
        "manifest": phase_i_manifest(),
        "source_preparation_count": source_preparation_count,
        "opening_rule_satisfied": opening,
        "representation_audit": representation_audit,
        "causal_classification": classification,
        "condition_summaries": summaries,
        "paired_loss_status": pairs,
        "attempts": attempts,
    }
