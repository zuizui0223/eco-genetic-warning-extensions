from eco_genetic_warning_extensions.mutation_scaling_regimes import (
    discrete_fixed_range_coefficients,
    fixed_range_moment_limit,
    nonlocal_uniform_generator_value,
)


def test_fixed_physical_range_coefficients_converge_to_nonzero_second_and_fourth_moments():
    mu, rho, dt = 0.2, 0.3, 0.5
    limit = fixed_range_moment_limit(
        mutation_rate=mu,
        physical_radius=rho,
        time_step=dt,
    )
    coarse = discrete_fixed_range_coefficients(
        mutation_rate=mu,
        physical_radius=rho,
        radius_bins=20,
        time_step=dt,
    )
    fine = discrete_fixed_range_coefficients(
        mutation_rate=mu,
        physical_radius=rho,
        radius_bins=200,
        time_step=dt,
    )
    assert abs(fine.diffusion_coefficient - limit.limiting_diffusion_coefficient) < abs(
        coarse.diffusion_coefficient - limit.limiting_diffusion_coefficient
    )
    assert abs(fine.fourth_derivative_coefficient - limit.limiting_fourth_derivative_coefficient) < abs(
        coarse.fourth_derivative_coefficient - limit.limiting_fourth_derivative_coefficient
    )
    assert limit.limiting_fourth_derivative_coefficient > 0.0
    assert abs(limit.fourth_to_second_scale_ratio - rho * rho / 20.0) < 1e-15


def test_fixed_range_refinement_does_not_make_fourth_order_coefficient_vanish():
    mu, rho, dt = 0.25, 0.2, 1.0
    c50 = discrete_fixed_range_coefficients(
        mutation_rate=mu,
        physical_radius=rho,
        radius_bins=50,
        time_step=dt,
    )
    c500 = discrete_fixed_range_coefficients(
        mutation_rate=mu,
        physical_radius=rho,
        radius_bins=500,
        time_step=dt,
    )
    limit = fixed_range_moment_limit(
        mutation_rate=mu,
        physical_radius=rho,
        time_step=dt,
    )
    assert c500.fourth_derivative_coefficient > 0.9 * limit.limiting_fourth_derivative_coefficient
    assert c500.fourth_derivative_coefficient > 0.5 * c50.fourth_derivative_coefficient


def test_nonlocal_generator_uses_neighbourhood_average_not_only_local_curvature():
    value = nonlocal_uniform_generator_value(
        local_value=0.8,
        neighbourhood_average=0.5,
        mutation_rate=0.2,
        time_step=0.5,
    )
    assert abs(value + 0.12) < 1e-15
