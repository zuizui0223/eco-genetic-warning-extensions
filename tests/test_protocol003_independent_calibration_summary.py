import json
from pathlib import Path


def test_independent_calibration_summary_lock() -> None:
    payload = json.loads(
        Path("artifacts/protocol003/independent_calibration_summary.json").read_text(encoding="utf-8")
    )
    assert payload["run_id"] == 29400915768
    assert payload["attempted_trajectories"] == 100
    assert payload["candidate_count"] == 4
    assert payload["eligible_candidate_count"] == 0
    assert payload["selected_for_confirmation"] == [0, 2]
    assert payload["endpoint_contract"] == "trait_loss_only"
    assert payload["domain_selected"] is False
    assert payload["type_s_result_claimed"] is False
