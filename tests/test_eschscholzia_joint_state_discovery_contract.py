import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = (ROOT / "manuscript" / "empirical_eschscholzia_joint_state_preregistration.md").read_text(encoding="utf-8")
RESULT = (ROOT / "manuscript" / "empirical_eschscholzia_joint_state_discovery_result.md").read_text(encoding="utf-8")
LOCK = json.loads((ROOT / "artifacts" / "empirical" / "eschscholzia_joint_state_schema_locked.json").read_text(encoding="utf-8"))
SCRIPT = (ROOT / "scripts" / "fetch_eschscholzia_joint_state_schema.py").read_text(encoding="utf-8")
WORKFLOW = (ROOT / ".github" / "workflows" / "eschscholzia-joint-state-discovery.yml").read_text(encoding="utf-8")

DOIS = (
    "10.5285/01906784-6742-44bf-b244-a4b63bed8d82",
    "10.5285/8caf2d8a-564d-4f2e-a797-174165a83796",
    "10.5285/5b400b69-b828-45e8-b04e-7ccbfdb0987f",
    "10.5285/7b721c07-bc38-4815-8669-4675867663d0",
)


def test_four_source_products_are_locked_before_schema_inspection() -> None:
    for doi in DOIS:
        assert doi in DOC
        assert doi in SCRIPT
    assert "Sixteen arrays" in DOC
    assert "48 focal plants" in DOC


def test_process_layers_are_fixed() -> None:
    for token in ("I/T", "F_seed", "G_mating/C", "`R`"):
        assert token in DOC
    assert "pollinator availability/community state" in DOC
    assert "not direct visits to each focal plant" in DOC


def test_schema_gate_cannot_read_outcomes() -> None:
    assert "No data rows" in SCRIPT
    assert "header labels" in DOC
    assert "must not calculate even descriptive outcome summaries" in DOC
    assert "Upload schema manifest only" in WORKFLOW


def test_discovery_decision_is_locked_from_headers_only() -> None:
    assert LOCK["decision"] == "joint_state_identifiable"
    assert "joint_state_identifiable" in RESULT
    assert "Block + Experimental array" in RESULT
    assert "Plant identification number" in RESULT
    assert "No row values were used" in RESULT
    assert LOCK["workflow_provenance"]["run_id"] == 32736330920
    assert LOCK["workflow_provenance"]["artifact_id"] == 9523523742


def test_locked_schema_preserves_array_to_plant_hierarchy() -> None:
    by_role = {row["role"]: row for row in LOCK["datasets"]}
    assert by_role["pollinator_availability"]["hierarchy"] == ["Block", "Experimental array"]
    for role in (
        "seed_function_supplemented_exposed",
        "seed_function_exposed_excluded",
        "paternity",
    ):
        assert len(by_role[role]["hierarchy"]) == 3
    assert "array-level pollinator availability" in by_role["pollinator_availability"]["process_role"]


def test_second_preregistration_is_still_required_before_outcomes() -> None:
    assert "exact second preregistration" in DOC
    assert "before any outcome row is inspected" in DOC
    assert "second exact-model preregistration" in RESULT
    assert "leave-one-array-out" in RESULT


def test_discovery_workflow_is_frozen_manual_only() -> None:
    assert "workflow_dispatch:" in WORKFLOW
    assert "pull_request:" not in WORKFLOW


def test_primary_question_preserves_endpoint_specific_sufficiency() -> None:
    assert "does floral habitat context become redundant" in DOC
    assert "reproductive assurance and mating connectivity retain distinct state information" in DOC
    assert "does not assume that one sufficient state exists for every downstream process" in DOC
