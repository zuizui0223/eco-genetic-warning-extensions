from __future__ import annotations

from math import exp, log


DEFAULT_KAPPA = 4.5
DEFAULT_TARGET_Q = 0.625
DEFAULT_ALPHA = 0.6
DEFAULT_BETA_TRAIT = 0.3
DEFAULT_GAMMA_ALLELE = 0.1


def sigmoid(x: float) -> float:
    if x >= 0:
        z = exp(-x)
        return 1.0 / (1.0 + z)
    z = exp(x)
    return z / (1.0 + z)


def logit(p: float) -> float:
    if not 0.0 < p < 1.0:
        raise ValueError("p must lie strictly inside (0,1)")
    return log(p / (1.0 - p))


def target_headroom(
    theta: float,
    *,
    target_q: float = DEFAULT_TARGET_Q,
    kappa: float = DEFAULT_KAPPA,
) -> float:
    """Required density-weighted support for q_next to reach target_q."""
    if kappa <= 0.0:
        raise ValueError("kappa must be positive")
    return theta + logit(target_q) / kappa


def eco_genetic_bundle(
    trait_state: float,
    allele_state: float,
    *,
    beta_trait: float = DEFAULT_BETA_TRAIT,
    gamma_allele: float = DEFAULT_GAMMA_ALLELE,
) -> float:
    lam = beta_trait + gamma_allele
    if lam <= 0.0:
        raise ValueError("beta_trait + gamma_allele must be positive")
    return (beta_trait * trait_state + gamma_allele * allele_state) / lam


def support_signal(
    interaction: float,
    trait_state: float,
    allele_state: float,
    *,
    alpha: float = DEFAULT_ALPHA,
    beta_trait: float = DEFAULT_BETA_TRAIT,
    gamma_allele: float = DEFAULT_GAMMA_ALLELE,
) -> float:
    return alpha * interaction + beta_trait * trait_state + gamma_allele * allele_state


def route_margin(
    interaction: float,
    trait_state: float,
    allele_state: float,
    density: float,
    theta: float,
    *,
    area_ratio: float = 1.0,
    alpha: float = DEFAULT_ALPHA,
    beta_trait: float = DEFAULT_BETA_TRAIT,
    gamma_allele: float = DEFAULT_GAMMA_ALLELE,
    target_q: float = DEFAULT_TARGET_Q,
    kappa: float = DEFAULT_KAPPA,
) -> float:
    """Signed margin whose sign exactly determines q_next-target_q."""
    signal = support_signal(
        interaction,
        trait_state,
        allele_state,
        alpha=alpha,
        beta_trait=beta_trait,
        gamma_allele=gamma_allele,
    )
    return area_ratio * density * signal - target_headroom(theta, target_q=target_q, kappa=kappa)


def q_only_route_margin(
    interaction: float,
    density: float,
    theta: float,
    *,
    area_ratio: float = 1.0,
    target_q: float = DEFAULT_TARGET_Q,
    kappa: float = DEFAULT_KAPPA,
) -> float:
    return area_ratio * density * interaction - target_headroom(theta, target_q=target_q, kappa=kappa)


def next_interaction_from_state(
    interaction: float,
    trait_state: float,
    allele_state: float,
    density: float,
    theta: float,
    *,
    area_ratio: float = 1.0,
    alpha: float = DEFAULT_ALPHA,
    beta_trait: float = DEFAULT_BETA_TRAIT,
    gamma_allele: float = DEFAULT_GAMMA_ALLELE,
    kappa: float = DEFAULT_KAPPA,
) -> float:
    signal = support_signal(
        interaction,
        trait_state,
        allele_state,
        alpha=alpha,
        beta_trait=beta_trait,
        gamma_allele=gamma_allele,
    )
    return sigmoid(kappa * (area_ratio * density * signal - theta))


def selected_high_allele_frequency(p: float, q_next: float) -> float:
    """Pinned high-allele selection closure used by the finite model."""
    if not 0.0 <= p <= 1.0:
        raise ValueError("p must lie in [0,1]")
    w = 0.75 + 0.4 * q_next
    denominator = 1.0 - p + p * w
    return p * w / denominator


def repair_shift(
    interaction: float,
    trait_state: float,
    allele_state: float,
    density: float,
    *,
    area_ratio: float = 1.0,
    alpha: float = DEFAULT_ALPHA,
    beta_trait: float = DEFAULT_BETA_TRAIT,
    gamma_allele: float = DEFAULT_GAMMA_ALLELE,
) -> float:
    """Full-feedback route-margin shift relative to q-only when weights sum to one."""
    if abs(alpha + beta_trait + gamma_allele - 1.0) > 1e-12:
        raise ValueError("repair_shift identity requires feedback weights to sum to one")
    lam = beta_trait + gamma_allele
    bundle = eco_genetic_bundle(
        trait_state,
        allele_state,
        beta_trait=beta_trait,
        gamma_allele=gamma_allele,
    )
    return area_ratio * density * lam * (bundle - interaction)


def critical_bundle_for_target(
    interaction: float,
    density: float,
    theta: float,
    *,
    area_ratio: float = 1.0,
    alpha: float = DEFAULT_ALPHA,
    beta_trait: float = DEFAULT_BETA_TRAIT,
    gamma_allele: float = DEFAULT_GAMMA_ALLELE,
    target_q: float = DEFAULT_TARGET_Q,
    kappa: float = DEFAULT_KAPPA,
) -> float:
    """Bundle value B at which the full-feedback route margin is exactly zero."""
    if density <= 0.0 or area_ratio <= 0.0:
        raise ValueError("density and area_ratio must be positive")
    lam = beta_trait + gamma_allele
    if lam <= 0.0:
        raise ValueError("beta_trait + gamma_allele must be positive")
    required_support = target_headroom(theta, target_q=target_q, kappa=kappa) / (area_ratio * density)
    return (required_support - alpha * interaction) / lam


def classify_margin(margin: float, *, tolerance: float = 1e-12) -> str:
    if margin > tolerance:
        return "above_switch"
    if margin < -tolerance:
        return "below_switch"
    return "on_switch"
