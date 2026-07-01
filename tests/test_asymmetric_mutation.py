import pytest

from eco_genetic_warning_extensions.asymmetric_mutation import AsymmetricMutation, mutate_frequency
from eco_genetic_warning_extensions.protocol001 import (
    CalibrationCandidate,
    assert_blind_calibration_columns,
    select_protocol_001_domain,
)


def test_symmetric_bridge_matches_predecessor_operator() -> None:
    for p in (0.0, 0.2, 0.5, 0.9, 1.0):
        assert mutate_frequency(p, low_to_high=0.10, high_to_low=0.10) == pytest.approx(0.10 + 0.80 * p)


def test_operator_preserves_frequency_domain() -> None:
    mutation = AsymmetricMutation(low_to_high=0.05, high_to_low=0.15)
    for p in (0.0, 0.1, 0.5, 1.0):
        assert 0.0 <= mutation.apply(p) <= 1.0
    assert mutation.mutation_only_equilibrium == pytest.approx(0.25)
    assert mutation.contraction_factor == pytest.approx(0.80)


def test_invalid_rate_pair_is_rejected() -> None:
    with pytest.raises(ValueError):
        AsymmetricMutation(low_to_high=0.7, high_to_low=0.4)


def test_calibration_rejects_warning_leakage() -> None:
    with pytest.raises(ValueError, match="trait-loss-only"):
        assert_blind_calibration_columns(["panel", "h_alpha_warning_time"])


def test_selection_uses_predeclared_tie_breaks() -> None:
    long = CalibrationCandidate("SYM", 1.0, 4.5, 30, 210, 0.15, (0.5,) * 5)
    short = CalibrationCandidate("SYM", 1.0, 4.5, 30, 90, 0.15, (0.5,) * 5)
    ineligible = CalibrationCandidate("SYM", 0.8, 3.0, 30, 90, 0.15, (0.2,) * 5)
    assert select_protocol_001_domain([long, ineligible, short], panel="SYM") == short


def test_selection_returns_none_without_eligible_domain() -> None:
    candidate = CalibrationCandidate("DOWN", 0.8, 3.0, 30, 90, 0.15, (0.1,) * 5)
    assert select_protocol_001_domain([candidate], panel="DOWN") is None
