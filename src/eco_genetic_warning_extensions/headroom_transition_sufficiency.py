from __future__ import annotations

from math import exp, log
from typing import Iterable


def sigmoid(x: float) -> float:
    return 1.0 / (1.0 + exp(-x))


def logit(x: float) -> float:
    if not 0.0 < x < 1.0:
        raise ValueError("x must lie strictly between 0 and 1")
    return log(x / (1.0 - x))


def interaction_from_headroom(
    headroom: float,
    *,
    target_q: float = 0.625,
    kappa: float = 4.5,
) -> float:
    return sigmoid(logit(target_q) + kappa * headroom)


def interaction_field_from_headroom(
    headroom: Iterable[float],
    *,
    target_q: float = 0.625,
    kappa: float = 4.5,
) -> tuple[float, ...]:
    return tuple(interaction_from_headroom(h, target_q=target_q, kappa=kappa) for h in headroom)


def headroom_from_explicit_state(
    interaction: Iterable[float],
    trait: Iterable[float],
    allele: Iterable[float],
    density: Iterable[float],
    theta: float,
    *,
    target_q: float = 0.625,
    kappa: float = 4.5,
    area_ratio: Iterable[float] | None = None,
    alpha: float = 0.6,
    beta_trait: float = 0.3,
    gamma_allele: float = 0.1,
) -> tuple[float, ...]:
    q = tuple(float(x) for x in interaction)
    t = tuple(float(x) for x in trait)
    g = tuple(float(x) for x in allele)
    d = tuple(float(x) for x in density)
    if not (len(q) == len(t) == len(g) == len(d)):
        raise ValueError("state vectors must have equal length")
    a = tuple(1.0 for _ in q) if area_ratio is None else tuple(float(x) for x in area_ratio)
    if len(a) != len(q):
        raise ValueError("area_ratio must match patch count")
    offset = logit(target_q) / kappa
    return tuple(
        ai * di * (alpha * qi + beta_trait * ti + gamma_allele * gi) - theta - offset
        for ai, di, qi, ti, gi in zip(a, d, q, t, g)
    )


def next_interaction_from_explicit_state(
    interaction: Iterable[float],
    trait: Iterable[float],
    allele: Iterable[float],
    density: Iterable[float],
    theta: float,
    **kwargs: object,
) -> tuple[float, ...]:
    h = headroom_from_explicit_state(interaction, trait, allele, density, theta, **kwargs)
    target_q = float(kwargs.get("target_q", 0.625))
    kappa = float(kwargs.get("kappa", 4.5))
    return interaction_field_from_headroom(h, target_q=target_q, kappa=kappa)
