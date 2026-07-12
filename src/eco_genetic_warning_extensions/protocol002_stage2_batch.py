"""Resumable Protocol 002 Stage II trait-loss-only calibration batches.

Each batch is one mutation/source/schedule candidate cell and retains 25 attempts:
five calibration master seeds by five replicates. The runner records only source
preparation, projection, baseline eligibility, and realised trait-loss timing.
"""
from __future__ import annotations

import importlib
import json
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Any

from .mutation_coordinates import MutationCoordinates, primary_phase_grid
from .protocol002_calibration import (
    CALIBRATION_BARRIER_INCREASES,
    CALIBRATION_HOLD_GENERATIONS,
    CALIBRATION_MASTER_SEEDS,
    CALIBRATION_RAMP_GENERATIONS,
    CALIBRATION_REPLICATES_PER_CELL,
    assert_protocol002_blind_calibration_columns,
)
from .protocol002_source_grid import (
    SOURCE_AREA_REFERENCES,
    SOURCE_HOLD_GENERATIONS,
    SOURCE_KAPPAS,
    SOURCE_NESTED_BARRIER_GRIDS,
    SOURCE_STAGE_GENERATIONS,
)
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


@dataclass(frozen=True)
class Stage2BatchCell:
    batch_index: int
    coordinate: MutationCoordinates
    area_reference: float
    kappa: float
    hold_generations: int
    normalised_barrier_increase: float

    @property
    def ramp_generations(self) -> int:
        return CALIBRATION_RAMP_GENERATIONS

    @property
    def horizon(self) -> int:
        return self.ramp_generations + self.hold_generations

    def identity(self) -> dict[str, int | float]:
        return {
            "batch_index": self.batch_index,
            "kappa_mu": self.coordinate.kappa_mu,
            "p_star": self.coordinate.p_star,
            "area_reference": self.area_reference,
            "kappa": self.kappa,
            "ramp_generations": self.ramp_generations,
            "hold_generations": self.hold_generations,
            "horizon": self.horizon,
            "normalised_barrier_increase": self.normalised_barrier_increase,
        }


def stage2_batch_cells() -> tuple[Stage2BatchCell, ...]:
    cells: list[Stage2BatchCell] = []
    for coordinate in primary_phase_grid():
        for area_reference in SOURCE_AREA_REFERENCES:
            for kappa in SOURCE_KAPPAS:
                for hold in CALIBRATION_HOLD_GENERATIONS:
                    for increase in CALIBRATION_BARRIER_INCREASES:
                        cells.append(
                            Stage2BatchCell(
                                batch_index=len(cells),
                                coordinate=coordinate,
                                area_reference=area_reference,
                                kappa=kappa,
                                hold_generations=hold,
                                normalised_barrier_increase=increase,
                            )
                        )
    return tuple(cells)


def stage2_batch_cell(batch_index: int) -> Stage2BatchCell:
    cells = stage2_batch_cells()
    index = int(batch_index)
    if not 0 <= index < len(cells):
        raise ValueError(f"batch_index must lie in [0, {len(cells) - 1}]")
    return cells[index]


def default_stage2_batch_path(batch_index: int) -> Path:
    return Path(f"artifacts/protocol002/stage2_batches/batch_{int(batch_index):03d}.json")


def _assert_blind_artifact(artifact: dict[str, Any]) -> None:
    def walk(value: Any) -> None:
        if isinstance(value, dict):
            assert_protocol002_blind_calibration_columns(value.keys())
            for child in value.values():
                walk(child)
        elif isinstance(value, (list, tuple)):
            for child in value:
                walk(child)

    walk(artifact)


