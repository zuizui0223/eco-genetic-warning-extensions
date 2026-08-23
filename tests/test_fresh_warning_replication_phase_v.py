from eco_genetic_warning_extensions.fresh_warning_replication_phase_v import (
    PHASE_V_MASTER_SEEDS,
    evaluate_parent_summary,
    phase_v_manifest,
)


def _endpoint(valid=30, leads=30, ties=0, lags=0, diversity_id="H_alpha", decline=0.05):
    return {
        "definition": {"diversity_id": diversity_id, "relative_decline_fraction": decline},
        "trajectory_available_count": 80,
        "warning_observed_count": 60,
        "trait_loss_observed_count": 35,
        "valid_pair_count": valid,
        "censored_count": 45,
        "warning_lead_count": leads,
        "warning_tie_count": ties,
        "warning_lag_count": lags,
        "seed_blocks": [],
    }


def _summary(rows):
    return {
        "denominators": {
            "attempted_seed_replicates": 100,
            "h1_full_state_source_prepared_count": 85,
            "projection_supported_count": 83,
            "trajectory_available_count": 83,
            "trait_loss_observed_count": 35,
        },
        "endpoint_summaries": rows,
    }


def _six_rows(valid=30, leads=30, ties=0, lags=0):
    return [
        _endpoint(valid, leads, ties, lags, diversity_id, decline)
        for diversity_id in ("H_alpha", "H_gamma")
        for decline in (0.05, 0.10, 0.20)
    ]


def test_manifest_freezes_domain_seeds_and_decision_rules():
    manifest = phase_v_manifest()
    assert PHASE_V_MASTER_SEEDS == (20291110, 20291111, 20291112, 20291113, 20291114)
    assert manifest["attempted_trajectories"] == 100
    assert manifest["frozen_domain"] == {
        "mutation_rate": 0.10,
        "area_reference": 0.8,
        "interaction_feedback": 6.0,
        "ramp_generations": 30,
        "hold_generations": 90,
        "total_generations": 120,
        "total_normalized_barrier_increase": 0.15,
        "profile": "standard",
    }
    assert len(manifest["endpoint_family"]) == 6
    assert manifest["minimum_valid_pairs_per_endpoint"] == 20
    assert "no replacement" in manifest["seed_selection"]
    assert "no recalibration" in manifest["opening_boundary"]


def test_strict_replication_requires_all_valid_pairs_to_lead():
    result = evaluate_parent_summary(_summary(_six_rows(valid=30, leads=30)))
    assert result["decision"] == "strict_replication"
    assert all(row["strict_endpoint_replication"] for row in result["endpoint_summaries"])


def test_directional_replication_can_survive_a_few_nonleads():
    result = evaluate_parent_summary(_summary(_six_rows(valid=30, leads=24, ties=2, lags=4)))
    assert result["decision"] == "directional_replication_only"
    assert all(row["directional_endpoint_replication"] for row in result["endpoint_summaries"])
    assert not any(row["strict_endpoint_replication"] for row in result["endpoint_summaries"])


def test_any_endpoint_below_precision_blocks_replication_claim():
    rows = _six_rows(valid=30, leads=30)
    rows[-1] = _endpoint(valid=19, leads=19, diversity_id="H_gamma", decline=0.20)
    result = evaluate_parent_summary(_summary(rows))
    assert result["decision"] == "insufficient_precision"


def test_any_directional_failure_yields_not_replicated():
    rows = _six_rows(valid=30, leads=24, ties=2, lags=4)
    rows[-1] = _endpoint(valid=30, leads=17, ties=4, lags=9, diversity_id="H_gamma", decline=0.20)
    result = evaluate_parent_summary(_summary(rows))
    assert result["decision"] == "not_replicated"
