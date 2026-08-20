import pytest

from eco_genetic_warning_extensions.recurrent_transition_frontier import (
    critical_p_star_for_support,
    critical_p_star_kappa_derivative,
    support_frontier_kappa_relation,
)


def apply_transition(kappa_mu: float, p_star: float, p: float) -> float:
    return kappa_mu * p_star + (1.0 - kappa_mu) * p


def test_critical_pstar_lands_exactly_on_support_boundary() -> None:
    p = 0.45
    p_c = 0.50
    k = 0.20
    p_star = critical_p_star_for_support(
        kappa_mu=k,
        pre_transition_frequency=p,
        post_transition_threshold=p_c,
    )
    assert p_star == pytest.approx(0.70)
    assert apply_transition(k, p_star, p) == pytest.approx(p_c)


def test_stronger_transition_lowers_required_pstar_below_threshold() -> None:
    p = 0.45
    p_c = 0.50
    weak = critical_p_star_for_support(
        kappa_mu=0.20,
        pre_transition_frequency=p,
        post_transition_threshold=p_c,
    )
    strong = critical_p_star_for_support(
        kappa_mu=0.35,
        pre_transition_frequency=p,
        post_transition_threshold=p_c,
    )
    assert strong < weak
    assert support_frontier_kappa_relation(
        pre_transition_frequency=p,
        post_transition_threshold=p_c,
    ) == "lower_p_star_required"


def test_kappa_derivative_matches_finite_difference() -> None:
    k = 0.35
    p = 0.45
    p_c = 0.50
    eps = 1e-6
    low = critical_p_star_for_support(
        kappa_mu=k - eps,
        pre_transition_frequency=p,
        post_transition_threshold=p_c,
    )
    high = critical_p_star_for_support(
        kappa_mu=k + eps,
        pre_transition_frequency=p,
        post_transition_threshold=p_c,
    )
    numerical = (high - low) / (2.0 * eps)
    exact = critical_p_star_kappa_derivative(
        kappa_mu=k,
        pre_transition_frequency=p,
        post_transition_threshold=p_c,
    )
    assert exact < 0.0
    assert numerical == pytest.approx(exact, rel=1e-7)


def test_frontier_can_be_outside_admissible_pstar_range() -> None:
    p_star = critical_p_star_for_support(
        kappa_mu=0.20,
        pre_transition_frequency=0.20,
        post_transition_threshold=0.50,
    )
    assert p_star > 1.0


def test_frontier_direction_changes_above_threshold() -> None:
    assert support_frontier_kappa_relation(
        pre_transition_frequency=0.60,
        post_transition_threshold=0.50,
    ) == "higher_p_star_required"
    assert critical_p_star_kappa_derivative(
        kappa_mu=0.20,
        pre_transition_frequency=0.60,
        post_transition_threshold=0.50,
    ) > 0.0


def test_frontier_is_kappa_independent_on_threshold() -> None:
    assert support_frontier_kappa_relation(
        pre_transition_frequency=0.50,
        post_transition_threshold=0.50,
    ) == "frontier_independent_of_kappa_mu"
    assert critical_p_star_kappa_derivative(
        kappa_mu=0.20,
        pre_transition_frequency=0.50,
        post_transition_threshold=0.50,
    ) == pytest.approx(0.0)
