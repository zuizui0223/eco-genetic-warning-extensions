"""Resumable Protocol 002 Stage I source reconstruction campaign batches.

The full declared campaign has 135 phase cells. Each batch is one mutation
coordinate x one area reference x one interaction-feedback value and contains
25 attempts: five master seeds x five replicates.
"""
from __future__ import annotations

import importlib
import json
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Any

from .mutation_coordinates import MutationCoordinates, primary_phase_grid
from .protocol002_source_grid import (
    SOURCE_AREA_REFERENCES,
    SOURCE_HOLD_GENERATIONS,
    SOURCE_KAPPAS,
    SOURCE_MASTER_SEEDS,
    SOURCE_NESTED_BARRIER_GRIDS,
    SOURCE_REPLICATES_PER_CELL,
    SOURCE_STAGE_GENERATIONS,
)
from .protocol002_stage0 import UPSTREAM_COMMIT, UPSTREAM_REPOSITORY
from .protocol002_stage1_pilot import _support_status
from .protocol002_stage1_projection_pilot import UPSTREAM_CHAIN_RUNTIME_MODULE
from .protocol002_upstream_h1_asym_smoke import (
    UPSTREAM_EXPERIMENT_MODULE,
    UPSTREAM_H1_MODULE,
    UPSTREAM_MUTATION_MODULE,
    _upstream_import_path,
    patched_protocol002_mutation_runner,
)


@dataclass(frozen=True)
class Stage1BatchCell:
    batch_index: int
    coordinate: MutationCoordinates
    area_reference: float
    kappa: float

    def identity(self) -> dict[str, int | float]:
        return {
            "batch_index": self.batch_index,
            "kappa_mu": self.coordinate.kappa_mu,
            "p_star": self.coordinate.p_star,
            "area_reference": self.area_reference,
            "kappa": self.kappa,
        }


def stage1_batch_cells() -> tuple[Stage1BatchCell, ...]:
    cells: list[Stage1BatchCell] = []
    for coordinate in primary_phase_grid():
        for area_reference in SOURCE_AREA_REFERENCES:
            for kappa in SOURCE_KAPPAS:
                cells.append(
                    Stage1BatchCell(
                        batch_index=len(cells),
                        coordinate=coordinate,
                        area_reference=area_reference,
                        kappa=kappa,
                    )
                )
    return tuple(cells)


def stage1_batch_cell(batch_index: int) -> Stage1BatchCell:
    cells = stage1_batch_cells()
    index = int(batch_index)
    if not 0 <= index < len(cells):
        raise ValueError(f"batch_index must lie in [0, {len(cells) - 1}]")
    return cells[index]


def default_stage1_batch_path(batch_index: int) -> Path:
    return Path(f"artifacts/protocol002/stage1_batches/batch_{int(batch_index):03d}.json")


