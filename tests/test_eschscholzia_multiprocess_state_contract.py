import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = (ROOT / "manuscript" / "empirical_eschscholzia_multiprocess_test_preregistration.md").read_text(encoding="utf-8")
CORRECTION = (ROOT / "manuscript" / "empirical_eschscholzia_source_lock_correction.md").read_text(encoding="utf-8")
RESULT_DOC = (ROOT / "manuscript" / "empirical_eschscholzia_multiprocess_result.md").read_text(encoding="utf-8")
LOCKED_RESULT = json.loads((ROOT / "artifacts" / "empirical" / "eschscholzia_multiprocess_state_locked_result.json").read_text(encoding="utf-8"))
SCRIPT = (ROOT / "scripts" / "run_eschscholzia_multiprocess_state_test.py").read_text(encoding="utf-8")
ADAPTER = (ROOT / "scripts" / "run_eschscholzia_multiprocess_state_test_locked_source.py").read_text(encoding="utf-8")
WORKFLOW = (ROOT / ".github" / "workflows" / "eschscholzia-multiprocess-state.yml").read_text(encoding="utf-8")


def test_second_preregistration_precedes_outcome_analysis() -> None:
    assert "second exact-model preregistration" in DOC
    assert "No data row" in DOC
    assert "No data row" in DOC.split("## Scientific question")[0]
    assert "before any outcome row was opened" in CORRECTION


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


def test_source_identity_is_csv_member_locked_after_transport_correction() -> None:
    for sha in (
        "db063840850fb4f358db7e99271feb9b9a92f6701b889d1b59a1348ffada89ef",
        "83ab56cc8b3e4b2ae2b7141e55683b1cff2734006d4fa4f6735605d3a2be379f",
        "ad52e8b52885cde66a0ed5476bffb0e9894b4d0429e42d927ea72b388b3ea27b",
        "6805ceb4164fefa373ba758a0fcf0a58fe67624b432d3aea6d344d690efd71f2",
    ):
        assert sha in SCRIPT
        assert sha in CORRECTION
    assert "outer ZIP SHA" in CORRECTION
    assert "not** an identity criterion" in CORRECTION
    assert "base._download_source = _download_source_member_locked" in ADAPTER
    assert "No model, endpoint, key, seed, validation unit or" in ADAPTER
    assert "sys.modules[spec.name] = base" in ADAPTER


def test_locked_result_preserves_preregistered_nonidentifiability() -> None:
    assert LOCKED_RESULT["decision"] == "multi_endpoint_not_identifiable"
    assert LOCKED_RESULT["F_seed"]["decision"] == "not_identifiable_for_endpoint"
    assert "Fallow graound vs Fallow ground" in LOCKED_RESULT["F_seed"]["reason"]
    assert "not repaired" in RESULT_DOC
    assert LOCKED_RESULT["G_mating"]["decision"] == "process_state_not_predictively_supported"
    assert LOCKED_RESULT["C_pollen"]["decision"] == "process_state_not_predictively_supported"
    assert LOCKED_RESULT["R_state"]["G_extension"]["semantic_decision"] == "no_detected_R_gain"
    assert LOCKED_RESULT["result_generating_provenance"]["workflow_run"] == 32801092027
    assert LOCKED_RESULT["result_generating_provenance"]["artifact_id"] == 9546498746


def test_result_keeps_measurement_boundary_not_ecological_null() -> None:
    assert "measurement boundary" in RESULT_DOC
    assert "availability proxy" in RESULT_DOC
    assert "It is not interpreted as biological irrelevance of habitat" in RESULT_DOC
    assert "Do not claim" in RESULT_DOC


def test_workflow_is_frozen_after_locked_result() -> None:
    assert "workflow_dispatch:" in WORKFLOW
    assert "pull_request:" not in WORKFLOW
    assert "Upload derived result only" in WORKFLOW
