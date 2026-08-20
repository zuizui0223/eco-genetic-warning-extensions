import pytest

from eco_genetic_warning_extensions.mutation_coordinates import (
    MutationCoordinates,
    PRIMARY_KAPPA_MU,
    PRIMARY_P_STAR,
    alpha_gamma_diversity,
    heterozygosity,
    primary_phase_grid,
)


def test_directional_rate_round_trip() -> None:
    coordinate = MutationCoordinates(kappa_mu=0.20, p_star=0.75)
    recovered = MutationCoordinates.from_directional_rates(
        low_to_high=coordinate.low_to_high,
        high_to_low=coordinate.high_to_low,
    )
    assert recovered.kappa_mu == pytest.approx(0.20)
    assert recovered.p_star == pytest.approx(0.75)


def test_symmetric_coordinate_recovers_symmetric_operator() -> None:
    coordinate = MutationCoordinates(kappa_mu=0.20, p_star=0.50)
    assert coordinate.is_symmetric
    assert coordinate.low_to_high == pytest.approx(0.10)
    assert coordinate.high_to_low == pytest.approx(0.10)
    assert coordinate.apply(0.40) == pytest.approx(0.10 + 0.80 * 0.40)


def test_fixed_kappa_has_fixed_contraction_but_directional_flux_varies() -> None:
    upward = MutationCoordinates(kappa_mu=0.20, p_star=0.75)
    downward = MutationCoordinates(kappa_mu=0.20, p_star=0.25)
    assert upward.contraction_factor == pytest.approx(downward.contraction_factor)
    assert upward.expected_flux(0.0) == pytest.approx(0.15)
    assert downward.expected_flux(0.0) == pytest.approx(0.05)
    assert upward.expected_flux(0.5) == pytest.approx(0.10)
    assert downward.expected_flux(0.5) == pytest.approx(0.10)


def test_local_pre_mutation_threshold_follows_declared_algebra() -> None:
    coordinate = MutationCoordinates(kappa_mu=0.20, p_star=0.75)
    threshold = coordinate.pre_mutation_threshold(0.50)
    assert threshold == pytest.approx((0.50 - 0.20 * 0.75) / 0.80)
    assert coordinate.apply(threshold) == pytest.approx(0.50)


def test_pre_mutation_threshold_decreases_with_pstar() -> None:
    coordinate = MutationCoordinates(kappa_mu=0.20, p_star=0.75)
    assert coordinate.pre_mutation_threshold_pstar_derivative() == pytest.approx(-0.25)
    eps = 1e-6
    low = MutationCoordinates(kappa_mu=0.20, p_star=0.75 - eps)
    high = MutationCoordinates(kappa_mu=0.20, p_star=0.75 + eps)
    numerical = (high.pre_mutation_threshold(0.70) - low.pre_mutation_threshold(0.70)) / (2.0 * eps)
    assert numerical == pytest.approx(coordinate.pre_mutation_threshold_pstar_derivative(), rel=1e-7)


def test_support_margin_always_increases_with_pstar() -> None:
    coordinate = MutationCoordinates(kappa_mu=0.20, p_star=0.90)
    assert coordinate.high_state_support_margin_pstar_derivative() == pytest.approx(0.20)
    eps = 1e-6
    low = MutationCoordinates(kappa_mu=0.20, p_star=0.90 - eps)
    high = MutationCoordinates(kappa_mu=0.20, p_star=0.90 + eps)
    numerical = (
        high.high_state_support_margin(0.80, 0.70)
        - low.high_state_support_margin(0.80, 0.70)
    ) / (2.0 * eps)
    assert numerical == pytest.approx(0.20, rel=1e-7)


def test_heterozygosity_change_matches_direct_evaluation() -> None:
    coordinate = MutationCoordinates(kappa_mu=0.20, p_star=0.80)
    p = 0.20
    direct = heterozygosity(coordinate.apply(p)) - heterozygosity(p)
    assert coordinate.heterozygosity_change(p) == pytest.approx(direct)


def test_transition_toward_half_increases_heterozygosity() -> None:
    low_state_upward = MutationCoordinates(kappa_mu=0.20, p_star=0.80)
    high_state_downward = MutationCoordinates(kappa_mu=0.20, p_star=0.20)
    assert low_state_upward.heterozygosity_change(0.20) > 0.0
    assert high_state_downward.heterozygosity_change(0.80) > 0.0


def test_transition_away_from_half_decreases_heterozygosity() -> None:
    low_state_downward = MutationCoordinates(kappa_mu=0.20, p_star=0.00)
    high_state_upward = MutationCoordinates(kappa_mu=0.20, p_star=1.00)
    assert low_state_downward.heterozygosity_change(0.20) < 0.0
    assert high_state_upward.heterozygosity_change(0.80) < 0.0


def test_pstar_effect_has_no_universal_sign_across_states() -> None:
    coordinate = MutationCoordinates(kappa_mu=0.20, p_star=0.50)
    assert coordinate.heterozygosity_pstar_derivative(0.20) > 0.0
    assert coordinate.heterozygosity_pstar_derivative(0.80) < 0.0


