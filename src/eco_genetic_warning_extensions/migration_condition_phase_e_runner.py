"""Paired warning-blind migration-condition Phase E runner."""
from __future__ import annotations

import importlib
import json
from collections import defaultdict
from dataclasses import replace
from pathlib import Path
from typing import Any

from .migration_condition_phase_e import (
    PHASE_E_AREA_REFERENCE,
    PHASE_E_BARRIER_INCREASE,
    PHASE_E_HOLD_GENERATIONS,
    PHASE_E_INTERACTION_KAPPA,
    PHASE_E_MASTER_SEEDS,
    PHASE_E_MIN_BASELINE_ELIGIBLE_PER_SEED,
    PHASE_E_RAMP_GENERATIONS,
    PHASE_E_REPLICATES_PER_SEED,
    phase_e_conditions,
    phase_e_coordinate,
    phase_e_manifest,
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


def run_phase_e(upstream_checkout: str | Path) -> dict[str, Any]:
    checkout = Path(upstream_checkout)
    if not checkout.exists():
        raise FileNotFoundError(f"upstream checkout does not exist: {checkout}")

    coordinate = phase_e_coordinate()
    conditions = phase_e_conditions()
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
            PHASE_E_RAMP_GENERATIONS,
            PHASE_E_HOLD_GENERATIONS,
            PHASE_E_BARRIER_INCREASE,
        )

        for master_seed in PHASE_E_MASTER_SEEDS:
            spec = replace(
                experiments.standard_profile(),
                experiment_id="migration_condition_phase_e",
                generations=1,
                replicates=PHASE_E_REPLICATES_PER_SEED,
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
                    raise RuntimeError("Phase E must return exactly one H1 cell per master seed")
                cell = cells[0]
                isolated = experiments.scenario_equal_isolated(spec)

                for record in cell.replicates:
                    source_preparation_count += 1
                    source_base: dict[str, Any] = {
                        "kappa_mu": coordinate.kappa_mu,
                        "p_star": coordinate.p_star,
                        "area_reference": PHASE_E_AREA_REFERENCE,
                        "kappa": PHASE_E_INTERACTION_KAPPA,
                        "ramp_generations": PHASE_E_RAMP_GENERATIONS,
                        "hold_generations": PHASE_E_HOLD_GENERATIONS,
                        "horizon": PHASE_E_RAMP_GENERATIONS + PHASE_E_HOLD_GENERATIONS,
                        "normalised_barrier_increase": PHASE_E_BARRIER_INCREASE,
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
                            attempts.append({
                                **source_base,
                                "migration_rate": condition.migration_rate,
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
                        raise RuntimeError("prepared Phase-E source requires a positive canonical interval")
                    interval_width = interval[1] - interval[0]
                    barriers = calibration.ramp_and_hold_barrier_schedule(
                        anchor_barrier=anchor_barrier,
                        canonical_interval_width=interval_width,
                        schedule=schedule,
                    )

                    for condition in conditions:
                        scenario = experiments.LandscapeScenario(
                            scenario_id=f"equal_fragmented_m_{condition.migration_rate:.3f}",
                            patch_areas=isolated.patch_areas,
                            migration_rate=condition.migration_rate,
                        )
                        template = chain.parameters_for_cell(
                            spec,
                            scenario,
                            replace(cell.parameters, interaction_barrier=anchor_barrier),
                            seed=record.seed,
                        )
                        projected, invariants = chain.project_full_state(source, template)
                        base = {**source_base, "migration_rate": condition.migration_rate}
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


def _build_artifact(attempts: list[dict[str, Any]], source_preparation_count: int) -> dict[str, Any]:
    expected_sources = len(PHASE_E_MASTER_SEEDS) * PHASE_E_REPLICATES_PER_SEED
    expected_rows = expected_sources * len(phase_e_conditions())
    if source_preparation_count != expected_sources:
        raise RuntimeError(f"Phase E must attempt {expected_sources} source preparations")
    if len(attempts) != expected_rows:
        raise RuntimeError(f"Phase E must retain {expected_rows} migration-level rows")

    by_rate: dict[float, list[dict[str, Any]]] = defaultdict(list)
    for row in attempts:
        by_rate[float(row["migration_rate"])].append(row)

    condition_rows: list[dict[str, Any]] = []
    for condition in phase_e_conditions():
        rate = condition.migration_rate
        rows = by_rate[rate]
        eligible = [row for row in rows if row["eligible_for_trait_loss_denominator"]]
        losses = [row for row in eligible if row["trait_loss_observed_post_baseline"] is True]
        seed_blocks = []
        rates = []
        sufficient = True
        for seed in PHASE_E_MASTER_SEEDS:
            seed_eligible = [row for row in eligible if row["master_seed"] == seed]
            seed_losses = [row for row in seed_eligible if row["trait_loss_observed_post_baseline"] is True]
            if len(seed_eligible) < PHASE_E_MIN_BASELINE_ELIGIBLE_PER_SEED:
                sufficient = False
            seed_rate = None if not seed_eligible else len(seed_losses) / len(seed_eligible)
            seed_blocks.append({
                "master_seed": seed,
                "baseline_eligible_count": len(seed_eligible),
                "trait_loss_count": len(seed_losses),
                "trait_loss_rate": seed_rate,
            })
            if seed_rate is not None:
                rates.append(seed_rate)

        if not sufficient or len(rates) != len(PHASE_E_MASTER_SEEDS):
            regime = "insufficient_highrep_support"
        else:
            base_regime = classify_seed_rates(tuple(rates))
            regime = {
                "warning_evaluable": "R4_highrep",
                "rapid_loss": "R2_highrep",
                "persistence": "R1_highrep",
                "seed_heterogeneous": "R3_highrep",
            }[base_regime]

        condition_rows.append({
            "migration_rate": rate,
            "status_counts": {
                "attempted": len(rows),
                "source_prepared": sum(row["source_prepared"] is True for row in rows),
                "projection_supported": sum(row["projection_supported"] is True for row in rows),
                "baseline_eligible": len(eligible),
                "trait_loss": len(losses),
            },
            "seed_blocks": seed_blocks,
            "seed_rate_range": None if not rates else max(rates) - min(rates),
            "pooled_trait_loss_rate": None if not eligible else len(losses) / len(eligible),
            "highrep_support_sufficient": sufficient,
            "regime": regime,
        })

    reference = {(row["master_seed"], row["replicate"]): row for row in by_rate[0.0]}
    paired_rows = []
    for condition in phase_e_conditions()[1:]:
        comparable = 0
        loss_to_no_loss = 0
        no_loss_to_loss = 0
        same_loss = 0
        same_no_loss = 0
        for row in by_rate[condition.migration_rate]:
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
            "migration_rate": condition.migration_rate,
            "reference_migration_rate": 0.0,
            "comparable_pair_count": comparable,
            "loss_to_no_loss": loss_to_no_loss,
            "no_loss_to_loss": no_loss_to_loss,
            "same_loss": same_loss,
            "same_no_loss": same_no_loss,
        })

    return {
        "stage": "warning-blind migration-condition Phase E",
        "calibration_scope": "trait_loss_only",
        "manifest": phase_e_manifest(),
        "upstream": {"repository": UPSTREAM_REPOSITORY, "commit": UPSTREAM_COMMIT},
        "source_preparation_count": source_preparation_count,
        "migration_condition_summaries": condition_rows,
        "paired_loss_status_vs_isolation": paired_rows,
        "attempts": attempts,
        "domain_selected": False,
    }


def write_phase_e(upstream_checkout: str | Path, output: str | Path) -> Path:
    destination = Path(output)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(run_phase_e(upstream_checkout), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return destination
