"""Prospective high-precision Phase T dynamic partner-architecture test.

Phase T asks whether temporal partner availability changes functional-loss
incidence or between-block heterogeneity when *expected* interaction support is
held at 0.75.  It deliberately does not introduce adaptive rewiring yet.

The constant-support comparator is the exact Phase-N even-partner-loss closure.
Two explicit four-partner architectures share the same independent availability
draws each generation and the same expected support, but differ in contribution
concentration and therefore support variance.
"""
from __future__ import annotations

from dataclasses import dataclass

from .partner_redundancy_phase_g import (
    PHASE_G_AREA_REFERENCE,
    PHASE_G_BARRIER_INCREASE,
    PHASE_G_HOLD_GENERATIONS,
    PHASE_G_INTERACTION_KAPPA,
    PHASE_G_KAPPA_MU,
    PHASE_G_MASTER_SEEDS,
    PHASE_G_MIGRATION_RATE,
    PHASE_G_P_STAR,
    PHASE_G_RAMP_GENERATIONS,
)

PHASE_T_REPLICATES_PER_SEED = 100
PHASE_T_MIN_BASELINE_ELIGIBLE_PER_SEED = 70
PHASE_T_PARTNER_COUNT = 4
PHASE_T_PARTNER_AVAILABILITY = 0.75
PHASE_T_CONSTANT_SUPPORT = 0.75
PHASE_T_NETWORK_SEED_OFFSET = 2_410_731

PHASE_T_EVEN_WEIGHTS = (0.25, 0.25, 0.25, 0.25)
PHASE_T_DOMINANT_WEIGHTS = (0.70, 0.10, 0.10, 0.10)

# Exact Phase-N high-precision even-redundant blocks: (losses, eligible),
# ordered by PHASE_G_MASTER_SEEDS.  The constant-support comparator must replay
# these counts exactly before dynamic-network results are interpreted.
PHASE_T_PHASE_N_CONSTANT_BLOCKS = (
    (51, 86),
    (45, 90),
    (45, 86),
    (46, 91),
    (53, 88),
)

# Original first-20 Phase-G even-loss prefixes: (eligible, losses).
PHASE_T_PHASE_G_PREFIX_COUNTS = {
    20290610: (18, 10),
    20290611: (17, 8),
    20290612: (18, 8),
    20290613: (20, 13),
    20290614: (17, 12),
}


@dataclass(frozen=True)
class PartnerArchitecture:
    name: str
    weights: tuple[float, ...]

    def __post_init__(self) -> None:
        if len(self.weights) != PHASE_T_PARTNER_COUNT:
            raise ValueError("Phase T requires exactly four partner weights")
        if any(weight < 0.0 for weight in self.weights):
            raise ValueError("partner weights must be nonnegative")
        if abs(sum(self.weights) - 1.0) > 1e-12:
            raise ValueError("partner weights must sum to one")

    @property
    def expected_support(self) -> float:
        return PHASE_T_PARTNER_AVAILABILITY * sum(self.weights)

    @property
    def support_variance(self) -> float:
        p = PHASE_T_PARTNER_AVAILABILITY
        return p * (1.0 - p) * sum(weight * weight for weight in self.weights)

    @property
    def contribution_cv(self) -> float:
        mean = 1.0 / PHASE_T_PARTNER_COUNT
        variance = sum((weight - mean) ** 2 for weight in self.weights) / PHASE_T_PARTNER_COUNT
        return variance ** 0.5 / mean


PHASE_T_ARCHITECTURES = (
    PartnerArchitecture("even_dynamic", PHASE_T_EVEN_WEIGHTS),
    PartnerArchitecture("dominant_dynamic", PHASE_T_DOMINANT_WEIGHTS),
)

PHASE_T_CONDITIONS = (
    "constant_support_075",
    "even_dynamic",
    "dominant_dynamic",
)


