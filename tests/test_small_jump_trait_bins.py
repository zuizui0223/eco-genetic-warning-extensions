from eco_genetic_warning_extensions.small_jump_trait_bins import (
    diffusion_coefficient_from_small_jump,
    interior_jump_variance,
    local_trait_mutation,
    selection_mutation_step,
    viability_selection,
)


def test_local_mutation_conserves_mass_and_support():
    f = (0.0, 0.0, 1.0, 0.0, 0.0)
    moved = local_trait_mutation(f, mutation_rate=0.4, radius_bins=1)
    assert moved == (0.0, 0.2, 0.6, 0.2, 0.0)
    assert abs(sum(moved) - 1.0) < 1e-12


def test_zero_radius_is_identity():
    f = (0.2, 0.3, 0.5)
    assert local_trait_mutation(f, mutation_rate=1.0, radius_bins=0) == f


def test_selection_matches_multiplicative_trait_bin_update():
    f = (0.5, 0.5)
    selected = viability_selection(f, (1.0, 2.0))
    assert abs(selected[0] - 1.0 / 3.0) < 1e-12
    assert abs(selected[1] - 2.0 / 3.0) < 1e-12


def test_selection_mutation_step_is_separable():
    step = selection_mutation_step(
        (0.5, 0.5, 0.0),
        (1.0, 2.0, 1.0),
        mutation_rate=0.0,
        radius_bins=1,
    )
    assert step.after_selection == step.after_mutation


def test_interior_variance_and_diffusion_scaling():
    var = interior_jump_variance(
        mutation_rate=0.2, radius_bins=1, grid_spacing=0.01
    )
    assert abs(var - 0.00002) < 1e-15
    d = diffusion_coefficient_from_small_jump(
        mutation_rate=0.2, radius_bins=1, grid_spacing=0.01, time_step=0.5
    )
    assert abs(d - 0.00002) < 1e-15
