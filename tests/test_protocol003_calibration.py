from eco_genetic_warning_extensions.protocol003_calibration import (
    CALIBRATION_MASTER_SEEDS,
    CALIBRATION_REPLICATES_PER_SEED,
    protocol003_calibration_cells,
)


def test_protocol003_calibration_grid_is_locked() -> None:
    cells = protocol003_calibration_cells()
    assert len(cells) == 4
    assert [cell.cell_index for cell in cells] == [0, 1, 2, 3]
    assert CALIBRATION_MASTER_SEEDS == (20270610, 20270611, 20270612, 20270613, 20270614)
    assert CALIBRATION_REPLICATES_PER_SEED == 5
    assert len(cells) * len(CALIBRATION_MASTER_SEEDS) * CALIBRATION_REPLICATES_PER_SEED == 100
    assert [(cell.label, cell.hold_generations, cell.normalised_barrier_increase) for cell in cells] == [
        ("symmetric_bridge", 210, 0.20),
        ("symmetric_bridge", 300, 0.30),
        ("transition", 90, 0.10),
        ("transition", 90, 0.15),
    ]
