"""Declared Protocol 002 Stage I source-coordinate grid enumerator.

This module enumerates planned source attempts only. It does not run H1 source
reconstruction or produce Type S ecological evidence.
"""
from __future__ import annotations

import hashlib
import json
from collections.abc import Iterable
from pathlib import Path
from typing import Any

from .mutation_coordinates import MutationCoordinates, primary_phase_grid
from .protocol002_source_skeleton import Protocol002SourceCoordinate, SourceSkeletonManifest, skeleton_record

SOURCE_AREA_REFERENCES: tuple[float, ...] = (0.8, 1.0, 1.2)
SOURCE_KAPPAS: tuple[float, ...] = (3.0, 4.5, 6.0)
SOURCE_MASTER_SEEDS: tuple[int, ...] = (20270210, 20270211, 20270212, 20270213, 20270214)
SOURCE_REPLICATES_PER_CELL: int = 5
SOURCE_NESTED_BARRIER_GRIDS: tuple[int, ...] = (25, 49, 97)
SOURCE_STAGE_GENERATIONS: int = 30
SOURCE_HOLD_GENERATIONS: int = 30

DEFAULT_SOURCE_GRID_PATH = Path("artifacts/protocol002/source_grid_planned_manifest.json")
DEFAULT_SOURCE_GRID_LOCK_PATH = Path("artifacts/protocol002/source_grid_planned_lock.json")


def protocol002_source_grid(
    *,
    coordinates: Iterable[MutationCoordinates] | None = None,
    area_references: Iterable[float] = SOURCE_AREA_REFERENCES,
    kappas: Iterable[float] = SOURCE_KAPPAS,
    nested_barrier_grids: Iterable[int] = SOURCE_NESTED_BARRIER_GRIDS,
    master_seeds: Iterable[int] = SOURCE_MASTER_SEEDS,
    replicates_per_cell: int = SOURCE_REPLICATES_PER_CELL,
    stage_generations: int = SOURCE_STAGE_GENERATIONS,
    hold_generations: int = SOURCE_HOLD_GENERATIONS,
) -> tuple[Protocol002SourceCoordinate, ...]:
    """Enumerate declared Stage I source attempts.

    The nested barrier grids are one resolution set used inside every H1 attempt,
    not three independent experimental conditions. The retained legacy field
    ``nested_barrier_grid`` stores the finest grid size for row identity while the
    full set is locked in ``SOURCE_NESTED_BARRIER_GRIDS``.

    Default attempts: 15 mutation coordinates x 3 area references x 3 kappas x
    5 master seeds x 5 replicates = 3,375 rows.
    """
    if replicates_per_cell <= 0:
        raise ValueError("replicates_per_cell must be positive")
    nested = tuple(int(value) for value in nested_barrier_grids)
    if not nested or any(value <= 0 for value in nested):
        raise ValueError("nested_barrier_grids must contain positive values")
    if tuple(sorted(set(nested))) != nested:
        raise ValueError("nested_barrier_grids must be strictly increasing and unique")
    finest_grid = nested[-1]
    mutation_coordinates = tuple(primary_phase_grid() if coordinates is None else coordinates)
    rows: list[Protocol002SourceCoordinate] = []
    for coordinate in mutation_coordinates:
        for area_reference in area_references:
            for kappa in kappas:
                for master_seed in master_seeds:
                    for replicate in range(replicates_per_cell):
                        rows.append(
                            Protocol002SourceCoordinate(
                                coordinate=coordinate,
                                area_reference=area_reference,
                                kappa=kappa,
                                nested_barrier_grid=finest_grid,
                                stage_generations=stage_generations,
                                hold_generations=hold_generations,
                                master_seed=master_seed,
                                replicate=replicate,
                            )
                        )
    return tuple(rows)


def planned_source_grid_manifest() -> SourceSkeletonManifest:
    return SourceSkeletonManifest(records=tuple(skeleton_record(row) for row in protocol002_source_grid()))


def planned_source_grid_artifact() -> dict:
    return planned_source_grid_manifest().to_artifact()


def artifact_sha256(artifact: dict[str, Any]) -> str:
    payload = json.dumps(artifact, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def planned_source_grid_lock_artifact() -> dict[str, Any]:
    artifact = planned_source_grid_artifact()
    return {
        "artifact": "Protocol 002 Stage I planned source-grid manifest lock",
        "full_manifest_path": DEFAULT_SOURCE_GRID_PATH.as_posix(),
        "full_manifest_sha256": artifact_sha256(artifact),
        "record_count": artifact["record_count"],
        "simulation_result_present": artifact["simulation_result_present"],
        "status_counts": artifact["status_counts"],
        "grid": {
            "mutation_coordinate_count": len(primary_phase_grid()),
            "area_references": list(SOURCE_AREA_REFERENCES),
            "kappas": list(SOURCE_KAPPAS),
            "nested_barrier_grids": list(SOURCE_NESTED_BARRIER_GRIDS),
            "nested_barrier_grids_form_one_resolution_set": True,
            "master_seeds": list(SOURCE_MASTER_SEEDS),
            "replicates_per_cell": SOURCE_REPLICATES_PER_CELL,
            "stage_generations": SOURCE_STAGE_GENERATIONS,
            "hold_generations": SOURCE_HOLD_GENERATIONS,
        },
        "interpretation": {
            "planned_rows_only": True,
            "source_reconstruction_run": False,
            "type_s_result_present": False,
        },
    }


def write_planned_source_grid(path: str | Path = DEFAULT_SOURCE_GRID_PATH) -> Path:
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(planned_source_grid_artifact(), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return destination


def write_planned_source_grid_lock(path: str | Path = DEFAULT_SOURCE_GRID_LOCK_PATH) -> Path:
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(planned_source_grid_lock_artifact(), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return destination
