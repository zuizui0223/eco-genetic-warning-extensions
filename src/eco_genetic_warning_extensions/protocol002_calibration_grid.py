"""Protocol 002 Stage II trait-loss-only calibration grid.

This module enumerates planned calibration attempts and produces a lightweight
lock for the full deterministic manifest. It does not run calibration and must
not expose warning or diversity outcomes.
"""
from __future__ import annotations

import hashlib
import json
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .mutation_coordinates import MutationCoordinates, primary_phase_grid
from .protocol002_calibration import (
    CALIBRATION_BARRIER_INCREASES,
    CALIBRATION_HOLD_GENERATIONS,
    CALIBRATION_MASTER_SEEDS,
    CALIBRATION_RAMP_GENERATIONS,
    CALIBRATION_REPLICATES_PER_CELL,
)
from .protocol002_source_grid import SOURCE_AREA_REFERENCES, SOURCE_KAPPAS

DEFAULT_CALIBRATION_GRID_PATH = Path("artifacts/protocol002/stage2_calibration_planned_manifest.json")
DEFAULT_CALIBRATION_GRID_LOCK_PATH = Path("artifacts/protocol002/stage2_calibration_planned_lock.json")


@dataclass(frozen=True)
class Protocol002CalibrationAttempt:
    """One planned Stage II trait-loss-only calibration attempt."""

    coordinate: MutationCoordinates
    area_reference: float
    kappa: float
    ramp_generations: int
    hold_generations: int
    normalised_barrier_increase: float
    master_seed: int
    replicate: int

    def __post_init__(self) -> None:
        if self.area_reference <= 0.0:
            raise ValueError("area_reference must be positive")
        if self.kappa <= 0.0:
            raise ValueError("kappa must be positive")
        if self.ramp_generations <= 0 or self.hold_generations <= 0:
            raise ValueError("ramp and hold generations must be positive")
        if not 0.0 < self.normalised_barrier_increase <= 1.0:
            raise ValueError("normalised_barrier_increase must lie in (0, 1]")
        if self.replicate < 0:
            raise ValueError("replicate must be non-negative")

    @property
    def horizon(self) -> int:
        return self.ramp_generations + self.hold_generations

    def identity(self) -> dict[str, int | float]:
        """Return the stable blind identity for one planned attempt."""
        return {
            "kappa_mu": self.coordinate.kappa_mu,
            "p_star": self.coordinate.p_star,
            "area_reference": self.area_reference,
            "kappa": self.kappa,
            "ramp_generations": self.ramp_generations,
            "hold_generations": self.hold_generations,
            "horizon": self.horizon,
            "normalised_barrier_increase": self.normalised_barrier_increase,
            "master_seed": self.master_seed,
            "replicate": self.replicate,
        }


def protocol002_calibration_grid(
    *,
    coordinates: Iterable[MutationCoordinates] | None = None,
    area_references: Iterable[float] = SOURCE_AREA_REFERENCES,
    kappas: Iterable[float] = SOURCE_KAPPAS,
    hold_generations: Iterable[int] = CALIBRATION_HOLD_GENERATIONS,
    barrier_increases: Iterable[float] = CALIBRATION_BARRIER_INCREASES,
    master_seeds: Iterable[int] = CALIBRATION_MASTER_SEEDS,
    replicates_per_cell: int = CALIBRATION_REPLICATES_PER_CELL,
    ramp_generations: int = CALIBRATION_RAMP_GENERATIONS,
) -> tuple[Protocol002CalibrationAttempt, ...]:
    """Enumerate the full blind Stage II calibration attempt grid."""
    if replicates_per_cell <= 0:
        raise ValueError("replicates_per_cell must be positive")
    mutation_coordinates = tuple(primary_phase_grid() if coordinates is None else coordinates)
    rows: list[Protocol002CalibrationAttempt] = []
    for coordinate in mutation_coordinates:
        for area_reference in area_references:
            for kappa in kappas:
                for hold in hold_generations:
                    for increase in barrier_increases:
                        for master_seed in master_seeds:
                            for replicate in range(replicates_per_cell):
                                rows.append(
                                    Protocol002CalibrationAttempt(
                                        coordinate=coordinate,
                                        area_reference=area_reference,
                                        kappa=kappa,
                                        ramp_generations=ramp_generations,
                                        hold_generations=hold,
                                        normalised_barrier_increase=increase,
                                        master_seed=master_seed,
                                        replicate=replicate,
                                    )
                                )
    return tuple(rows)


def planned_calibration_grid_artifact() -> dict[str, Any]:
    """Return the full deterministic no-simulation calibration plan."""
    attempts = protocol002_calibration_grid()
    candidate_cell_count = (
        len(primary_phase_grid())
        * len(SOURCE_AREA_REFERENCES)
        * len(SOURCE_KAPPAS)
        * len(CALIBRATION_HOLD_GENERATIONS)
        * len(CALIBRATION_BARRIER_INCREASES)
    )
    return {
        "stage": "Protocol 002 Stage II trait-loss-only calibration plan",
        "simulation_result_present": False,
        "warning_fields_present": False,
        "candidate_cell_count": candidate_cell_count,
        "attempt_count": len(attempts),
        "attempts_per_candidate_cell": len(CALIBRATION_MASTER_SEEDS) * CALIBRATION_REPLICATES_PER_CELL,
        "attempts": [attempt.identity() for attempt in attempts],
    }


def artifact_sha256(artifact: dict[str, Any]) -> str:
    payload = json.dumps(artifact, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def planned_calibration_grid_lock_artifact() -> dict[str, Any]:
    """Return a lightweight lock for the full 20,250-attempt plan."""
    artifact = planned_calibration_grid_artifact()
    return {
        "artifact": "Protocol 002 Stage II calibration grid lock",
        "full_manifest_path": DEFAULT_CALIBRATION_GRID_PATH.as_posix(),
        "full_manifest_sha256": artifact_sha256(artifact),
        "candidate_cell_count": artifact["candidate_cell_count"],
        "attempt_count": artifact["attempt_count"],
        "attempts_per_candidate_cell": artifact["attempts_per_candidate_cell"],
        "grid": {
            "mutation_coordinate_count": len(primary_phase_grid()),
            "area_references": list(SOURCE_AREA_REFERENCES),
            "kappas": list(SOURCE_KAPPAS),
            "ramp_generations": CALIBRATION_RAMP_GENERATIONS,
            "hold_generations": list(CALIBRATION_HOLD_GENERATIONS),
            "normalised_barrier_increases": list(CALIBRATION_BARRIER_INCREASES),
            "master_seeds": list(CALIBRATION_MASTER_SEEDS),
            "replicates_per_cell": CALIBRATION_REPLICATES_PER_CELL,
        },
        "interpretation": {
            "planned_rows_only": True,
            "trait_loss_only": True,
            "warning_fields_present": False,
            "simulation_result_present": False,
            "domain_selected": False,
        },
    }


def write_planned_calibration_grid(path: str | Path = DEFAULT_CALIBRATION_GRID_PATH) -> Path:
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(
        json.dumps(planned_calibration_grid_artifact(), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return destination


def write_planned_calibration_grid_lock(path: str | Path = DEFAULT_CALIBRATION_GRID_LOCK_PATH) -> Path:
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(
        json.dumps(planned_calibration_grid_lock_artifact(), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return destination
