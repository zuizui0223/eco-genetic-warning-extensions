from __future__ import annotations

import math

import pytest

from eco_genetic_warning_extensions.pathway_edge_decomposition import (
    _parameters,
    barrier_schedule,
    load_protocol,
)


def _require_parent() -> None:
    pytest.importorskip("causal_model.multipatch_criticality_dynamics")


def test_protocol_is_locked_and_finite() -> None:
    p = load_protocol()
    assert p["experiment_id"] == "pathway_edge_decomposition_v1"
    assert p["status"] == "prospective_locked_before_run"
    assert len(p["interventions"]) == 8
    assert p["replication"]["pairs_per_intervention"] == 1500
    assert p["forcing"]["report_horizons"] == [1, 5, 10, 20, 40]
    assert "No additional edge deletions" in p["stop_rule"]


def test_all_interventions_keep_direct_tg_to_q_deleted() -> None:
    _require_parent()
    p = load_protocol()
    for name, intervention in p["interventions"].items():
        params = _parameters(p, intervention, "AA", seed=1, generations=40)
        assert params.q_feedback_alpha == 1.0, name
        assert params.q_feedback_beta_trait == 0.0, name
        assert params.q_feedback_gamma_allele == 0.0, name
        assert params.migration_rate == 0.0, name


def test_declared_edge_deletions_map_to_expected_parameters() -> None:
    _require_parent()
    p = load_protocol()
    base = _parameters(p, p["interventions"]["baseline_indirect"], "AA", seed=1, generations=40)
    no_g = _parameters(p, p["interventions"]["delete_allele_recruitment"], "AA", seed=1, generations=40)
    no_t_memory = _parameters(p, p["interventions"]["delete_resident_inheritance"], "AA", seed=1, generations=40)
    no_demo = _parameters(p, p["interventions"]["delete_state_dependent_demography"], "AA", seed=1, generations=40)

    assert base.genotype_trait_recruitment == "two_kernel_recruitment"
    assert math.isclose(base.inheritance_weight, 0.5)
    assert no_g.genotype_trait_recruitment == "resident_trait_only"
    assert math.isclose(no_t_memory.inheritance_weight, 0.0)
    assert math.isclose(no_demo.interaction_growth, 0.0)
    assert math.isclose(no_demo.high_allele_growth, 0.0)
    assert base.interaction_growth > 0.0
    assert base.high_allele_growth > 0.0


def test_barrier_schedule_is_original_reference_path() -> None:
    b = barrier_schedule(40)
    assert len(b) == 40
    assert math.isclose(b[0], 0.50 + 0.15 / 60.0)
    assert math.isclose(b[-1], 0.50 + 0.15 * 40.0 / 60.0)


def test_baseline_q_only_generation1_is_assignment_invariant() -> None:
    _require_parent()
    from causal_model.multipatch_criticality_dynamics import sigmoid

    p = load_protocol()
    q0 = tuple(float(x) for x in p["fixed_state"]["initial_interaction"])
    barrier = barrier_schedule(40)[0]
    q1_aa = tuple(sigmoid(4.5 * (q - barrier)) for q in q0)
    q1_rr = tuple(sigmoid(4.5 * (q - barrier)) for q in q0)
    assert q1_aa == q1_rr
