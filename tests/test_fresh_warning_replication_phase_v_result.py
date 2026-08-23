import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_phase_v_locked_summary_records_strict_fresh_replication():
    payload = json.loads((ROOT / "artifacts/fresh_warning_replication/phase_v_locked_summary.json").read_text())
    assert payload["decision"] == "strict_replication"
    assert payload["provenance"]["workflow_run"] == 32636847803
    assert payload["provenance"]["aggregate_artifact"] == 9492587604
    assert payload["provenance"]["artifact_digest"] == "sha256:c1dd951c961999c42255b46327d4650d2298afa98ee4d0a45d04a1e1c5fe6031"
    assert payload["denominators"]["attempted_seed_replicates"] == 100
    assert payload["denominators"]["trajectory_available_count"] == 82
    assert payload["denominators"]["trait_loss_observed_count"] == 33
    endpoints = payload["endpoint_family"]
    assert len(endpoints) == 6
    assert all(row["valid_pairs"] == 33 for row in endpoints)
    assert all(row["leads"] == 33 for row in endpoints)
    assert all(row["ties"] == 0 and row["lags"] == 0 for row in endpoints)
    assert payload["seed_block_valid_pairs_each_endpoint"] == [7, 7, 7, 7, 5]
    assert payload["seed_block_leads_each_endpoint"] == [7, 7, 7, 7, 5]
