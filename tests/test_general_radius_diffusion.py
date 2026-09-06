from eco_genetic_warning_extensions.general_radius_diffusion import (
    boundary_influence_fraction,
    continuum_coefficients,
    diffusion_coefficient_general_radius,
    finite_operator_generator_residual,
    translation_invariant_interior,
    translation_invariant_interior_count,
)
from eco_genetic_warning_extensions.small_jump_trait_bins import (
    diffusion_coefficient_from_small_jump,
)


def test_general_radius_interior_stencil_is_exact_for_j1_j2_j3_when_destination_is_2j_deep():
    f = (
        0.01, 0.02, 0.03, 0.05, 0.08,
        0.11, 0.14, 0.16, 0.14, 0.10,
        0.07, 0.04, 0.025, 0.015, 0.005,
    )
    for radius in (1, 2, 3):
        assert translation_invariant_interior(7, len(f), radius)
        residual = finite_operator_generator_residual(
            f,
            index=7,
            mutation_rate=0.2,
            radius_bins=radius,
            time_step=0.5,
        )
        assert abs(residual) < 1e-12


def test_source_boundary_renormalization_extends_boundary_influence_to_2j_bins():
    assert not translation_invariant_interior(4, 15, 3)
    try:
        finite_operator_generator_residual(
            tuple(range(1, 16)),
            index=4,
            mutation_rate=0.2,
            radius_bins=3,
            time_step=0.5,
        )
    except ValueError as exc:
        assert "2*radius_bins" in str(exc)
    else:
        raise AssertionError("boundary-influenced destination should not use invariant stencil")


def test_translation_invariant_interior_count_is_n_minus_4j():
    assert translation_invariant_interior_count(15, 3) == 3
    assert translation_invariant_interior_count(13, 3) == 1
    assert translation_invariant_interior_count(12, 3) == 0
    assert abs(boundary_influence_fraction(20, 3) - 0.6) < 1e-12


def test_j1_general_formula_recovers_existing_small_jump_diffusion_coefficient():
    general = diffusion_coefficient_general_radius(
        mutation_rate=0.3,
        radius_bins=1,
        grid_spacing=0.02,
        time_step=0.1,
    )
    existing = diffusion_coefficient_from_small_jump(
        mutation_rate=0.3,
        radius_bins=1,
        grid_spacing=0.02,
        time_step=0.1,
    )
    assert abs(general - existing) < 1e-15


def test_diffusion_coefficient_matches_jump_second_moment_for_radius_three():
    mu, J, h, dt = 0.24, 3, 0.01, 0.2
    expected_mean_square_bins = sum(k * k for k in range(1, J + 1)) / J
    expected = mu * expected_mean_square_bins * h * h / (2.0 * dt)
    actual = diffusion_coefficient_general_radius(
        mutation_rate=mu,
        radius_bins=J,
        grid_spacing=h,
        time_step=dt,
    )
    assert abs(actual - expected) < 1e-15


def test_fixed_diffusion_scaling_makes_fourth_order_term_shrink_as_h_squared():
    coarse = continuum_coefficients(
        mutation_rate=0.2,
        radius_bins=2,
        grid_spacing=0.02,
        time_step=0.004,
    )
    fine = continuum_coefficients(
        mutation_rate=0.2,
        radius_bins=2,
        grid_spacing=0.01,
        time_step=0.001,
    )
    assert abs(coarse.diffusion_coefficient - fine.diffusion_coefficient) < 1e-15
    assert abs(fine.fourth_derivative_coefficient / coarse.fourth_derivative_coefficient - 0.25) < 1e-12
