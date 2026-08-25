from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = (ROOT / "manuscript" / "empirical_campanula_effective_interaction_test_preregistration.md").read_text(encoding="utf-8")
SCRIPT = (ROOT / "scripts" / "run_campanula_effective_interaction_test.py").read_text(encoding="utf-8")


def test_second_preregistration_precedes_numeric_analysis() -> None:
    assert "second exact-model preregistration" in DOC
    assert "No numeric study-cell value" in DOC.split("## Scientific question")[0]


def test_source_and_population_endpoint_are_locked() -> None:
    for token in (
        "10.5061/dryad.5nj81nf",
        "4969330",
        "2d26307743e8a22384781854b8f2f33b",
        "b81b77248b75330049e1ddd8ae026db127f838e979620a0415a5addb9a7e8f27",
        "PopVis Rates_ PL_Depletion",
        "Pollen Limitation 2016",
        "exactly 23",
    ):
        assert token in DOC
        assert token in SCRIPT or token == "exactly 23"


def test_representations_are_exactly_fixed() -> None:
    raw = ("Bumblebee Rate", "Megachile Rate", "Small Rate")
    phase = (
        "Bumble Female Rate", "Megachile Female Rate", "Small Female Rate",
        "Bumble Male Rate", "Megachile Male Rate", "Small Male Rate",
    )
    effective = (
        "Bumble Grains Dep Per Hour", "Mega Grains Dep Per Hour", "Small Grains Dep Per Hour",
        "Bumble Grains Rem Per Hour", "Mega Grains Rem Per Hour", "Small Grains Rem Per Hour",
    )
    for token in (*raw, *phase, *effective):
        assert token in DOC
        assert token in SCRIPT
    assert "The three source-defined `... Depletion` columns are not included" in DOC


def test_model_validation_and_bootstrap_are_fixed() -> None:
    assert "Ridge(alpha=1.0)" in DOC
    assert "Ridge(alpha=1.0)" in SCRIPT
    assert "leave-one-population-out" in DOC
    assert '"held_out_unit": "Population"' in SCRIPT
    assert "10,000" in DOC
    assert "RNG_SEED = 20260825" in SCRIPT
    assert "np.random.default_rng(RNG_SEED)" in SCRIPT
    assert "no hyperparameter search" in DOC


def test_primary_effective_vs_raw_contrast_and_decisions_are_fixed() -> None:
    assert "effective gain over raw" in DOC
    assert "primary contrast" in DOC
    for label in (
        "effective_interaction_supported_over_raw",
        "effective_interaction_supported_no_gain_over_raw",
        "phase_matched_visitation_supported_no_effective_support",
        "raw_visitation_supported_no_effective_support",
        "no_interaction_representation_supported",
        "not_identifiable_for_primary_endpoint",
    ):
        assert label in DOC
        assert label in SCRIPT


def test_no_outcome_informed_efficiency_or_geography_is_opened() -> None:
    assert "does **not** estimate efficiency weights from `Pollen Limitation 2016`" in DOC
    assert "Do not switch to total visitation" in DOC
    assert "latitude/longitude" in DOC
