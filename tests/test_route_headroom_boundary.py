from __future__ import annotations

import math

from eco_genetic_warning_extensions.route_headroom_boundary import (
    direct_recoupling_headroom_shift,
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
