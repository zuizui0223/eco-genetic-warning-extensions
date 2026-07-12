"""Small declared Protocol 002 Stage I source-support pilot.

This pilot uses the real pinned upstream finite H1 boundary-resolution runner with
the Protocol 002 mutation operator. It is the first multi-coordinate Stage I
execution subset, but it does not yet run projection or the full 3,375-attempt
campaign.
"""
from __future__ import annotations

import importlib
import json
from dataclasses import replace
from pathlib import Path
from typing import Any

from .mutation_coordinates import MutationCoordinates
from .protocol002_source_grid import SOURCE_NESTED_BARRIER_GRIDS, SOURCE_STAGE_GENERATIONS
from .protocol002_stage0 import UPSTREAM_COMMIT, UPSTREAM_REPOSITORY
from .protocol002_upstream_h1_asym_smoke import (
    UPSTREAM_EXPERIMENT_MODULE,
    UPSTREAM_H1_MODULE,
    UPSTREAM_MUTATION_MODULE,
    _upstream_import_path,
    patched_protocol002_mutation_runner,
)

PILOT_COORDINATES: tuple[MutationCoordinates, ...] = (
    MutationCoordinates(kappa_mu=0.20, p_star=0.25),
    MutationCoordinates(kappa_mu=0.20, p_star=0.50),
    MutationCoordinates(kappa_mu=0.20, p_star=0.75),
)
PILOT_MASTER_SEEDS: tuple[int, ...] = (20270210, 20270211)
PILOT_AREA_REFERENCE = 1.0
PILOT_KAPPA = 4.5
PILOT_REPLICATES = 1
DEFAULT_STAGE1_PILOT_PATH = Path("artifacts/protocol002/stage1_source_support_pilot.json")


def _support_status(value: bool | None) -> str:
    if value is True:
        return "source_supported"
    if value is False:
        return "source_support_failed"
    return "source_support_indeterminate"


def run_stage1_source_support_pilot(upstream_checkout: str | Path) -> dict[str, Any]:
    """Run the six-attempt declared Stage I source-support pilot."""
    checkout = Path(upstream_checkout)
    if not checkout.exists():
        raise FileNotFoundError(f"upstream checkout does not exist: {checkout}")

    attempts: list[dict[str, Any]] = []
    with _upstream_import_path(checkout):
        audit = importlib.import_module(UPSTREAM_H1_MODULE)
        experiments = importlib.import_module(UPSTREAM_EXPERIMENT_MODULE)
        mutation = importlib.import_module(UPSTREAM_MUTATION_MODULE)

        for coordinate in PILOT_COORDINATES:
            for master_seed in PILOT_MASTER_SEEDS:
                spec = replace(
                    experiments.standard_profile(),
                    experiment_id="protocol002_stage1_source_support_pilot",
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
                    raise RuntimeError("Stage I pilot attempt must return exactly one parameter cell")
                cell = cells[0]
                if len(cell.replicates) != PILOT_REPLICATES:
                    raise RuntimeError("Stage I pilot attempt returned an unexpected replicate count")
                record = cell.replicates[0]
                support = record.resolution_stable_h1_loop_mechanism_supported
                attempts.append(
                    {
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
                        "source_support": support,
                        "source_status": _support_status(support),
                        "projection_status": "not_run",
                    }
                )

    counts = {
        status: sum(attempt["source_status"] == status for attempt in attempts)
        for status in ("source_supported", "source_support_failed", "source_support_indeterminate")
    }
    return {
        "stage": "Protocol 002 Stage I source-support pilot",
        "upstream": {
            "repository": UPSTREAM_REPOSITORY,
            "commit": UPSTREAM_COMMIT,
            "h1_module": UPSTREAM_H1_MODULE,
        },
        "design": {
            "coordinate_count": len(PILOT_COORDINATES),
            "master_seeds": list(PILOT_MASTER_SEEDS),
            "replicates_per_coordinate_seed": PILOT_REPLICATES,
            "attempt_count": len(attempts),
            "area_reference": PILOT_AREA_REFERENCE,
            "kappa": PILOT_KAPPA,
            "nested_barrier_grids": list(SOURCE_NESTED_BARRIER_GRIDS),
            "nested_barrier_grids_form_one_resolution_set": True,
            "stage_generations": SOURCE_STAGE_GENERATIONS,
        },
        "status_counts": counts,
        "attempts": attempts,
        "real_h1_source_support_run_present": True,
        "projection_run_present": False,
        "full_stage_i_campaign": False,
        "type_s_result_claimed": False,
    }


def write_stage1_source_support_pilot(
    upstream_checkout: str | Path,
    output: str | Path = DEFAULT_STAGE1_PILOT_PATH,
) -> Path:
    target = Path(output)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        json.dumps(run_stage1_source_support_pilot(upstream_checkout), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return target
