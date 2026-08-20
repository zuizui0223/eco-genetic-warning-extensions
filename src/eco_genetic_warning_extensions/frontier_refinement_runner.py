"""Warning-blind Phase-A frontier-refinement simulation runner.

Each cell reconstructs its own high-function source under the declared recurrent-
transition coordinate, projects to equal isolation, and records realised trait
loss only. Diversity and warning fields are forbidden from the artifact.
"""
from __future__ import annotations

import importlib
import json
from dataclasses import replace
from pathlib import Path
from typing import Any

from .frontier_refinement_manifest import (
    PHASE_A_HOLD_GENERATIONS,
    PHASE_A_MASTER_SEEDS,
    PHASE_A_RAMP_GENERATIONS,
    PHASE_A_REPLICATES_PER_SEED,
    phase_a_cells,
)
from .protocol002_calibration import assert_protocol002_blind_calibration_columns
from .protocol002_condition_map import classify_seed_rates
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


def _assert_blind(value: Any) -> None:
    if isinstance(value, dict):
        assert_protocol002_blind_calibration_columns(value.keys())
        for child in value.values():
            _assert_blind(child)
    elif isinstance(value, (list, tuple)):
        for child in value:
            _assert_blind(child)


def phase_a_cell(cell_index: int):
    cells = phase_a_cells()
    index = int(cell_index)
    if not 0 <= index < len(cells):
        raise ValueError(f"cell_index must lie in [0, {len(cells)-1}]")
    return cells[index]


def run_phase_a_cell(upstream_checkout: str | Path, cell_index: int) -> dict[str, Any]:
    checkout = Path(upstream_checkout)
    if not checkout.exists():
        raise FileNotFoundError(f"upstream checkout does not exist: {checkout}")

    phase_cell = phase_a_cell(cell_index)
    coordinate = phase_cell.coordinate
    anchor = phase_cell.anchor
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
            PHASE_A_RAMP_GENERATIONS,
            PHASE_A_HOLD_GENERATIONS,
            anchor.normalised_barrier_increase,
        )

        for master_seed in PHASE_A_MASTER_SEEDS:
            spec = replace(
                experiments.standard_profile(),
                experiment_id=f"frontier_refinement_phase_a_{phase_cell.cell_index:02d}",
                generations=1,
                replicates=PHASE_A_REPLICATES_PER_SEED,
                master_seed=master_seed,
                area_reference_values=(anchor.area_reference,),
                interaction_feedback_values=(anchor.interaction_kappa,),
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
                    raise RuntimeError("frontier refinement must return exactly one H1 cell")
                cell = cells[0]
                scenarios = chain._scenario_map(spec)
                isolated = scenarios[experiments.SCENARIO_EQUAL_ISOLATED]

                for record in cell.replicates:
                    base: dict[str, Any] = {
                        **phase_cell.identity(),
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
                        raise RuntimeError("prepared source requires a positive canonical interval")
                    interval_width = interval[1] - interval[0]
                    template = chain.parameters_for_cell(
                        spec,
                        isolated,
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

                    barriers = calibration.ramp_and_hold_barrier_schedule(
                        anchor_barrier=anchor_barrier,
                        canonical_interval_width=interval_width,
                        schedule=schedule,
                    )
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

    artifact = _build_artifact(phase_cell, attempts)
    _assert_blind(artifact)
    return artifact


def _build_artifact(phase_cell, attempts: list[dict[str, Any]]) -> dict[str, Any]:
    expected = len(PHASE_A_MASTER_SEEDS) * PHASE_A_REPLICATES_PER_SEED
    if len(attempts) != expected:
        raise RuntimeError(f"Phase-A cell must retain {expected} attempts")
    eligible = [row for row in attempts if row["eligible_for_trait_loss_denominator"]]
    losses = [row for row in eligible if row["trait_loss_observed_post_baseline"] is True]
    seed_blocks = []
    rates = []
    for seed in PHASE_A_MASTER_SEEDS:
        seed_eligible = [row for row in eligible if row["master_seed"] == seed]
        seed_losses = [row for row in seed_eligible if row["trait_loss_observed_post_baseline"] is True]
        rate = None if not seed_eligible else len(seed_losses) / len(seed_eligible)
        seed_blocks.append({
            "master_seed": seed,
            "baseline_eligible_count": len(seed_eligible),
            "trait_loss_count": len(seed_losses),
            "trait_loss_rate": rate,
        })
        if rate is not None:
            rates.append(rate)

    regime = "incomplete"
    if len(rates) == len(PHASE_A_MASTER_SEEDS):
        regime = classify_seed_rates(tuple(rates))

    return {
        "stage": "warning-blind recurrent-transition frontier refinement Phase A",
        "cell": phase_cell.identity(),
        "upstream": {"repository": UPSTREAM_REPOSITORY, "commit": UPSTREAM_COMMIT},
        "design": {
            "master_seeds": list(PHASE_A_MASTER_SEEDS),
            "replicates_per_seed": PHASE_A_REPLICATES_PER_SEED,
            "projection_scenario": "equal_isolated",
            "trait_loss_only": True,
        },
        "status_counts": {
            "attempted": len(attempts),
            "source_prepared": sum(row["source_prepared"] is True for row in attempts),
            "projection_supported": sum(row["projection_supported"] is True for row in attempts),
            "baseline_eligible": len(eligible),
            "trait_loss": len(losses),
        },
        "pooled_trait_loss_rate": None if not eligible else len(losses) / len(eligible),
        "seed_blocks": seed_blocks,
        "regime": regime,
        "attempts": attempts,
        "warning_fields_available": False,
        "diversity_fields_available": False,
        "domain_selected": False,
    }


def write_phase_a_cell(upstream_checkout: str | Path, cell_index: int, output: str | Path) -> Path:
    destination = Path(output)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(
        json.dumps(run_phase_a_cell(upstream_checkout, cell_index), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return destination