def test_pstar_derivative_changes_sign_at_post_transition_half() -> None:
    coordinate = MutationCoordinates(kappa_mu=0.20, p_star=0.50)
    assert coordinate.apply(0.50) == pytest.approx(0.50)
    assert coordinate.heterozygosity_pstar_derivative(0.50) == pytest.approx(0.0)


def test_high_frequency_state_has_support_diversity_opposition() -> None:
    coordinate = MutationCoordinates(kappa_mu=0.20, p_star=0.90)
    assert coordinate.apply(0.80) > 0.50
    assert coordinate.high_state_support_margin_pstar_derivative() > 0.0
    assert coordinate.heterozygosity_pstar_derivative(0.80) < 0.0
    assert coordinate.function_diversity_direction_relation(0.80, 0.70) == "opposed"


def test_low_frequency_state_has_aligned_support_diversity_direction() -> None:
    coordinate = MutationCoordinates(kappa_mu=0.20, p_star=0.60)
    assert coordinate.apply(0.20) < 0.50
    assert coordinate.high_state_support_margin_pstar_derivative() > 0.0
    assert coordinate.heterozygosity_pstar_derivative(0.20) > 0.0
    assert coordinate.function_diversity_direction_relation(0.20, 0.30) == "aligned"


def test_half_frequency_state_changes_support_without_first_order_diversity_change() -> None:
    coordinate = MutationCoordinates(kappa_mu=0.20, p_star=0.50)
    assert coordinate.apply(0.50) == pytest.approx(0.50)
    assert coordinate.high_state_support_margin_pstar_derivative() > 0.0
    assert coordinate.heterozygosity_pstar_derivative(0.50) == pytest.approx(0.0)
    assert coordinate.function_diversity_direction_relation(0.50, 0.50) == "support_only"


def test_alpha_gamma_gap_contracts_independently_of_direction() -> None:
    frequencies = (0.10, 0.80, 0.55)
    weights = (2.0, 3.0, 5.0)
    before_alpha, before_gamma = alpha_gamma_diversity(frequencies, weights)
    gaps = []
    for p_star in (0.10, 0.50, 0.90):
        coordinate = MutationCoordinates(kappa_mu=0.20, p_star=p_star)
        after_alpha, after_gamma = coordinate.diversity_after_transition(frequencies, weights)
        expected_gap = coordinate.contraction_factor**2 * (before_gamma - before_alpha)
        assert after_gamma - after_alpha == pytest.approx(expected_gap)
        assert coordinate.expected_alpha_gamma_gap_after_transition(frequencies, weights) == pytest.approx(expected_gap)
        gaps.append(after_gamma - after_alpha)
    assert gaps[0] == pytest.approx(gaps[1])
    assert gaps[1] == pytest.approx(gaps[2])


def test_alpha_and_gamma_have_same_directional_derivative_at_fixed_weights() -> None:
    frequencies = (0.15, 0.45, 0.85)
    weights = (1.0, 2.0, 1.0)
    coordinate = MutationCoordinates(kappa_mu=0.20, p_star=0.55)
    eps = 1e-6
    low = MutationCoordinates(kappa_mu=coordinate.kappa_mu, p_star=coordinate.p_star - eps)
    high = MutationCoordinates(kappa_mu=coordinate.kappa_mu, p_star=coordinate.p_star + eps)
    low_alpha, low_gamma = low.diversity_after_transition(frequencies, weights)
    high_alpha, high_gamma = high.diversity_after_transition(frequencies, weights)
    numerical_alpha = (high_alpha - low_alpha) / (2.0 * eps)
    numerical_gamma = (high_gamma - low_gamma) / (2.0 * eps)
    exact = coordinate.diversity_pstar_derivative(frequencies, weights)
    assert numerical_alpha == pytest.approx(exact, rel=1e-6, abs=1e-8)
    assert numerical_gamma == pytest.approx(exact, rel=1e-6, abs=1e-8)


def test_primary_grid_is_complete_and_admissible() -> None:
    grid = primary_phase_grid()
    assert len(grid) == len(PRIMARY_KAPPA_MU) * len(PRIMARY_P_STAR) == 15
    assert {(point.kappa_mu, point.p_star) for point in grid} == {
        (kappa_mu, p_star) for kappa_mu in PRIMARY_KAPPA_MU for p_star in PRIMARY_P_STAR
    }
    assert all(0.0 <= point.low_to_high <= 1.0 for point in grid)
    assert all(0.0 <= point.high_to_low <= 1.0 for point in grid)


def test_identity_operator_is_not_an_identifiable_phase_coordinate() -> None:
    with pytest.raises(ValueError, match="kappa_mu"):
        MutationCoordinates(kappa_mu=0.0, p_star=0.5)
    with pytest.raises(ValueError, match="identifiable"):
        MutationCoordinates.from_directional_rates(low_to_high=0.0, high_to_low=0.0)


def test_threshold_derivative_is_undefined_at_full_contraction() -> None:
    coordinate = MutationCoordinates(kappa_mu=1.0, p_star=0.5)
    with pytest.raises(ValueError, match="undefined"):
        coordinate.pre_mutation_threshold_pstar_derivative()
