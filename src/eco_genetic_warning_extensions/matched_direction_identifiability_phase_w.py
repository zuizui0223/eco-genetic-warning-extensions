"""Deterministic identifiability audit for a direction-only warning comparison.

Phase W adds no simulation and inspects no genetic-warning outcome. It reuses five
immutable Protocol-002 Stage-II batch artifacts that already share the Phase-V
symmetric ecology/deterioration anchor while holding recurrent-transition strength
``kappa_mu=0.20`` fixed and varying only ``p_star``.

The question is upstream of warning: does the predeclared same-strength p_star grid
contain a directional coordinate with an intermediate functional-loss process under
the exact same ecology and deterioration schedule as the symmetric benchmark?
"""
from __future__ import annotations

from dataclasses import dataclass

TARGET_LOSS_BAND = (0.30, 0.70)
REFERENCE_ALPHA = 0.05


@dataclass(frozen=True)
class LockedStage2Cell:
    p_star: float
    batch_index: int
    artifact_id: int
    artifact_digest: str
    baseline_eligible: int
    trait_loss: int
    seed_blocks: tuple[tuple[int, int], ...]
    kappa_mu: float = 0.20
    area_reference: float = 0.8
    interaction_kappa: float = 6.0
    ramp_generations: int = 30
    hold_generations: int = 90
    normalised_barrier_increase: float = 0.15

    @property
    def horizon(self) -> int:
        return self.ramp_generations + self.hold_generations

    @property
    def pooled_loss(self) -> float:
        return self.trait_loss / self.baseline_eligible

    def as_dict(self) -> dict[str, object]:
        return {
            "p_star": self.p_star,
            "kappa_mu": self.kappa_mu,
            "area_reference": self.area_reference,
            "interaction_kappa": self.interaction_kappa,
            "ramp_generations": self.ramp_generations,
            "hold_generations": self.hold_generations,
            "horizon": self.horizon,
            "normalised_barrier_increase": self.normalised_barrier_increase,
            "batch_index": self.batch_index,
            "artifact_id": self.artifact_id,
            "artifact_digest": self.artifact_digest,
            "baseline_eligible": self.baseline_eligible,
            "trait_loss": self.trait_loss,
            "pooled_loss": self.pooled_loss,
            "seed_blocks": [
                {"eligible": eligible, "losses": losses, "rate": losses / eligible}
                for eligible, losses in self.seed_blocks
            ],
        }


SAME_STRENGTH_CELLS = (
    LockedStage2Cell(
        p_star=0.10,
        batch_index=282,
        artifact_id=8260028479,
        artifact_digest="sha256:a88a1c5614054263ad08290acadb671977ae1d66e428c2c2dcc9936c5d21a0a9",
        baseline_eligible=22,
        trait_loss=22,
        seed_blocks=((4, 4), (4, 4), (5, 5), (4, 4), (5, 5)),
    ),
    LockedStage2Cell(
        p_star=0.25,
        batch_index=336,
        artifact_id=8260079020,
        artifact_digest="sha256:07201c3e7704b60eb85961390ab9641267279f520574b67b619237606578e2e9",
        baseline_eligible=17,
        trait_loss=17,
        seed_blocks=((3, 3), (4, 4), (2, 2), (3, 3), (5, 5)),
    ),
    LockedStage2Cell(
        p_star=0.50,
        batch_index=390,
        artifact_id=8260125567,
        artifact_digest="sha256:4b842a4ccc113309623c87d1c2228dfa9abc36d93d4598b28c4bc72fc984a42e",
        baseline_eligible=20,
        trait_loss=8,
        seed_blocks=((5, 3), (3, 2), (3, 0), (5, 3), (4, 0)),
    ),
    LockedStage2Cell(
        p_star=0.75,
        batch_index=444,
        artifact_id=8260180102,
        artifact_digest="sha256:df96e9d5951b1f9a03afed3efbf9a86f973d2ec62cbe041d221cada341020d5b",
        baseline_eligible=21,
        trait_loss=0,
        seed_blocks=((5, 0), (4, 0), (3, 0), (5, 0), (4, 0)),
    ),
    LockedStage2Cell(
        p_star=0.90,
        batch_index=498,
        artifact_id=8260233506,
        artifact_digest="sha256:fc8b53ef8a24038d6f728655d2bec20bd5acbd01812c6439ae08e07a7c23fd83",
        baseline_eligible=22,
        trait_loss=0,
        seed_blocks=((5, 0), (3, 0), (4, 0), (5, 0), (5, 0)),
    ),
)

