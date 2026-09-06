from __future__ import annotations

import json
import math
from pathlib import Path

import pytest

from eco_genetic_warning_extensions.direct_feedback_recoupling_theorem import (
    certificate,
    direct_feedback_logit_shift,
    eco_genetic_bundle,
    full_support,
    next_q,
    support_contraction_factor,
    support_minus_bundle,
    support_minus_q,
    transition_displacement_bound,
)


def test_locked_support_is_convex_recoupling_operator() -> None:
    assert math.isclose(support_contraction_factor(), 0.6, abs_tol=1e-12)
    for q, t, g in (
        (0.65, 0.2, 0.2),
        (0.65, 0.8, 0.8),
        (0.85, 0.6, 0.4),
        (0.95, 0.2, 0.8),
    ):
        b = eco_genetic_bundle(t, g)
        s = full_support(q, t, g)
        assert math.isclose(b, 0.75 * t + 0.25 * g, abs_tol=1e-12)
        assert math.isclose(s, 0.6 * q + 0.4 * b, abs_tol=1e-12)
        assert math.isclose(support_minus_bundle(q, t, g), 0.6 * (q - b), abs_tol=1e-12)
        assert math.isclose(support_minus_q(q, t, g), 0.4 * (b - q), abs_tol=1e-12)
        assert math.isclose(abs(s - b), 0.6 * abs(q - b), abs_tol=1e-12)


def test_direct_feedback_next_q_shift_has_exact_bundle_minus_q_sign() -> None:
    density = 0.8
    barrier = 0.55
    for q, t, g in (
        (0.65, 0.8, 0.8),
        (0.75, 0.4, 0.4),
        (0.85, 0.85, 0.85),
    ):
        b = eco_genetic_bundle(t, g)
        s = full_support(q, t, g)
        full = next_q(s, density, barrier)
        qonly = next_q(q, density, barrier)
        shift = direct_feedback_logit_shift(q, t, g, density)
        assert math.isclose(shift, 1.8 * density * (b - q), abs_tol=1e-12)
        if b > q:
            assert full > qonly
            assert shift > 0.0
        elif b < q:
            assert full < qonly
            assert shift < 0.0
        else:
            assert math.isclose(full, qonly, abs_tol=1e-12)
            assert math.isclose(shift, 0.0, abs_tol=1e-12)
        assert abs(full - qonly) <= transition_displacement_bound(q, t, g, density) + 1e-12


def test_certificate_locks_exact_coefficients() -> None:
    c = certificate()
    assert c["bundle_trait_weight"] == 0.75
    assert c["bundle_allele_weight"] == 0.25
    assert c["support_mismatch_contraction_factor"] == 0.6
    assert c["support_mismatch_reduction_fraction"] == 0.4
    assert c["locked_logit_shift_coefficient_at_density_one"] == 1.8
    assert c["locked_transition_displacement_bound_coefficient_at_density_one"] == 0.45


def test_parent_support_implementation_matches_theorem_when_installed() -> None:
    pytest.importorskip("causal_model.multipatch_criticality_dynamics")
    from causal_model.multipatch_criticality_dynamics import DynamicsParameters, interaction_support_signal

    params = DynamicsParameters(
        patch_areas=(1.0,),
        q_feedback_alpha=0.6,
        q_feedback_beta_trait=0.3,
        q_feedback_gamma_allele=0.1,
    )
    for q, t, g in ((0.65, 0.2, 0.8), (0.85, 0.6, 0.4), (0.95, 0.8, 0.2)):
        actual = interaction_support_signal(q, t, g, params)
        assert math.isclose(actual, full_support(q, t, g), abs_tol=1e-12)


def test_locked_paired_feedback_contrast_is_preferential_buffering() -> None:
    root = Path(__file__).resolve().parents[1]
    d = json.loads((root / "artifacts" / "direct_feedback_recoupling" / "locked_derived_result.json").read_text())
    assert d["source"]["workflow_run"] == 34012983845
    assert d["source"]["artifact_id"] == 9983093178
    assert d["source"]["paired_keys"] == 1500

    g20 = d["generation_20"]
    assert g20["RR"]["paired_ci95"][0] > 0.05
    assert g20["RR_minus_AA_buffering_benefit_DID"] > 0.079
    assert g20["DID_ci95"][0] > 0.03

    g40 = d["generation_40"]
    assert g40["RR"]["paired_ci95"][0] > 0.04
    assert g40["RR_minus_AA_buffering_benefit_DID"] > 0.063
    assert g40["DID_ci95"][0] > 0.018


def test_theorem_document_preserves_claim_ceiling() -> None:
    root = Path(__file__).resolve().parents[1]
    text = (root / "docs" / "DIRECT_FEEDBACK_RECOUPLING_THEOREM_2026-09-06.md").read_text().casefold()
    assert "support stage contracts interaction–bundle mismatch by exactly **40%**".casefold() in text
    assert "not a claim that full feedback always increases q" in text
    assert "not a separately predeclared primary estimand" in text
    assert "do not establish a universal natural recoupling law" in text
