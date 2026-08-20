"""Predeclared manifests for warning-blind recurrent-transition frontier refinement."""
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

PHASE_B_KAPPA_MU = 0.35
PHASE_B_P_STAR = (0.30, 0.35, 0.40, 0.45)
PHASE_B_MASTER_SEEDS = (20281210, 20281211, 20281212, 20281213, 20281214)
PHASE_B_REPLICATES_PER_SEED = 5
PHASE_B_CONFIRMATION_MASTER_SEEDS = (20290110, 20290111, 20290112, 20290113, 20290114)
PHASE_B_CONFIRMATION_REPLICATES_PER_SEED = 20
PHASE_B_RAMP_GENERATIONS = 30
PHASE_B_HOLD_GENERATIONS = 90


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

PHASE_B_ANCHOR = FrontierAnchor(
    "B1", area_reference=1.0, interaction_kappa=4.5, normalised_barrier_increase=0.30
)


@dataclass(frozen=True)
class FrontierRefinementCell:
    cell_index: int
    anchor: FrontierAnchor
    coordinate: MutationCoordinates
    ramp_generations: int = 30
    hold_generations: int = 90

    @property
    def horizon(self) -> int:
        return self.ramp_generations + self.hold_generations

    def identity(self) -> dict[str, int | float | str]:
        return {
            "cell_index": self.cell_index,
            "anchor_id": self.anchor.anchor_id,
            "kappa_mu": self.coordinate.kappa_mu,
            "p_star": self.coordinate.p_star,
            "area_reference": self.anchor.area_reference,
            "kappa": self.anchor.interaction_kappa,
            "ramp_generations": self.ramp_generations,
            "hold_generations": self.hold_generations,
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
                    ramp_generations=PHASE_A_RAMP_GENERATIONS,
                    hold_generations=PHASE_A_HOLD_GENERATIONS,
                )
            )
    return tuple(cells)


def phase_b_cells() -> tuple[FrontierRefinementCell, ...]:
    return tuple(
        FrontierRefinementCell(
            cell_index=index,
            anchor=PHASE_B_ANCHOR,
            coordinate=MutationCoordinates(kappa_mu=PHASE_B_KAPPA_MU, p_star=p_star),
            ramp_generations=PHASE_B_RAMP_GENERATIONS,
            hold_generations=PHASE_B_HOLD_GENERATIONS,
        )
        for index, p_star in enumerate(PHASE_B_P_STAR)
    )


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


def phase_b_manifest() -> dict[str, object]:
    cells = phase_b_cells()
    return {
        "protocol": "warning-blind recurrent-transition frontier refinement Phase B",
        "historical_bracket": {
            "low": {"batch_index": 619, "p_star": 0.25, "seed_rates": [1.0] * 5, "regime": "rapid_loss"},
            "high": {"batch_index": 673, "p_star": 0.50, "seed_rates": [0.0] * 5, "regime": "persistence"},
        },
        "cell_count": len(cells),
        "attempts_per_cell": len(PHASE_B_MASTER_SEEDS) * PHASE_B_REPLICATES_PER_SEED,
        "planned_refinement_attempts": len(cells) * len(PHASE_B_MASTER_SEEDS) * PHASE_B_REPLICATES_PER_SEED,
        "master_seeds": list(PHASE_B_MASTER_SEEDS),
        "replicates_per_seed": PHASE_B_REPLICATES_PER_SEED,
        "confirmation_master_seeds": list(PHASE_B_CONFIRMATION_MASTER_SEEDS),
        "confirmation_replicates_per_seed": PHASE_B_CONFIRMATION_REPLICATES_PER_SEED,
        "warning_fields_available": False,
        "diversity_fields_available": False,
        "cells": [cell.identity() for cell in cells],
    }
