"""Pinned upstream integration smoke for Protocol 002 Stage I.

This module dynamically imports the pinned ``eco-genetic-criticality`` checkout
and runs a tiny symmetric-mutation H1 boundary-resolution smoke. The smoke is an
integration gate only, not publication evidence and not the full Stage I grid.
"""
from __future__ import annotations

import importlib
import json
import sys
from contextlib import contextmanager
from dataclasses import replace
from pathlib import Path
from typing import Any, Iterator

from .protocol002_stage0 import UPSTREAM_COMMIT, UPSTREAM_REPOSITORY

UPSTREAM_H1_MODULE = "causal_model.finite_h1_boundary_resolution_audit"
UPSTREAM_EXPERIMENT_MODULE = "causal_model.multipatch_criticality_experiments"
UPSTREAM_MUTATION_MODULE = "causal_model.symmetric_allele_mutation_closure"
DEFAULT_UPSTREAM_H1_SMOKE_PATH = Path("artifacts/protocol002/upstream_h1_sym_smoke.json")


@contextmanager
def _upstream_import_path(checkout: str | Path) -> Iterator[None]:
    path = str(Path(checkout).resolve())
    sys.path.insert(0, path)
    try:
        yield
    finally:
        if sys.path and sys.path[0] == path:
            sys.path.pop(0)
        else:
            try:
                sys.path.remove(path)
            except ValueError:
                pass


def run_upstream_h1_sym_smoke(
    upstream_checkout: str | Path,
    *,
    symmetric_mutation_rate: float = 0.10,
    master_seed: int = 20270210,
    stage_generations: int = 4,
    nested_barrier_points: tuple[int, ...] = (25, 49),
) -> dict[str, Any]:
    """Run one tiny pinned-upstream H1 boundary-resolution integration smoke.

    The Protocol 002 bridge coordinate is ``kappa_mu=2*mu`` and ``p_star=0.5``.
    The default therefore exercises ``(kappa_mu=0.20, p_star=0.50)`` through the
    exact upstream symmetric mutation closure.
    """
    if not 0.0 <= symmetric_mutation_rate < 0.5:
        raise ValueError("symmetric_mutation_rate must lie in [0, 0.5)")
    checkout = Path(upstream_checkout)
    if not checkout.exists():
        raise FileNotFoundError(f"upstream checkout does not exist: {checkout}")

    with _upstream_import_path(checkout):
        audit = importlib.import_module(UPSTREAM_H1_MODULE)
        experiments = importlib.import_module(UPSTREAM_EXPERIMENT_MODULE)
        mutation = importlib.import_module(UPSTREAM_MUTATION_MODULE)

        spec = replace(
            experiments.standard_profile(),
            experiment_id="protocol002_upstream_h1_sym_smoke",
            generations=1,
            replicates=1,
            master_seed=master_seed,
            area_reference_values=(1.0,),
            interaction_feedback_values=(4.5,),
            interaction_barrier_values=(0.5,),
        )
        with mutation.patched_h1_mutation_runner(symmetric_mutation_rate):
            cells = audit.run_finite_h1_boundary_resolution_audit(
                spec,
                endpoint_padding_fraction=0.5,
                stage_generations=stage_generations,
                nested_barrier_points=nested_barrier_points,
                interaction_separation_threshold=0.05,
                maximum_normalized_bracket_width=0.10,
            )

    if len(cells) != 1:
        raise RuntimeError("upstream H1 smoke must return exactly one parameter cell")
    cell = cells[0]
    replicate_support = [
        record.resolution_stable_h1_loop_mechanism_supported
        for record in cell.replicates
    ]
    return {
        "stage": "Protocol 002 pinned upstream H1 SYM integration smoke",
        "upstream": {
            "repository": UPSTREAM_REPOSITORY,
            "commit": UPSTREAM_COMMIT,
            "h1_module": UPSTREAM_H1_MODULE,
            "mutation_module": UPSTREAM_MUTATION_MODULE,
        },
        "protocol002_coordinate": {
            "kappa_mu": 2.0 * symmetric_mutation_rate,
            "p_star": 0.5,
            "symmetric_mutation_rate": symmetric_mutation_rate,
        },
        "design": {
            "area_reference": 1.0,
            "kappa": 4.5,
            "master_seed": master_seed,
            "replicates": 1,
            "stage_generations": stage_generations,
            "nested_barrier_points": list(nested_barrier_points),
        },
        "cell_count": len(cells),
        "replicate_count": len(cell.replicates),
        "replicate_support": replicate_support,
        "cell_summary": dict(cell.summary),
        "integration_run_present": True,
        "full_stage_i_campaign": False,
        "type_s_result_claimed": False,
    }


def write_upstream_h1_sym_smoke(
    upstream_checkout: str | Path,
    output: str | Path = DEFAULT_UPSTREAM_H1_SMOKE_PATH,
) -> Path:
    """Run the integration smoke and write its JSON artifact."""
    target = Path(output)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        json.dumps(run_upstream_h1_sym_smoke(upstream_checkout), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return target
