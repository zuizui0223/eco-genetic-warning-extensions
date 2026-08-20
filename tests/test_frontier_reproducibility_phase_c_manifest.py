from eco_genetic_warning_extensions.frontier_refinement_manifest import (
    PHASE_C_MASTER_SEEDS,
    PHASE_C_MIN_BASELINE_ELIGIBLE_PER_SEED,
    PHASE_C_P_STAR,
    PHASE_C_REPLICATES_PER_SEED,
    phase_c_cells,
    phase_c_manifest,
)


def test_phase_c_manifest_is_fixed_high_rep_and_trait_loss_only() -> None:
    cells = phase_c_cells()
    assert len(cells) == 2
    assert {cell.coordinate.p_star for cell in cells} == set(PHASE_C_P_STAR) == {0.35, 0.40}
    assert {cell.coordinate.kappa_mu for cell in cells} == {0.35}
    assert {cell.anchor.area_reference for cell in cells} == {1.0}
    assert {cell.anchor.interaction_kappa for cell in cells} == {4.5}
    assert {cell.anchor.normalised_barrier_increase for cell in cells} == {0.30}
    assert {cell.horizon for cell in cells} == {120}
    assert PHASE_C_REPLICATES_PER_SEED == 20
    assert PHASE_C_MIN_BASELINE_ELIGIBLE_PER_SEED == 10

    manifest = phase_c_manifest()
    assert manifest["cell_count"] == 2
    assert manifest["attempts_per_cell"] == 100
    assert manifest["planned_attempts"] == 200
    assert manifest["warning_fields_available"] is False
    assert manifest["diversity_fields_available"] is False


def test_phase_c_seed_family_is_unique_and_fixed() -> None:
    assert PHASE_C_MASTER_SEEDS == (20290210, 20290211, 20290212, 20290213, 20290214)
