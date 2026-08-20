"""Exact local support-frontier identities for the affine recurrent transition.

These functions describe the local allele-state condition M(p) >= p_c. They do
not determine the full stochastic functional-loss regime or warning ordering.
"""
from __future__ import annotations


def _validate_frequency(value: float, name: str) -> float:
    result = float(value)
    if not 0.0 <= result <= 1.0:
        raise ValueError(f"{name} must lie in [0, 1]")
    return result


def critical_p_star_for_support(
    *,
    kappa_mu: float,
    pre_transition_frequency: float,
    post_transition_threshold: float,
) -> float:
    """Return the transition equilibrium required for ``M(p)=p_c``.

    For ``M(p)=kappa_mu*p_star+(1-kappa_mu)*p``, the exact frontier is

    ``p_star_crit = p + (p_c-p)/kappa_mu``.

    Values outside ``[0, 1]`` are retained: they certify that no admissible
    ``p_star`` can place this particular pre-transition state exactly on the
    local support boundary at the given transition strength.
    """
    k = float(kappa_mu)
    if not 0.0 < k <= 1.0:
        raise ValueError("kappa_mu must lie in (0, 1]")
    p = _validate_frequency(pre_transition_frequency, "pre_transition_frequency")
    p_c = _validate_frequency(post_transition_threshold, "post_transition_threshold")
    return p + (p_c - p) / k


def critical_p_star_kappa_derivative(
    *,
    kappa_mu: float,
    pre_transition_frequency: float,
    post_transition_threshold: float,
) -> float:
    """Return ``d p_star_crit / d kappa_mu = -(p_c-p)/kappa_mu^2``.

    Hence, when ``p < p_c``, stronger recurrent-transition relaxation lowers
    the directional equilibrium required to reach the same local high-state
    threshold. When ``p > p_c`` the sign reverses; at ``p == p_c`` the local
    frontier is independent of ``kappa_mu``.
    """
    k = float(kappa_mu)
    if not 0.0 < k <= 1.0:
        raise ValueError("kappa_mu must lie in (0, 1]")
    p = _validate_frequency(pre_transition_frequency, "pre_transition_frequency")
    p_c = _validate_frequency(post_transition_threshold, "post_transition_threshold")
    return -(p_c - p) / (k * k)


def support_frontier_kappa_relation(
    *,
    pre_transition_frequency: float,
    post_transition_threshold: float,
) -> str:
    """Classify how stronger ``kappa_mu`` shifts the local ``p_star`` frontier."""
    p = _validate_frequency(pre_transition_frequency, "pre_transition_frequency")
    p_c = _validate_frequency(post_transition_threshold, "post_transition_threshold")
    if p < p_c:
        return "lower_p_star_required"
    if p > p_c:
        return "higher_p_star_required"
    return "frontier_independent_of_kappa_mu"
