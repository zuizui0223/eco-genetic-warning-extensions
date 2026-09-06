from __future__ import annotations

import math

from eco_genetic_warning_extensions.branching_headroom_theorem import (
    Q_STAR,
    allele_logodds_increment_from_next_q,
    allele_selection_delta,
    barrier,
    branch_growth_increment,
    frozen_support_crossing_generation,
    headroom,
    next_q,
    opening_certificate,
    recoupling_headroom_shift,
    support_from_bundle,
    switch_offset,
)


def test_headroom_sign_is_exact_route_switch() -> None:
    for q in (0.65, 0.75, 0.85, 0.95):
        for b in (0.2, 0.4, 0.6, 0.8):
            h = headroom(q, b, 1.0, barrier(1))
            qn = next_q(q, b, 1.0, barrier(1))
            inc = allele_logodds_increment_from_next_q(qn)
            assert (h > 0) == (qn > Q_STAR)
            assert (h < 0) == (qn < Q_STAR)
            assert (h > 0) == (inc > 0)
            assert (h < 0) == (inc < 0)


def test_zero_headroom_hits_shared_switch_exactly() -> None:
    theta = barrier(20)
    q = 0.8
    b = 0.6
    s = support_from_bundle(q, b)
    d = (theta + switch_offset()) / s
    assert math.isclose(headroom(q, b, d, theta), 0.0, abs_tol=1e-12)
    assert math.isclose(next_q(q, b, d, theta), Q_STAR, abs_tol=1e-12)
    assert math.isclose(allele_logodds_increment_from_next_q(Q_STAR), 0.0, abs_tol=1e-12)


def test_headroom_sign_also_sets_selection_and_smooth_growth_direction() -> None:
    for q in (0.65, 0.75, 0.85, 0.95):
        for b in (0.2, 0.4, 0.6, 0.8):
            h = headroom(q, b, 1.0, barrier(1))
            qn = next_q(q, b, 1.0, barrier(1))
            for p in (0.2, 0.5, 0.8):
                dp = allele_selection_delta(p, qn)
                dg = branch_growth_increment(p, qn)
                assert (h > 0) == (dp > 0)
                assert (h < 0) == (dp < 0)
                assert (h > 0) == (dg > 0)
                assert (h < 0) == (dg < 0)


def test_branch_growth_increment_is_zero_on_route_surface() -> None:
    for p in (0.2, 0.5, 0.8):
        assert math.isclose(allele_selection_delta(p, Q_STAR), 0.0, abs_tol=1e-12)
        assert math.isclose(branch_growth_increment(p, Q_STAR), 0.0, abs_tol=1e-12)


def test_direct_recoupling_moves_headroom_by_exact_amount() -> None:
    for q, b, d in ((0.8, 0.3, 1.0), (0.4, 0.8, 0.7), (0.6, 0.6, 0.5)):
        full = d * support_from_bundle(q, b)
        q_only = d * q
        assert math.isclose(full - q_only, recoupling_headroom_shift(q, b, d), abs_tol=1e-12)


def test_opening_equalization_refuge_geometry() -> None:
    cert = opening_certificate()
    assert math.isclose(cert["generation_1_boundary"], 0.6160168052813313, abs_tol=1e-12)
    assert tuple(round(x, 2) for x in cert["AA_support"]) == (0.47, 0.61, 0.75, 0.89)
    assert tuple(round(x, 2) for x in cert["RR_support"]) == (0.71, 0.69, 0.67, 0.65)
    aa = cert["AA_headroom"]
    rr = cert["RR_headroom"]
    assert sum(x > 0 for x in aa) == 2
    assert sum(x > 0 for x in rr) == 4
    assert max(aa) > max(rr)
    assert min(aa) < 0 < min(rr)

    assert tuple(round(x, 4) for x in cert["AA_next_q"]) == (0.4635, 0.6186, 0.7528, 0.8512)
    assert tuple(round(x, 4) for x in cert["RR_next_q"]) == (0.7178, 0.6993, 0.68, 0.6601)
    assert tuple(round(x, 4) for x in cert["AA_allele_logodds_increment"]) == (-0.0668, -0.0026, 0.0499, 0.0866)
    assert tuple(round(x, 4) for x in cert["RR_allele_logodds_increment"]) == (0.0365, 0.0293, 0.0218, 0.0139)


def test_frozen_crossing_times_show_shallow_rr_headroom() -> None:
    cert = opening_certificate()
    aa = cert["AA_frozen_crossing"]
    rr = cert["RR_frozen_crossing"]
    assert aa[0] < 1 and aa[1] < 1
    assert math.isclose(aa[2], 54.59327788746747, abs_tol=1e-10)
    assert math.isclose(aa[3], 110.59327788746746, abs_tol=1e-10)
    assert tuple(round(x, 2) for x in rr) == (38.59, 30.59, 22.59, 14.59)


def test_document_preserves_claim_ceiling() -> None:
    from pathlib import Path

    text = (Path(__file__).resolve().parents[1] / "docs" / "BRANCHING_HEADROOM_THEOREM_2026-09-06.md").read_text()
    lower = text.casefold()
    assert "opening-state diagnostic" in lower
    assert "not forecasts of natural generations" in lower
    assert "no universal ecological headroom threshold" in lower
