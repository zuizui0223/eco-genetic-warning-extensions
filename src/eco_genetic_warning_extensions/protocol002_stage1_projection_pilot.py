"""Protocol 002 Stage I full-state preparation and projection pilot.

This runner repeats the six-attempt source-support pilot against the pinned
upstream implementation, then reconstructs and holds the full high source state
for supported H1 attempts and projects that complete state into the three
validated landscape scenarios. It stops before H2/H3 horizon simulation.
"""
from __future__ import annotations

import importlib
import json
from dataclasses import replace
from pathlib import Path
from typing import Any

from .protocol002_source_grid import (
    SOURCE_HOLD_GENERATIONS,
    SOURCE_NESTED_BARRIER_GRIDS,
    SOURCE_STAGE_GENERATIONS,
)
from .protocol002_stage0 import UPSTREAM_COMMIT, UPSTREAM_REPOSITORY
from .protocol002_stage1_pilot import (
    PILOT_AREA_REFERENCE,
    PILOT_COORDINATES,
    PILOT_KAPPA,
    PILOT_MASTER_SEEDS,
    PILOT_REPLICATES,
    _support_status,
)
from .protocol002_upstream_h1_asym_smoke import (
    UPSTREAM_EXPERIMENT_MODULE,
    UPSTREAM_H1_MODULE,
    UPSTREAM_MUTATION_MODULE,
    _upstream_import_path,
    patched_protocol002_mutation_runner,
)

UPSTREAM_CHAIN_MODULE = "causal_model.mutation_primary_h1_h2_h3_chain"
DEFAULT_STAGE1_PROJECTION_PILOT_PATH = Path(
    "artifacts/protocol002/stage1_source_projection_pilot.json"
)


