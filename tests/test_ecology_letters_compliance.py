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


def test_cover_letter_centres_ecological_contribution() -> None:
    text = (ROOT / "manuscript/cover_letter.md").read_text(encoding="utf-8")
    assert "eco-genetic closure" in text
    assert "functional-trait loss" in text
    assert "not an intrinsic property of the diversity statistic" in text
    assert "ecological and conceptual rather than a model sensitivity analysis" in text
    assert "[AUTHOR CONFIRMATION:" in text


def test_letter_allocation_has_six_figures_and_no_main_tables() -> None:
    allocation = (ROOT / "manuscript/main_vs_supplement.md").read_text(encoding="utf-8")
    captions = (ROOT / "manuscript/table_captions.md").read_text(encoding="utf-8")
    assert "exactly six main display items" in allocation
    assert "no main-text tables or text boxes" in allocation
    for number in range(1, 7):
        assert f"### Figure {number}" in allocation
    for number in range(1, 6):
        assert f"## Table S{number}." in captions
    assert "## Table 1." not in captions
    assert "## Table 2." not in captions
