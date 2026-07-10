"""Protocol 002 Stage I source-runner skeleton.

This module defines the attempt/status/artifact schema for H1 source
reconstruction. It deliberately does not run the full source grid or produce Type
S ecological evidence.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
from enum import StrEnum
from typing import Any

from .mutation_coordinates import MutationCoordinates
from .protocol002_stage0 import UPSTREAM_COMMIT, UPSTREAM_REPOSITORY


class SourceAttemptStatus(StrEnum):
    """Closed set of source-attempt statuses retained in Protocol 002 artifacts."""

    NOT_RUN = "not_run"
    PREPARATION_FAILED = "preparation_failed"
    SOURCE_SUPPORT_FAILED = "source_support_failed"
    PROJECTION_FAILED = "projection_failed"
    SUCCESS = "success"


@dataclass(frozen=True)
class Protocol002SourceCoordinate:
    """One declared source-reconstruction coordinate."""

    coordinate: MutationCoordinates
    area_reference: float
    kappa: float
    nested_barrier_grid: int
    stage_generations: int
    hold_generations: int
    master_seed: int
    replicate: int

    def __post_init__(self) -> None:
        if self.area_reference <= 0.0:
            raise ValueError("area_reference must be positive")
        if self.kappa <= 0.0:
            raise ValueError("kappa must be positive")
        if self.nested_barrier_grid <= 0:
            raise ValueError("nested_barrier_grid must be positive")
        if self.stage_generations <= 0:
            raise ValueError("stage_generations must be positive")
        if self.hold_generations <= 0:
            raise ValueError("hold_generations must be positive")
        if self.replicate < 0:
            raise ValueError("replicate must be non-negative")

    def identity(self) -> dict[str, int | float]:
        """Return a stable coordinate identity suitable for artifact rows."""
        return {
            "kappa_mu": self.coordinate.kappa_mu,
            "p_star": self.coordinate.p_star,
            "area_reference": self.area_reference,
            "kappa": self.kappa,
            "nested_barrier_grid": self.nested_barrier_grid,
            "stage_generations": self.stage_generations,
            "hold_generations": self.hold_generations,
            "master_seed": self.master_seed,
            "replicate": self.replicate,
        }


@dataclass(frozen=True)
class SourceAttemptRecord:
    """One retained source-attempt record, including failures."""

    source_coordinate: Protocol002SourceCoordinate
    status: SourceAttemptStatus
    source_prepared: bool
    source_supported: bool
    projection_supported: bool
    reason: str

    def __post_init__(self) -> None:
        if not self.reason:
            raise ValueError("reason must be non-empty")
        if self.status is SourceAttemptStatus.SUCCESS:
            if not (self.source_prepared and self.source_supported and self.projection_supported):
                raise ValueError("success requires source_prepared, source_supported, and projection_supported")
        if not self.source_prepared and self.status not in {
            SourceAttemptStatus.NOT_RUN,
            SourceAttemptStatus.PREPARATION_FAILED,
        }:
            raise ValueError("unprepared sources must be not_run or preparation_failed")

    def to_artifact_row(self) -> dict[str, Any]:
        """Return a flat, stable row for JSON/CSV artifact writing."""
        return {
            **self.source_coordinate.identity(),
            "status": self.status.value,
            "source_prepared": self.source_prepared,
            "source_supported": self.source_supported,
            "projection_supported": self.projection_supported,
            "reason": self.reason,
        }


@dataclass(frozen=True)
class SourceSkeletonManifest:
    """Manifest for a source-runner skeleton artifact."""

    records: tuple[SourceAttemptRecord, ...]
    simulation_result_present: bool = False
    stage: str = "Protocol 002 Stage I source-runner skeleton"
    upstream_repository: str = UPSTREAM_REPOSITORY
    upstream_commit: str = UPSTREAM_COMMIT

    def __post_init__(self) -> None:
        if self.simulation_result_present:
            raise ValueError("source skeleton artifacts must not claim simulation results")
        if not self.records:
            raise ValueError("at least one source-attempt record is required")

    def to_artifact(self) -> dict[str, Any]:
        """Return deterministic manifest content for serialization."""
        return {
            "stage": self.stage,
            "upstream": {
                "repository": self.upstream_repository,
                "commit": self.upstream_commit,
            },
            "simulation_result_present": self.simulation_result_present,
            "record_count": len(self.records),
            "status_counts": status_counts(self.records),
            "records": [record.to_artifact_row() for record in self.records],
        }


def status_counts(records: tuple[SourceAttemptRecord, ...]) -> dict[str, int]:
    """Count records by every declared status, including zeros."""
    counts = {status.value: 0 for status in SourceAttemptStatus}
    for record in records:
        counts[record.status.value] += 1
    return counts


def skeleton_record(
    source_coordinate: Protocol002SourceCoordinate,
    *,
    status: SourceAttemptStatus = SourceAttemptStatus.NOT_RUN,
    reason: str | None = None,
) -> SourceAttemptRecord:
    """Create an explicit no-simulation record for a source coordinate."""
    default_reason = "source reconstruction not run in skeleton stage"
    return SourceAttemptRecord(
        source_coordinate=source_coordinate,
        status=status,
        source_prepared=False,
        source_supported=False,
        projection_supported=False,
        reason=default_reason if reason is None else reason,
    )
