"""Predeclared Phase-A manifest for warning-blind frontier refinement."""
from __future__ import annotations

from dataclasses import dataclass

from .mutation_coordinates import MutationCoordinates

PHASE_A_KAPPA_MU = 0.05
PHASE_A_P_STAR = (0.775, 0.800, 0.825, 0.850, 0.875)
PHASE_A_MASTER_SEEDS = (20281010, 20281011, 20281012, 20281013, 20281014)
PHASE_A_REPLICATES_PER_SEED = 5
PHASE_A_CONFIRMATION_MASTER_SEEDS = (20281110, 20281111, 20281112, 20281113, 20281114)
PHASE_A_CONFIRMATION_REPLICATES_PER_SEED = 20
PHASE_A_RAMP_GENERATIONS = 30
PHASE_A_HOLD_GENERATIONS = 90


@dataclass(frozen=True)
class FrontierAnchor:
    anchor_id: str
    area_reference: float
    interaction_kappa: float
    normalised_barrier_increase: float


PHASE_A_ANCHORS = (
    FrontierAnchor("A1", area_reference=0.8, interaction_kappa=4.5, normalised_barrier_increase=0.45),
    FrontierAnchor("A2", area_reference=0.8, interaction_kappa=3.0, normalised_barrier_increase=0.15),
)


@dataclass(frozen=True)
class FrontierRefinementCell:
    cell_index: int
    anchor: FrontierAnchor
    coordinate: MutationCoordinates

    @property
    def horizon(self) -> int:
        return PHASE_A_RAMP_GENERATIONS + PHASE_A_HOLD_GENERATIONS

    def identity(self) -> dict[str, int | float | str]:
        return {
            "cell_index": self.cell_index,
            "anchor_id": self.anchor.anchor_id,
            "kappa_mu": self.coordinate.kappa_mu,
            "p_star": self.coordinate.p_star,
            "area_reference": self.anchor.area_reference,
            "kappa": self.anchor.interaction_kappa,
            "ramp_generations": PHASE_A_RAMP_GENERATIONS,
            "hold_generations": PHASE_A_HOLD_GENERATIONS,
            "horizon": self.horizon,
            "normalised_barrier_increase": self.anchor.normalised_barrier_increase,
        }


def phase_a_cells() -> tuple[FrontierRefinementCell, ...]:
    cells: list[FrontierRefinementCell] = []
    for anchor in PHASE_A_ANCHORS:
        for p_star in PHASE_A_P_STAR:
            cells.append(
                FrontierRefinementCell(
                    cell_index=len(cells),
                    anchor=anchor,
                    coordinate=MutationCoordinates(kappa_mu=PHASE_A_KAPPA_MU, p_star=p_star),
                )
            )
    return tuple(cells)


def phase_a_manifest() -> dict[str, object]:
    cells = phase_a_cells()
    return {
        "protocol": "warning-blind recurrent-transition frontier refinement Phase A",
        "cell_count": len(cells),
        "attempts_per_cell": len(PHASE_A_MASTER_SEEDS) * PHASE_A_REPLICATES_PER_SEED,
        "planned_refinement_attempts": len(cells) * len(PHASE_A_MASTER_SEEDS) * PHASE_A_REPLICATES_PER_SEED,
        "master_seeds": list(PHASE_A_MASTER_SEEDS),
        "replicates_per_seed": PHASE_A_REPLICATES_PER_SEED,
        "confirmation_master_seeds": list(PHASE_A_CONFIRMATION_MASTER_SEEDS),
        "confirmation_replicates_per_seed": PHASE_A_CONFIRMATION_REPLICATES_PER_SEED,
        "warning_fields_available": False,
        "diversity_fields_available": False,
        "cells": [cell.identity() for cell in cells],
    }
