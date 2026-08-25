from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = (ROOT / "manuscript" / "empirical_eschscholzia_multiprocess_test_preregistration.md").read_text(encoding="utf-8")
SCRIPT = (ROOT / "scripts" / "run_eschscholzia_multiprocess_state_test.py").read_text(encoding="utf-8")
WORKFLOW = (ROOT / ".github" / "workflows" / "eschscholzia-multiprocess-state.yml").read_text(encoding="utf-8")


def test_second_preregistration_precedes_outcome_analysis() -> None:
    assert "second exact-model preregistration" in DOC
    assert "No data row" in DOC
    assert "No data row" in DOC.split("## Scientific question")[0]


def test_locked_hierarchy_and_held_out_unit() -> None:
    assert "Block -> Experimental array -> focal plant -> fruit/progeny" in DOC
    assert "leave-one-array-out (LOAO)" in DOC
    assert "Row-wise, progeny-wise or plant-wise cross-validation is prohibited" in DOC
    assert "held_out_unit\": \"Experimental array" in SCRIPT


def test_pollinator_state_is_fixed_and_proxy_bounded() -> None:
    assert "I_count" in DOC
    assert "T_mean_ITD" in DOC
    assert "Species richness" in DOC
    assert "not a claim that pan traps measure direct visitation to focal plants" in DOC
    assert "availability proxy" in DOC
    assert "I_log_count" in SCRIPT
    assert "T_mean_ITD" in SCRIPT


def test_primary_responses_are_fixed() -> None:
    assert "Mean_number_of_seeds_from_field_exposed_flowers" in DOC
    assert "Parentage` only" in DOC
    assert "containing `outcross`" in DOC
    assert "containing `self`" in DOC
    assert "Distance_of_pollen_movement" in DOC
    assert "Habitat_crossed" in DOC


def test_secondary_state_coordinates_are_fixed() -> None:
    assert "D_capacity" in DOC
    assert "R_auto" in DOC
    assert "Sample type" in DOC
    assert "containing `exclud`" in DOC
    assert "containing `expos`" in DOC


def test_model_sequence_and_regularization_are_fixed() -> None:
    for state in ("### S0", "### S1", "### S2"):
        assert state in DOC
    assert "Ridge(alpha=1.0" in DOC
    assert "C=1.0" in DOC
    assert "no hyperparameter search" in DOC
    assert "Ridge(alpha=1.0" in SCRIPT
    assert "C=1.0" in SCRIPT


def test_bootstrap_and_decisions_are_fixed() -> None:
    assert "10,000" in DOC
    assert "20260825" in DOC
    assert "N_BOOT = 10_000" in SCRIPT
    assert "RNG_SEED = 20260825" in SCRIPT
    for token in (
        "process_state_informative_no_detected_residual_context",
        "residual_context_detected_after_process_state",
        "process_state_not_predictively_supported",
        "multi_endpoint_partial_state_convergence_supported",
        "multi_endpoint_state_insufficiency_detected",
        "multi_endpoint_convergence_not_established",
        "multi_endpoint_not_identifiable",
    ):
        assert token in DOC
        assert token in SCRIPT


def test_source_hashes_are_hard_locked() -> None:
    for sha in (
        "66b0b9eec2ffcf6df8bc19f4677c159e5f574a4a23aa452221cc2b552b01f0c5",
        "b541f46ecee09ba7c5dbbcbe06f30f343e2620e3942289c5839f98382d089859",
        "6781fed48c9c7b8a293e713434a02769a2490d68c6f2e218167f623af1c60ec1",
        "e785a2aad2ba43ef5a5a6b90122badc2b70b1682a4ada5719e8a2ed25cddf033",
    ):
        assert sha in SCRIPT


def test_workflow_runs_only_derived_result() -> None:
    assert "Run preregistered multi-process analysis" in WORKFLOW
    assert "Upload derived result only" in WORKFLOW
    assert "eschscholzia_multiprocess_state_result.json" in WORKFLOW
