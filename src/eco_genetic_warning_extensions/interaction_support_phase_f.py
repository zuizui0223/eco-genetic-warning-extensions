"""Predeclared warning-blind interaction-support Phase F manifest.

Phase F tests the existing interaction-feedback parameter as an aggregate
interaction-support axis around the independently recovered R4 anchor.  It does
not introduce a partner network and therefore must not be interpreted as a
direct manipulation of interaction richness, connectance, or dimensionality.
"""
from __future__ import annotations

from dataclasses import dataclass

from .mutation_coordinates import MutationCoordinates

# Reuse the three interaction-feedback values declared in the original
# Protocol 002 source grid.  This avoids post-hoc fine tuning around kappa=4.5.
PHASE_F_INTERACTION_KAPPAS = (3.0, 4.5, 6.0)
PHASE_F_MASTER_SEEDS = (20290510, 20290511, 20290512, 20290513, 20290514)
PHASE_F_REPLICATES_PER_SEED = 20
PHASE_F_MIN_BASELINE_ELIGIBLE_PER_SEED = 10
PHASE_F_RAMP_GENERATIONS = 30
PHASE_F_HOLD_GENERATIONS = 90
PHASE_F_AREA_REFERENCE = 1.0
PHASE_F_KAPPA_MU = 0.35
PHASE_F_P_STAR = 0.35
PHASE_F_BARRIER_INCREASE = 0.30
PHASE_F_MIGRATION_RATE = 0.0


@dataclass(frozen=True)
class InteractionSupportCondition:
    interaction_kappa: float

    def __post_init__(self) -> None:
        if float(self.interaction_kappa) <= 0.0:
            raise ValueError("interaction_kappa must be positive")

    def identity(self) -> dict[str, float]:
        return {"interaction_kappa": float(self.interaction_kappa)}


def phase_f_coordinate() -> MutationCoordinates:
    return MutationCoordinates(kappa_mu=PHASE_F_KAPPA_MU, p_star=PHASE_F_P_STAR)


def phase_f_conditions() -> tuple[InteractionSupportCondition, ...]:
    return tuple(InteractionSupportCondition(value) for value in PHASE_F_INTERACTION_KAPPAS)


def phase_f_manifest() -> dict[str, object]:
    return {
        "protocol": "warning-blind interaction-support Phase F",
        "scientific_scope": "aggregate_interaction_feedback_condition_map",
        "calibration_scope": "source_and_trait_loss_only",
        "coordinate": {"kappa_mu": PHASE_F_KAPPA_MU, "p_star": PHASE_F_P_STAR},
        "fixed_conditions": {
            "area_reference": PHASE_F_AREA_REFERENCE,
            "ramp_generations": PHASE_F_RAMP_GENERATIONS,
            "hold_generations": PHASE_F_HOLD_GENERATIONS,
            "horizon": PHASE_F_RAMP_GENERATIONS + PHASE_F_HOLD_GENERATIONS,
            "normalised_barrier_increase": PHASE_F_BARRIER_INCREASE,
            "fragmentation_geometry": "four_equal_patches_fixed_total_area",
            "migration_rate": PHASE_F_MIGRATION_RATE,
        },
        "interaction_kappas": list(PHASE_F_INTERACTION_KAPPAS),
        "interaction_kappa_provenance": "original_protocol002_source_grid_values",
        "master_seeds": list(PHASE_F_MASTER_SEEDS),
        "replicates_per_seed": PHASE_F_REPLICATES_PER_SEED,
        "minimum_baseline_eligible_per_seed": PHASE_F_MIN_BASELINE_ELIGIBLE_PER_SEED,
        "source_preparations_per_condition": len(PHASE_F_MASTER_SEEDS) * PHASE_F_REPLICATES_PER_SEED,
        "condition_count": len(PHASE_F_INTERACTION_KAPPAS),
        "warning_blind": True,
        "output_scope": "source_projection_baseline_and_trait_loss_only",
        "interpretation_boundary": (
            "interaction_kappa is the existing aggregate positive-feedback strength; "
            "it is not partner richness, connectance, network dimensionality, pollinator diversity, "
            "or a direct habitat-fragmentation metric"
        ),
        "stop_rule": (
            "classify the three pre-existing kappa levels once; do not refine kappa merely to create "
            "or widen an R4 interval"
        ),
    }
