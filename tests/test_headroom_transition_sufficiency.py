from __future__ import annotations

import math

import pytest

from eco_genetic_warning_extensions.headroom_transition_sufficiency import (
    headroom_from_explicit_state,
    interaction_field_from_headroom,
    next_interaction_from_explicit_state,
)


def test_headroom_vector_exactly_factorizes_next_interaction_transition() -> None:
    q = (0.65, 0.75, 0.85, 0.95)
    t = (0.20, 0.40, 0.60, 0.80)
    g = (0.20, 0.40, 0.60, 0.80)
    d = (1.0, 0.9, 0.8, 0.7)
    theta = 0.55
    h = headroom_from_explicit_state(q, t, g, d, theta)
    factored = interaction_field_from_headroom(h)
    direct = next_interaction_from_explicit_state(q, t, g, d, theta)
    assert factored == direct


def test_same_headroom_implies_same_next_interaction_even_with_different_states() -> None:
    theta = 0.55
    # State A has support 1 at density .7; state B has support .7 at density 1.
    # Both therefore have the same density-weighted support and the same H.
    h_a = headroom_from_explicit_state((1.0,), (1.0,), (1.0,), (0.7,), theta)
    h_b = headroom_from_explicit_state((0.5,), (1.0,), (1.0,), (1.0,), theta)
    assert math.isclose(h_a[0], h_b[0], abs_tol=1e-12)
    assert interaction_field_from_headroom(h_a) == interaction_field_from_headroom(h_b)


def test_matched_marginal_AA_RR_have_different_headroom_and_transition() -> None:
    q = (0.65, 0.75, 0.85, 0.95)
    aa = (0.20, 0.40, 0.60, 0.80)
    rr = tuple(reversed(aa))
    d = (1.0,) * 4
    theta = 0.5025
    h_aa = headroom_from_explicit_state(q, aa, aa, d, theta)
    h_rr = headroom_from_explicit_state(q, rr, rr, d, theta)
    assert h_aa != h_rr
    q_aa = interaction_field_from_headroom(h_aa)
    q_rr = interaction_field_from_headroom(h_rr)
    assert max(abs(x - y) for x, y in zip(q_aa, q_rr)) > 0.25


def test_factorization_matches_pinned_parent_support_transition_when_parent_installed() -> None:
    parent = pytest.importorskip("causal_model.multipatch_criticality_dynamics")
    params = parent.DynamicsParameters(
        patch_areas=(1.0, 1.0),
        interaction_feedback=4.5,
        interaction_barrier=0.55,
        q_feedback_alpha=0.6,
        q_feedback_beta_trait=0.3,
        q_feedback_gamma_allele=0.1,
    )
    q = (0.7, 0.9)
    t = (0.4, 0.8)
    g = (0.6, 0.2)
    d = (0.75, 1.0)
    expected = []
    for qi, ti, gi, di in zip(q, t, g, d):
        s = parent.interaction_support_signal(qi, ti, gi, params)
        expected.append(parent.sigmoid(params.interaction_feedback * (di * s - params.interaction_barrier)))
    got = next_interaction_from_explicit_state(q, t, g, d, 0.55)
    assert all(math.isclose(x, y, abs_tol=1e-12) for x, y in zip(got, expected))
