from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class HeadroomState:
    q: float
    trait: float
    allele: float
    density: float
    theta: float


def support(state: HeadroomState, alpha: float = 0.6, beta: float = 0.3, gamma: float = 0.1) -> float:
    return alpha * state.q + beta * state.trait + gamma * state.allele


def budget_terms(
    before: HeadroomState,
    after: HeadroomState,
    *,
    area_ratio: float = 1.0,
    alpha: float = 0.6,
    beta: float = 0.3,
    gamma: float = 0.1,
) -> dict[str, float]:
    """Exact symmetric discrete decomposition of delta H.

    For H=a*d*S-theta-constant and S=alpha*q+beta*T+gamma*G,
    d1*S1-d0*S0 = mean(d)*delta(S) + mean(S)*delta(d).
    """
    s0 = support(before, alpha, beta, gamma)
    s1 = support(after, alpha, beta, gamma)
    dbar = 0.5 * (before.density + after.density)
    sbar = 0.5 * (s0 + s1)
    dq = after.q - before.q
    dt = after.trait - before.trait
    dg = after.allele - before.allele
    dd = after.density - before.density
    dtheta = after.theta - before.theta

    q_term = area_ratio * dbar * alpha * dq
    trait_term = area_ratio * dbar * beta * dt
    allele_term = area_ratio * dbar * gamma * dg
    density_term = area_ratio * sbar * dd
    forcing_term = -dtheta
    total = q_term + trait_term + allele_term + density_term + forcing_term
    direct = area_ratio * after.density * s1 - after.theta - (
        area_ratio * before.density * s0 - before.theta
    )
    return {
        "interaction": q_term,
        "trait": trait_term,
        "allele": allele_term,
        "density": density_term,
        "forcing": forcing_term,
        "sum": total,
        "direct_delta_headroom": direct,
        "closure_error": total - direct,
    }


def accumulated_budget(states: list[HeadroomState], **kwargs: float) -> dict[str, float]:
    if len(states) < 2:
        raise ValueError("at least two states are required")
    keys = ("interaction", "trait", "allele", "density", "forcing", "sum", "direct_delta_headroom")
    totals = {key: 0.0 for key in keys}
    max_abs_closure = 0.0
    for before, after in zip(states, states[1:]):
        row = budget_terms(before, after, **kwargs)
        for key in keys:
            totals[key] += row[key]
        max_abs_closure = max(max_abs_closure, abs(row["closure_error"]))
    totals["max_abs_step_closure_error"] = max_abs_closure
    totals["accumulated_closure_error"] = totals["sum"] - totals["direct_delta_headroom"]
    return totals
