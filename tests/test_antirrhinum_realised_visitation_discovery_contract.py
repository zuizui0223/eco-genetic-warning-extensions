from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = (ROOT / "manuscript" / "empirical_antirrhinum_realised_visitation_preregistration.md").read_text(encoding="utf-8")
SCRIPT = (ROOT / "scripts" / "fetch_antirrhinum_realised_visitation_schema.py").read_text(encoding="utf-8")
WORKFLOW = (ROOT / ".github" / "workflows" / "antirrhinum-realised-visitation-discovery.yml").read_text(encoding="utf-8")


def test_wild_sources_and_md5s_are_locked() -> None:
    for token in (
        "10.15479/AT:ISTA:36",
        "10.15479/AT:ISTA:37",
        "cbc61b523d4d475a04a737d50dc470ef",
        "4ae751b1fa4897fa216241f975a57313",
    ):
        assert token in DOC
        assert token in SCRIPT


def test_controlled_array_archive_is_excluded_from_primary_bridge() -> None:
    assert "10.15479/AT:ISTA:35" in DOC
    assert "not** part of this primary discovery" in DOC
    assert "different experimental system" in DOC
    assert "2012" in DOC


def test_visitation_is_realised_proxy_not_direct_observation() -> None:
    assert "I_realised_proxy" in DOC
    assert "not direct visual observation" in DOC
    assert "tag loss" in DOC
    assert "not pollinator availability" in DOC


def test_schema_boundary_and_allowed_decisions_are_fixed() -> None:
    assert "first header row only" in DOC
    assert "No data-row value" in SCRIPT
    assert "Upload schema manifest only" in WORKFLOW
    for decision in (
        "wild_IFG_joint_state_identifiable",
        "wild_IG_partial_state_identifiable",
        "wild_state_not_identifiable",
    ):
        assert decision in DOC
    assert "second preregistration" in DOC


def test_F_can_open_only_if_explicit_in_locked_wild_archives() -> None:
    assert "only if one is explicitly present in the locked wild archives" in DOC
    assert "No new reproductive endpoint may be imported from another experiment" in DOC
