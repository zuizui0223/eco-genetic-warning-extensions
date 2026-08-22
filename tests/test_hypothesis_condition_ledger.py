from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _ledger() -> str:
    return (ROOT / "manuscript/hypothesis_condition_ledger.md").read_text(encoding="utf-8")


def test_condition_ledger_records_recovered_hierarchy_and_precision_boundaries() -> None:
    text = _ledger()
    lower = text.lower()
    for token in ("C0", "C1", "C2", "C3", "C4"):
        assert token in text
    assert "2,269/3,375" in text
    assert "322" in text and "242" in text and "84" in text
    assert "15/15" in text and "no_domain_selected" in text
    assert "asymmetric incidence frontier" in lower
    assert "0.0205" in text
    assert "high-precision negative result" in lower
    assert "3.0" in text and "4.5" in text and "6.0" in text


def test_opening_rule_is_frozen_before_warning_is_read() -> None:
    text = _ledger().lower()
    assert "no warning/diversity-informed event-regime selection" in text
    assert "no finer `p_star`, migration or kappa tuning merely to create/widen r4" in text
    assert "proof of possibility" in text
    assert "warning" in text


def test_failed_generality_is_closed_as_a_boundary_not_retuned() -> None:
    text = _ledger().lower()
    assert "record a failed generality as a boundary rather than continuing until the hypothesis appears true" in text
    assert "the kappa axis is closed" in text
    assert "not partner richness" in text
    assert "network dimensionality" in text
