from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = (ROOT / "manuscript" / "empirical_eschscholzia_joint_state_preregistration.md").read_text(encoding="utf-8")
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


def test_discovery_decisions_and_second_preregistration_are_fixed() -> None:
    for decision in (
        "joint_state_identifiable",
        "partial_joint_state_identifiable",
        "not_identifiable_from_archive",
    ):
        assert decision in DOC
    assert "exact second preregistration" in DOC
    assert "before any outcome row is inspected" in DOC


def test_primary_question_preserves_endpoint_specific_sufficiency() -> None:
    assert "does floral habitat context become redundant" in DOC
    assert "reproductive assurance and mating connectivity retain distinct state information" in DOC
    assert "does not assume that one sufficient state exists for every downstream process" in DOC
