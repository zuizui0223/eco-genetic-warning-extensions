"""Protocol 003 blind sentinel bracket pilot.

This pilot searches only for realised trait-loss brackets. It never calculates or
retains diversity, warning, lead/lag, or event-pair fields. Four sentinel mutation
coordinates are crossed with four predeclared deterioration schedules. Each cell
uses two bracket-search master seeds and two replicates.
"""
from __future__ import annotations

import importlib
import json
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Any

from .mutation_coordinates import MutationCoordinates
from .protocol002_calibration import assert_protocol002_blind_calibration_columns
from .protocol002_source_grid import (
    SOURCE_HOLD_GENERATIONS,
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

BRACKET_MASTER_SEEDS = (20270510, 20270511)
BRACKET_REPLICATES_PER_CELL = 2
BRACKET_RAMP_GENERATIONS = 30


@dataclass(frozen=True)
class Protocol003BracketCell:
    cell_index: int
    label: str
    coordinate: MutationCoordinates
    area_reference: float
    kappa: float
    hold_generations: int
    normalised_barrier_increase: float

    @property
    def horizon(self) -> int:
        return BRACKET_RAMP_GENERATIONS + self.hold_generations

    def identity(self) -> dict[str, Any]:
        return {
            "cell_index": self.cell_index,
            "label": self.label,
            "kappa_mu": self.coordinate.kappa_mu,
            "p_star": self.coordinate.p_star,
            "low_to_high": self.coordinate.low_to_high,
            "high_to_low": self.coordinate.high_to_low,
            "area_reference": self.area_reference,
            "kappa": self.kappa,
            "ramp_generations": BRACKET_RAMP_GENERATIONS,
            "hold_generations": self.hold_generations,
            "horizon": self.horizon,
            "normalised_barrier_increase": self.normalised_barrier_increase,
        }


def protocol003_sentinel_schedules() -> tuple[tuple[str, MutationCoordinates, float, float, tuple[tuple[int, float], ...]], ...]:
    return (
        ("rapid_loss", MutationCoordinates(0.20, 0.25), 0.8, 6.0, ((90, 0.05), (150, 0.10), (210, 0.15), (300, 0.20))),
        ("symmetric_bridge", MutationCoordinates(0.20, 0.50), 0.8, 6.0, ((90, 0.10), (150, 0.15), (210, 0.20), (300, 0.30))),
        ("transition", MutationCoordinates(0.05, 0.90), 1.0, 4.5, ((90, 0.15), (150, 0.20), (210, 0.30), (300, 0.45))),
        ("persistence", MutationCoordinates(0.20, 0.90), 1.0, 4.5, ((90, 0.30), (150, 0.45), (210, 0.60), (300, 0.75))),
    )


def protocol003_bracket_cells() -> tuple[Protocol003BracketCell, ...]:
    cells: list[Protocol003BracketCell] = []
    for label, coordinate, area_reference, kappa, schedules in protocol003_sentinel_schedules():
        for hold, increase in schedules:
            cells.append(
                Protocol003BracketCell(
                    cell_index=len(cells),
                    label=label,
                    coordinate=coordinate,
                    area_reference=area_reference,
                    kappa=kappa,
                    hold_generations=hold,
                    normalised_barrier_increase=increase,
                )
            )
    return tuple(cells)


def _assert_blind(value: Any) -> None:
    if isinstance(value, dict):
        assert_protocol002_blind_calibration_columns(value.keys())
        for child in value.values():
            _assert_blind(child)
    elif isinstance(value, (list, tuple)):
        for child in value:
            _assert_blind(child)


def run_protocol003_bracket_cell(
    upstream_checkout: str | Path,
    cell_index: int,
) -> dict[str, Any]:
    checkout = Path(upstream_checkout)
    if not checkout.exists():
        raise FileNotFoundError(f"upstream checkout does not exist: {checkout}")
    cells = protocol003_bracket_cells()
    if not 0 <= int(cell_index) < len(cells):
        raise ValueError(f"cell_index must lie in [0, {len(cells) - 1}]")
    cell = cells[int(cell_index)]
    coordinate = cell.coordinate
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
            BRACKET_RAMP_GENERATIONS,
            cell.hold_generations,
            cell.normalised_barrier_increase,
        )

        for master_seed in BRACKET_MASTER_SEEDS:
            spec = replace(
                experiments.standard_profile(),
                experiment_id=f"protocol003_bracket_{cell.cell_index:02d}",
                generations=1,
                replicates=BRACKET_REPLICATES_PER_CELL,
                master_seed=master_seed,
                area_reference_values=(cell.area_reference,),
                interaction_feedback_values=(cell.kappa,),
                interaction_barrier_values=(0.5,),
            )
            with patched_protocol002_mutation_runner(mutation, coordinate):
                h1_cells = audit.run_finite_h1_boundary_resolution_audit(
                    spec,
                    endpoint_padding_fraction=0.5,
                    stage_generations=SOURCE_STAGE_GENERATIONS,
                    nested_barrier_points=SOURCE_NESTED_BARRIER_GRIDS,
                    interaction_separation_threshold=0.05,
                    maximum_normalized_bracket_width=0.03,
                )
                if len(h1_cells) != 1:
                    raise RuntimeError("Protocol 003 bracket cell must return exactly one H1 cell")
                h1_cell = h1_cells[0]
                scenarios = chain._scenario_map(spec)
                isolated = scenarios[experiments.SCENARIO_EQUAL_ISOLATED]

                for record in h1_cell.replicates:
                    row: dict[str, Any] = {
                        **cell.identity(),
                        "master_seed": master_seed,
                        "replicate": record.replicate_index,
                        "bracket_seed": record.seed,
                        "source_support": record.resolution_stable_h1_loop_mechanism_supported,
                    }
                    prepared = chain._prepare_mutation_high_state(
                        driver_rate,
                        spec,
                        h1_cell,
                        record,
                        endpoint_padding_fraction=0.5,
                        stage_generations=SOURCE_STAGE_GENERATIONS,
                        hold_generations=SOURCE_HOLD_GENERATIONS,
                        interaction_separation_threshold=0.05,
                    )
                    if prepared is None:
                        row.update({
                            "status": "source_preparation_failed",
                            "source_prepared": False,
                            "projection_supported": None,
                            "baseline_realised_high_trait_present": None,
                            "eligible_for_trait_loss_denominator": False,
                            "trait_loss_time_post_baseline": None,
                            "trait_loss_observed_post_baseline": None,
                        })
                        attempts.append(row)
                        continue

                    source, anchor = prepared
                    interval = h1_cell.canonical_bistable_barrier_interval
                    if interval is None or interval[1] <= interval[0]:
                        raise RuntimeError("Protocol 003 prepared source requires a positive interval")
                    interval_width = interval[1] - interval[0]
                    template = chain.parameters_for_cell(
                        spec,
                        isolated,
                        replace(h1_cell.parameters, interaction_barrier=anchor),
                        seed=record.seed,
                    )
                    projected, invariants = chain.project_full_state(source, template)
                    if not invariants.projection_supported:
                        row.update({
                            "status": "projection_failed",
                            "source_prepared": True,
                            "projection_supported": False,
                            "baseline_realised_high_trait_present": None,
                            "eligible_for_trait_loss_denominator": False,
                            "trait_loss_time_post_baseline": None,
                            "trait_loss_observed_post_baseline": None,
                        })
                        attempts.append(row)
                        continue

                    barriers = calibration.ramp_and_hold_barrier_schedule(
                        anchor_barrier=anchor,
                        canonical_interval_width=interval_width,
                        schedule=schedule,
                    )
                    result = mutation.simulate_with_symmetric_allele_mutation(
                        replace(projected, generations=schedule.total_generations, random_seed=record.seed),
                        mutation_rate=driver_rate,
                        interaction_barrier_schedule=barriers,
                    )
                    baseline_present = any(
                        item.realised_high_trait_occupied
                        for item in result.snapshots[0].trait_occupancy
                    )
                    raw_loss_time = dynamics.tau_trait_realised(result)
                    loss_time = None if raw_loss_time is None or raw_loss_time == 0 else raw_loss_time
                    row.update({
                        "status": "completed",
                        "source_prepared": True,
                        "projection_supported": True,
                        "baseline_realised_high_trait_present": baseline_present,
                        "eligible_for_trait_loss_denominator": bool(baseline_present),
                        "trait_loss_time_post_baseline": loss_time,
                        "trait_loss_observed_post_baseline": None if not baseline_present else loss_time is not None,
                    })
                    attempts.append(row)

    eligible = [row for row in attempts if row["eligible_for_trait_loss_denominator"]]
    losses = [row for row in eligible if row["trait_loss_observed_post_baseline"] is True]
    artifact = {
        "stage": "Protocol 003 blind sentinel bracket pilot",
        "cell": cell.identity(),
        "upstream": {"repository": UPSTREAM_REPOSITORY, "commit": UPSTREAM_COMMIT},
        "design": {
            "master_seeds": list(BRACKET_MASTER_SEEDS),
            "replicates_per_seed": BRACKET_REPLICATES_PER_CELL,
            "trait_loss_only": True,
            "warning_fields_present": False,
            "domain_selected": False,
        },
        "status_counts": {
            "attempted": len(attempts),
            "baseline_eligible": len(eligible),
            "trait_loss": len(losses),
        },
        "pooled_trait_loss_rate": None if not eligible else len(losses) / len(eligible),
        "attempts": attempts,
        "trait_loss_only": True,
        "domain_selected": False,
        "type_s_result_claimed": False,
    }
    _assert_blind(artifact)
    return artifact


def write_protocol003_bracket_cell(
    upstream_checkout: str | Path,
    cell_index: int,
    output: str | Path,
) -> Path:
    target = Path(output)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        json.dumps(run_protocol003_bracket_cell(upstream_checkout, cell_index), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return target
