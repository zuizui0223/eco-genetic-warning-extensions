import pytest

from eco_genetic_warning_extensions.protocol002_stage2_smoke import (
    _assert_blind_artifact,
    stage2_smoke_design,
)


def test_stage2_smoke_design_is_declared_tiny_fixture() -> None:
    design = stage2_smoke_design()
    assert design["protocol002_coordinate"] == {
        "kappa_mu": 0.20,
        "p_star": 0.75,
        "low_to_high": 0.15,
        "high_to_low": 0.05,
    }
    assert design["source"]["area_reference"] == 1.0
    assert design["source"]["kappa"] == 4.5
    assert design["source"]["master_seed"] == 20270210
    assert design["source"]["replicates"] == 1
    assert design["calibration"] == {
        "master_seed": 20270310,
        "ramp_generations": 30,
        "hold_generations": 90,
        "horizon": 120,
        "normalised_barrier_increase": 0.15,
        "projection_scenario": "equal_isolated",
    }


def test_stage2_smoke_blind_guard_accepts_trait_loss_only_fields() -> None:
    _assert_blind_artifact(
        {
            "stage": "Stage II smoke",
            "trait_loss_time_post_baseline": 42,
            "trait_loss_observed_post_baseline": True,
            "baseline_realised_high_trait_present": True,
        }
    )


@pytest.mark.parametrize(
    "field",
    ["warning_time", "lead_time", "h_alpha", "h_gamma", "diversity", "heterozygosity", "event_pair"],
)
def test_stage2_smoke_blind_guard_rejects_forbidden_fields(field: str) -> None:
    with pytest.raises(ValueError):
        _assert_blind_artifact({field: 1})
