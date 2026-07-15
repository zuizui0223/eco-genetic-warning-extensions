import pytest

from eco_genetic_warning_extensions.protocol003_bracket_pilot import (
    BRACKET_MASTER_SEEDS,
    BRACKET_REPLICATES_PER_CELL,
    _assert_blind,
    protocol003_bracket_cells,
)


def test_protocol003_bracket_design_is_predeclared_and_small() -> None:
    cells = protocol003_bracket_cells()
    assert len(cells) == 16
    assert len(BRACKET_MASTER_SEEDS) == 2
    assert BRACKET_REPLICATES_PER_CELL == 2
    assert len(cells) * len(BRACKET_MASTER_SEEDS) * BRACKET_REPLICATES_PER_CELL == 64
    assert [cell.cell_index for cell in cells] == list(range(16))
    assert {cell.label for cell in cells} == {
        "rapid_loss",
        "symmetric_bridge",
        "transition",
        "persistence",
    }


def test_protocol003_bracket_seed_family_is_new() -> None:
    assert BRACKET_MASTER_SEEDS == (20270510, 20270511)


def test_protocol003_bracket_schedule_endpoints() -> None:
    cells = protocol003_bracket_cells()
    assert cells[0].identity() == {
        "cell_index": 0,
        "label": "rapid_loss",
        "kappa_mu": 0.2,
        "p_star": 0.25,
        "low_to_high": 0.05,
        "high_to_low": 0.15000000000000002,
        "area_reference": 0.8,
        "kappa": 6.0,
        "ramp_generations": 30,
        "hold_generations": 90,
        "horizon": 120,
        "normalised_barrier_increase": 0.05,
    }
    assert cells[-1].label == "persistence"
    assert cells[-1].hold_generations == 300
    assert cells[-1].normalised_barrier_increase == 0.75


def test_protocol003_artifact_metadata_remains_blind() -> None:
    _assert_blind(
        {
            "design": {
                "endpoint_contract": "trait_loss_only",
                "domain_selected": False,
            },
            "trait_loss_only": True,
        }
    )
    with pytest.raises(ValueError, match="forbidden calibration columns"):
        _assert_blind({"design": {"warning_fields_present": False}})
