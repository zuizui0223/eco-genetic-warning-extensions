from eco_genetic_warning_extensions.small_jump_diffusion_bridge import (
    audit_radius_one_diffusion_identity,
    diffusive_time_step,
)
from eco_genetic_warning_extensions.small_jump_trait_bins import (
    diffusion_coefficient_from_small_jump,
)


def test_diffusive_time_step_preserves_target_D_under_grid_refinement():
    for h in (0.2, 0.1, 0.05, 0.025):
        dt = diffusive_time_step(
            mutation_rate=0.2,
            grid_spacing=h,
            target_diffusion=0.4,
        )
        D = diffusion_coefficient_from_small_jump(
            mutation_rate=0.2,
            radius_bins=1,
            grid_spacing=h,
            time_step=dt,
        )
        assert abs(D - 0.4) < 1e-12


def test_radius_one_mutation_is_exact_discrete_diffusion_in_strict_interior():
    audit = audit_radius_one_diffusion_identity(
        (0.02, 0.08, 0.20, 0.40, 0.20, 0.08, 0.02),
        mutation_rate=0.15,
        grid_spacing=0.1,
        time_step=0.005,
    )
    assert audit.checked_indices == (2, 3, 4)
    assert audit.max_abs_residual < 1e-12


def test_boundary_adjacent_bin_is_not_silently_called_neumann_diffusion():
    audit = audit_radius_one_diffusion_identity(
        (0.2, 0.2, 0.2, 0.2, 0.2),
        mutation_rate=0.2,
        grid_spacing=0.1,
        time_step=0.01,
    )
    assert audit.checked_indices == (2,)
    # The current finite-bin endpoint sends all mutated mass inward, whereas an
    # interior source splits it over two neighbours. Thus bin 1 has a boundary
    # correction even though the centered Laplacian of a uniform vector is zero.
    assert abs(audit.generator[1] - audit.diffusion_rhs[1]) > 1e-6
    assert audit.max_abs_residual < 1e-12
