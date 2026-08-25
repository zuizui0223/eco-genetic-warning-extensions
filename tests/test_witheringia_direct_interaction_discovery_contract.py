from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = (ROOT / "manuscript" / "empirical_witheringia_direct_interaction_preregistration.md").read_text(encoding="utf-8")
SCRIPT = (ROOT / "scripts" / "fetch_witheringia_direct_interaction_schema.py").read_text(encoding="utf-8")
WORKFLOW = (ROOT / ".github" / "workflows" / "witheringia-direct-interaction-discovery.yml").read_text(encoding="utf-8")


def test_source_and_files_are_locked() -> None:
    assert "10.5061/dryad.f8539" in DOC
    assert "10.1111/evo.12419" in DOC
    for name in ("pollinators_all.xls", "FruitSet.xlsx", "paternity.xlsx", "abortion_data_2011.xlsx"):
        assert name in DOC
        assert name in SCRIPT


def test_direct_interaction_role_and_claim_boundary_are_explicit() -> None:
    assert "single focal plants" in DOC
    assert "I_realised" in DOC
    assert "F_reproduction" in DOC
    assert "G_mating/C_pollen" in DOC
    assert "measurement-validation system" in DOC
    assert "not a fragmentation-regime test" in DOC


def test_schema_only_gate_cannot_inspect_outcomes() -> None:
    assert "first-row column labels" in DOC
    assert "No data row" in SCRIPT
    assert "Upload schema manifest only" in WORKFLOW
    assert "effect direction" in DOC


def test_identifiability_outcomes_and_second_preregistration_are_fixed() -> None:
    for decision in (
        "direct_joint_state_identifiable",
        "direct_partial_state_identifiable",
        "not_identifiable_from_archive",
    ):
        assert decision in DOC
    assert "second preregistration" in DOC
    assert "before any outcome row is read" in DOC


def test_future_question_requires_endpoint_relevant_direct_interaction() -> None:
    assert "Does direct realised focal-plant interaction provide endpoint-relevant predictive information" in DOC
    assert "common-garden identity itself as a mechanistic state" in DOC