def support_from_availability(weights: tuple[float, ...], availability: tuple[bool, ...]) -> float:
    if len(weights) != PHASE_T_PARTNER_COUNT or len(availability) != PHASE_T_PARTNER_COUNT:
        raise ValueError("weights and availability must both contain four partners")
    return sum(weight for weight, active in zip(weights, availability) if active)


def phase_t_manifest() -> dict[str, object]:
    return {
        "protocol": "warning-blind dynamic partner architecture Phase T",
        "scientific_scope": "matched_expected_support_temporal_partner_availability",
        "master_seeds": list(PHASE_G_MASTER_SEEDS),
        "replicates_per_seed": PHASE_T_REPLICATES_PER_SEED,
        "minimum_baseline_eligible_per_seed": PHASE_T_MIN_BASELINE_ELIGIBLE_PER_SEED,
        "coordinate": {"kappa_mu": PHASE_G_KAPPA_MU, "p_star": PHASE_G_P_STAR},
        "fixed_conditions": {
            "area_reference": PHASE_G_AREA_REFERENCE,
            "interaction_kappa": PHASE_G_INTERACTION_KAPPA,
            "migration_rate": PHASE_G_MIGRATION_RATE,
            "ramp_generations": PHASE_G_RAMP_GENERATIONS,
            "hold_generations": PHASE_G_HOLD_GENERATIONS,
            "horizon": PHASE_G_RAMP_GENERATIONS + PHASE_G_HOLD_GENERATIONS,
            "normalised_barrier_increase": PHASE_G_BARRIER_INCREASE,
        },
        "conditions": list(PHASE_T_CONDITIONS),
        "constant_comparator": {
            "support_multiplier": PHASE_T_CONSTANT_SUPPORT,
            "provenance": "exact Phase-N even_redundant closure",
        },
        "dynamic_network": {
            "focal_node_count": 1,
            "partner_count": PHASE_T_PARTNER_COUNT,
            "availability_probability_per_partner_per_generation": PHASE_T_PARTNER_AVAILABILITY,
            "availability_draws": "independent across partners and generations; paired/common across even and dominant architectures",
            "network_rng": "separate from parent life-cycle RNG",
            "support_mapping": "sum(partner_weight * availability_indicator)",
            "architectures": [
                {
                    "name": architecture.name,
                    "weights": list(architecture.weights),
                    "expected_support": architecture.expected_support,
                    "support_variance": architecture.support_variance,
                    "contribution_cv": architecture.contribution_cv,
                }
                for architecture in PHASE_T_ARCHITECTURES
            ],
        },
        "matched_quantity": "expected support = 0.75 for constant, even_dynamic, and dominant_dynamic",
        "not_matched": "realised per-generation support variance; this is the intended mechanism",
        "opening_rule": (
            "The constant_support_075 condition must exactly reproduce the original first-20 Phase-G even-loss prefixes and all five locked 100-attempt Phase-N even-redundant block counts. "
            "Dynamic conditions must have paired baseline eligibility identical to the constant comparator."
        ),
        "primary_questions": [
            "Does even dynamic partner availability alter pooled loss or between-block heterogeneity relative to constant support with the same expectation?",
            "Does contribution concentration (dominant versus even) alter pooled loss or between-block heterogeneity under exactly the same availability draws?",
        ],
        "secondary_outputs": [
            "paired McNemar status switches",
            "realised support mean and variance",
            "zero-support generation frequency",
        ],
        "blinding_scope": "source, network support trajectory, and functional loss only; no warning/diversity fields",
        "rewiring": "not included; only opened in a new prospective phase if Phase T establishes a dynamic-network effect worth mechanistically decomposing",
        "interpretation_boundary": (
            "Phase T is an explicit one-focal-node/four-partner temporal availability closure. Partner availability is stochastic but has no abundance dynamics, coextinction, spatial partner movement, adaptive rewiring, or multispecies feedback. "
            "Expected support is matched, not realised support at every generation."
        ),
        "stop_rule": (
            "Run only the three declared conditions once at 100 attempts per locked Phase-G seed. Do not change availability probability, partner weights, correlation structure, seeds, or precision after outcomes to create a network effect."
        ),
    }
