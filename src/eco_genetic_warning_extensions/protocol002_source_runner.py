"""Protocol 002 Stage I source-runner interface.

This module provides the interface that maps planned source coordinates to
retained attempt records. It includes a tiny deterministic fixture evaluator for
schema and transition testing only. It does not run H1 source reconstruction.
"""
from __future__ import annotations

from collections.abc import Callable, Iterable
from dataclasses import dataclass

from .mutation_coordinates import MutationCoordinates
from .protocol002_source_grid import protocol002_source_grid
from .protocol002_source_skeleton import (
    Protocol002SourceCoordinate,
    SourceAttemptRecord,
    SourceAttemptStatus,
    SourceSkeletonManifest,
)


@dataclass(frozen=True)
class SourceAttemptEvaluation:
    """Evaluator output before it is attached to a source coordinate."""

    status: SourceAttemptStatus
    source_prepared: bool
    source_supported: bool
    projection_supported: bool
    reason: str

    def to_record(self, coordinate: Protocol002SourceCoordinate) -> SourceAttemptRecord:
        """Attach this evaluation to one coordinate as a retained record."""
        return SourceAttemptRecord(
            source_coordinate=coordinate,
            status=self.status,
            source_prepared=self.source_prepared,
            source_supported=self.source_supported,
            projection_supported=self.projection_supported,
            reason=self.reason,
        )


SourceAttemptEvaluator = Callable[[Protocol002SourceCoordinate], SourceAttemptEvaluation]


def evaluate_source_attempts(
    source_coordinates: Iterable[Protocol002SourceCoordinate],
    evaluator: SourceAttemptEvaluator,
) -> SourceSkeletonManifest:
    """Evaluate planned source coordinates and retain every attempt record."""
    records = tuple(evaluator(coordinate).to_record(coordinate) for coordinate in source_coordinates)
    return SourceSkeletonManifest(records=records)


def not_run_evaluator(coordinate: Protocol002SourceCoordinate) -> SourceAttemptEvaluation:
    """Return the explicit not-run evaluation for a planned coordinate."""
    return SourceAttemptEvaluation(
        status=SourceAttemptStatus.NOT_RUN,
        source_prepared=False,
        source_supported=False,
        projection_supported=False,
        reason="source reconstruction not run by runner interface",
    )


def deterministic_fixture_evaluator(coordinate: Protocol002SourceCoordinate) -> SourceAttemptEvaluation:
    """Return deterministic status coverage by replicate index.

    This fixture is for tests only. Replicate indices 0–4 map to success,
    preparation failure, source-support failure, projection failure, and not-run,
    respectively. Larger replicate indices cycle through the same pattern.
    """
    slot = coordinate.replicate % 5
    if slot == 0:
        return SourceAttemptEvaluation(
            status=SourceAttemptStatus.SUCCESS,
            source_prepared=True,
            source_supported=True,
            projection_supported=True,
            reason="deterministic fixture success",
        )
    if slot == 1:
        return SourceAttemptEvaluation(
            status=SourceAttemptStatus.PREPARATION_FAILED,
            source_prepared=False,
            source_supported=False,
            projection_supported=False,
            reason="deterministic fixture preparation failure",
        )
    if slot == 2:
        return SourceAttemptEvaluation(
            status=SourceAttemptStatus.SOURCE_SUPPORT_FAILED,
            source_prepared=True,
            source_supported=False,
            projection_supported=False,
            reason="deterministic fixture source support failure",
        )
    if slot == 3:
        return SourceAttemptEvaluation(
            status=SourceAttemptStatus.PROJECTION_FAILED,
            source_prepared=True,
            source_supported=True,
            projection_supported=False,
            reason="deterministic fixture projection failure",
        )
    return SourceAttemptEvaluation(
        status=SourceAttemptStatus.NOT_RUN,
        source_prepared=False,
        source_supported=False,
        projection_supported=False,
        reason="deterministic fixture not run",
    )


def deterministic_fixture_source_coordinates() -> tuple[Protocol002SourceCoordinate, ...]:
    """Return five tiny fixture coordinates covering all retained statuses."""
    return protocol002_source_grid(
        coordinates=(MutationCoordinates(kappa_mu=0.20, p_star=0.75),),
        area_references=(1.0,),
        kappas=(4.5,),
        nested_barrier_grids=(49,),
        master_seeds=(20270210,),
        replicates_per_cell=5,
    )


def deterministic_fixture_source_manifest() -> SourceSkeletonManifest:
    """Return a tiny deterministic manifest covering all retained statuses."""
    return evaluate_source_attempts(
        deterministic_fixture_source_coordinates(),
        deterministic_fixture_evaluator,
    )


def deterministic_fixture_source_artifact() -> dict:
    """Return JSON-serializable content for the deterministic runner fixture."""
    return deterministic_fixture_source_manifest().to_artifact()