def run_stage2_batch(upstream_checkout: str | Path, batch_index: int) -> dict[str, Any]:
    checkout = Path(upstream_checkout)
    if not checkout.exists():
        raise FileNotFoundError(f"upstream checkout does not exist: {checkout}")

    batch = stage2_batch_cell(batch_index)
    coordinate = batch.coordinate
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
            batch.ramp_generations,
            batch.hold_generations,
            batch.normalised_barrier_increase,
        )

        for master_seed in CALIBRATION_MASTER_SEEDS:
            spec = replace(
                experiments.standard_profile(),
                experiment_id=f"protocol002_stage2_batch_{batch.batch_index:03d}",
                generations=1,
                replicates=CALIBRATION_REPLICATES_PER_CELL,
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
                    raise RuntimeError("Stage II batch must return exactly one H1 cell")
                cell = cells[0]
                if len(cell.replicates) != CALIBRATION_REPLICATES_PER_CELL:
                    raise RuntimeError("Stage II batch returned an unexpected replicate count")

                scenarios = chain._scenario_map(spec)
                isolated = scenarios[experiments.SCENARIO_EQUAL_ISOLATED]

                for record in cell.replicates:
                    base: dict[str, Any] = {
                        **batch.identity(),
                        "low_to_high": coordinate.low_to_high,
                        "high_to_low": coordinate.high_to_low,
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
                        base.update(
                            {
                                "status": "source_preparation_failed",
                                "source_prepared": False,
                                "projection_supported": None,
                                "baseline_realised_high_trait_present": None,
                                "eligible_for_trait_loss_denominator": False,
                                "trait_loss_time_post_baseline": None,
                                "trait_loss_observed_post_baseline": None,
                                "simulation_run_present": False,
                            }
                        )
                        attempts.append(base)
                        continue

                    source, anchor = prepared
                    interval = cell.canonical_bistable_barrier_interval
                    if interval is None or interval[1] <= interval[0]:
                        raise RuntimeError("prepared Stage II source requires a positive canonical interval")
                    interval_width = interval[1] - interval[0]
                    trajectory_seed = record.seed
                    template = chain.parameters_for_cell(
                        spec,
                        isolated,
                        replace(cell.parameters, interaction_barrier=anchor),
                        seed=trajectory_seed,
                    )
                    projected, invariants = chain.project_full_state(source, template)
                    if not invariants.projection_supported:
                        base.update(
                            {
                                "status": "projection_failed",
                                "source_prepared": True,
                                "anchor_barrier": anchor,
                                "canonical_interval_width": interval_width,
                                "projection_supported": False,
                                "baseline_realised_high_trait_present": None,
                                "eligible_for_trait_loss_denominator": False,
                                "trait_loss_time_post_baseline": None,
                                "trait_loss_observed_post_baseline": None,
                                "simulation_run_present": False,
                            }
                        )
                        attempts.append(base)
                        continue

                    barriers = calibration.ramp_and_hold_barrier_schedule(
                        anchor_barrier=anchor,
                        canonical_interval_width=interval_width,
                        schedule=schedule,
                    )
                    result = mutation.simulate_with_symmetric_allele_mutation(
                        replace(
                            projected,
                            generations=schedule.total_generations,
                            random_seed=trajectory_seed,
                        ),
                        mutation_rate=driver_rate,
                        interaction_barrier_schedule=barriers,
                    )
                    baseline_present = any(
                        item.realised_high_trait_occupied
                        for item in result.snapshots[0].trait_occupancy
                    )
                    raw_loss_time = dynamics.tau_trait_realised(result)
                    loss_time = None if raw_loss_time is None or raw_loss_time == 0 else raw_loss_time
                    base.update(
                        {
                            "status": "completed",
                            "source_prepared": True,
                            "anchor_barrier": anchor,
                            "canonical_interval_width": interval_width,
                            "projection_supported": True,
                            "baseline_realised_high_trait_present": baseline_present,
                            "eligible_for_trait_loss_denominator": bool(baseline_present),
                            "barrier_first_generation": barriers[0],
                            "barrier_at_hold": barriers[-1],
                            "trait_loss_time_post_baseline": loss_time,
                            "trait_loss_observed_post_baseline": (
                                None if not baseline_present else loss_time is not None
                            ),
                            "simulation_run_present": True,
                        }
                    )
                    attempts.append(base)

    artifact = _batch_artifact(batch, attempts)
    _assert_blind_artifact(artifact)
    return artifact


def _batch_artifact(batch: Stage2BatchCell, attempts: list[dict[str, Any]]) -> dict[str, Any]:
    expected = len(CALIBRATION_MASTER_SEEDS) * CALIBRATION_REPLICATES_PER_CELL
    if len(attempts) != expected:
        raise RuntimeError(f"Stage II batch must retain {expected} attempts")
    eligible = [item for item in attempts if item["eligible_for_trait_loss_denominator"]]
    losses = [item for item in eligible if item["trait_loss_observed_post_baseline"] is True]
    seed_blocks = []
    for seed in CALIBRATION_MASTER_SEEDS:
        seed_eligible = [item for item in eligible if item["master_seed"] == seed]
        seed_losses = [item for item in seed_eligible if item["trait_loss_observed_post_baseline"] is True]
        seed_blocks.append(
            {
                "master_seed": seed,
                "baseline_eligible_count": len(seed_eligible),
                "trait_loss_count": len(seed_losses),
                "trait_loss_rate": None if not seed_eligible else len(seed_losses) / len(seed_eligible),
            }
        )
    return {
        "stage": "Protocol 002 Stage II trait-loss-only calibration batch",
        "campaign": {
            "batch_index": batch.batch_index,
            "batch_count": len(stage2_batch_cells()),
            "attempts_per_batch": expected,
            "full_campaign_attempt_count": len(stage2_batch_cells()) * expected,
            "resumable_unit": "one mutation coordinate x area_reference x kappa x hold x barrier increase",
        },
        "cell": batch.identity(),
        "upstream": {
            "repository": UPSTREAM_REPOSITORY,
            "commit": UPSTREAM_COMMIT,
            "h1_module": UPSTREAM_H1_MODULE,
            "calibration_module": UPSTREAM_CALIBRATION_MODULE,
        },
        "design": {
            "master_seeds": list(CALIBRATION_MASTER_SEEDS),
            "replicates_per_seed": CALIBRATION_REPLICATES_PER_CELL,
            "nested_barrier_grids": list(SOURCE_NESTED_BARRIER_GRIDS),
            "source_stage_generations": SOURCE_STAGE_GENERATIONS,
            "source_hold_generations": SOURCE_HOLD_GENERATIONS,
            "projection_scenario": "equal_isolated",
            "trait_loss_only": True,
        },
        "status_counts": {
            "attempted": len(attempts),
            "source_prepared": sum(item["source_prepared"] is True for item in attempts),
            "projection_supported": sum(item["projection_supported"] is True for item in attempts),
            "baseline_eligible": len(eligible),
            "trait_loss": len(losses),
        },
        "pooled_trait_loss_rate": None if not eligible else len(losses) / len(eligible),
        "seed_blocks": seed_blocks,
        "attempts": attempts,
        "trait_loss_only": True,
        "domain_selected": False,
        "type_s_result_claimed": False,
    }


def write_stage2_batch(
    upstream_checkout: str | Path,
    batch_index: int,
    output: str | Path | None = None,
) -> Path:
    target = default_stage2_batch_path(batch_index) if output is None else Path(output)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        json.dumps(run_stage2_batch(upstream_checkout, batch_index), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return target
