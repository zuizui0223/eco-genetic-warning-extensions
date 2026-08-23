import json

from eco_genetic_warning_extensions.protocol002_condition_map import (
    candidate_from_batch,
    classify_seed_rates,
    condition_map,
)


def fake_batch(index: int, rates=(0.4, 0.5, 0.6, 0.5, 0.4)) -> dict:
    pooled = None if any(rate is None for rate in rates) else sum(rates) / len(rates)
    return {
        "campaign": {"batch_index": index},
        "cell": {
            "batch_index": index,
            "kappa_mu": 0.20,
            "p_star": 0.50,
            "area_reference": 1.0,
            "kappa": 4.5,
            "horizon": 120,
            "normalised_barrier_increase": 0.30,
        },
        "seed_blocks": [
            {"master_seed": 20270310 + i, "trait_loss_rate": rate}
            for i, rate in enumerate(rates)
        ],
        "pooled_trait_loss_rate": pooled,
    }


def test_regime_classification_and_candidate_diagnostics() -> None:
    assert classify_seed_rates((0.4, 0.5, 0.6, 0.5, 0.4)) == "warning_evaluable"
    assert classify_seed_rates((0.8, 0.8, 1.0, 0.8, 1.0)) == "rapid_loss"
    assert classify_seed_rates((0.0, 0.2, 0.0, 0.2, 0.0)) == "persistence"
    assert classify_seed_rates((0.2, 0.4, 0.8, 0.6, 0.2)) == "seed_heterogeneous"

    row = candidate_from_batch(fake_batch(1))
    assert row is not None
    assert row["regime"] == "warning_evaluable"
    assert row["inside_band_seed_count"] == 5
    assert row["total_distance_to_band"] == 0.0


def test_full_campaign_condition_map_preserves_warning_blind_boundary(tmp_path) -> None:
    for index in range(810):
        if index < 648:
            rates = (0.8, 0.8, 0.8, 0.8, 0.8)
        else:
            rates = (0.8, 0.8, None, 0.8, 0.8)
        (tmp_path / f"batch_{index:03d}.json").write_text(
            json.dumps(fake_batch(index, rates=rates)), encoding="utf-8"
        )

    artifact = condition_map(tmp_path.glob("batch_*.json"))
    assert artifact["batch_count"] == 810
    assert artifact["complete_candidate_count"] == 648
    assert artifact["incomplete_candidate_count"] == 162
    assert artifact["global_regime_counts"] == {"rapid_loss": 648}
    assert artifact["warning_fields_inspected"] is False
    assert artifact["diversity_fields_inspected"] is False
    assert artifact["selection_rule_changed"] is False
