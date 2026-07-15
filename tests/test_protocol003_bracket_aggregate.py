from eco_genetic_warning_extensions.protocol003_bracket_aggregate import aggregate_bracket_artifacts


def _artifact(index: int, label: str, rate: float) -> dict:
    return {
        "stage": "Protocol 003 blind sentinel bracket pilot",
        "cell": {
            "cell_index": index,
            "label": label,
            "kappa_mu": 0.2,
            "p_star": 0.5,
            "area_reference": 0.8,
            "kappa": 6.0,
            "ramp_generations": 30,
            "hold_generations": 90 + 30 * (index % 4),
            "horizon": 120 + 30 * (index % 4),
            "normalised_barrier_increase": 0.1 + 0.05 * (index % 4),
        },
        "status_counts": {"attempted": 4, "baseline_eligible": 4, "trait_loss": round(rate * 4)},
        "pooled_trait_loss_rate": rate,
    }


def test_aggregate_selects_closest_schedule_and_retains_blind_contract() -> None:
    labels = ("rapid_loss", "symmetric_bridge", "transition", "persistence")
    rates = (0.0, 0.25, 0.5, 1.0)
    artifacts = []
    for group, label in enumerate(labels):
        for offset, rate in enumerate(rates):
            artifacts.append(_artifact(group * 4 + offset, label, rate))

    result = aggregate_bracket_artifacts(artifacts)
    assert result["cell_count"] == 16
    assert result["trajectory_attempt_count"] == 64
    assert result["endpoint_contract"] == "trait_loss_only"
    assert result["domain_selected"] is False
    assert len(result["sentinels"]) == 4
    for sentinel in result["sentinels"]:
        assert sentinel["closest_schedule"]["pooled_trait_loss_rate"] == 0.5
        assert sentinel["bracket_crosses_half"] is True
        assert sentinel["ready_for_independent_calibration"] is True
