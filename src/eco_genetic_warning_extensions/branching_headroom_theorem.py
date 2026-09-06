from __future__ import annotations

from math import exp, log

Q_STAR = 0.625
KAPPA = 4.5
ALPHA_Q = 0.6
BETA_BUNDLE = 0.4
BARRIER_START = 0.50
BARRIER_SLOPE = 0.0025


def logit(x: float) -> float:
    if not 0.0 < x < 1.0:
        raise ValueError("x must lie strictly inside (0,1)")
    return log(x / (1.0 - x))


def sigmoid(x: float) -> float:
    return 1.0 / (1.0 + exp(-x))


def switch_offset(q_star: float = Q_STAR, kappa: float = KAPPA) -> float:
    return logit(q_star) / kappa


def bundle(trait: float, allele: float) -> float:
    return 0.75 * trait + 0.25 * allele


def support(q: float, trait: float, allele: float) -> float:
    return ALPHA_Q * q + 0.3 * trait + 0.1 * allele


def support_from_bundle(q: float, b: float) -> float:
    return ALPHA_Q * q + BETA_BUNDLE * b


def barrier(generation: int) -> float:
    return BARRIER_START + BARRIER_SLOPE * generation


def headroom(q: float, b: float, density: float, theta: float) -> float:
    return density * support_from_bundle(q, b) - theta - switch_offset()


def next_q(q: float, b: float, density: float, theta: float) -> float:
    s = support_from_bundle(q, b)
    return sigmoid(KAPPA * (density * s - theta))


def allele_logodds_increment_from_next_q(q_next: float) -> float:
    return log(0.75 + 0.4 * q_next)


def recoupling_headroom_shift(q: float, b: float, density: float) -> float:
    return BETA_BUNDLE * density * (b - q)


def frozen_support_crossing_generation(s: float, density: float = 1.0) -> float:
    # theta_g + c* = 0.50 + 0.0025g + c*.
    return (density * s - BARRIER_START - switch_offset()) / BARRIER_SLOPE


def opening_certificate() -> dict[str, object]:
    q = (0.65, 0.75, 0.85, 0.95)
    aa_b = (0.20, 0.40, 0.60, 0.80)
    rr_b = (0.80, 0.60, 0.40, 0.20)
    theta1 = barrier(1)
    aa_s = tuple(support_from_bundle(x, b) for x, b in zip(q, aa_b))
    rr_s = tuple(support_from_bundle(x, b) for x, b in zip(q, rr_b))
    aa_h = tuple(headroom(x, b, 1.0, theta1) for x, b in zip(q, aa_b))
    rr_h = tuple(headroom(x, b, 1.0, theta1) for x, b in zip(q, rr_b))
    return {
        "q_star": Q_STAR,
        "switch_offset": switch_offset(),
        "generation_1_boundary": theta1 + switch_offset(),
        "AA_support": aa_s,
        "RR_support": rr_s,
        "AA_headroom": aa_h,
        "RR_headroom": rr_h,
        "AA_frozen_crossing": tuple(frozen_support_crossing_generation(s) for s in aa_s),
        "RR_frozen_crossing": tuple(frozen_support_crossing_generation(s) for s in rr_s),
    }
