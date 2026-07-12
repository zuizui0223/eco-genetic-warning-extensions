"""Pinned upstream H1 integration smoke for Protocol 002 asymmetric mutation.

This module reuses the pinned upstream finite life cycle and H1 boundary runner.
Only the mutation transform is temporarily replaced with the Protocol 002 affine
map. Selection, migration, finite drift, trait recruitment, and H1 continuation
logic remain upstream code.
"""
from __future__ import annotations

import importlib
import json
from contextlib import contextmanager
from dataclasses import replace
from pathlib import Path
from typing import Any, Iterator

from .mutation_coordinates import MutationCoordinates
from .protocol002_stage0 import UPSTREAM_COMMIT, UPSTREAM_REPOSITORY
from .protocol002_upstream_h1_smoke import (
    UPSTREAM_EXPERIMENT_MODULE,
    UPSTREAM_H1_MODULE,
    UPSTREAM_MUTATION_MODULE,
    _upstream_import_path,
)

DEFAULT_UPSTREAM_H1_ASYM_SMOKE_PATH = Path("artifacts/protocol002/upstream_h1_asym_smoke.json")


@contextmanager
def patched_protocol002_mutation_runner(
    mutation_module: Any,
    coordinate: MutationCoordinates,
) -> Iterator[None]:
    """Route the pinned upstream H1 life cycle through one Protocol 002 coordinate.

    The upstream scoped H1 patch already routes continuation code through its
    mutation-enabled simulator. We preserve that simulator and temporarily
    replace only its mutation transform. The driver rate is ``kappa_mu / 2``;
    it is used only to activate the upstream mutation-enabled route, while the
    patched transform ignores that symmetric-rate argument and applies the
    Protocol 002 affine map directly.
    """
    driver_rate = coordinate.kappa_mu / 2.0
    if not 0.0 < driver_rate < 0.5:
        raise ValueError("Protocol 002 H1 smoke requires 0 < kappa_mu < 1")

    original_transform = mutation_module.apply_symmetric_allele_mutation

    def protocol002_transform(frequency: float, _mutation_rate: float) -> float:
        return coordinate.apply(frequency)

    mutation_module.apply_symmetric_allele_mutation = protocol002_transform
    try:
        with mutation_module.patched_h1_mutation_runner(driver_rate):
            yield
    finally:
        mutation_module.apply_symmetric_allele_mutation = original_transform


def run_upstream_h1_asym_smoke(
    upstream_checkout: str | Path,
    *,
    coordinate: MutationCoordinates,
    master_seed: int = 20270210,
    stage_generations: int = 4,
    nested_barrier_points: tuple[int, ...] = (25, 49),
) -> dict[str, Any]:
    """Run one tiny pinned-upstream H1 smoke for an asymmetric coordinate."""
    checkout = Path(upstream_checkout)
    if not checkout.exists():
        raise FileNotFoundError(f"upstream checkout does not exist: {checkout}")
    if coordinate.p_star == 0.5:
        raise ValueError("asymmetric smoke requires p_star != 0.5")

    with _upstream_import_path(checkout):
        audit = importlib.import_module(UPSTREAM_H1_MODULE)
        experiments = importlib.import_module(UPSTREAM_EXPERIMENT_MODULE)
        mutation = importlib.import_module(UPSTREAM_MUTATION_MODULE)

        spec = replace(
            experiments.standard_profile(),
            experiment_id="protocol002_upstream_h1_asym_smoke",
            generations=1,
            replicates=1,
            master_seed=master_seed,
            area_reference_values=(1.0,),
            interaction_feedback_values=(4.5,),
            interaction_barrier_values=(0.5,),
        )
        with patched_protocol002_mutation_runner(mutation, coordinate):
            cells = audit.run_finite_h1_boundary_resolution_audit(
                spec,
                endpoint_padding_fraction=0.5,
                stage_generations=stage_generations,
                nested_barrier_points=nested_barrier_points,
                interaction_separation_threshold=0.05,
                maximum_normalized_bracket_width=0.10,
            )

    if len(cells) != 1:
        raise RuntimeError("upstream H1 asymmetric smoke must return exactly one parameter cell")
    cell = cells[0]
    replicate_support = [
        record.resolution_stable_h1_loop_mechanism_supported
        for record in cell.replicates
    ]
    return {
        "stage": "Protocol 002 pinned upstream H1 asymmetric integration smoke",
        "upstream": {
            "repository": UPSTREAM_REPOSITORY,
            "commit": UPSTREAM_COMMIT,
            "h1_module": UPSTREAM_H1_MODULE,
            "mutation_module": UPSTREAM_MUTATION_MODULE,
        },
        "protocol002_coordinate": {
            "kappa_mu": coordinate.kappa_mu,
            "p_star": coordinate.p_star,
            "low_to_high": coordinate.low_to_high,
            "high_to_low": coordinate.high_to_low,
        },
        "design": {
            "area_reference": 1.0,
            "kappa": 4.5,
            "master_seed": master_seed,
            "replicates": 1,
            "stage_generations": stage_generations,
            "nested_barrier_points": list(nested_barrier_points),
            "mutation_timing": "after selection and migration, before finite drift",
        },
        "cell_count": len(cells),
        "replicate_count": len(cell.replicates),
        "replicate_support": replicate_support,
        "cell_summary": dict(cell.summary),
        "integration_run_present": True,
        "asymmetric_protocol002_mutation_present": True,
        "full_stage_i_campaign": False,
        "type_s_result_claimed": False,
    }


def run_upstream_h1_asym_smoke_panel(upstream_checkout: str | Path) -> dict[str, Any]:
    """Run paired DOWN and UP asymmetric H1 smoke coordinates."""
    coordinates = (
        MutationCoordinates(kappa_mu=0.20, p_star=0.25),
        MutationCoordinates(kappa_mu=0.20, p_star=0.75),
    )
    runs = [run_upstream_h1_asym_smoke(upstream_checkout, coordinate=coordinate) for coordinate in coordinates]
    return {
        "stage": "Protocol 002 pinned upstream H1 asymmetric smoke panel",
        "upstream": {
            "repository": UPSTREAM_REPOSITORY,
            "commit": UPSTREAM_COMMIT,
        },
        "runs": runs,
        "run_count": len(runs),
        "full_stage_i_campaign": False,
        "type_s_result_claimed": False,
    }


def write_upstream_h1_asym_smoke(
    upstream_checkout: str | Path,
    output: str | Path = DEFAULT_UPSTREAM_H1_ASYM_SMOKE_PATH,
) -> Path:
    """Run the asymmetric smoke panel and write its JSON artifact."""
    target = Path(output)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        json.dumps(run_upstream_h1_asym_smoke_panel(upstream_checkout), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return target
