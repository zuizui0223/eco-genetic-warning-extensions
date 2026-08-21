"""Prospective warning-blind pollen-movement Phase I manifest and operators.

Phase I separates pollen-mediated gene flow from the simulator's legacy
allele-frequency mixing.  Under the declared diploid random-mating closure, a
fraction g of paternal contribution from a census-weighted regional pollen pool
produces the exact allele update of legacy global mixing with m=g/2.  A second
pollen kernel restricts the paternal pool to ring-neighbour patches while holding
g fixed.

The purpose is to distinguish biological movement process and spatial kernel,
not to relabel legacy ``migration_rate`` as pollen dispersal.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import isclose
from typing import Sequence

from .mutation_coordinates import MutationCoordinates

PHASE_I_MASTER_SEEDS = (20290810, 20290811, 20290812, 20290813, 20290814)
PHASE_I_REPLICATES_PER_SEED = 20
PHASE_I_MIN_BASELINE_ELIGIBLE_PER_SEED = 10
PHASE_I_RAMP_GENERATIONS = 30
PHASE_I_HOLD_GENERATIONS = 90
PHASE_I_AREA_REFERENCE = 1.0
PHASE_I_INTERACTION_KAPPA = 4.5
PHASE_I_KAPPA_MU = 0.35
PHASE_I_P_STAR = 0.35
PHASE_I_BARRIER_INCREASE = 0.30
PHASE_I_POLLEN_POOL_FRACTION = 0.20
PHASE_I_EQUIVALENT_GLOBAL_MIGRATION_RATE = PHASE_I_POLLEN_POOL_FRACTION / 2.0


@dataclass(frozen=True)
class PollenMovementCondition:
    name: str
    operator: str
    pollen_pool_fraction: float
    legacy_migration_rate: float

    def __post_init__(self) -> None:
        if self.operator not in {"none", "regional_pollen", "ring_pollen", "legacy_global_mixing"}:
            raise ValueError("unknown Phase-I movement operator")
        if not 0.0 <= self.pollen_pool_fraction <= 1.0:
            raise ValueError("pollen_pool_fraction must lie in [0, 1]")
        if not 0.0 <= self.legacy_migration_rate <= 1.0:
            raise ValueError("legacy_migration_rate must lie in [0, 1]")
        if self.operator == "legacy_global_mixing" and self.pollen_pool_fraction != 0.0:
            raise ValueError("legacy mixing comparator must not also apply pollen movement")
        if self.operator != "legacy_global_mixing" and self.legacy_migration_rate != 0.0:
            raise ValueError("pollen conditions must keep legacy migration_rate at zero")

    def identity(self) -> dict[str, object]:
        return {
            "name": self.name,
            "operator": self.operator,
            "pollen_pool_fraction": self.pollen_pool_fraction,
            "legacy_migration_rate": self.legacy_migration_rate,
        }


PHASE_I_CONDITIONS = (
    PollenMovementCondition("no_pollen_control", "none", 0.0, 0.0),
    PollenMovementCondition("regional_pollen_pool_g020", "regional_pollen", PHASE_I_POLLEN_POOL_FRACTION, 0.0),
    PollenMovementCondition(
        "legacy_allele_mixing_m010",
        "legacy_global_mixing",
        0.0,
        PHASE_I_EQUIVALENT_GLOBAL_MIGRATION_RATE,
    ),
    PollenMovementCondition("ring_pollen_pool_g020", "ring_pollen", PHASE_I_POLLEN_POOL_FRACTION, 0.0),
)


def phase_i_coordinate() -> MutationCoordinates:
    return MutationCoordinates(kappa_mu=PHASE_I_KAPPA_MU, p_star=PHASE_I_P_STAR)


def phase_i_conditions() -> tuple[PollenMovementCondition, ...]:
    return PHASE_I_CONDITIONS


def equivalent_global_migration_rate(pollen_pool_fraction: float) -> float:
    g = float(pollen_pool_fraction)
    if not 0.0 <= g <= 1.0:
        raise ValueError("pollen_pool_fraction must lie in [0, 1]")
    return g / 2.0


def offspring_allele_frequency(
    local_selected_frequency: float,
    paternal_pool_frequency: float,
    pollen_pool_fraction: float,
) -> float:
    """Diploid offspring frequency with local maternal and mixed paternal genes.

    Maternal contribution is local selected frequency. Paternal contribution is
    ``(1-g)*local + g*pool``. Averaging maternal and paternal gene copies gives

        p_off = (1-g/2) p_local + (g/2) p_pool.
    """
    p = float(local_selected_frequency)
    pool = float(paternal_pool_frequency)
    g = float(pollen_pool_fraction)
    if not 0.0 <= p <= 1.0 or not 0.0 <= pool <= 1.0:
        raise ValueError("allele frequencies must lie in [0, 1]")
    if not 0.0 <= g <= 1.0:
        raise ValueError("pollen_pool_fraction must lie in [0, 1]")
    return (1.0 - g / 2.0) * p + (g / 2.0) * pool


def census_weighted_regional_pool(
    selected_frequencies: Sequence[float],
    census_weights: Sequence[float],
) -> tuple[float, ...]:
    frequencies = tuple(float(value) for value in selected_frequencies)
    weights = tuple(float(value) for value in census_weights)
    if not frequencies or len(frequencies) != len(weights):
        raise ValueError("frequencies and census weights must be nonempty and aligned")
    if any(value < 0.0 or value > 1.0 for value in frequencies):
        raise ValueError("selected frequencies must lie in [0, 1]")
    if any(weight <= 0.0 for weight in weights):
        raise ValueError("census weights must be positive")
    mean = sum(weight * p for weight, p in zip(weights, frequencies)) / sum(weights)
    return tuple(mean for _ in frequencies)


def census_weighted_ring_pool(
    selected_frequencies: Sequence[float],
    census_weights: Sequence[float],
) -> tuple[float, ...]:
    """Return a two-neighbour circular pollen pool for each focal patch."""
    frequencies = tuple(float(value) for value in selected_frequencies)
    weights = tuple(float(value) for value in census_weights)
    n = len(frequencies)
    if n < 3 or n != len(weights):
        raise ValueError("ring pollen pool requires at least three aligned patches")
    if any(value < 0.0 or value > 1.0 for value in frequencies):
        raise ValueError("selected frequencies must lie in [0, 1]")
    if any(weight <= 0.0 for weight in weights):
        raise ValueError("census weights must be positive")
    pools = []
    for focal in range(n):
        donors = ((focal - 1) % n, (focal + 1) % n)
        denominator = sum(weights[index] for index in donors)
        pools.append(sum(weights[index] * frequencies[index] for index in donors) / denominator)
    return tuple(pools)


def pollen_offspring_frequencies(
    selected_frequencies: Sequence[float],
    census_weights: Sequence[float],
    *,
    pollen_pool_fraction: float,
    kernel: str,
) -> tuple[float, ...]:
    selected = tuple(float(value) for value in selected_frequencies)
    if kernel == "regional":
        pools = census_weighted_regional_pool(selected, census_weights)
    elif kernel == "ring":
        pools = census_weighted_ring_pool(selected, census_weights)
    elif kernel == "none":
        pools = selected
    else:
        raise ValueError("unknown pollen kernel")
    return tuple(
        offspring_allele_frequency(local, pool, pollen_pool_fraction)
        for local, pool in zip(selected, pools)
    )


def global_pollen_equals_legacy_mixing(
    selected_frequencies: Sequence[float],
    census_weights: Sequence[float],
    pollen_pool_fraction: float,
) -> bool:
    selected = tuple(float(value) for value in selected_frequencies)
    regional = pollen_offspring_frequencies(
        selected,
        census_weights,
        pollen_pool_fraction=pollen_pool_fraction,
        kernel="regional",
    )
    mean = census_weighted_regional_pool(selected, census_weights)[0]
    m = equivalent_global_migration_rate(pollen_pool_fraction)
    legacy = tuple((1.0 - m) * p + m * mean for p in selected)
    return all(isclose(a, b, rel_tol=0.0, abs_tol=1e-15) for a, b in zip(regional, legacy))


def phase_i_manifest() -> dict[str, object]:
    return {
        "protocol": "warning-blind pollen-movement Phase I",
        "scientific_scope": "process_resolved_pollen_gene_flow_and_spatial_kernel",
        "calibration_scope": "source_and_trait_loss_only",
        "coordinate": {"kappa_mu": PHASE_I_KAPPA_MU, "p_star": PHASE_I_P_STAR},
        "fixed_conditions": {
            "area_reference": PHASE_I_AREA_REFERENCE,
            "interaction_kappa": PHASE_I_INTERACTION_KAPPA,
            "ramp_generations": PHASE_I_RAMP_GENERATIONS,
            "hold_generations": PHASE_I_HOLD_GENERATIONS,
            "horizon": PHASE_I_RAMP_GENERATIONS + PHASE_I_HOLD_GENERATIONS,
            "normalised_barrier_increase": PHASE_I_BARRIER_INCREASE,
            "fragmentation_geometry": "four_equal_patches_fixed_total_area",
        },
        "pollen_pool_fraction": PHASE_I_POLLEN_POOL_FRACTION,
        "exact_global_equivalence": {
            "identity": "p_off=(1-g/2)p_local+(g/2)p_regional",
            "legacy_migration_rate": PHASE_I_EQUIVALENT_GLOBAL_MIGRATION_RATE,
            "scope": "census-weighted regional pollen pool under the declared diploid random-mating closure",
        },
        "ring_kernel": "two circular nearest-neighbour donor patches, census-weighted within neighbour set",
        "conditions": [condition.identity() for condition in PHASE_I_CONDITIONS],
        "master_seeds": list(PHASE_I_MASTER_SEEDS),
        "replicates_per_seed": PHASE_I_REPLICATES_PER_SEED,
        "minimum_baseline_eligible_per_seed": PHASE_I_MIN_BASELINE_ELIGIBLE_PER_SEED,
        "prepared_source_count": len(PHASE_I_MASTER_SEEDS) * PHASE_I_REPLICATES_PER_SEED,
        "trajectory_count": len(PHASE_I_CONDITIONS) * len(PHASE_I_MASTER_SEEDS) * PHASE_I_REPLICATES_PER_SEED,
        "paired_across_movement_conditions": True,
        "output_scope": "source_projection_pollen_operator_diagnostics_and_trait_loss_only",
        "blinding_scope": "source_movement_and_trait_loss_only",
        "opening_rule": (
            "Interpret the pollen-kernel comparison only if the fresh no-pollen control is R4_highrep and the "
            "regional-pollen implementation is trajectory-exact with legacy m=g/2 global allele mixing for every "
            "completed paired trajectory. Otherwise record the failed opening without changing g, kernel, seeds, or thresholds."
        ),
        "comparison_rule": (
            "If opening succeeds, compare regional versus ring pollen at the same g=0.20 once. Record whether the "
            "predeclared loss-regime classification changes; do not tune g or the kernel to obtain a difference."
        ),
        "stop_rule": (
            "Do not tune pollen_pool_fraction, regional or ring kernels, patch ordering, seeds, deterioration, or R4 "
            "thresholds after observing the Phase-I result."
        ),
        "interpretation_boundary": (
            "Phase I models pollen-mediated paternal gene contribution only. It does not move census individuals, "
            "seeds/propagules, realised trait bins, or interaction partners and does not make legacy migration_rate "
            "a general pollen-dispersal parameter."
        ),
    }
