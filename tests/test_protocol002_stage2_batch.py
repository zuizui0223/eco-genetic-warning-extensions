import pytest

from eco_genetic_warning_extensions.protocol002_stage2_batch import (
    Stage2BatchCell,
    _batch_artifact,
    stage2_batch_cell,
    stage2_batch_cells,
)


def test_stage2_batches_cover_declared_candidate_cells() -> None:
    cells = stage2_batch_cells()
    assert len(cells) == 810
    assert [cell.batch_index for cell in cells] == list(range(810))
    assert len({tuple(cell.identity().items()) for cell in cells}) == 810


def test_stage2_batch_order_starts_with_first_coordinate_and_schedules() -> None:
    first = stage2_batch_cell(0)
    assert first.identity() == {
        "batch_index": 0,
        "kappa_mu": 0.05,
        "p_star": 0.10,
        "area_reference": 0.8,
        "kappa": 3.0,
        "ramp_generations": 30,
        "hold_generations": 90,
        "horizon": 120,
        "normalised_barrier_increase": 0.15,
    }
    assert stage2_batch_cell(1).normalised_barrier_increase == pytest.approx(0.30)
    assert stage2_batch_cell(2).normalised_barrier_increase == pytest.approx(0.45)
    assert stage2_batch_cell(3).hold_generations == 210


def test_stage2_batch_rejects_out_of_range_index() -> None:
    with pytest.raises(ValueError, match="batch_index"):
        stage2_batch_cell(-1)
    with pytest.raises(ValueError, match="batch_index"):
        stage2_batch_cell(810)


def test_batch_artifact_retains_25_attempts_and_seed_rates() -> None:
    cell = stage2_batch_cell(0)
    attempts = []
    for seed in (20270310, 20270311, 20270312, 20270313, 20270314):
        for replicate in range(5):
            observed = replicate < 2
            attempts.append(
                {
                    **cell.identity(),
                    "master_seed": seed,
                    "replicate": replicate,
                    "source_prepared": True,
                    "projection_supported": True,
                    "eligible_for_trait_loss_denominator": True,
                    "trait_loss_observed_post_baseline": observed,
                }
            )
    artifact = _batch_artifact(cell, attempts)
    assert artifact["campaign"]["batch_count"] == 810
    assert artifact["campaign"]["full_campaign_attempt_count"] == 20250
    assert artifact["status_counts"]["attempted"] == 25
    assert artifact["status_counts"]["trait_loss"] == 10
    assert artifact["pooled_trait_loss_rate"] == pytest.approx(0.4)
    assert [block["trait_loss_rate"] for block in artifact["seed_blocks"]] == pytest.approx([0.4] * 5)
    assert artifact["trait_loss_only"] is True
    assert artifact["domain_selected"] is False
