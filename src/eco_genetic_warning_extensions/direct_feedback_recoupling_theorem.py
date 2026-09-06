from __future__ import annotations

from math import exp


def sigmoid(x: float) -> float:
    if x >= 0.0:
        z = exp(-x)
        return 1.0 / (1.0 + z)
    z = exp(x)
    return z / (1.0 + z)


def eco_genetic_bundle(
    trait_mass: float,
    allele_frequency: float,
    beta_trait: float = 0.3,
    gamma_allele: float = 0.1,
) -> float:
    total = beta_trait + gamma_allele
    if total <= 0.0:
        raise ValueError("eco-genetic weights must have positive sum")
    return (beta_trait * trait_mass + gamma_allele * allele_frequency) / total


def full_support(
    q: float,
    trait_mass: float,
    allele_frequency: float,
    alpha_q: float = 0.6,
    beta_trait: float = 0.3,
    gamma_allele: float = 0.1,
) -> float:
    return alpha_q * q + beta_trait * trait_mass + gamma_allele * allele_frequency


def support_contraction_factor(
    alpha_q: float = 0.6,
    beta_trait: float = 0.3,
    gamma_allele: float = 0.1,
) -> float:
    if abs(alpha_q + beta_trait + gamma_allele - 1.0) > 1e-12:
        raise ValueError("recoupling contraction requires weights summing to one")
    return alpha_q


def support_minus_bundle(
    q: float,
    trait_mass: float,
    allele_frequency: float,
    alpha_q: float = 0.6,
    beta_trait: float = 0.3,
    gamma_allele: float = 0.1,
) -> float:
    bundle = eco_genetic_bundle(trait_mass, allele_frequency, beta_trait, gamma_allele)
    return full_support(q, trait_mass, allele_frequency, alpha_q, beta_trait, gamma_allele) - bundle


def support_minus_q(
    q: float,
    trait_mass: float,
    allele_frequency: float,
    alpha_q: float = 0.6,
    beta_trait: float = 0.3,
    gamma_allele: float = 0.1,
) -> float:
    return full_support(q, trait_mass, allele_frequency, alpha_q, beta_trait, gamma_allele) - q


def next_q(
    support: float,
    density: float,
    barrier: float,
    kappa: float = 4.5,
    area_ratio: float = 1.0,
) -> float:
    return sigmoid(kappa * (area_ratio * density * support - barrier))


def direct_feedback_logit_shift(
    q: float,
    trait_mass: float,
    allele_frequency: float,
    density: float,
    kappa: float = 4.5,
    area_ratio: float = 1.0,
    alpha_q: float = 0.6,
    beta_trait: float = 0.3,
    gamma_allele: float = 0.1,
) -> float:
    signal_delta = support_minus_q(
        q,
        trait_mass,
        allele_frequency,
        alpha_q,
        beta_trait,
        gamma_allele,
    )
    return kappa * area_ratio * density * signal_delta


def transition_displacement_bound(
    q: float,
    trait_mass: float,
    allele_frequency: float,
    density: float,
    kappa: float = 4.5,
    area_ratio: float = 1.0,
    alpha_q: float = 0.6,
    beta_trait: float = 0.3,
    gamma_allele: float = 0.1,
) -> float:
    # The logistic derivative is <= 1/4 everywhere.
    return 0.25 * abs(
        direct_feedback_logit_shift(
            q,
            trait_mass,
            allele_frequency,
            density,
            kappa,
            area_ratio,
            alpha_q,
            beta_trait,
            gamma_allele,
        )
    )


def certificate() -> dict[str, float | str]:
    return {
        "alpha_q": 0.6,
        "beta_trait": 0.3,
        "gamma_allele": 0.1,
        "bundle_trait_weight": 0.75,
        "bundle_allele_weight": 0.25,
        "support_mismatch_contraction_factor": 0.6,
        "support_mismatch_reduction_fraction": 0.4,
        "locked_logit_shift_coefficient_at_density_one": 1.8,
        "locked_transition_displacement_bound_coefficient_at_density_one": 0.45,
        "interpretation": "support-stage recoupling toward the normalized trait/allele bundle",
    }
