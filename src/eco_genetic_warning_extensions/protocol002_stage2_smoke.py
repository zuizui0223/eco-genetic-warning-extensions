"""Pinned-upstream Protocol 002 Stage II trait-loss-only smoke runner.

The smoke reconstructs one H1 source, projects it to the equal-isolated
landscape, applies one ramp-and-hold deterioration schedule, and records only the
realised trait-loss endpoint. Warning and diversity fields are forbidden.
"""
from __future__ import annotations

import importlib
import json
from dataclasses import replace
from pathlib import Path
from typing import Any

from .mutation_coordinates import MutationCoordinates
from .protocol002_calibration import assert_protocol002_blind_calibration_columns
from .protocol002_source_grid import SOURCE_NESTED_BARRIER_GRIDS, SOURCE_STAGE_GENERATIONS
from .protocol002_stage0 import UPSTREAM_COMMIT, UPSTREAM_REPOSITORY
from .protocol002_stage1_projection_pilot import UPSTREAM_CHAIN_RUNTIME_MODULE
from .protocol002_upstream_h1_asym_smoke import (
    UPSTREAM_EXPERIMENT_MODULE,
    UPSTREAM_H1_MODULE,
    UPSTREAM_MUTATION_MODULE,
    _upstream_import_path,
    patched_protocol002_mutation_runner,
)

UPSTREAM_CALIBRATION_MODULE = "causal_model.h2r_ramp_hold_trait_loss_calibration"
UPSTREAM_DYNAMICS_MODULE = "causal_model.multipatch_criticality_dynamics"
DEFAULT_STAGE2_SMOKE_PATH = Path("artifacts/protocol002/stage2_trait_loss_smoke.json")


def stage2_smoke_design() -> dict[str, Any]:
    return {
        "protocol002_coordinate": {
            "kappa_mu": 0.20,
            "p_star": 0.75,
            "low_to_high": 0.15,
            "high_to_low": 0.05,
        },
        "source": {
            "area_reference": 1.0,
            "kappa": 4.5,
            "master_seed": 20270210,
            "replicates": 1,
            "stage_generations": 30,
            "hold_generations": 30,
            "nested_barrier_grids": [25, 49, 97],
        },
        "calibration": {
            "master_seed": 20270310,
            "ramp_generations": 30,
            "hold_generations": 90,
            "horizon": 120,
            "normalised_barrier_increase": 0.15,
            "projection_scenario": "equal_isolated",
        },
    }


def _assert_blind_artifact(artifact: dict[str, Any]) -> None:
    forbidden = (
        "warning",
        "lead",
        "lag",
        "diversity",
        "heterozygosity",
        "h_alpha",
        "h_gamma",
        "event_pair",
    )

    def walk(value: Any) -> None:
        if isinstance(value, dict):
            assert_protocol002_blind_calibration_columns(value.keys())
            for key, child in value.items():
                lowered = str(key).lower()
                if any(token in lowered for token in forbidden):
                    raise ValueError(f"forbidden Stage II smoke field: {key}")
                walk(child)
        elif isinstance(value, (list, tuple)):
            for child in value:
                walk(child)

    walk(artifact)


