import json
from pathlib import Path


ARTIFACT = Path("artifacts/protocol003/stage3_validation_summary.json")


def test_locked_stage3_summary_matches_completed_campaign():
    payload = json.loads(ARTIFACT.read_text())
    assert payload["source_workflow_run_id"] == 29417632137
    assert len(payload["domains"]) == 2
    assert sum(domain["attempted"] for domain in payload["domains"]) == 200

    bridge, transition = payload["domains"]
    assert bridge["domain"]["label"] == "symmetric_bridge"
    assert bridge["aggregate_ordering_across_six_endpoints"] == {
        "lag": 0,
        "lead": 323,
        "tie": 1,
        "valid_pairs": 324,
    }
    assert transition["domain"]["label"] == "transition"
    assert transition["aggregate_ordering_across_six_endpoints"] == {
        "lag": 12,
        "lead": 184,
        "tie": 5,
        "valid_pairs": 201,
    }


def test_all_six_endpoints_are_retained_per_domain():
    payload = json.loads(ARTIFACT.read_text())
    expected = {
        "H_alpha_0.05", "H_alpha_0.10", "H_alpha_0.20",
        "H_gamma_0.05", "H_gamma_0.10", "H_gamma_0.20",
    }
    for domain in payload["domains"]:
        assert set(domain["endpoint_summary"]) == expected
