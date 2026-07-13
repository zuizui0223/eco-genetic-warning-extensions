import pytest

from eco_genetic_warning_extensions.protocol002_stage2_selection import (
    candidate_from_batch_artifact,
    stage2_selection_artifact,
)


def fake_batch(index: int, *, rates=(0.4, 0.5, 0.6, 0.5, 0.5)) -> dict:
    return {
        "campaign": {"batch_index": index},
        "cell": {
            "kappa_mu": 0.20,
            "p_star": 0.50,
            "area_reference": 1.0,
            "kappa": 4.5,
            "ramp_generations": 30,
            "hold_generations": 90,
            "normalised_barrier_increase": 0.30,
        },
        "status_counts": {"attempted": 25},
        "seed_blocks": [
            {"master_seed": 20270310 + i, "trait_loss_rate": rate}
            for i, rate in enumerate(rates)
        ],
    }


def test_candidate_from_batch_artifact_requires_complete_seed_blocks() -> None:
    assert candidate_from_batch_artifact(fake_batch(0)) is not None
    assert candidate_from_batch_artifact(fake_batch(0, rates=(0.4, 0.5, None, 0.5, 0.5))) is None


def test_candidate_from_batch_artifact_preserves_blind_selection_fields() -> None:
    candidate = candidate_from_batch_artifact(fake_batch(0))
    assert candidate is not None
    assert candidate.is_eligible() is True
    assert candidate.pooled_trait_loss_rate == pytest.approx(0.5)


def test_stage2_selection_artifact_selects_best_eligible_candidate() -> None:
    base = fake_batch(0, rates=(0.4, 0.4, 0.4, 0.4, 0.4))
    best = fake_batch(1, rates=(0.5, 0.5, 0.5, 0.5, 0.5))
    best["cell"] = {**best["cell"], "normalised_barrier_increase": 0.15}
    artifact = stage2_selection_artifact((base, best))
    assert artifact["selected_domain_count"] == 1
    assert artifact["selected_domains"][0]["domain"]["pooled_trait_loss_rate"] == pytest.approx(0.5)
    assert artifact["warning_fields_inspected"] is False
    assert artifact["diversity_fields_inspected"] is False