def run_stage1_source_projection_pilot(upstream_checkout: str | Path) -> dict[str, Any]:
    """Run source support, full-state preparation, and projection for six attempts."""
    checkout = Path(upstream_checkout)
    if not checkout.exists():
        raise FileNotFoundError(f"upstream checkout does not exist: {checkout}")

    attempts: list[dict[str, Any]] = []
    with _upstream_import_path(checkout):
        audit = importlib.import_module(UPSTREAM_H1_MODULE)
        experiments = importlib.import_module(UPSTREAM_EXPERIMENT_MODULE)
        mutation = importlib.import_module(UPSTREAM_MUTATION_MODULE)
        chain = importlib.import_module(UPSTREAM_CHAIN_MODULE)

        scenario_ids = (
            experiments.SCENARIO_ONE_LARGE,
            experiments.SCENARIO_EQUAL_ISOLATED,
            experiments.SCENARIO_EQUAL_MIGRATING,
        )

        for coordinate in PILOT_COORDINATES:
            driver_rate = coordinate.kappa_mu / 2.0
            for master_seed in PILOT_MASTER_SEEDS:
                spec = replace(
                    experiments.standard_profile(),
                    experiment_id="protocol002_stage1_source_projection_pilot",
                    generations=1,
                    replicates=PILOT_REPLICATES,
                    master_seed=master_seed,
                    area_reference_values=(PILOT_AREA_REFERENCE,),
                    interaction_feedback_values=(PILOT_KAPPA,),
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
                        raise RuntimeError("Stage I projection pilot must return one calibration cell")
                    cell = cells[0]
                    if len(cell.replicates) != PILOT_REPLICATES:
                        raise RuntimeError("Stage I projection pilot returned unexpected replicate count")
                    record = cell.replicates[0]
                    support = record.resolution_stable_h1_loop_mechanism_supported
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

                base: dict[str, Any] = {
                    "kappa_mu": coordinate.kappa_mu,
                    "p_star": coordinate.p_star,
                    "low_to_high": coordinate.low_to_high,
                    "high_to_low": coordinate.high_to_low,
                    "area_reference": PILOT_AREA_REFERENCE,
                    "kappa": PILOT_KAPPA,
                    "master_seed": master_seed,
                    "replicate": record.replicate_index,
                    "calibration_seed": record.seed,
                    "nested_barrier_grids": list(SOURCE_NESTED_BARRIER_GRIDS),
                    "stage_generations": SOURCE_STAGE_GENERATIONS,
                    "hold_generations": SOURCE_HOLD_GENERATIONS,
                    "source_support": support,
                    "source_status": _support_status(support),
                }

                if prepared is None:
                    base.update(
                        {
                            "source_prepared": False,
                            "source_preparation_status": "preparation_failed_or_not_eligible",
                            "anchor_barrier": None,
                            "projection_status": "not_run",
                            "projections": None,
                        }
                    )
                    attempts.append(base)
                    continue

                source, anchor = prepared
                scenarios = chain._scenario_map(spec)
                anchor_cell = replace(cell.parameters, interaction_barrier=anchor)
                projections: dict[str, Any] = {}
                for scenario_id in scenario_ids:
                    template = chain.parameters_for_cell(
                        spec,
                        scenarios[scenario_id],
                        anchor_cell,
                        seed=chain._outcome_seed(record.seed, scenario_id),
                    )
                    _projected, invariant = chain.project_full_state(source, template)
                    projections[scenario_id] = invariant.as_dict()

                all_supported = all(
                    bool(value["projection_supported"]) for value in projections.values()
                )
                base.update(
                    {
                        "source_prepared": True,
                        "source_preparation_status": "prepared",
                        "anchor_barrier": anchor,
                        "projection_status": "projection_supported" if all_supported else "projection_failed",
                        "projections": projections,
                    }
                )
                attempts.append(base)

    return _artifact(attempts)


def _artifact(attempts: list[dict[str, Any]]) -> dict[str, Any]:
    source_supported = sum(item["source_support"] is True for item in attempts)
    source_prepared = sum(item["source_prepared"] is True for item in attempts)
    projection_supported = sum(item["projection_status"] == "projection_supported" for item in attempts)
    projection_failed = sum(item["projection_status"] == "projection_failed" for item in attempts)
    projection_not_run = sum(item["projection_status"] == "not_run" for item in attempts)
    return {
        "stage": "Protocol 002 Stage I source preparation and projection pilot",
        "upstream": {
            "repository": UPSTREAM_REPOSITORY,
            "commit": UPSTREAM_COMMIT,
            "h1_module": UPSTREAM_H1_MODULE,
            "chain_module": UPSTREAM_CHAIN_MODULE,
        },
        "design": {
            "coordinate_count": len(PILOT_COORDINATES),
            "master_seeds": list(PILOT_MASTER_SEEDS),
            "attempt_count": len(attempts),
            "area_reference": PILOT_AREA_REFERENCE,
            "kappa": PILOT_KAPPA,
            "nested_barrier_grids": list(SOURCE_NESTED_BARRIER_GRIDS),
            "stage_generations": SOURCE_STAGE_GENERATIONS,
            "hold_generations": SOURCE_HOLD_GENERATIONS,
            "projection_scenarios": ["one_large", "equal_isolated", "equal_migrating"],
        },
        "status_counts": {
            "source_supported": source_supported,
            "source_prepared": source_prepared,
            "projection_supported": projection_supported,
            "projection_failed": projection_failed,
            "projection_not_run": projection_not_run,
        },
        "attempts": attempts,
        "real_h1_source_support_run_present": True,
        "full_state_source_preparation_run_present": True,
        "projection_run_present": True,
        "h2_h3_horizon_run_present": False,
        "full_stage_i_campaign": False,
        "type_s_result_claimed": False,
    }


def write_stage1_source_projection_pilot(
    upstream_checkout: str | Path,
    output: str | Path = DEFAULT_STAGE1_PROJECTION_PILOT_PATH,
) -> Path:
    target = Path(output)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        json.dumps(run_stage1_source_projection_pilot(upstream_checkout), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return target
