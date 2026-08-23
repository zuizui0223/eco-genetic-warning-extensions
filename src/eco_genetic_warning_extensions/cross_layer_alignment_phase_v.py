"""Prospective Phase V: test whether coarse functional-fragmentation marginals are state-sufficient.

The experiment holds fixed the marginal distributions of interaction support,
allele frequency, realised high-trait mass, census abundance, habitat area and
standard genetic-diversity summaries.  It changes only the cross-patch alignment
between the ecological interaction layer and the paired genetic/trait-support
bundle.

This is a warning-blind C2 state-sufficiency test.  It is not an urban-versus-
island simulation and it does not inspect warning times or diversity decline.
"""
from __future__ import annotations

from math import exp

PHASE_V_MASTER_SEEDS = (20300110, 20300111, 20300112, 20300113, 20300114)
PHASE_V_REPLICATES_PER_SEED = 100
PHASE_V_PATCH_COUNT = 4
PHASE_V_PATCH_AREAS = (1.0, 1.0, 1.0, 1.0)
PHASE_V_POPULATION = (40, 40, 40, 40)
PHASE_V_Q_VALUES = (0.65, 0.75, 0.85, 0.95)
PHASE_V_BUNDLE_VALUES = (0.20, 0.40, 0.60, 0.80)
PHASE_V_TRAIT_GRID_SIZE = 31
PHASE_V_GENERATIONS = 60
PHASE_V_BARRIER_START = 0.50
PHASE_V_BARRIER_END = 0.65
PHASE_V_AREA_REFERENCE = 1.0
PHASE_V_INTERACTION_FEEDBACK = 4.5
PHASE_V_DENSITY_CAPACITY = 40.0
PHASE_V_Q_FEEDBACK = (0.6, 0.3, 0.1)  # q, realised high-trait mass, high-allele frequency
PHASE_V_CONDITIONS = ("aligned", "anti_aligned")
PHASE_V_ALPHA = 0.05
PHASE_V_SIGNATURE_TOLERANCE = 1e-15


def condition_bundle_values(condition: str) -> tuple[float, ...]:
    if condition == "aligned":
        return PHASE_V_BUNDLE_VALUES
    if condition == "anti_aligned":
        return tuple(reversed(PHASE_V_BUNDLE_VALUES))
    raise ValueError(f"unknown Phase-V condition: {condition}")


def trait_abundance_rows(condition: str) -> tuple[tuple[int, ...], ...]:
    """Return 31-bin rows whose realised high-trait masses equal the bundle values.

    Each patch has exactly 40 individuals.  Mass is placed only in the first
    (declared low) and last (declared high) trait bins, so the requested high
    masses are exact integer fractions and the global trait-bin totals are
    identical under the two patch permutations.
    """
    rows = []
    for fraction in condition_bundle_values(condition):
        high = int(round(40 * fraction))
        low = 40 - high
        row = [0] * PHASE_V_TRAIT_GRID_SIZE
        row[0] = low
        row[-1] = high
        rows.append(tuple(row))
    return tuple(rows)


def barrier_schedule() -> tuple[float, ...]:
    span = PHASE_V_BARRIER_END - PHASE_V_BARRIER_START
    return tuple(
        PHASE_V_BARRIER_START + span * generation / PHASE_V_GENERATIONS
        for generation in range(1, PHASE_V_GENERATIONS + 1)
    )


def _heterozygosity(p: float) -> float:
    return 2.0 * p * (1.0 - p)


def baseline_signature(condition: str) -> dict[str, object]:
    p = condition_bundle_values(condition)
    high_mass = condition_bundle_values(condition)
    q = PHASE_V_Q_VALUES
    p_bar = sum(p) / len(p)
    h_alpha = sum(_heterozygosity(value) for value in p) / len(p)
    h_gamma = _heterozygosity(p_bar)
    fst = 1.0 - h_alpha / h_gamma
    rows = trait_abundance_rows(condition)
    bin_totals = tuple(sum(row[index] for row in rows) for index in range(PHASE_V_TRAIT_GRID_SIZE))
    return {
        "patch_areas_sorted": tuple(sorted(PHASE_V_PATCH_AREAS)),
        "population_sorted": tuple(sorted(PHASE_V_POPULATION)),
        "q_sorted": tuple(sorted(q)),
        "p_sorted": tuple(sorted(p)),
        "high_trait_mass_sorted": tuple(sorted(high_mass)),
        "trait_bin_totals": bin_totals,
        "total_population": sum(PHASE_V_POPULATION),
        "mean_q": sum(q) / len(q),
        "mean_p": p_bar,
        "mean_high_trait_mass": sum(high_mass) / len(high_mass),
        "h_alpha": h_alpha,
        "h_gamma": h_gamma,
        "fst": fst,
    }


def signatures_match() -> bool:
    """Validate mathematical marginal equality without bitwise float dependence."""
    left = baseline_signature("aligned")
    right = baseline_signature("anti_aligned")
    exact_keys = (
        "patch_areas_sorted",
        "population_sorted",
        "q_sorted",
        "p_sorted",
        "high_trait_mass_sorted",
        "trait_bin_totals",
        "total_population",
    )
    if any(left[key] != right[key] for key in exact_keys):
        return False
    float_keys = ("mean_q", "mean_p", "mean_high_trait_mass", "h_alpha", "h_gamma", "fst")
    return all(
        abs(float(left[key]) - float(right[key])) <= PHASE_V_SIGNATURE_TOLERANCE
        for key in float_keys
    )


