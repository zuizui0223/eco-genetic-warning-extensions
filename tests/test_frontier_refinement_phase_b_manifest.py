from eco_genetic_warning_extensions.frontier_refinement_manifest import (
    PHASE_B_CONFIRMATION_MASTER_SEEDS,
    PHASE_B_MASTER_SEEDS,
    PHASE_B_P_STAR,
    phase_b_cells,
    phase_b_manifest,
)


def test_phase_b_manifest_is_fixed_matched_and_warning_blind() -> None:
    cells = phase_b_cells()
    assert len(cells) == 4
    assert {cell.coordinate.p_star for cell in cells} == set(PHASE_B_P_STAR)
    assert {cell.coordinate.kappa_mu for cell in cells} == {0.35}
    assert {cell.anchor.anchor_id for cell in cells} == {"B1"}
    assert {cell.anchor.area_reference for cell in cells} == {1.0}
    assert {cell.anchor.interaction_kappa for cell in cells} == {4.5}
    assert {cell.anchor.normalised_barrier_increase for cell in cells} == {0.30}
    assert {cell.horizon for cell in cells} == {120}

    manifest = phase_b_manifest()
    assert manifest["cell_count"] == 4
    assert manifest["attempts_per_cell"] == 25
    assert manifest["planned_refinement_attempts"] == 100
    assert manifest["historical_bracket"]["low"]["batch_index"] == 619
    assert manifest["historical_bracket"]["high"]["batch_index"] == 673
    assert manifest["warning_fields_available"] is False
    assert manifest["diversity_fields_available"] is False


def test_phase_b_refinement_and_confirmation_seeds_are_disjoint() -> None:
    assert len(PHASE_B_MASTER_SEEDS) == 5
    assert len(PHASE_B_CONFIRMATION_MASTER_SEEDS) == 5
    assert set(PHASE_B_MASTER_SEEDS).isdisjoint(PHASE_B_CONFIRMATION_MASTER_SEEDS)
