"""Selection rules for Protocol 001.

Calibration is deliberately blind to genetic-warning outcomes. Candidates contain
only post-baseline realised trait-loss frequencies by independent seed block.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Mapping

FORBIDDEN_CALIBRATION_TOKENS = ("h_alpha", "h_gamma", "warning", "lead", "lag", "lead_time")


@dataclass(frozen=True)
class CalibrationCandidate:
    panel: str
    area_reference: float
    kappa: float
    ramp_generations: int
    hold_generations: int
    normalised_barrier_increase: float
    seed_block_trait_loss_rates: tuple[float, ...]

    @property
    def horizon(self) -> int:
        return self.ramp_generations + self.hold_generations

    @property
    def pooled_trait_loss_rate(self) -> float:
        return sum(self.seed_block_trait_loss_rates) / len(self.seed_block_trait_loss_rates)

    def is_eligible(self) -> bool:
        return bool(self.seed_block_trait_loss_rates) and all(
            0.30 <= rate <= 0.70 for rate in self.seed_block_trait_loss_rates
        )

    def rank_key(self) -> tuple[float, int, float, float, float]:
        """Protocol 001's predeclared deterministic tie-break order."""
        return (
            abs(self.pooled_trait_loss_rate - 0.50),
            self.horizon,
            self.normalised_barrier_increase,
            self.area_reference,
            self.kappa,
        )


def assert_blind_calibration_columns(columns: Iterable[str]) -> None:
    """Reject inputs that could expose warning outcomes during schedule calibration."""
    lowered = tuple(str(column).strip().lower() for column in columns)
    leaked = [column for column in lowered if any(token in column for token in FORBIDDEN_CALIBRATION_TOKENS)]
    if leaked:
        raise ValueError(
            "Protocol 001 calibration is trait-loss-only; forbidden warning-related columns: "
            + ", ".join(sorted(leaked))
        )


def calibration_candidate_from_row(row: Mapping[str, object], *, seed_block_rates: Iterable[float]) -> CalibrationCandidate:
    """Build a candidate from non-warning metadata and independent seed-block rates."""
    assert_blind_calibration_columns(row.keys())
    rates = tuple(float(rate) for rate in seed_block_rates)
    if any(not 0.0 <= rate <= 1.0 for rate in rates):
        raise ValueError("seed-block trait-loss rates must lie in [0, 1]")
    return CalibrationCandidate(
        panel=str(row["panel"]),
        area_reference=float(row["area_reference"]),
        kappa=float(row["kappa"]),
        ramp_generations=int(row["ramp_generations"]),
        hold_generations=int(row["hold_generations"]),
        normalised_barrier_increase=float(row["normalised_barrier_increase"]),
        seed_block_trait_loss_rates=rates,
    )


def select_protocol_001_domain(candidates: Iterable[CalibrationCandidate], *, panel: str) -> CalibrationCandidate | None:
    """Select at most one eligible cell/schedule pair for one mutation panel member."""
    eligible = [candidate for candidate in candidates if candidate.panel == panel and candidate.is_eligible()]
    return min(eligible, key=lambda candidate: candidate.rank_key()) if eligible else None
