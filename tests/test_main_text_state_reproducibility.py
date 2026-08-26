from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEXT = (ROOT / "manuscript" / "main_text.md").read_text(encoding="utf-8")


def test_main_text_contains_full_denominator_warning_correction() -> None:
    assert "all 35 event trajectories crossed before loss" in TEXT
    assert "all 33 event trajectories crossed before loss" in TEXT
    assert "all 48 non-event trajectories" in TEXT
    assert "all 49 non-event trajectories" in TEXT
    assert "strict_replication" in TEXT
    assert "specificity was 0" in TEXT
    assert "binary-marker AUC was 0.5" in TEXT
    assert "not validated predictive early warning" in TEXT


def test_main_text_contains_direct_natural_residual_origin_results() -> None:
    assert "+4.08%" in TEXT
    assert "3/8" in TEXT
    assert "0/6" in TEXT
    assert "no_detected_residual_urban_information" in TEXT
    assert "ecological partial-state tests" in TEXT


def test_main_text_retains_representation_boundary_without_overclaim() -> None:
    assert "0.2543" in TEXT
    assert "McNemar `p=.143`" in TEXT
    assert "representation boundary" in TEXT
    assert "not a detected directional long-term loss-incidence effect" in TEXT


def test_main_text_keeps_cross_system_claim_conditional() -> None:
    assert "different fragmentation routes belong to the same operational functional-fragmentation regime only if" in TEXT
    assert "A residual origin effect is evidence to search for a missing process" in TEXT
    assert "absence of residual context does not prove state completeness" in TEXT
