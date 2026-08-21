"""High-rep warning-blind interaction-support Phase F runner."""
from __future__ import annotations

import importlib
import json
from collections import defaultdict
from dataclasses import replace
from pathlib import Path
from typing import Any

from .interaction_support_phase_f import (
    PHASE_F_AREA_REFERENCE,
    PHASE_F_BARRIER_INCREASE,
    PHASE_F_HOLD_GENERATIONS,
    PHASE_F_MASTER_SEEDS,
    PHASE_F_MIGRATION_RATE,
    PHASE_F_MIN_BASELINE_ELIGIBLE_PER_SEED,
    PHASE_F_RAMP_GENERATIONS,
    PHASE_F_REPLICATES_PER_SEED,
    phase_f_conditions,
    phase_f_coordinate,
    phase_f_manifest,
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


def run_phase_f(upstream_checkout: str | Path) -> dict[str, Any]:
    checkout = Path(upstream_checkout)
    if not checkout.exists():
        raise FileNotFoundError(f"upstream checkout does not exist: {checkout}")

    coordinate = phase_f_coordinate()
    driver_rate = coordinate.kappa_mu / 2.0
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
            PHASE_F_RAMP_GENERATIONS,
            PHASE_F_HOLD_GENERATIONS,
            PHASE_F_BARRIER_INCREASE,
        )

        for condition in phase_f_conditions():
            kappa = condition.interaction_kappa
            for master_seed in PHASE_F_MASTER_SEEDS:
                # kappa changes the H1 source geometry, so each condition receives
                # an independent source reconstruction rather than reusing a source
                # prepared at kappa=4.5.
                spec = replace(
                    experiments.standard_profile(),
                    experiment_id=f"interaction_support_phase_f_kappa_{kappa:g}",
                    generations=1,
                    replicates=PHASE_F_REPLICATES_PER_SEED,
                    master_seed=master_seed,
                    area_reference_values=(PHASE_F_AREA_REFERENCE,),
                    interaction_feedback_values=(kappa,),
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
                        raise RuntimeError("Phase F must return exactly one H1 cell per condition and master seed")
                    cell = cells[0]
                    isolated = experiments.scenario_equal_isolated(spec)

                    for record in cell.replicates:
                        base: dict[str, Any] = {
                            "kappa_mu": coordinate.kappa_mu,
                            "p_star": coordinate.p_star,
                            "area_reference": PHASE_F_AREA_REFERENCE,
                            "kappa": kappa,
                            "interaction_kappa": kappa,
                            "migration_rate": PHASE_F_MIGRATION_RATE,
                            "ramp_generations": PHASE_F_RAMP_GENERATIONS,
                            "hold_generations": PHASE_F_HOLD_GENERATIONS,
                            "horizon": PHASE_F_RAMP_GENERATIONS + PHASE_F_HOLD_GENERATIONS,
                            "normalised_barrier_increase": PHASE_F_BARRIER_INCREASE,
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
                            base.update({
                                "status": "source_preparation_failed",
                                "source_prepared": False,
                                "projection_supported": None,
                                "baseline_realised_high_trait_present": None,
                                "eligible_for_trait_loss_denominator": False,
                                "trait_loss_time_post_baseline": None,
                                "trait_loss_observed_post_baseline": None,
                            })
                            attempts.append(base)
                            continue

                        source, anchor_barrier = prepared
                        interval = cell.canonical_bistable_barrier_interval
                        if interval is None or interval[1] <= interval[0]:
                            raise RuntimeError("prepared Phase-F source requires a positive canonical interval")
                        interval_width = interval[1] - interval[0]
                        barriers = calibration.ramp_and_hold_barrier_schedule(
                            anchor_barrier=anchor_barrier,
                            canonical_interval_width=interval_width,
                            schedule=schedule,
                        )
                        scenario = experiments.LandscapeScenario(
                            scenario_id=f"equal_fragmented_kappa_{kappa:g}",
                            patch_areas=isolated.patch_areas,
                            migration_rate=PHASE_F_MIGRATION_RATE,
                        )
                        template = chain.parameters_for_cell(
                            spec,
                            scenario,
                            replace(cell.parameters, interaction_barrier=anchor_barrier),
                            seed=record.seed,
                        )
                        projected, invariants = chain.project_full_state(source, template)
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

    artifact = _build_artifact(attempts)
    _assert_blind(artifact)
    return artifact


def _build_artifact(attempts: list[dict[str, Any]]) -> dict[str, Any]:
    expected_per_condition = len(PHASE_F_MASTER_SEEDS) * PHASE_F_REPLICATES_PER_SEED
    expected_rows = expected_per_condition * len(phase_f_conditions())
    if len(attempts) != expected_rows:
        raise RuntimeError(f"Phase F must retain {expected_rows} rows")

    by_kappa: dict[float, list[dict[str, Any]]] = defaultdict(list)
    for row in attempts:
        by_kappa[float(row["interaction_kappa"])].append(row)

    condition_rows: list[dict[str, Any]] = []
    for condition in phase_f_conditions():
        kappa = condition.interaction_kappa
        rows = by_kappa[kappa]
        prepared = [row for row in rows if row["source_prepared"] is True]
        projected = [row for row in rows if row["projection_supported"] is True]
        eligible = [row for row in rows if row["eligible_for_trait_loss_denominator"]]
        losses = [row for row in eligible if row["trait_loss_observed_post_baseline"] is True]

        seed_blocks = []
        rates = []
        sufficient = True
        for seed in PHASE_F_MASTER_SEEDS:
            seed_rows = [row for row in rows if row["master_seed"] == seed]
            seed_eligible = [row for row in seed_rows if row["eligible_for_trait_loss_denominator"]]
            seed_losses = [row for row in seed_eligible if row["trait_loss_observed_post_baseline"] is True]
            if len(seed_eligible) < PHASE_F_MIN_BASELINE_ELIGIBLE_PER_SEED:
                sufficient = False
            rate = None if not seed_eligible else len(seed_losses) / len(seed_eligible)
            seed_blocks.append({
                "master_seed": seed,
                "attempted_count": len(seed_rows),
                "source_prepared_count": sum(row["source_prepared"] is True for row in seed_rows),
                "baseline_eligible_count": len(seed_eligible),
                "trait_loss_count": len(seed_losses),
                "trait_loss_rate": rate,
            })
            if rate is not None:
                rates.append(rate)

        if not sufficient or len(rates) != len(PHASE_F_MASTER_SEEDS):
            regime = "C0_source_or_baseline_limited"
        else:
            base_regime = classify_seed_rates(tuple(rates))
            regime = {
                "warning_evaluable": "R4_highrep",
                "rapid_loss": "R2_highrep",
                "persistence": "R1_highrep",
                "seed_heterogeneous": "R3_highrep",
            }[base_regime]

        condition_rows.append({
            "interaction_kappa": kappa,
            "source_preparation_rate": len(prepared) / len(rows),
            "projection_supported_rate": len(projected) / len(rows),
            "baseline_eligible_rate": len(eligible) / len(rows),
            "status_counts": {
                "attempted": len(rows),
                "source_prepared": len(prepared),
                "projection_supported": len(projected),
                "baseline_eligible": len(eligible),
                "trait_loss": len(losses),
            },
            "seed_blocks": seed_blocks,
            "seed_rate_range": None if not rates else max(rates) - min(rates),
            "pooled_trait_loss_rate": None if not eligible else len(losses) / len(eligible),
            "highrep_support_sufficient": sufficient,
            "regime": regime,
        })

    return {
        "stage": "warning-blind interaction-support Phase F",
        "calibration_scope": "source_and_trait_loss_only",
        "manifest": phase_f_manifest(),
        "upstream": {"repository": UPSTREAM_REPOSITORY, "commit": UPSTREAM_COMMIT},
        "interaction_support_summaries": condition_rows,
        "attempts": attempts,
        "domain_selected": False,
    }


def write_phase_f(upstream_checkout: str | Path, output: str | Path) -> Path:
    destination = Path(output)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(run_phase_f(upstream_checkout), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return destination
