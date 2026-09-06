from __future__ import annotations

import json
import math
from pathlib import Path

import pytest

from eco_genetic_warning_extensions.recruitment_buffer_theorem import (
    contraction_certificate,
    mismatch_after_recruitment,
    recruit_high_trait_mass,
    spatial_mean_squared_mismatch,
)


def test_exact_halfway_identity_for_locked_inheritance_weight() -> None:
    for m, p in ((0.1, 0.9), (0.2, 0.4), (0.8, 0.3), (0.5, 0.5)):
        r = recruit_high_trait_mass(m, p, 0.5)
        assert math.isclose(r, 0.5 * (m + p), rel_tol=0.0, abs_tol=1e-12)
        assert math.isclose(r - p, 0.5 * (m - p), rel_tol=0.0, abs_tol=1e-12)
        assert math.isclose(r - m, 0.5 * (p - m), rel_tol=0.0, abs_tol=1e-12)


def test_recruitment_contracts_absolute_and_squared_mismatch() -> None:
    for m, p in ((0.05, 0.85), (0.25, 0.60), (0.90, 0.15)):
        before = m - p
        after = mismatch_after_recruitment(m, p, 0.5)
        assert math.isclose(abs(after), 0.5 * abs(before), rel_tol=0.0, abs_tol=1e-12)
        assert math.isclose(after * after, 0.25 * before * before, rel_tol=0.0, abs_tol=1e-12)


def test_spatial_mean_squared_mismatch_contracts_fourfold() -> None:
    trait = (0.15, 0.35, 0.75, 0.90)
    allele = (0.60, 0.20, 0.55, 0.30)
    recruit = tuple(recruit_high_trait_mass(m, p, 0.5) for m, p in zip(trait, allele))
    before = spatial_mean_squared_mismatch(trait, allele)
    after = spatial_mean_squared_mismatch(recruit, allele)
    assert math.isclose(after, 0.25 * before, rel_tol=0.0, abs_tol=1e-12)


def test_buffering_direction_is_restorative_not_universally_high_trait_increasing() -> None:
    assert recruit_high_trait_mass(0.2, 0.8, 0.5) > 0.2
    assert recruit_high_trait_mass(0.8, 0.2, 0.5) < 0.8
    assert recruit_high_trait_mass(0.5, 0.5, 0.5) == 0.5


def test_locked_contraction_certificate() -> None:
    c = contraction_certificate(0.5)
    assert c == {
        "inheritance_weight": 0.5,
        "absolute_mismatch_factor": 0.5,
        "squared_mismatch_factor": 0.25,
        "allele_kernel_weight": 0.5,
    }


def test_parent_implementation_matches_theorem_when_available() -> None:
    pytest.importorskip("causal_model.multipatch_criticality_dynamics")
    from eco_genetic_warning_extensions.recruitment_buffer_theorem import verify_parent_recruitment

    for m, p in ((0.2, 0.8), (0.4, 0.1), (0.7, 0.6), (0.9, 0.3)):
        cert = verify_parent_recruitment(m, p, 0.5, trait_grid_size=31)
        assert math.isclose(
            cert["observed_recruit_high_trait_mass"],
            0.5 * (m + p),
            rel_tol=0.0,
            abs_tol=1e-12,
        )


def test_theorem_document_and_locked_endpoint_buffer_are_consistent() -> None:
    root = Path(__file__).resolve().parents[1]
    theorem = (root / "docs" / "RECRUITMENT_BUFFER_OPERATOR_THEOREM_2026-09-06.md").read_text(encoding="utf-8")
    assert "r=\\frac{m+p}{2}" in theorem
    assert "halved exactly" in theorem
    assert "countervailing buffer" in theorem

    result = json.loads((root / "artifacts" / "pathway_edge_decomposition" / "locked_result.json").read_text())
    edge = result["edge_deletions"]["allele_linked_recruitment"]
    assert edge["decision"] == "resolved_countervailing_buffer"
    assert edge["generation_20"]["DID_ci95"][1] < 0.0
    assert edge["generation_40"]["DID_ci95"][1] < 0.0
