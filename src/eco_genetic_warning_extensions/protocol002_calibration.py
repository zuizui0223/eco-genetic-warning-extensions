"""Protocol 002 Stage II trait-loss-only calibration schema and selection rules.

Calibration is blind to genetic-warning, lead/lag, diversity, and event-pair
outcomes. This module defines candidate rows and deterministic domain selection;
it does not run the calibration campaign.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Mapping

from .mutation_coordinates import MutationCoordinates

CALIBRATION_RAMP_GENERATIONS: int = 30
CALIBRATION_HOLD_GENERATIONS: tuple[int, ...] = (90, 210)
CALIBRATION_BARRIER_INCREASES: tuple[float, ...] = (0.15, 0.30, 0.45)
CALIBRATION_MASTER_SEEDS: tuple[int, ...] = (20270310, 20270311, 20270312, 20270313, 20270314)
CALIBRATION_REPLICATES_PER_CELL: int = 5
ELIGIBLE_TRAIT_LOSS_RATE_MIN: float = 0.30
ELIGIBLE_TRAIT_LOSS_RATE_MAX: float = 0.70

FORBIDDEN_CALIBRATION_TOKENS: tuple[str, ...] = (
    "h_alpha",
    "h_gamma",
    "warning",
    "lead",
    "lag",
    "lead_time",
    "diversity",
    "heterozygosity",
    "event_pair",
    "warning_time",
)


@dataclass(frozen=True)
class Protocol002CalibrationCandidate:
    """One Stage II schedule candidate for one mutation/source coordinate."""

    coordinate: MutationCoordinates
    area_reference: float
    kappa: float
    ramp_generations: int
    hold_generations: int
    normalised_barrier_increase: float
    seed_block_trait_loss_rates: tuple[float, ...]

    def __post_init__(self) -> None:
        if self.area_reference <= 0.0:
            raise ValueError("area_reference must be positive")
        if self.kappa <= 0.0:
            raise ValueError("kappa must be positive")
        if self.ramp_generations <= 0:
            raise ValueError("ramp_generations must be positive")
        if self.hold_generations <= 0:
            raise ValueError("hold_generations must be positive")
        if not 0.0 < self.normalised_barrier_increase <= 1.0:
            raise ValueError("normalised_barrier_increase must lie in (0, 1]")
        if not self.seed_block_trait_loss_rates:
            raise ValueError("at least one seed-block trait-loss rate is required")
        if any(not 0.0 <= rate <= 1.0 for rate in self.seed_block_trait_loss_rates):
            raise ValueError("seed-block trait-loss rates must lie in [0, 1]")

    @property
    def horizon(self) -> int:
        return self.ramp_generations + self.hold_generations

    @property
    def pooled_trait_loss_rate(self) -> float:
        return sum(self.seed_block_trait_loss_rates) / len(self.seed_block_trait_loss_rates)

    def is_eligible(self) -> bool:
        return all(
            ELIGIBLE_TRAIT_LOSS_RATE_MIN <= rate <= ELIGIBLE_TRAIT_LOSS_RATE_MAX
            for rate in self.seed_block_trait_loss_rates
        )

    def rank_key(self) -> tuple[float, int, float, float, float]:
        return (
            abs(self.pooled_trait_loss_rate - 0.50),
            self.horizon,
            self.normalised_barrier_increase,
            self.area_reference,
            self.kappa,
        )


def assert_protocol002_blind_calibration_columns(columns: Iterable[str]) -> None:
    """Reject fields that could leak warning/diversity outcomes into calibration."""
    lowered = tuple(str(column).strip().lower() for column in columns)
    leaked = [column for column in lowered if any(token in column for token in FORBIDDEN_CALIBRATION_TOKENS)]
    if leaked:
        raise ValueError(
            "Protocol 002 calibration is trait-loss-only; forbidden calibration columns: "
            + ", ".join(sorted(leaked))
        )


def protocol002_calibration_candidate_from_row(
    row: Mapping[str, object],
    *,
    seed_block_rates: Iterable[float],
) -> Protocol002CalibrationCandidate:
    """Build one typed candidate from blind metadata and seed-block rates."""
    assert_protocol002_blind_calibration_columns(row.keys())
    return Protocol002CalibrationCandidate(
        coordinate=MutationCoordinates(
            kappa_mu=float(row["kappa_mu"]),
            p_star=float(row["p_star"]),
        ),
        area_reference=float(row["area_reference"]),
        kappa=float(row["kappa"]),
        ramp_generations=int(row["ramp_generations"]),
        hold_generations=int(row["hold_generations"]),
        normalised_barrier_increase=float(row["normalised_barrier_increase"]),
        seed_block_trait_loss_rates=tuple(float(rate) for rate in seed_block_rates),
    )


def select_protocol002_calibration_domain(
    candidates: Iterable[Protocol002CalibrationCandidate],
    *,
    coordinate: MutationCoordinates,
) -> Protocol002CalibrationCandidate | None:
    """Select at most one eligible domain for one mutation coordinate."""
    eligible = [
        candidate
        for candidate in candidates
        if candidate.coordinate == coordinate and candidate.is_eligible()
    ]
    return min(eligible, key=lambda candidate: candidate.rank_key()) if eligible else None
