from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = (ROOT / "manuscript" / "empirical_miconia_joint_state_preregistration.md").read_text(encoding="utf-8")
SCRIPT = (ROOT / "scripts" / "fetch_miconia_joint_state_schema.py").read_text(encoding="utf-8")
WORKFLOW = (ROOT / ".github" / "workflows" / "miconia-joint-state-discovery.yml").read_text(encoding="utf-8")


def test_source_and_file_ids_are_fixed() -> None:
    assert "10.5061/dryad.1cm80" in DOC
    assert "10.1073/pnas.1619271114" in DOC
    for file_id in (30526, 30527, 30528, 30529):
        assert str(file_id) in DOC
        assert str(file_id) in SCRIPT


def test_discovery_is_schema_only() -> None:
    for phrase in (
        "schema-only discovery",
        "column names",
        "must not report outcome means",
        "No ecological conclusion is permitted",
    ):
        assert phrase in DOC
    assert "No data-cell values" in SCRIPT
    assert "Upload schema manifest only" in WORKFLOW


def test_joint_state_target_and_outcomes_are_predeclared() -> None:
    for token in ("I/T", "F_seed", "C_pollen", "G_parentage"):
        assert token in DOC
    assert "Does the measured pollinator state provide a sufficient natural representation" in DOC
    for decision in (
        "joint_state_identifiable",
        "partial_joint_state_identifiable",
        "not_identifiable_from_archive",
    ):
        assert decision in DOC


def test_second_preregistration_required_before_outcome_analysis() -> None:
    assert "Any exact model sequence must be committed in a second preregistration" in DOC
    assert "before outcome analysis" in DOC
