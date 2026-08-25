from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = (ROOT / "manuscript" / "empirical_carphephorus_effective_interaction_preregistration.md").read_text(encoding="utf-8")
SCRIPT = (ROOT / "scripts" / "fetch_carphephorus_effective_interaction_schema.py").read_text(encoding="utf-8")
WORKFLOW = (ROOT / ".github" / "workflows" / "carphephorus-effective-interaction-discovery.yml").read_text(encoding="utf-8")


def test_sources_are_locked_before_row_inspection() -> None:
    assert "10.5061/dryad.w9ghx3g48" in DOC
    assert "622e5266db24e99a983bcf89d63a2258ebf93662" in DOC
    for name in ("CARBEL-arthropods.csv", "CARBEL-floral.csv", "CARBEL-seeds.csv", "Patch_type.csv"):
        assert name in DOC
        assert name in SCRIPT


def test_realised_interaction_mapping_is_source_defined() -> None:
    assert 'visitor_type == "pollinator"' in DOC
    assert "plant_ID × sampling_round" in DOC
    assert "pollination_rate" in DOC
    assert "viable + no_predation" in DOC
    assert "joins that realised visitation to the seed table by `plant_ID`" in DOC


def test_schema_gate_cannot_read_outcomes() -> None:
    assert "Schema-only discovery boundary" in DOC
    assert "must not read data rows" in DOC
    assert "No data row" in SCRIPT
    assert "Upload schema manifest only" in WORKFLOW


def test_identifiability_decisions_are_fixed() -> None:
    for token in (
        "realised_interaction_state_identifiable",
        "partial_realised_interaction_state_identifiable",
        "not_identifiable_from_archive",
    ):
        assert token in DOC
    assert "second preregistration" in DOC
    assert "before outcome rows are read" in DOC


def test_claim_boundary_is_effective_interaction_not_universal_visitation() -> None:
    assert "realised focal-plant visitation" in DOC
    assert "would not make visitation a universally sufficient interaction state" in DOC
    assert "pollen receipt, donor identity" in DOC
