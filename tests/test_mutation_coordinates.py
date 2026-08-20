import pytest

from eco_genetic_warning_extensions.mutation_coordinates import (
    MutationCoordinates,
    PRIMARY_KAPPA_MU,
    PRIMARY_P_STAR,
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
