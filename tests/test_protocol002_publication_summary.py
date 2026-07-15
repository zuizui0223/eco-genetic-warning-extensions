import json
from pathlib import Path


SUMMARY = Path("artifacts/protocol002/stage2_no_domain_publication_summary.json")


def test_publication_summary_locks_completed_campaign() -> None:
    payload = json.loads(SUMMARY.read_text(encoding="utf-8"))
    assert payload["batch_count"] == 810
    assert payload["attempt_count"] == 20_250
    assert payload["coordinate_count"] == 15
    assert payload["complete_five_seed_candidate_count"] == 648
    assert payload["eligible_candidate_count"] == 0
    assert payload["selected_coordinate_count"] == 0
    assert payload["no_domain_selected_coordinate_count"] == 15
    assert sum(payload["complete_candidate_pattern_counts"].values()) == 648


def test_publication_summary_preserves_blindness_and_no_stage3_claim() -> None:
    payload = json.loads(SUMMARY.read_text(encoding="utf-8"))
    assert payload["warning_fields_inspected"] is False
    assert payload["diversity_fields_inspected"] is False
    assert payload["selection_rule_changed"] is False
    assert payload["stage3_run"] is False
    interpretation = payload["interpretation"].lower()
    assert "no claim about warning lead or lag" in interpretation
