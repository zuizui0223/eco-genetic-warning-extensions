from eco_genetic_warning_extensions.frontier_refinement_manifest import (
    PHASE_D_MASTER_SEEDS,
    PHASE_D_MIN_BASELINE_ELIGIBLE_PER_SEED,
    PHASE_D_P_STAR,
    PHASE_D_REPLICATES_PER_SEED,
    phase_d_cells,
    phase_d_manifest,
)


def test_phase_d_manifest_is_local_fixed_and_warning_blind() -> None:
    cells = phase_d_cells()
    assert len(cells) == 3
    assert {cell.coordinate.p_star for cell in cells} == set(PHASE_D_P_STAR) == {0.325, 0.35, 0.375}
    assert {cell.coordinate.kappa_mu for cell in cells} == {0.35}
    assert {cell.anchor.area_reference for cell in cells} == {1.0}
    assert {cell.anchor.interaction_kappa for cell in cells} == {4.5}
    assert {cell.anchor.normalised_barrier_increase for cell in cells} == {0.30}
    assert {cell.horizon for cell in cells} == {120}
    assert PHASE_D_REPLICATES_PER_SEED == 20
    assert PHASE_D_MIN_BASELINE_ELIGIBLE_PER_SEED == 10

    manifest = phase_d_manifest()
    assert manifest["cell_count"] == 3
    assert manifest["attempts_per_cell"] == 100
    assert manifest["planned_attempts"] == 300
    assert manifest["phase_c_r4_replay"] == 0.35
    assert manifest["warning_fields_available"] is False
    assert manifest["diversity_fields_available"] is False


def test_phase_d_seed_family_is_fixed() -> None:
    assert PHASE_D_MASTER_SEEDS == (20290310, 20290311, 20290312, 20290313, 20290314)
