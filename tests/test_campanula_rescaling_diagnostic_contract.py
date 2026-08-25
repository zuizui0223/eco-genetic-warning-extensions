from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = (ROOT / "manuscript" / "empirical_campanula_rescaling_diagnostic_preregistration.md").read_text(encoding="utf-8")
SCRIPT = (ROOT / "scripts" / "run_campanula_rescaling_diagnostic.py").read_text(encoding="utf-8")

PAIRS = (
    ("Bumble Female Rate", "Bumble Grains Dep Per Hour"),
    ("Megachile Female Rate", "Mega Grains Dep Per Hour"),
    ("Small Female Rate", "Small Grains Dep Per Hour"),
    ("Bumble Male Rate", "Bumble Grains Rem Per Hour"),
    ("Megachile Male Rate", "Mega Grains Rem Per Hour"),
    ("Small Male Rate", "Small Grains Rem Per Hour"),
)


def test_diagnostic_is_predictor_only() -> None:
    assert "Pollen Limitation 2016" in DOC
    assert "must not read" in DOC
    assert "Pollen Limitation 2016" not in SCRIPT
    assert "response_firewall" in SCRIPT


def test_source_is_locked_to_pr114_snapshot() -> None:
    for token in (
        "10.5061/dryad.5nj81nf",
        "4969330",
        "2d26307743e8a22384781854b8f2f33b",
        "b81b77248b75330049e1ddd8ae026db127f838e979620a0415a5addb9a7e8f27",
        "PopVis Rates_ PL_Depletion",
    ):
        assert token in DOC
        assert token in SCRIPT
    assert "EXPECTED_ROWS = 23" in SCRIPT


def test_six_pairs_are_fixed() -> None:
    for phase, effective in PAIRS:
        assert phase in DOC and effective in DOC
        assert phase in SCRIPT and effective in SCRIPT
    assert "No pair may be added" in DOC


def test_fixed_tolerance_and_decisions() -> None:
    assert "1e-10" in DOC
    assert "TOL = 1e-10" in SCRIPT
    for decision in (
        "constant_rescaling_confirmed",
        "not_constant_rescaling",
        "not_identifiable",
    ):
        assert decision in DOC
        assert decision in SCRIPT


def test_outcome_rescue_is_prohibited() -> None:
    assert "cannot change the #114 decision" in DOC
    assert "Do not inspect `Pollen Limitation 2016`" in DOC
    assert "construct summed fluxes" in DOC
    assert "change scaling" in DOC