def cross_layer_covariance(condition: str) -> float:
    q = PHASE_V_Q_VALUES
    bundle = condition_bundle_values(condition)
    q_bar = sum(q) / len(q)
    b_bar = sum(bundle) / len(bundle)
    return sum((left - q_bar) * (right - b_bar) for left, right in zip(q, bundle)) / len(q)


def support_signal_vector(condition: str) -> tuple[float, ...]:
    alpha, beta_trait, gamma = PHASE_V_Q_FEEDBACK
    bundle = condition_bundle_values(condition)
    return tuple(
        alpha * q + beta_trait * high_mass + gamma * p
        for q, high_mass, p in zip(PHASE_V_Q_VALUES, bundle, bundle)
    )


def _sigmoid(value: float) -> float:
    if value >= 0:
        return 1.0 / (1.0 + exp(-value))
    inverse = exp(value)
    return inverse / (1.0 + inverse)


def one_step_interaction_vector(condition: str) -> tuple[float, ...]:
    """Exact generation-1 q update at carrying density for the declared state."""
    first_barrier = barrier_schedule()[0]
    return tuple(
        _sigmoid(PHASE_V_INTERACTION_FEEDBACK * (signal - first_barrier))
        for signal in support_signal_vector(condition)
    )


def one_step_state_sufficiency_certificate() -> dict[str, object]:
    aligned = one_step_interaction_vector("aligned")
    anti = one_step_interaction_vector("anti_aligned")
    maximum_difference = max(abs(left - right) for left, right in zip(aligned, anti))
    return {
        "coarse_marginal_signatures_identical": signatures_match(),
        "aligned_cross_layer_covariance": cross_layer_covariance("aligned"),
        "anti_aligned_cross_layer_covariance": cross_layer_covariance("anti_aligned"),
        "aligned_support_signal": support_signal_vector("aligned"),
        "anti_aligned_support_signal": support_signal_vector("anti_aligned"),
        "aligned_generation1_interaction": aligned,
        "anti_aligned_generation1_interaction": anti,
        "maximum_patchwise_generation1_difference": maximum_difference,
        "coarse_marginals_are_transition_sufficient": maximum_difference <= 1e-12,
    }


def phase_v_manifest() -> dict[str, object]:
    return {
        "protocol": "warning-blind cross-layer alignment state-sufficiency Phase V",
        "scientific_scope": "operational_functional_fragmentation_regime_definition",
        "master_seeds": list(PHASE_V_MASTER_SEEDS),
        "replicates_per_seed": PHASE_V_REPLICATES_PER_SEED,
        "conditions": list(PHASE_V_CONDITIONS),
        "fixed_state": {
            "patch_areas": list(PHASE_V_PATCH_AREAS),
            "population": list(PHASE_V_POPULATION),
            "interaction_multiset": list(PHASE_V_Q_VALUES),
            "allele_frequency_multiset": list(PHASE_V_BUNDLE_VALUES),
            "realised_high_trait_mass_multiset": list(PHASE_V_BUNDLE_VALUES),
            "trait_grid_size": PHASE_V_TRAIT_GRID_SIZE,
        },
        "fixed_dynamics": {
            "area_reference": PHASE_V_AREA_REFERENCE,
            "interaction_feedback": PHASE_V_INTERACTION_FEEDBACK,
            "density_capacity": PHASE_V_DENSITY_CAPACITY,
            "q_feedback_weights": list(PHASE_V_Q_FEEDBACK),
            "trait_occupancy_mode": "finite_trait_bin_recruitment",
            "genotype_trait_recruitment": "two_kernel_recruitment",
            "inheritance_weight": 0.5,
            "migration_rate": 0.0,
            "symmetric_allele_mutation_rate": 0.0,
            "generations": PHASE_V_GENERATIONS,
            "barrier_schedule": [PHASE_V_BARRIER_START, PHASE_V_BARRIER_END],
            "barrier_schedule_rule": "linear over 60 generations; endpoints are existing standard-profile grid values",
        },
        "opening_rule": (
            "Aligned and anti-aligned states must have mathematically identical marginal signatures for habitat area, census, interaction, allele frequency, realised high-trait mass, trait-bin totals, H_alpha, H_gamma and FST. "
            "Discrete/multiset quantities are compared exactly and derived floating summaries within 1e-15. They must differ only in cross-patch alignment, with positive versus negative q-by-eco-genetic-bundle covariance."
        ),
        "primary_question": (
            "Can states with identical measured coarse marginals but different cross-layer alignment generate different downstream realised functional-loss incidence under identical future forcing?"
        ),
        "mechanistic_certificate": (
            "Before stochastic interpretation, test whether the exact generation-1 interaction transition differs despite identical coarse marginal signatures."
        ),
        "primary_inference": "paired exact McNemar test on post-baseline realised functional-loss occurrence",
        "alpha": PHASE_V_ALPHA,
        "warning_blind": True,
        "urban_island_scope": (
            "This is not a city-versus-island simulation. It tests a necessary condition for the prospective convergence hypothesis: whether a mechanism-agnostic operational regime can be defined from layer-wise marginals alone."
        ),
        "stop_rule": (
            "Run only the declared aligned and anti-aligned states, five predeclared unused master seeds and 100 replicates per seed. Do not change state values, barrier schedule, alpha, seeds, horizon or add intermediate permutations after seeing outcomes. A null multi-generation incidence contrast is retained if observed."
        ),
    }
