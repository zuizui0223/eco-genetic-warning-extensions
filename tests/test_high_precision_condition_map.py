import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_high_precision_condition_map_locks_final_c2_interpretation() -> None:
    payload = json.loads((ROOT / "artifacts/high_precision_condition_map.json").read_text())
    assert payload["interpretation_rule"]["R3"].startswith("mixed-block screen failure")
    frontier = payload["recurrent_turnover"]["conditions"]
    assert [round(row["p_star"], 3) for row in frontier] == [0.325, 0.35, 0.375, 0.4]
    assert payload["recurrent_turnover"]["conclusion"].startswith("asymmetric_high_to_low_loss_incidence_frontier")

    connectivity = {row["m"]: row for row in payload["connectivity"]["conditions"]}
    assert connectivity[0.10]["equal_rate_p"] < 0.05
    assert connectivity[0.20]["equal_rate_p"] > 0.05
    assert "not_freshly_replicated" in payload["connectivity"]["conclusion"]

    fresh = {row["m"]: row for row in payload["fresh_connectivity_replication"]["conditions"]}
    assert payload["fresh_connectivity_replication"]["decision"] == "historical_m010_heterogeneity_not_freshly_replicated"
    assert fresh[0.0]["equal_rate_p"] > 0.05
    assert fresh[0.10]["equal_rate_p"] > 0.05
    assert fresh[0.10]["equal_rate_p"] > connectivity[0.10]["equal_rate_p"]
    assert payload["fresh_connectivity_replication"]["mcnemar_p"] > 0.05

    partner = payload["reduced_form_partner_loss"]["conditions"]
    assert all(row["screen"] == "R4_highrep" for row in partner)
    kappa = payload["aggregate_interaction_support"]["conditions"]
    assert all(row["screen"] == "R4_highrep" for row in kappa)
