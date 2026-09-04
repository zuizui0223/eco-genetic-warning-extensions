from pathlib import Path
import importlib.util


ROOT = Path(__file__).resolve().parents[1]


def _load_checker():
    path = ROOT / "scripts/check_ecology_letters_compliance.py"
    spec = importlib.util.spec_from_file_location("el_compliance", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_ecology_letters_compliance_gate() -> None:
    checker = _load_checker()
    assert checker.main() == 0


def test_cover_letter_centres_state_predictability_contribution() -> None:
    text = (ROOT / "manuscript/cover_letter.md").read_text(encoding="utf-8")
    assert "Matching eco-genetic summaries can hide different ecological futures" in text
    assert "0.2543" in text
    assert "+5.33" in text
    assert "+5.20" in text
    assert "forecast horizon" in text
    assert "[AUTHOR CONFIRMATION:" in text
    for forbidden in ("35/35", "48/48", "33/33", "49/49", "Honshu", "Oenothera"):
        assert forbidden not in text


def test_state_letter_allocation_has_two_figures_and_no_integrated_leakage() -> None:
    allocation = (ROOT / "manuscript/state_validity_display_allocation.md").read_text(encoding="utf-8")
    assert "exactly two figures" in allocation
    assert "### Figure 1" in allocation
    assert "### Figure 2" in allocation
    assert "### Figure 3" not in allocation
    assert "35/35" in allocation  # explicit exclusion firewall, not a state result display
    assert "Do not include" in allocation
