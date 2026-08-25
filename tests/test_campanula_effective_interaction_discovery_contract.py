from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = (ROOT / "manuscript" / "empirical_campanula_effective_interaction_preregistration.md").read_text(encoding="utf-8")
RESULT = (ROOT / "manuscript" / "empirical_campanula_effective_interaction_discovery_result.md").read_text(encoding="utf-8")
SCRIPT = (ROOT / "scripts" / "fetch_campanula_effective_interaction_schema.py").read_text(encoding="utf-8")
WORKFLOW = (ROOT / ".github" / "workflows" / "campanula-effective-interaction-discovery.yml").read_text(encoding="utf-8")


def test_source_is_locked_before_schema_inspection() -> None:
    for token in (
        "10.5061/dryad.5nj81nf",
        "4969330",
        "Koski et al. 2018_Data_ProcRoySoc.xlsx",
        "2d26307743e8a22384781854b8f2f33b",
    ):
        assert token in DOC
        assert token in SCRIPT
    assert "b81b77248b75330049e1ddd8ae026db127f838e979620a0415a5addb9a7e8f27" in RESULT


def test_effective_state_must_be_outcome_independently_calibrated() -> None:
    assert "without using population pollen-limitation outcomes" in DOC
    assert "Population pollen limitation may never be used to choose or estimate those weights" in DOC
    assert "I_effective = Σ_g visitation_g × efficiency_g" in DOC
    assert "without reference to pollen limitation" in RESULT


def test_discovery_retains_only_schema_and_text_labels() -> None:
    assert "numeric data-cell values" in DOC
    assert "must contain no numeric outcome or predictor values" in DOC
    assert "TOP_ROWS = 10" in SCRIPT
    assert "METADATA_ROWS = 100" in SCRIPT
    assert "string labels" in SCRIPT
    assert "Numeric study-cell values" in SCRIPT
    assert "No numerical visitation rate" in RESULT


def test_required_layers_and_decisions_are_fixed() -> None:
    for token in (
        "F_PL",
        "I_visit",
        "E_deposition",
        "E_seed",
        "E_removal",
        "effective_interaction_state_identifiable",
        "partial_effective_interaction_state_identifiable",
        "not_identifiable_from_archive",
    ):
        assert token in DOC
    assert "second preregistration" in DOC
    assert "before any numeric data row is read" in DOC
    assert "**`effective_interaction_state_identifiable`**" in RESULT


def test_group_mapping_and_source_defined_fluxes_are_identifiable() -> None:
    for token in (
        "`B` = bumblebee",
        "`H` = small bee (Halictidae)",
        "`M` = *Megachile campanulae*",
        "Bumblebee Grains Dep",
        "Grains Dep Per Hour",
        "Grains Rem Per Hour",
    ):
        assert token in RESULT


def test_claim_ceiling_rejects_pollinator_size_rule() -> None:
    assert "does not establish that large or small bees are beneficial" in DOC
    assert "not a universal pollinator-size rule" in DOC
    assert "does not support any statement about which pollinator group is beneficial" in RESULT


def test_discovery_workflow_is_frozen_after_result() -> None:
    assert "workflow_dispatch" in WORKFLOW
    assert "pull_request:" not in WORKFLOW
