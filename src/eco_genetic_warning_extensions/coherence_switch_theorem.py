from __future__ import annotations

from math import exp, log


def sigmoid(x: float) -> float:
    return 1.0 / (1.0 + exp(-x))


def logit(x: float) -> float:
    if not 0.0 < x < 1.0:
        raise ValueError("x must lie strictly between 0 and 1")
    return log(x / (1.0 - x))


def q_from_headroom(
    headroom: float,
    *,
    target_q: float = 0.625,
    kappa: float = 4.5,
) -> float:
    """Exact next-q representation around the route-headroom boundary."""
    return sigmoid(logit(target_q) + kappa * headroom)


def high_trait_margin(q: float) -> float:
    """W(1;q)-1 for the pinned parent trait-performance surface."""
    return 0.8 * (q - 0.625)


def high_allele_relative_fitness(q: float, selection_strength: float = 0.5) -> float:
    """Relative high-allele fitness used by the deterministic selection step."""
    return 1.0 + selection_strength * high_trait_margin(q)


def selected_high_allele_frequency(p: float, q: float) -> float:
    if not 0.0 <= p <= 1.0:
        raise ValueError("p must lie in [0, 1]")
    w = high_allele_relative_fitness(q)
    return p * w / (1.0 - p + p * w)


def allele_log_odds_increment(q: float) -> float:
    return log(high_allele_relative_fitness(q))


def coherence_switch_certificate(headroom: float, p: float = 0.5) -> dict[str, float | bool]:
    q = q_from_headroom(headroom)
    margin = high_trait_margin(q)
    p_selected = selected_high_allele_frequency(p, q)
    return {
        "headroom": headroom,
        "q_next": q,
        "high_trait_margin": margin,
        "allele_frequency_before_selection": p,
        "allele_frequency_after_selection": p_selected,
        "allele_selection_change": p_selected - p,
        "allele_log_odds_increment": allele_log_odds_increment(q),
        "interaction_high_side": q >= 0.625,
        "trait_potential_viable_at_z1": margin >= 0.0,
        "high_allele_non_decreasing": p_selected >= p,
    }


def boundary_sensitivities(
    *,
    target_q: float = 0.625,
    kappa: float = 4.5,
) -> dict[str, float]:
    if target_q != 0.625:
        raise ValueError("the pinned trait/allele coherence switch is defined at q=0.625")
    dq_dh = kappa * target_q * (1.0 - target_q)
    dmargin_dh = 0.8 * dq_dh
    dw_dh = 0.4 * dq_dh
    # At q*=0.625, the relative high-allele fitness w is exactly one, so the
    # derivative of log(w) equals dw/dH.
    dlogodds_increment_dh = dw_dh
    return {
        "dq_next_dH_at_boundary": dq_dh,
        "d_high_trait_margin_dH_at_boundary": dmargin_dh,
        "d_high_allele_relative_fitness_dH_at_boundary": dw_dh,
        "d_allele_log_odds_increment_dH_at_boundary": dlogodds_increment_dh,
    }
