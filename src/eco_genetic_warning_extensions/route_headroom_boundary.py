from __future__ import annotations

from math import exp, log
from statistics import fmean
from typing import Iterable


def logit(x: float) -> float:
    if not 0.0 < x < 1.0:
        raise ValueError("x must lie strictly between 0 and 1")
    return log(x / (1.0 - x))


def sigmoid(x: float) -> float:
    return 1.0 / (1.0 + exp(-x))


def target_offset(target_q: float = 0.625, kappa: float = 4.5) -> float:
    if kappa <= 0.0:
        raise ValueError("kappa must be positive")
    return logit(target_q) / kappa


def support_signal(
    q: float,
    trait: float,
    allele: float,
    alpha: float = 0.6,
    beta_trait: float = 0.3,
    gamma_allele: float = 0.1,
) -> float:
    return alpha * q + beta_trait * trait + gamma_allele * allele


def route_headroom(
    q: float,
    trait: float,
    allele: float,
    density: float,
    theta: float,
    *,
    target_q: float = 0.625,
    kappa: float = 4.5,
    area_ratio: float = 1.0,
    alpha: float = 0.6,
    beta_trait: float = 0.3,
    gamma_allele: float = 0.1,
) -> float:
    if not 0.0 <= density <= 1.0:
        raise ValueError("density must lie in [0, 1]")
    signal = support_signal(q, trait, allele, alpha, beta_trait, gamma_allele)
    return area_ratio * density * signal - theta - target_offset(target_q, kappa)


def next_q_from_state(
    q: float,
    trait: float,
    allele: float,
    density: float,
    theta: float,
    *,
    kappa: float = 4.5,
    area_ratio: float = 1.0,
    alpha: float = 0.6,
    beta_trait: float = 0.3,
    gamma_allele: float = 0.1,
) -> float:
    signal = support_signal(q, trait, allele, alpha, beta_trait, gamma_allele)
    return sigmoid(kappa * (area_ratio * density * signal - theta))


def eco_genetic_bundle(trait: float, allele: float) -> float:
    # Normalized bundle for the locked beta:gamma = 3:1 support weights.
    return 0.75 * trait + 0.25 * allele


def direct_recoupling_headroom_shift(
    q: float,
    trait: float,
    allele: float,
    density: float,
    *,
    area_ratio: float = 1.0,
) -> float:
    bundle = eco_genetic_bundle(trait, allele)
    return 0.4 * area_ratio * density * (bundle - q)


def _population_variance(values: Iterable[float]) -> float:
    vals = tuple(float(x) for x in values)
    mean = fmean(vals)
    return fmean((x - mean) ** 2 for x in vals)


def initial_matched_marginal_certificate() -> dict[str, object]:
    q = (0.65, 0.75, 0.85, 0.95)
    ascending = (0.20, 0.40, 0.60, 0.80)
    reversed_bundle = tuple(reversed(ascending))
    theta = 0.50 + 0.15 / 60.0
    threshold = theta + target_offset()

    out: dict[str, object] = {
        "theta_generation_1": theta,
        "target_q": 0.625,
        "target_support_boundary_at_density_1": threshold,
        "conditions": {},
    }
    for label, bundle in (("AA", ascending), ("RR", reversed_bundle)):
        support = tuple(support_signal(x, b, b) for x, b in zip(q, bundle))
        headroom = tuple(x - threshold for x in support)
        out["conditions"][label] = {
            "support": support,
            "support_mean": fmean(support),
            "support_variance": _population_variance(support),
            "headroom": headroom,
            "headroom_mean": fmean(headroom),
            "headroom_variance": _population_variance(headroom),
            "positive_headroom_patch_count": sum(x >= 0.0 for x in headroom),
            "maximum_headroom": max(headroom),
            "minimum_headroom": min(headroom),
        }
    return out
