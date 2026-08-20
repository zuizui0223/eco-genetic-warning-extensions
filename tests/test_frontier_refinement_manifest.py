from eco_genetic_warning_extensions.frontier_refinement_manifest import (
    PHASE_A_CONFIRMATION_MASTER_SEEDS,
    PHASE_A_MASTER_SEEDS,
    PHASE_A_P_STAR,
    phase_a_cells,
    phase_a_manifest,
)


def test_phase_a_manifest_is_small_fixed_and_warning_blind() -> None:
    cells = phase_a_cells()
    assert len(cells) == 10
    assert {cell.coordinate.p_star for cell in cells} == set(PHASE_A_P_STAR)
    assert {cell.anchor.anchor_id for cell in cells} == {"A1", "A2"}
    assert all(cell.coordinate.kappa_mu == 0.05 for cell in cells)
    assert all(cell.horizon == 120 for cell in cells)

    manifest = phase_a_manifest()
    assert manifest["cell_count"] == 10
    assert manifest["attempts_per_cell"] == 25
    assert manifest["planned_refinement_attempts"] == 250
    assert manifest["warning_fields_available"] is False
    assert manifest["diversity_fields_available"] is False


def test_refinement_and_confirmation_seed_families_are_disjoint() -> None:
    assert len(PHASE_A_MASTER_SEEDS) == 5
    assert len(PHASE_A_CONFIRMATION_MASTER_SEEDS) == 5
    assert set(PHASE_A_MASTER_SEEDS).isdisjoint(PHASE_A_CONFIRMATION_MASTER_SEEDS)
