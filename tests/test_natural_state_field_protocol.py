from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEXT = (ROOT / "manuscript" / "natural_state_field_protocol.md").read_text(encoding="utf-8")


def test_protocol_uses_synchronized_site_year_cohort_units() -> None:
    assert "population/site × observation window × cohort" in TEXT
    assert "same ecological unit" in TEXT
    assert "Do not merge measurements from different years or cohorts" in TEXT


def test_protocol_measures_full_natural_search_basis() -> None:
    for token in (
        "### `D`",
        "### `I`",
        "### `T`",
        "### `C`",
        "### `R`",
        "### `G_by_cohort`",
        "### `M`",
        "### `A`",
    ):
        assert token in TEXT
    assert "C_pollen" in TEXT
    assert "C_seed" in TEXT
    assert "C_partner" in TEXT


def test_protocol_recognises_process_states_not_threshold_classes() -> None:
    for label in ("U-LIM", "I-COMP", "U-LAG", "T-JOINT", "T-MATCH"):
        assert label in TEXT
    assert "Do not classify U-LIM from low density alone" in TEXT
    assert "Do not infer compensation merely from stable `F`" in TEXT
    assert "High adult diversity alone does not establish lag" in TEXT


def test_protocol_uses_residual_origin_predictive_test() -> None:
    assert "future functional trajectory ⟂ fragmentation origin/history" in TEXT
    assert "Model S0" in TEXT
    assert "Model S1" in TEXT
    assert "Model S2" in TEXT
    assert "held-out prediction/calibration" in TEXT
    assert "measured_state_convergence_supported" in TEXT
    assert "measured_state_incomplete" in TEXT
    assert "not_identifiable_with_current_measurements" in TEXT


def test_warning_is_downstream_of_empirical_state() -> None:
    assert "Only after the loss-generating state has been defined" in TEXT
    assert "replicate inside the same state before asking portability across states" in TEXT
    assert "not automatically portable" in TEXT


def test_no_universal_anchor_cutoffs() -> None:
    assert "Do not create universal field thresholds" in TEXT
    assert "process configurations and predictive sufficiency" in TEXT
