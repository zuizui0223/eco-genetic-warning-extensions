"""Minimal H1 source-runner adapter and deterministic smoke execution.

This module fixes the ordered runner contract:
prepare source -> test source support -> test projection support -> retain status.
The included smoke execution uses deterministic callbacks only. It is not a full
Stage I ecological source-reconstruction campaign and produces no Type S result.
"""
from __future__ import annotations

from collections.abc import Callable, Iterable

from .mutation_coordinates import MutationCoordinates
from .protocol002_source_grid import protocol002_source_grid
from .protocol002_source_runner import SourceAttemptEvaluation, evaluate_source_attempts
from .protocol002_source_skeleton import (
    Protocol002SourceCoordinate,
    SourceAttemptStatus,
    SourceSkeletonManifest,
)

StageCheck = Callable[[Protocol002SourceCoordinate], bool]


def evaluate_h1_source_coordinate(
    coordinate: Protocol002SourceCoordinate,
    *,
    prepare_source: StageCheck,
    source_support: StageCheck,
    projection_support: StageCheck,
) -> SourceAttemptEvaluation:
    """Evaluate one coordinate in the declared H1 source-runner order."""
    if not prepare_source(coordinate):
        return SourceAttemptEvaluation(
            status=SourceAttemptStatus.PREPARATION_FAILED,
            source_prepared=False,
            source_supported=False,
            projection_supported=False,
            reason="source preparation failed",
        )
    if not source_support(coordinate):
        return SourceAttemptEvaluation(
            status=SourceAttemptStatus.SOURCE_SUPPORT_FAILED,
            source_prepared=True,
            source_supported=False,
            projection_supported=False,
            reason="source support failed",
        )
    if not projection_support(coordinate):
        return SourceAttemptEvaluation(
            status=SourceAttemptStatus.PROJECTION_FAILED,
            source_prepared=True,
            source_supported=True,
            projection_supported=False,
            reason="projection support failed",
        )
    return SourceAttemptEvaluation(
        status=SourceAttemptStatus.SUCCESS,
        source_prepared=True,
        source_supported=True,
        projection_supported=True,
        reason="source preparation, support, and projection checks passed",
    )


def run_h1_source_adapter(
    source_coordinates: Iterable[Protocol002SourceCoordinate],
    *,
    prepare_source: StageCheck,
    source_support: StageCheck,
    projection_support: StageCheck,
) -> SourceSkeletonManifest:
    """Run the ordered adapter over coordinates and retain every attempt."""
    return evaluate_source_attempts(
        source_coordinates,
        lambda coordinate: evaluate_h1_source_coordinate(
            coordinate,
            prepare_source=prepare_source,
            source_support=source_support,
            projection_support=projection_support,
        ),
    )


def h1_smoke_coordinates() -> tuple[Protocol002SourceCoordinate, ...]:
    """Return a tiny declared smoke subset: one coordinate, one seed, two replicates."""
    return protocol002_source_grid(
        coordinates=(MutationCoordinates(kappa_mu=0.20, p_star=0.50),),
        area_references=(1.0,),
        kappas=(4.5,),
        nested_barrier_grids=(49,),
        master_seeds=(20270210,),
        replicates_per_cell=2,
    )


def deterministic_h1_smoke_manifest() -> SourceSkeletonManifest:
    """Run the adapter smoke fixture with deterministic passing callbacks."""
    always_pass: StageCheck = lambda coordinate: True
    return run_h1_source_adapter(
        h1_smoke_coordinates(),
        prepare_source=always_pass,
        source_support=always_pass,
        projection_support=always_pass,
    )


def deterministic_h1_smoke_artifact() -> dict:
    """Return JSON-serializable content for the deterministic H1 adapter smoke run."""
    return deterministic_h1_smoke_manifest().to_artifact()
