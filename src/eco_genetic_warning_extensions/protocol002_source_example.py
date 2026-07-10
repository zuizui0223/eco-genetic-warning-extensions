"""Deterministic example manifest for the Protocol 002 source skeleton.

The example exists to test serialization and artifact shape only. It contains no
source-reconstruction result.
"""
from __future__ import annotations

import json
from pathlib import Path

from .mutation_coordinates import MutationCoordinates
from .protocol002_source_skeleton import (
    Protocol002SourceCoordinate,
    SourceSkeletonManifest,
    skeleton_record,
)

DEFAULT_SOURCE_EXAMPLE_PATH = Path("artifacts/protocol002/source_skeleton_example_manifest.json")


def example_source_coordinate() -> Protocol002SourceCoordinate:
    """Return one deterministic Protocol 002 source coordinate for schema tests."""
    return Protocol002SourceCoordinate(
        coordinate=MutationCoordinates(kappa_mu=0.20, p_star=0.75),
        area_reference=1.0,
        kappa=4.5,
        nested_barrier_grid=49,
        stage_generations=30,
        hold_generations=30,
        master_seed=20270210,
        replicate=0,
    )


def example_source_skeleton_manifest() -> SourceSkeletonManifest:
    """Return a no-simulation example manifest with one explicit not-run record."""
    return SourceSkeletonManifest(records=(skeleton_record(example_source_coordinate()),))


def example_source_skeleton_artifact() -> dict:
    """Return deterministic JSON-serializable content for the example manifest."""
    return example_source_skeleton_manifest().to_artifact()


def write_source_skeleton_example(path: str | Path = DEFAULT_SOURCE_EXAMPLE_PATH) -> Path:
    """Write the deterministic source-skeleton example manifest."""
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(
        json.dumps(example_source_skeleton_artifact(), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return destination