def run_stage2_trait_loss_smoke(upstream_checkout: str | Path) -> dict[str, Any]:
    checkout = Path(upstream_checkout)
    if not checkout.exists():
        raise FileNotFoundError(f"upstream checkout does not exist: {checkout}")

    design = stage2_smoke_design()
    coordinate = MutationCoordinates(kappa_mu=0.20, p_star=0.75)
    driver_rate = coordinate.kappa_mu / 2.0

    with _upstream_import_path(checkout):
        audit = importlib.import_module(UPSTREAM_H1_MODULE)
        experiments = importlib.import_module(UPSTREAM_EXPERIMENT_MODULE)
        mutation = importlib.import_module(UPSTREAM_MUTATION_MODULE)
        runtime = importlib.import_module(UPSTREAM_CHAIN_RUNTIME_MODULE)
        calibration = importlib.import_module(UPSTREAM_CALIBRATION_MODULE)
        dynamics = importlib.import_module(UPSTREAM_DYNAMICS_MODULE)
        chain = runtime.chain

        spec = replace(
            experiments.standard_profile(),
            experiment_id="protocol002_stage2_trait_loss_smoke",
            generations=1,
            replicates=1,
            master_seed=design["source"]["master_seed"],
            area_reference_values=(design["source"]["area_reference"],),
            interaction_feedback_values=(design["source"]["kappa"],),
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
            if len(cells) != 1 or len(cells[0].replicates) != 1:
                raise RuntimeError("Stage II smoke must yield one H1 cell and one replicate")
            cell = cells[0]
            record = cell.replicates[0]
            prepared = chain._prepare_mutation_high_state(
                driver_rate,
                spec,
                cell,
                record,
                endpoint_padding_fraction=0.5,
                stage_generations=SOURCE_STAGE_GENERATIONS,
                hold_generations=30,
                interaction_separation_threshold=0.05,
            )
            if prepared is None:
                artifact = {
                    "stage": "Protocol 002 Stage II trait-loss-only smoke",
                    "upstream": {"repository": UPSTREAM_REPOSITORY, "commit": UPSTREAM_COMMIT},
                    "design": design,
                    "status": "source_preparation_failed",
                    "source_support": record.resolution_stable_h1_loop_mechanism_supported,
                    "source_prepared": False,
                    "projection_supported": None,
                    "baseline_realised_high_trait_present": None,
                    "trait_loss_time_post_baseline": None,
                    "trait_loss_observed_post_baseline": None,
                    "trait_loss_only": True,
                    "simulation_run_present": False,
                    "domain_selected": False,
                }
                _assert_blind_artifact(artifact)
                return artifact

            source, anchor = prepared
            interval = cell.canonical_bistable_barrier_interval
            if interval is None or interval[1] <= interval[0]:
                raise RuntimeError("Stage II smoke requires a positive canonical interval")
            interval_width = interval[1] - interval[0]
            scenarios = chain._scenario_map(spec)
            isolated = scenarios[experiments.SCENARIO_EQUAL_ISOLATED]
            template = chain.parameters_for_cell(
                spec,
                isolated,
                replace(cell.parameters, interaction_barrier=anchor),
                seed=design["calibration"]["master_seed"],
            )
            projected, invariants = chain.project_full_state(source, template)
            if not invariants.projection_supported:
                artifact = {
                    "stage": "Protocol 002 Stage II trait-loss-only smoke",
                    "upstream": {"repository": UPSTREAM_REPOSITORY, "commit": UPSTREAM_COMMIT},
                    "design": design,
                    "status": "projection_failed",
                    "source_support": record.resolution_stable_h1_loop_mechanism_supported,
                    "source_prepared": True,
                    "anchor_barrier": anchor,
                    "canonical_interval_width": interval_width,
                    "projection_supported": False,
                    "baseline_realised_high_trait_present": None,
                    "trait_loss_time_post_baseline": None,
                    "trait_loss_observed_post_baseline": None,
                    "trait_loss_only": True,
                    "simulation_run_present": False,
                    "domain_selected": False,
                }
                _assert_blind_artifact(artifact)
                return artifact

            schedule = calibration.RampHoldSchedule(30, 90, 0.15)
            barriers = calibration.ramp_and_hold_barrier_schedule(
                anchor_barrier=anchor,
                canonical_interval_width=interval_width,
                schedule=schedule,
            )
            result = mutation.simulate_with_symmetric_allele_mutation(
                replace(
                    projected,
                    generations=schedule.total_generations,
                    random_seed=design["calibration"]["master_seed"],
                ),
                mutation_rate=driver_rate,
                interaction_barrier_schedule=barriers,
            )

        baseline_present = any(
            item.realised_high_trait_occupied for item in result.snapshots[0].trait_occupancy
        )
        raw_loss_time = dynamics.tau_trait_realised(result)
        loss_time = None if raw_loss_time is None or raw_loss_time == 0 else raw_loss_time
        eligible = bool(baseline_present)
        artifact = {
            "stage": "Protocol 002 Stage II trait-loss-only smoke",
            "upstream": {
                "repository": UPSTREAM_REPOSITORY,
                "commit": UPSTREAM_COMMIT,
                "calibration_module": UPSTREAM_CALIBRATION_MODULE,
            },
            "design": design,
            "status": "completed",
            "source_support": record.resolution_stable_h1_loop_mechanism_supported,
            "source_prepared": True,
            "anchor_barrier": anchor,
            "canonical_interval_width": interval_width,
            "projection_supported": True,
            "baseline_realised_high_trait_present": baseline_present,
            "eligible_for_trait_loss_denominator": eligible,
            "barrier_first_generation": barriers[0],
            "barrier_at_hold": barriers[-1],
            "trait_loss_time_post_baseline": loss_time,
            "trait_loss_observed_post_baseline": None if not eligible else loss_time is not None,
            "trait_loss_only": True,
            "simulation_run_present": True,
            "asymmetric_protocol002_mutation_present": True,
            "domain_selected": False,
            "type_s_result_claimed": False,
        }
        _assert_blind_artifact(artifact)
        return artifact


def write_stage2_trait_loss_smoke(
    upstream_checkout: str | Path,
    output: str | Path = DEFAULT_STAGE2_SMOKE_PATH,
) -> Path:
    target = Path(output)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        json.dumps(run_stage2_trait_loss_smoke(upstream_checkout), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return target
