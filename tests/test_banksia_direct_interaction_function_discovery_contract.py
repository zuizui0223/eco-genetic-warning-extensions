from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = (ROOT / "manuscript" / "empirical_banksia_direct_interaction_function_preregistration.md").read_text(encoding="utf-8")
SCRIPT = (ROOT / "scripts" / "fetch_banksia_direct_interaction_function_schema.py").read_text(encoding="utf-8")
WORKFLOW = (ROOT / ".github" / "workflows" / "banksia-direct-interaction-function-discovery.yml").read_text(encoding="utf-8")


def test_source_snapshot_is_immutable() -> None:
    for token in (
        "10.1093/botlinnean/boae024",
        "stanwawrzyczek/Pollination-of-Banksia-catoglypta-Data",
        "1ab685d62d005865935435bbd49cadba50080741",
        "91cc21eb4d967b702bd18f87f91be1b52cacb6a3",
    ):
        assert token in DOC
        assert token in SCRIPT
    assert "_git_blob_sha" in SCRIPT


def test_scientific_role_is_direct_interaction_to_function_only() -> None:
    assert "I_realised" in DOC
    assert "F_reproduction" in DOC
    assert "measurement-validation system" in DOC
    assert "not a fragmentation-regime test" in DOC
    assert "does not contain a preregistered genetic/paternity endpoint" in DOC


def test_schema_gate_cannot_read_outcomes() -> None:
    assert "first header row only" in DOC
    assert "No data-row value" in SCRIPT
    assert "Upload schema manifest only" in WORKFLOW
    assert "fruit-set value" in DOC


def test_discovery_decisions_and_second_preregistration_are_fixed() -> None:
    for decision in (
        "direct_IF_joint_state_identifiable",
        "direct_IF_partial_state_identifiable",
        "direct_IF_not_identifiable",
    ):
        assert decision in DOC
    assert "second preregistration" in DOC
    assert "before any outcome row is inspected" in DOC


def test_no_posthoc_paternity_or_endpoint_search() -> None:
    assert "Do not infer paternity" in DOC
    assert "Do not choose among visitor groups" in DOC
    assert "Do not repair IDs by fuzzy matching" in DOC
