"""Declared Protocol 002 Stage I source-coordinate grid enumerator.

This module enumerates planned source attempts only. It does not run H1 source
reconstruction or produce Type S ecological evidence.
"""
from __future__ import annotations

import json
from collections.abc import Iterable
from pathlib import Path

from .mutation_coordinates import MutationCoordinates, primary_phase_grid
from .protocol002_source_skeleton import (
    Protocol002SourceCoordinate,
    SourceSkeletonManifest,
    skeleton_record,
)

SOURCE_AREA_REFERENCES: tuple[float, ...] = (0.8, 1.0, 1.2)
SOURCE_KAPPAS: tuple[float, ...] = (3.0, 4.5, 6.0)
SOURCE_MASTER_SEEDS: tuple[int, ...] = (20270210, 20270211, 20270212, 20270213, 20270214)
SOURCE_REPLICATES_PER_CELL: int = 5
SOURCE_NESTED_BARRIER_GRIDS: tuple[int, ...] = (25, 49, 97)
SOURCE_STAGE_GENERATIONS: int = 30
SOURCE_HOLD_GENERATIONS: int = 30

DEFAULT_SOURCE_GRID_PATH = Path("artifacts/protocol002/source_grid_planned_manifest.json")


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
    """Enumerate declared Stage I source-attempt coordinates.

    The default grid has 15 mutation coordinates, three area references, three
    kappa values, three nested barrier grids, five master seeds, and five
    replicates per seed block, for 10,125 planned attempt rows.
    """
    if replicates_per_cell <= 0:
        raise ValueError("replicates_per_cell must be positive")
    mutation_coordinates = tuple(primary_phase_grid() if coordinates is None else coordinates)
    rows: list[Protocol002SourceCoordinate] = []
    for coordinate in mutation_coordinates:
        for area_reference in area_references:
            for kappa in kappas:
                for nested_barrier_grid in nested_barrier_grids:
                    for master_seed in master_seeds:
                        for replicate in range(replicates_per_cell):
                            rows.append(
                                Protocol002SourceCoordinate(
                                    coordinate=coordinate,
                                    area_reference=area_reference,
                                    kappa=kappa,
                                    nested_barrier_grid=nested_barrier_grid,
                                    stage_generations=stage_generations,
                                    hold_generations=hold_generations,
                                    master_seed=master_seed,
                                    replicate=replicate,
                                )
                            )
    return tuple(rows)


def planned_source_grid_manifest() -> SourceSkeletonManifest:
    """Return a no-simulation manifest containing every planned source row."""
    return SourceSkeletonManifest(records=tuple(skeleton_record(row) for row in protocol002_source_grid()))


def planned_source_grid_artifact() -> dict:
    """Return deterministic JSON-serializable content for the planned source grid."""
    return planned_source_grid_manifest().to_artifact()


def write_planned_source_grid(path: str | Path = DEFAULT_SOURCE_GRID_PATH) -> Path:
    """Write the no-simulation planned source grid manifest."""
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(
        json.dumps(planned_source_grid_artifact(), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return destination