def run_stage1_batch(upstream_checkout: str | Path, batch_index: int) -> dict[str, Any]:
    checkout = Path(upstream_checkout)
    if not checkout.exists():
        raise FileNotFoundError(f"upstream checkout does not exist: {checkout}")

    batch = stage1_batch_cell(batch_index)
    coordinate = batch.coordinate
    driver_rate = coordinate.kappa_mu / 2.0
    attempts: list[dict[str, Any]] = []

    with _upstream_import_path(checkout):
        audit = importlib.import_module(UPSTREAM_H1_MODULE)
        experiments = importlib.import_module(UPSTREAM_EXPERIMENT_MODULE)
        mutation = importlib.import_module(UPSTREAM_MUTATION_MODULE)
        runtime = importlib.import_module(UPSTREAM_CHAIN_RUNTIME_MODULE)
        chain = runtime.chain
        scenario_ids = (
            experiments.SCENARIO_ONE_LARGE,
            experiments.SCENARIO_EQUAL_ISOLATED,
            experiments.SCENARIO_EQUAL_MIGRATING,
        )

        for master_seed in SOURCE_MASTER_SEEDS:
            spec = replace(
                experiments.standard_profile(),
                experiment_id=f"protocol002_stage1_batch_{batch.batch_index:03d}",
                generations=1,
                replicates=SOURCE_REPLICATES_PER_CELL,
                master_seed=master_seed,
                area_reference_values=(batch.area_reference,),
                interaction_feedback_values=(batch.kappa,),
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
                    raise RuntimeError("Stage I batch must return exactly one calibration cell")
                cell = cells[0]
                if len(cell.replicates) != SOURCE_REPLICATES_PER_CELL:
                    raise RuntimeError("Stage I batch returned an unexpected replicate count")

                prepared_by_replicate: list[tuple[Any, Any]] = []
                for record in cell.replicates:
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
                    prepared_by_replicate.append((record, prepared))

            scenarios = chain._scenario_map(spec)
            for record, prepared in prepared_by_replicate:
                support = record.resolution_stable_h1_loop_mechanism_supported
                base: dict[str, Any] = {
                    **batch.identity(),
                    "low_to_high": coordinate.low_to_high,
                    "high_to_low": coordinate.high_to_low,
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
                all_supported = all(bool(value["projection_supported"]) for value in projections.values())
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

    return _batch_artifact(batch, attempts)


def _batch_artifact(batch: Stage1BatchCell, attempts: list[dict[str, Any]]) -> dict[str, Any]:
    expected_attempts = len(SOURCE_MASTER_SEEDS) * SOURCE_REPLICATES_PER_CELL
    if len(attempts) != expected_attempts:
        raise RuntimeError(f"Stage I batch must retain {expected_attempts} attempts")
    return {
        "stage": "Protocol 002 Stage I source reconstruction batch",
        "campaign": {
            "batch_index": batch.batch_index,
            "batch_count": len(stage1_batch_cells()),
            "attempts_per_batch": expected_attempts,
            "full_campaign_attempt_count": len(stage1_batch_cells()) * expected_attempts,
            "resumable_unit": "one mutation coordinate x one area_reference x one kappa",
        },
        "cell": batch.identity(),
        "upstream": {
            "repository": UPSTREAM_REPOSITORY,
            "commit": UPSTREAM_COMMIT,
            "h1_module": UPSTREAM_H1_MODULE,
            "chain_runtime_module": UPSTREAM_CHAIN_RUNTIME_MODULE,
        },
        "design": {
            "master_seeds": list(SOURCE_MASTER_SEEDS),
            "replicates_per_seed": SOURCE_REPLICATES_PER_CELL,
            "nested_barrier_grids": list(SOURCE_NESTED_BARRIER_GRIDS),
            "stage_generations": SOURCE_STAGE_GENERATIONS,
            "hold_generations": SOURCE_HOLD_GENERATIONS,
            "projection_scenarios": ["one_large", "equal_isolated", "equal_migrating"],
        },
        "status_counts": {
            "source_supported": sum(item["source_support"] is True for item in attempts),
            "source_prepared": sum(item["source_prepared"] is True for item in attempts),
            "projection_supported": sum(item["projection_status"] == "projection_supported" for item in attempts),
            "projection_failed": sum(item["projection_status"] == "projection_failed" for item in attempts),
            "projection_not_run": sum(item["projection_status"] == "not_run" for item in attempts),
        },
        "attempts": attempts,
        "real_h1_source_support_run_present": True,
        "full_state_source_preparation_run_present": True,
        "projection_run_present": True,
        "h2_h3_horizon_run_present": False,
        "full_stage_i_campaign_complete": False,
        "type_s_result_claimed": False,
    }


def write_stage1_batch(
    upstream_checkout: str | Path,
    batch_index: int,
    output: str | Path | None = None,
) -> Path:
    target = default_stage1_batch_path(batch_index) if output is None else Path(output)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        json.dumps(run_stage1_batch(upstream_checkout, batch_index), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return target
