from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "manuscript" / "empirical_cross_origin_minimal_bridge_metadata_gate_result.md"
PREREG = ROOT / "manuscript" / "empirical_cross_origin_minimal_bridge_preregistration.md"


def test_metadata_gate_closes_locked_four_archive_origin_contrast_without_outcomes() -> None:
    text = RESULT.read_text(encoding="utf-8")
    assert "minimal_bridge_origin_replication_not_met_from_locked_archives" in text
    assert "I2_hawaii2019" in text
    assert "minimal_bridge_not_identifiable_from_archive" in text
    assert "n_island_eligible <= 1 < 2" in text
    assert "No candidate reproductive outcome values were opened" in text


def test_locked_candidates_are_not_replaced_after_metadata_failure() -> None:
    text = RESULT.read_text(encoding="utf-8")
    assert "No fifth archive is added" in text
    assert "No archive is substituted after this result" in text


def test_preregistered_stage_a_allows_metadata_failure_and_requires_reproduction() -> None:
    prereg = PREREG.read_text(encoding="utf-8")
    assert "explicit metadata/README definitions" in prereg
    assert "a realised reproductive endpoint from the same ecological unit or a defensible joinable unit" in prereg
    assert "minimal_bridge_not_identifiable_from_archive" in prereg
    assert "at least two island and two urban systems" in prereg
