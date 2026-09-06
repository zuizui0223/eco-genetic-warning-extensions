from __future__ import annotations

import math
from pathlib import Path

import pytest

from eco_genetic_warning_extensions.route_headroom_boundary import (
    continuous_static_crossing_generation,
    direct_recoupling_headroom_shift,
    first_static_unsafe_generation,
    initial_matched_marginal_certificate,
    next_q_from_state,
    route_headroom,
    support_signal,
    target_offset,
)


def test_headroom_sign_is_exactly_equivalent_to_next_q_side() -> None:
    c = 0.625
    for q in (0.2, 0.5, 0.8, 0.95):
        for trait in (0.1, 0.5, 0.9):
            for allele in (0.1, 0.5, 0.9):
                for density in (0.4, 0.7, 1.0):
                    for theta in (0.50, 0.55, 0.60):
                        h = route_headroom(q, trait, allele, density, theta, target_q=c)
                        qn = next_q_from_state(q, trait, allele, density, theta)
                        assert (h >= 0.0) == (qn >= c)


def test_boundary_is_exact_at_zero_headroom() -> None:
    c = 0.625
    q, trait, allele, density = 0.8, 0.7, 0.6, 0.9
    signal = support_signal(q, trait, allele)
    theta = density * signal - target_offset(c, 4.5)
    h = route_headroom(q, trait, allele, density, theta, target_q=c)
    qn = next_q_from_state(q, trait, allele, density, theta)
    assert math.isclose(h, 0.0, abs_tol=1e-12)
    assert math.isclose(qn, c, abs_tol=1e-12)


def test_initial_AA_RR_certificate_exhibits_coverage_reserve_tradeoff() -> None:
    cert = initial_matched_marginal_certificate()
    aa = cert["conditions"]["AA"]
    rr = cert["conditions"]["RR"]

    assert math.isclose(aa["support_mean"], 0.68, abs_tol=1e-12)
    assert math.isclose(rr["support_mean"], 0.68, abs_tol=1e-12)
    assert math.isclose(aa["headroom_mean"], rr["headroom_mean"], abs_tol=1e-12)
    assert math.isclose(aa["support_variance"], 0.0245, abs_tol=1e-12)
    assert math.isclose(rr["support_variance"], 0.0005, abs_tol=1e-12)
    assert math.isclose(aa["headroom_variance"] / rr["headroom_variance"], 49.0, abs_tol=1e-12)

    assert aa["positive_headroom_patch_count"] == 2
    assert rr["positive_headroom_patch_count"] == 4
    assert aa["maximum_headroom"] > rr["maximum_headroom"]
    assert aa["minimum_headroom"] < 0.0 < rr["minimum_headroom"]

    assert math.isclose(aa["maximum_headroom"], 0.2739831947186687, abs_tol=1e-12)
    assert math.isclose(rr["maximum_headroom"], 0.09398319471866867, abs_tol=1e-12)


def test_frozen_support_benchmark_converts_coverage_to_endurance() -> None:
    cert = initial_matched_marginal_certificate()
    aa = cert["conditions"]["AA"]
    rr = cert["conditions"]["RR"]

    assert aa["frozen_state_first_unsafe_generation"] == (1, 1, 55, 111)
    assert rr["frozen_state_first_unsafe_generation"] == (39, 31, 23, 15)

    # By generation 40, the frozen RR support field would have no patch left
    # above the moving q*=0.625 boundary, whereas AA would retain two.
    assert sum(g > 40 for g in aa["frozen_state_first_unsafe_generation"]) == 2
    assert sum(g > 40 for g in rr["frozen_state_first_unsafe_generation"]) == 0

    assert math.isclose(continuous_static_crossing_generation(0.75), 54.59327788746747, abs_tol=1e-12)
    assert first_static_unsafe_generation(0.75) == 55


def test_direct_recoupling_shift_is_exact_headroom_difference_from_q_only() -> None:
    q, trait, allele, density, theta = 0.65, 0.8, 0.8, 1.0, 0.5025
    full = route_headroom(q, trait, allele, density, theta)
    q_only = route_headroom(
        q,
        trait,
        allele,
        density,
        theta,
        alpha=1.0,
        beta_trait=0.0,
        gamma_allele=0.0,
    )
    shift = direct_recoupling_headroom_shift(q, trait, allele, density)
    assert math.isclose(full - q_only, shift, abs_tol=1e-12)
    assert shift > 0.0


def test_headroom_is_monotone_in_density_and_support_components() -> None:
    base = route_headroom(0.7, 0.5, 0.5, 0.7, 0.55)
    assert route_headroom(0.71, 0.5, 0.5, 0.7, 0.55) > base
    assert route_headroom(0.7, 0.51, 0.5, 0.7, 0.55) > base
    assert route_headroom(0.7, 0.5, 0.51, 0.7, 0.55) > base
    assert route_headroom(0.7, 0.5, 0.5, 0.71, 0.55) > base


def test_support_signal_matches_pinned_parent_when_parent_is_installed() -> None:
    parent = pytest.importorskip("causal_model.multipatch_criticality_dynamics")
    params = parent.DynamicsParameters(
        patch_areas=(1.0,),
        q_feedback_alpha=0.6,
        q_feedback_beta_trait=0.3,
        q_feedback_gamma_allele=0.1,
    )
    for q, trait, allele in ((0.65, 0.2, 0.2), (0.8, 0.6, 0.4), (0.95, 0.8, 0.8)):
        got = parent.interaction_support_signal(q, trait, allele, params)
        expected = support_signal(q, trait, allele)
        assert math.isclose(got, expected, abs_tol=1e-12)


def test_route_headroom_document_preserves_claim_ceiling() -> None:
    root = Path(__file__).resolve().parents[1]
    text = (root / "docs" / "ROUTE_HEADROOM_BOUNDARY_THEOREM_2026-09-06.md").read_text()
    lower = text.casefold()
    assert "h_j(t;c)" in text
    assert "0.1135168053" in text
    assert "coverage–reserve trade-off" in text
    assert "not, by itself, an exact predictor" in lower
    assert "not universal natural thresholds" in lower
