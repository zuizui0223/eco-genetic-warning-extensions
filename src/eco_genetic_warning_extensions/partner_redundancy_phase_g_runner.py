"""Paired warning-blind partner-redundancy Phase G runner."""
from __future__ import annotations

import importlib
import json
from collections import defaultdict
from contextlib import contextmanager
from dataclasses import replace
from pathlib import Path
from typing import Any, Iterator

from .partner_redundancy_phase_g import (
    PHASE_G_AREA_REFERENCE,
    PHASE_G_BARRIER_INCREASE,
    PHASE_G_HOLD_GENERATIONS,
    PHASE_G_INTERACTION_KAPPA,
    PHASE_G_MASTER_SEEDS,
    PHASE_G_MIGRATION_RATE,
    PHASE_G_MIN_BASELINE_ELIGIBLE_PER_SEED,
    PHASE_G_RAMP_GENERATIONS,
    PHASE_G_REPLICATES_PER_SEED,
    lost_partner_index,
    phase_g_conditions,
    phase_g_coordinate,
    phase_g_manifest,
    retained_support,
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
def patched_interaction_support_multiplier(mutation_module: Any, multiplier: float) -> Iterator[None]:
    """Scale the local interaction-support signal during the deterioration run only."""
    factor = float(multiplier)
    if not 0.0 <= factor <= 1.0:
        raise ValueError("interaction support multiplier must lie in [0, 1]")
    original = mutation_module.interaction_support_signal

    def scaled_signal(interaction: float, realised_high_trait_mass: float, high_allele_frequency: float, parameters: Any) -> float:
        return factor * original(interaction, realised_high_trait_mass, high_allele_frequency, parameters)

    mutation_module.interaction_support_signal = scaled_signal
    try:
        yield
    finally:
        mutation_module.interaction_support_signal = original


def run_phase_g(upstream_checkout: str | Path) -> dict[str, Any]:
    checkout = Path(upstream_checkout)
    if not checkout.exists():
        raise FileNotFoundError(f"upstream checkout does not exist: {checkout}")

    coordinate = phase_g_coordinate()
    conditions = phase_g_conditions()
    driver_rate = coordinate.kappa_mu / 2.0
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

        schedule = calibration.RampHoldSchedule(
            PHASE_G_RAMP_GENERATIONS,
            PHASE_G_HOLD_GENERATIONS,
            PHASE_G_BARRIER_INCREASE,
        )

        for master_seed in PHASE_G_MASTER_SEEDS:
            spec = replace(
                experiments.standard_profile(),
                experiment_id="partner_redundancy_phase_g",
                generations=1,
                replicates=PHASE_G_REPLICATES_PER_SEED,
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
                    raise RuntimeError("Phase G must return exactly one H1 cell per master seed")
                cell = cells[0]
                isolated = experiments.scenario_equal_isolated(spec)
                scenario = experiments.LandscapeScenario(
                    scenario_id="equal_fragmented_partner_redundancy_phase_g",
                    patch_areas=isolated.patch_areas,
                    migration_rate=PHASE_G_MIGRATION_RATE,
                )

                for record in cell.replicates:
                    source_preparation_count += 1
                    source_base: dict[str, Any] = {
                        "kappa_mu": coordinate.kappa_mu,
                        "p_star": coordinate.p_star,
                        "area_reference": PHASE_G_AREA_REFERENCE,
                        "kappa": PHASE_G_INTERACTION_KAPPA,
                        "migration_rate": PHASE_G_MIGRATION_RATE,
                        "ramp_generations": PHASE_G_RAMP_GENERATIONS,
                        "hold_generations": PHASE_G_HOLD_GENERATIONS,
                        "horizon": PHASE_G_RAMP_GENERATIONS + PHASE_G_HOLD_GENERATIONS,
                        "normalised_barrier_increase": PHASE_G_BARRIER_INCREASE,
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
                        for condition in conditions:
                            index = None if not condition.remove_one_partner else lost_partner_index(record.replicate_index)
                            attempts.append({
                                **source_base,
                                "partner_architecture": condition.name,
                                "partner_contribution_cv": condition.contribution_cv,
                                "lost_partner_index": index,
                                "lost_partner_weight": None if index is None else condition.partner_weights[index],
                                "retained_interaction_support": retained_support(condition, record.replicate_index),
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
                        raise RuntimeError("prepared Phase-G source requires a positive canonical interval")
                    interval_width = interval[1] - interval[0]
                    barriers = calibration.ramp_and_hold_barrier_schedule(
                        anchor_barrier=anchor_barrier,
                        canonical_interval_width=interval_width,
                        schedule=schedule,
                    )
                    template = chain.parameters_for_cell(
                        spec,
                        scenario,
                        replace(cell.parameters, interaction_barrier=anchor_barrier),
                        seed=record.seed,
                    )
                    projected, invariants = chain.project_full_state(source, template)

                    for condition in conditions:
                        index = None if not condition.remove_one_partner else lost_partner_index(record.replicate_index)
                        multiplier = retained_support(condition, record.replicate_index)
                        base = {
                            **source_base,
                            "partner_architecture": condition.name,
                            "partner_contribution_cv": condition.contribution_cv,
                            "lost_partner_index": index,
                            "lost_partner_weight": None if index is None else condition.partner_weights[index],
                            "retained_interaction_support": multiplier,
                        }
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

                        with patched_interaction_support_multiplier(mutation, multiplier):
                            result = mutation.simulate_with_symmetric_allele_mutation(
                                replace(projected, generations=schedule.total_generations, random_seed=record.seed),
                                mutation_rate=driver_rate,
                                interaction_barrier_schedule=barriers,
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
    for seed in PHASE_G_MASTER_SEEDS:
        seed_rows = [row for row in rows if row["master_seed"] == seed and row["eligible_for_trait_loss_denominator"]]
        seed_losses = [row for row in seed_rows if row["trait_loss_observed_post_baseline"] is True]
        if len(seed_rows) < PHASE_G_MIN_BASELINE_ELIGIBLE_PER_SEED:
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
    if not sufficient or len(rates) != len(PHASE_G_MASTER_SEEDS):
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


def _build_artifact(attempts: list[dict[str, Any]], source_preparation_count: int) -> dict[str, Any]:
    expected_sources = len(PHASE_G_MASTER_SEEDS) * PHASE_G_REPLICATES_PER_SEED
    expected_rows = expected_sources * len(phase_g_conditions())
    if source_preparation_count != expected_sources:
        raise RuntimeError(f"Phase G must attempt {expected_sources} source preparations")
    if len(attempts) != expected_rows:
        raise RuntimeError(f"Phase G must retain {expected_rows} architecture-level rows")

    by_condition: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in attempts:
        by_condition[str(row["partner_architecture"])].append(row)

    condition_rows: list[dict[str, Any]] = []
    for condition in phase_g_conditions():
        rows = by_condition[condition.name]
        eligible = [row for row in rows if row["eligible_for_trait_loss_denominator"]]
        losses = [row for row in eligible if row["trait_loss_observed_post_baseline"] is True]
        seed_blocks, pooled, sufficient, regime = _regime_for_rows(rows)
        support_values = [float(row["retained_interaction_support"]) for row in rows]
        strata = []
        if condition.remove_one_partner:
            for index in range(4):
                stratum = [row for row in rows if row["lost_partner_index"] == index]
                stratum_eligible = [row for row in stratum if row["eligible_for_trait_loss_denominator"]]
                stratum_losses = [row for row in stratum_eligible if row["trait_loss_observed_post_baseline"] is True]
                strata.append({
                    "lost_partner_index": index,
                    "partner_weight": condition.partner_weights[index],
                    "retained_interaction_support": 1.0 - condition.partner_weights[index],
                    "attempted_count": len(stratum),
                    "baseline_eligible_count": len(stratum_eligible),
                    "trait_loss_count": len(stratum_losses),
                    "pooled_trait_loss_rate": None if not stratum_eligible else len(stratum_losses) / len(stratum_eligible),
                })
        condition_rows.append({
            "partner_architecture": condition.name,
            "partner_weights": list(condition.partner_weights),
            "partner_contribution_cv": condition.contribution_cv,
            "remove_one_partner": condition.remove_one_partner,
            "retained_support_mean": sum(support_values) / len(support_values),
            "retained_support_min": min(support_values),
            "retained_support_max": max(support_values),
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
            "partner_loss_strata": strata,
        })

    reference = {(row["master_seed"], row["replicate"]): row for row in by_condition["intact_control"]}
    paired_rows = []
    for condition in phase_g_conditions()[1:]:
        comparable = 0
        loss_to_no_loss = 0
        no_loss_to_loss = 0
        same_loss = 0
        same_no_loss = 0
        for row in by_condition[condition.name]:
            ref = reference[(row["master_seed"], row["replicate"])]
            if not (row["eligible_for_trait_loss_denominator"] and ref["eligible_for_trait_loss_denominator"]):
                continue
            comparable += 1
            ref_loss = ref["trait_loss_observed_post_baseline"] is True
            new_loss = row["trait_loss_observed_post_baseline"] is True
            if ref_loss and not new_loss:
                loss_to_no_loss += 1
            elif not ref_loss and new_loss:
                no_loss_to_loss += 1
            elif ref_loss and new_loss:
                same_loss += 1
            else:
                same_no_loss += 1
        paired_rows.append({
            "partner_architecture": condition.name,
            "reference": "intact_control",
            "comparable_pair_count": comparable,
            "loss_to_no_loss": loss_to_no_loss,
            "no_loss_to_loss": no_loss_to_loss,
            "same_loss": same_loss,
            "same_no_loss": same_no_loss,
        })

    intact_row = next(row for row in condition_rows if row["partner_architecture"] == "intact_control")
    opening_rule_satisfied = bool(intact_row["highrep_support_sufficient"] and intact_row["regime"] == "R4_highrep")
    return {
        "stage": "warning-blind partner-redundancy Phase G",
        "calibration_scope": "source_and_trait_loss_only",
        "manifest": phase_g_manifest(),
        "upstream": {"repository": UPSTREAM_REPOSITORY, "commit": UPSTREAM_COMMIT},
        "source_preparation_count": source_preparation_count,
        "opening_rule_satisfied": opening_rule_satisfied,
        "partner_architecture_summaries": condition_rows,
        "paired_loss_status_vs_intact": paired_rows,
        "attempts": attempts,
        "domain_selected": False,
    }


def write_phase_g(upstream_checkout: str | Path, output: str | Path) -> Path:
    destination = Path(output)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(run_phase_g(upstream_checkout), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return destination
