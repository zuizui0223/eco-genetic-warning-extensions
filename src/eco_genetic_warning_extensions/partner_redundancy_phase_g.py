"""Predeclared warning-blind partner-redundancy Phase G manifest.

Phase G introduces a deliberately minimal partner-contribution layer around the
independently recovered R4 anchor.  All loss architectures begin with four
partners whose contributions sum to one.  Exactly one partner is removed at the
start of deterioration.  Partner identity is balanced by replicate index, so
every 20-replicate seed block loses each of the four partners exactly five times.

The three loss architectures therefore have the same mean retained aggregate
support (0.75) and the same partner richness before/after loss (4 -> 3).  They
differ only in how strongly interaction support is concentrated among partners.
This is a reduced-form functional-redundancy test, not a full ecological-network
model and not a test of connectance or adaptive rewiring.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import sqrt

from .mutation_coordinates import MutationCoordinates

PHASE_G_MASTER_SEEDS = (20290610, 20290611, 20290612, 20290613, 20290614)
PHASE_G_REPLICATES_PER_SEED = 20
PHASE_G_MIN_BASELINE_ELIGIBLE_PER_SEED = 10
PHASE_G_PARTNER_COUNT = 4
PHASE_G_RAMP_GENERATIONS = 30
PHASE_G_HOLD_GENERATIONS = 90
PHASE_G_AREA_REFERENCE = 1.0
PHASE_G_INTERACTION_KAPPA = 4.5
PHASE_G_KAPPA_MU = 0.35
PHASE_G_P_STAR = 0.35
PHASE_G_BARRIER_INCREASE = 0.30
PHASE_G_MIGRATION_RATE = 0.0


@dataclass(frozen=True)
class PartnerArchitectureCondition:
    name: str
    partner_weights: tuple[float, ...]
    remove_one_partner: bool

    def __post_init__(self) -> None:
        if len(self.partner_weights) != PHASE_G_PARTNER_COUNT:
            raise ValueError("Phase G requires exactly four partner weights")
        if any(value < 0.0 for value in self.partner_weights):
            raise ValueError("partner weights must be nonnegative")
        if abs(sum(self.partner_weights) - 1.0) > 1e-12:
            raise ValueError("partner weights must sum to one")

    @property
    def contribution_cv(self) -> float:
        mean = 1.0 / PHASE_G_PARTNER_COUNT
        variance = sum((value - mean) ** 2 for value in self.partner_weights) / PHASE_G_PARTNER_COUNT
        return sqrt(variance) / mean

    def identity(self) -> dict[str, object]:
        return {
            "name": self.name,
            "partner_weights": list(self.partner_weights),
            "remove_one_partner": self.remove_one_partner,
            "contribution_cv": self.contribution_cv,
        }


PHASE_G_CONDITIONS = (
    PartnerArchitectureCondition("intact_control", (0.25, 0.25, 0.25, 0.25), False),
    PartnerArchitectureCondition("even_redundant", (0.25, 0.25, 0.25, 0.25), True),
    PartnerArchitectureCondition("graded_contributions", (0.40, 0.30, 0.20, 0.10), True),
    PartnerArchitectureCondition("dominant_partner", (0.70, 0.10, 0.10, 0.10), True),
)


def phase_g_coordinate() -> MutationCoordinates:
    return MutationCoordinates(kappa_mu=PHASE_G_KAPPA_MU, p_star=PHASE_G_P_STAR)


def phase_g_conditions() -> tuple[PartnerArchitectureCondition, ...]:
    return PHASE_G_CONDITIONS


def lost_partner_index(replicate_index: int) -> int:
    if replicate_index < 0:
        raise ValueError("replicate_index must be nonnegative")
    return replicate_index % PHASE_G_PARTNER_COUNT


def retained_support(condition: PartnerArchitectureCondition, replicate_index: int) -> float:
    if not condition.remove_one_partner:
        return 1.0
    return 1.0 - condition.partner_weights[lost_partner_index(replicate_index)]


def mean_retained_support_per_seed(condition: PartnerArchitectureCondition) -> float:
    values = [retained_support(condition, index) for index in range(PHASE_G_REPLICATES_PER_SEED)]
    return sum(values) / len(values)


def phase_g_manifest() -> dict[str, object]:
    loss_conditions = [condition for condition in PHASE_G_CONDITIONS if condition.remove_one_partner]
    return {
        "protocol": "warning-blind partner-redundancy Phase G",
        "scientific_scope": "partner_contribution_concentration_under_matched_single_partner_loss",
        "calibration_scope": "source_and_trait_loss_only",
        "coordinate": {"kappa_mu": PHASE_G_KAPPA_MU, "p_star": PHASE_G_P_STAR},
        "fixed_conditions": {
            "area_reference": PHASE_G_AREA_REFERENCE,
            "interaction_kappa": PHASE_G_INTERACTION_KAPPA,
            "ramp_generations": PHASE_G_RAMP_GENERATIONS,
            "hold_generations": PHASE_G_HOLD_GENERATIONS,
            "horizon": PHASE_G_RAMP_GENERATIONS + PHASE_G_HOLD_GENERATIONS,
            "normalised_barrier_increase": PHASE_G_BARRIER_INCREASE,
            "fragmentation_geometry": "four_equal_patches_fixed_total_area",
            "migration_rate": PHASE_G_MIGRATION_RATE,
        },
        "partner_count_before_loss": PHASE_G_PARTNER_COUNT,
        "partner_count_after_loss": PHASE_G_PARTNER_COUNT - 1,
        "conditions": [condition.identity() for condition in PHASE_G_CONDITIONS],
        "loss_assignment": "lost_partner_index = replicate_index mod 4",
        "balanced_partner_loss_per_seed": True,
        "losses_per_partner_per_seed": PHASE_G_REPLICATES_PER_SEED // PHASE_G_PARTNER_COUNT,
        "mean_retained_support_loss_conditions": {
            condition.name: mean_retained_support_per_seed(condition) for condition in loss_conditions
        },
        "master_seeds": list(PHASE_G_MASTER_SEEDS),
        "replicates_per_seed": PHASE_G_REPLICATES_PER_SEED,
        "minimum_baseline_eligible_per_seed": PHASE_G_MIN_BASELINE_ELIGIBLE_PER_SEED,
        "prepared_source_count": len(PHASE_G_MASTER_SEEDS) * PHASE_G_REPLICATES_PER_SEED,
        "trajectory_count": len(PHASE_G_CONDITIONS) * len(PHASE_G_MASTER_SEEDS) * PHASE_G_REPLICATES_PER_SEED,
        "paired_across_partner_architectures": True,
        "output_scope": "source_projection_baseline_and_trait_loss_only",
        "blinding_scope": "source_and_trait_loss_only",
        "interpretation_boundary": (
            "Phase G is a reduced-form partner-contribution and functional-redundancy closure. "
            "It does not model partner population dynamics, connectance, network dimensionality, "
            "adaptive rewiring, pollen movement, or pollinator movement."
        ),
        "opening_rule": (
            "Interpret architecture contrasts only if the fresh intact control has sufficient high-rep "
            "support and is classified R4_highrep; otherwise record failure to reproduce the anchor "
            "without changing seeds, weights, or thresholds."
        ),
        "stop_rule": (
            "Classify these predeclared architectures once. Do not tune partner weights, removal identity, "
            "or support multipliers to create an R4 boundary."
        ),
    }
