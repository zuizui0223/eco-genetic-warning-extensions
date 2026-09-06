from __future__ import annotations

import math
from pathlib import Path
from statistics import fmean

import pytest

from eco_genetic_warning_extensions.allele_sorting_single_edge_proof import (
    _proof_seed,
    load_protocol,
    selected_frequency,
    selected_frequency_q_derivative,
)
from eco_genetic_warning_extensions.pathway_edge_decomposition import _seed as pathway_seed


def test_protocol_is_fixed_precision_followup() -> None:
    protocol = load_protocol()
    assert protocol["experiment_id"] == "allele_sorting_single_edge_proof_v1"
    assert protocol["status"] == "prospective_locked_before_run"
    assert tuple(protocol["conditions"]) == (
        "baseline_local_allele_selection",
        "delete_local_allele_selection",
    )
    assert protocol["primary_endpoint"]["primary_horizon"] == 40
    assert protocol["replication"]["pairs_per_condition"] == 6000
    assert protocol["replication"]["replicates_per_seed"] == 500
    assert len(protocol["replication"]["master_seeds"]) == 12
    assert "Do not add seeds" in protocol["stop_rule"]


def test_new_master_seeds_do_not_reuse_previous_pathway_seeds() -> None:
    protocol = load_protocol()
    previous = {310031, 420041, 530053, 640063, 750077}
    current = set(int(x) for x in protocol["replication"]["master_seeds"])
    assert len(current) == 12
    assert current.isdisjoint(previous)


def test_only_local_allele_selection_edge_differs() -> None:
    protocol = load_protocol()
    baseline = dict(protocol["conditions"]["baseline_local_allele_selection"])
    deletion = dict(protocol["conditions"]["delete_local_allele_selection"])
    assert baseline.pop("allele_selection_mode") == "local_q"
    assert deletion.pop("allele_selection_mode") == "spatial_mean_q"
    assert baseline == deletion


def test_common_random_number_seed_matches_audited_helper() -> None:
    for master_seed in (860089, 2070259):
        for replicate in (0, 17, 499):
            assert _proof_seed(master_seed, replicate) == pathway_seed(master_seed, replicate, 0)


def test_operator_formula_has_exact_switch_and_strict_q_monotonicity() -> None:
    for p in (0.1, 0.2, 0.5, 0.8, 0.9):
        assert selected_frequency(p, 0.2) < p
        assert math.isclose(selected_frequency(p, 0.625), p, rel_tol=0.0, abs_tol=1e-12)
        assert selected_frequency(p, 0.9) > p
        for q in (0.0, 0.2, 0.625, 0.9, 1.0):
            assert selected_frequency_q_derivative(p, q) > 0.0


def test_one_selection_step_strictly_increases_q_logit_p_covariance() -> None:
    q = (0.55, 0.65, 0.75, 0.90)
    p = (0.70, 0.45, 0.30, 0.20)

    def logit(x: float) -> float:
        return math.log(x / (1.0 - x))

    def cov(x, y) -> float:
        mx, my = fmean(x), fmean(y)
        return fmean((a - mx) * (b - my) for a, b in zip(x, y))

    before = cov(q, tuple(logit(x) for x in p))
    after_p = tuple(selected_frequency(pi, qi) for pi, qi in zip(p, q))
    after = cov(q, tuple(logit(x) for x in after_p))
    increment = after - before

    g = tuple(math.log(0.75 + 0.4 * qi) for qi in q)
    exact_increment = cov(q, g)
    assert exact_increment > 0.0
    assert math.isclose(increment, exact_increment, rel_tol=0.0, abs_tol=1e-12)


def test_theorem_document_is_present() -> None:
    path = Path(__file__).resolve().parents[1] / "docs" / "ALLELE_SORTING_OPERATOR_THEOREM_2026-09-06.md"
    text = path.read_text(encoding="utf-8")
    assert "logit}(p^+)" in text
    assert "q=0.625" in text
    assert "Cov}(q,\\operatorname{logit}p^+)" in text
    assert "does **not** prove" in text


def test_locked_result_is_materialized_and_resolved() -> None:
    path = Path(__file__).resolve().parents[1] / "artifacts" / "allele_sorting_single_edge" / "locked_result.json"
    import json

    payload = json.loads(path.read_text(encoding="utf-8"))
    assert payload["source"]["workflow_run"] == 34016797940
    assert payload["source"]["artifact_id"] == 9984306657
    primary = payload["primary_generation_40_DID"]
    assert primary["n_paired_keys"] == 6000
    assert primary["decision"] == "resolved_positive_sorting_contribution"
    assert primary["paired_ci95"][0] > 0.0


def test_parent_certificate_matches_pinned_equations_when_parent_installed() -> None:
    pytest.importorskip("causal_model.multipatch_criticality_dynamics")
    from eco_genetic_warning_extensions.allele_sorting_single_edge_proof import operator_certificate

    certificate = operator_certificate(load_protocol())
    assert math.isclose(certificate["fitness_intercept"], 0.5, abs_tol=1e-12)
    assert math.isclose(certificate["fitness_slope"], 0.8, abs_tol=1e-12)
    assert math.isclose(certificate["allele_multiplier_intercept"], 0.75, abs_tol=1e-12)
    assert math.isclose(certificate["allele_multiplier_slope"], 0.4, abs_tol=1e-12)
    assert math.isclose(certificate["q_switch"], 0.625, abs_tol=1e-12)