# A historical exact-ecology/schedule cell with similar pooled incidence exists
# only after recurrent-transition strength is also changed. It is retained as an
# identification counterexample, not as a direction-only comparator.
CROSS_STRENGTH_BRIDGE = {
    "kappa_mu": 0.05,
    "p_star": 0.90,
    "area_reference": 0.8,
    "interaction_kappa": 6.0,
    "ramp_generations": 30,
    "hold_generations": 90,
    "horizon": 120,
    "normalised_barrier_increase": 0.15,
    "batch_index": 228,
    "artifact_id": 8260226534,
    "artifact_digest": "sha256:3e1795a43f0afb5bc528be62513f40860950f2ba6d58ab4eaff4a52f0f97662b",
    "baseline_eligible": 21,
    "trait_loss": 10,
    "pooled_loss": 10 / 21,
    "seed_blocks": ((5, 3), (3, 2), (5, 1), (4, 2), (4, 2)),
}


def extreme_clopper_pearson_reference(losses: int, eligible: int, alpha: float = REFERENCE_ALPHA) -> tuple[float, float] | None:
    """Two-sided Clopper-Pearson interval for all-loss or no-loss blocks.

    Only the closed-form boundary cases used by this audit are implemented.
    This reference does not assume simulator trajectories are iid Bernoulli; it
    quantifies how far the observed extreme pooled proportions lie from the old
    intermediate-loss band under a standard finite-sample reference.
    """
    if eligible < 1 or not 0 <= losses <= eligible:
        raise ValueError("invalid loss/eligible counts")
    if not 0.0 < alpha < 1.0:
        raise ValueError("alpha must lie in (0,1)")
    tail = alpha / 2.0
    if losses == eligible:
        return tail ** (1.0 / eligible), 1.0
    if losses == 0:
        return 0.0, 1.0 - tail ** (1.0 / eligible)
    return None


def phase_w_audit() -> dict[str, object]:
    rows = tuple(SAME_STRENGTH_CELLS)
    symmetric = next(row for row in rows if row.p_star == 0.50)
    directional = tuple(row for row in rows if row.p_star != 0.50)
    lower, upper = TARGET_LOSS_BAND

    directional_reference = []
    for row in directional:
        interval = extreme_clopper_pearson_reference(row.trait_loss, row.baseline_eligible)
        directional_reference.append({
            "p_star": row.p_star,
            "pooled_loss": row.pooled_loss,
            "extreme_reference_interval_95": None if interval is None else list(interval),
            "inside_historical_intermediate_band": lower <= row.pooled_loss <= upper,
        })

    exact_match_candidates = [row.p_star for row in directional if lower <= row.pooled_loss <= upper]
    opened = bool(exact_match_candidates)
    decision = (
        "direction_only_warning_comparison_opened"
        if opened
        else "direction_only_warning_comparison_not_identifiable_under_frozen_common_schedule"
    )

    return {
        "stage": "matched recurrent-transition direction identifiability audit Phase W",
        "simulation_added": False,
        "warning_outcomes_inspected": False,
        "source_workflow_run": 29192711417,
        "fixed_common_context": {
            "kappa_mu": 0.20,
            "area_reference": 0.8,
            "interaction_kappa": 6.0,
            "ramp_generations": 30,
            "hold_generations": 90,
            "horizon": 120,
            "normalised_barrier_increase": 0.15,
            "projection": "equal_isolated",
            "historical_intermediate_loss_band": list(TARGET_LOSS_BAND),
        },
        "same_strength_cells": [row.as_dict() for row in rows],
        "symmetric_reference": symmetric.as_dict(),
        "directional_extreme_reference": directional_reference,
        "same_strength_directional_candidates_inside_band": exact_match_candidates,
        "cross_strength_bridge": {
            **{key: value for key, value in CROSS_STRENGTH_BRIDGE.items() if key != "seed_blocks"},
            "seed_blocks": [
                {"eligible": eligible, "losses": losses, "rate": losses / eligible}
                for eligible, losses in CROSS_STRENGTH_BRIDGE["seed_blocks"]
            ],
            "identification_role": (
                "similar intermediate incidence is obtainable under the exact ecology/schedule only after changing kappa_mu as well as p_star; "
                "therefore this cell cannot identify a direction-only warning effect"
            ),
        },
        "direction_only_warning_comparison_opened": opened,
        "decision": decision,
        "conclusion": (
            "Within the predeclared kappa_mu=0.20 p_star grid, holding ecology and deterioration exactly fixed moves the loss process from "
            "all observed losses at p_star=0.10/0.25 through intermediate loss at p_star=0.50 to no observed losses at p_star=0.75/0.90. "
            "No same-strength directional coordinate therefore supplies the matched intermediate-loss process required for a direction-only warning comparison."
        ),
        "boundary": (
            "Opening a matched warning comparison would require adding finer p_star values or retuning kappa_mu, ecology, deterioration magnitude, or horizon. "
            "Those changes would either be outcome-guided refinement or destroy single-factor identification, so they are not opened in the present programme."
        ),
    }
