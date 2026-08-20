"""Predeclared warning-blind migration-condition Phase E manifest."""
from __future__ import annotations

from dataclasses import dataclass

from .mutation_coordinates import MutationCoordinates

PHASE_E_MIGRATION_RATES = (0.0, 0.025, 0.05, 0.10, 0.20)
PHASE_E_MASTER_SEEDS = (20290410, 20290411, 20290412, 20290413, 20290414)
PHASE_E_REPLICATES_PER_SEED = 20
PHASE_E_MIN_BASELINE_ELIGIBLE_PER_SEED = 10
PHASE_E_RAMP_GENERATIONS = 30
PHASE_E_HOLD_GENERATIONS = 90
PHASE_E_AREA_REFERENCE = 1.0
PHASE_E_INTERACTION_KAPPA = 4.5
PHASE_E_KAPPA_MU = 0.35
PHASE_E_P_STAR = 0.35
PHASE_E_BARRIER_INCREASE = 0.30


@dataclass(frozen=True)
class MigrationCondition:
    migration_rate: float

    def __post_init__(self) -> None:
        if not 0.0 <= float(self.migration_rate) <= 1.0:
            raise ValueError("migration_rate must lie in [0, 1]")

    def identity(self) -> dict[str, float]:
        return {"migration_rate": float(self.migration_rate)}


def phase_e_coordinate() -> MutationCoordinates:
    return MutationCoordinates(kappa_mu=PHASE_E_KAPPA_MU, p_star=PHASE_E_P_STAR)


def phase_e_conditions() -> tuple[MigrationCondition, ...]:
    return tuple(MigrationCondition(rate) for rate in PHASE_E_MIGRATION_RATES)


def deviation_contraction_factor(migration_rate: float) -> float:
    """Return exact contraction of p_i-p_bar under p_i'=(1-m)p_i+m*p_bar."""
    condition = MigrationCondition(migration_rate)
    return 1.0 - condition.migration_rate


def variance_contraction_factor(migration_rate: float) -> float:
    """Return exact contraction factor for weighted among-patch frequency variance."""
    factor = deviation_contraction_factor(migration_rate)
    return factor * factor


def phase_e_manifest() -> dict[str, object]:
    conditions = phase_e_conditions()
    return {
        "protocol": "warning-blind migration-condition Phase E",
        "scientific_scope": "allele_frequency_mixing_condition_map",
        "calibration_scope": "trait_loss_only",
        "coordinate": {"kappa_mu": PHASE_E_KAPPA_MU, "p_star": PHASE_E_P_STAR},
        "ecological_anchor": {
            "area_reference": PHASE_E_AREA_REFERENCE,
            "interaction_kappa": PHASE_E_INTERACTION_KAPPA,
            "ramp_generations": PHASE_E_RAMP_GENERATIONS,
            "hold_generations": PHASE_E_HOLD_GENERATIONS,
            "horizon": PHASE_E_RAMP_GENERATIONS + PHASE_E_HOLD_GENERATIONS,
            "normalised_barrier_increase": PHASE_E_BARRIER_INCREASE,
            "fragmentation_geometry": "four_equal_patches_fixed_total_area",
        },
        "migration_rates": [condition.migration_rate for condition in conditions],
        "master_seeds": list(PHASE_E_MASTER_SEEDS),
        "replicates_per_seed": PHASE_E_REPLICATES_PER_SEED,
        "minimum_baseline_eligible_per_seed": PHASE_E_MIN_BASELINE_ELIGIBLE_PER_SEED,
        "prepared_source_count": len(PHASE_E_MASTER_SEEDS) * PHASE_E_REPLICATES_PER_SEED,
        "trajectory_count": len(conditions) * len(PHASE_E_MASTER_SEEDS) * PHASE_E_REPLICATES_PER_SEED,
        "paired_across_migration_rates": True,
        "warning_or_diversity_fields_permitted": False,
        "migration_scope_boundary": (
            "migration_rate mixes allele frequencies toward the population-weighted mean; "
            "it is not demographic, pollinator, seed, recolonisation, or trait-bin dispersal"
        ),
    }
