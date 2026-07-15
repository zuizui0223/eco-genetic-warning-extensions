from eco_genetic_warning_extensions.protocol003_confirmation_calibration import (
    CONFIRMATION_MASTER_SEEDS,
    CONFIRMATION_REPLICATES_PER_SEED,
    protocol003_confirmation_cells,
)


def test_confirmation_design_is_locked() -> None:
    cells = protocol003_confirmation_cells()
    assert len(cells) == 2
    assert CONFIRMATION_MASTER_SEEDS == (20270620, 20270621, 20270622, 20270623, 20270624)
    assert CONFIRMATION_REPLICATES_PER_SEED == 20
    assert len(cells) * len(CONFIRMATION_MASTER_SEEDS) * CONFIRMATION_REPLICATES_PER_SEED == 200
    assert cells[0].label == "symmetric_bridge"
    assert cells[0].hold_generations == 210
    assert cells[0].normalised_barrier_increase == 0.20
    assert cells[1].label == "transition"
    assert cells[1].hold_generations == 90
    assert cells[1].normalised_barrier_increase == 0.10
