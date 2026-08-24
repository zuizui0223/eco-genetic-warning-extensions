from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEXT = (ROOT / "manuscript" / "empirical_condition_map.md").read_text(encoding="utf-8")


def test_condition_map_contains_contrasting_real_mechanisms() -> None:
    for phrase in (
        "Density–interaction limitation",
        "Functional-partner / trait-matching limitation",
        "Movement-mediated compensation",
        "Focal-function-specific urban filtering",
        "Crepis sancta",
        "Camellia japonica",
        "Honshu–Izu",
        "Zurich",
    ):
        assert phrase in TEXT


def test_coarse_habitat_descriptors_are_explicitly_rejected() -> None:
    for phrase in (
        "geometry alone",
        "local interaction/resource density alone",
        "species richness alone",
        "urban/island label alone",
        "one connectivity scalar",
        "neutral genetic diversity alone",
    ):
        assert phrase in TEXT


def test_empirical_state_includes_compensation_and_alignment() -> None:
    assert "S_emp(t)" in TEXT
    for token in ("C_partner", "C_pollen", "joint spatial alignment", "F_baseline", "ecological memory"):
        assert token in TEXT
    assert "reduce** this state only after predictive sufficiency is demonstrated" in TEXT


def test_candidate_patterns_are_not_promoted_to_universal_classes() -> None:
    assert "search templates, not universal biological classes" in TEXT
    assert "become regimes only if they predict future functional trajectories" in TEXT


def test_empirical_convergence_is_residual_origin_test() -> None:
    assert "future functional trajectory ⟂ fragmentation origin/history" in TEXT
    assert "A residual origin/history effect identifies a missing state coordinate" in TEXT
    assert "residual-origin analysis" in TEXT
