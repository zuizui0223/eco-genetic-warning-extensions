import json
from collections import Counter
from pathlib import Path


ARTIFACT_PATH = Path("artifacts/protocol002/stage1_source_support_pilot.json")


def test_committed_stage1_pilot_artifact_has_declared_scope() -> None:
    artifact = json.loads(ARTIFACT_PATH.read_text(encoding="utf-8"))
    assert artifact["design"]["attempt_count"] == 6
    assert artifact["design"]["nested_barrier_grids"] == [25, 49, 97]
    assert artifact["design"]["nested_barrier_grids_form_one_resolution_set"] is True
    assert artifact["real_h1_source_support_run_present"] is True
    assert artifact["projection_run_present"] is False
    assert artifact["full_stage_i_campaign"] is False
    assert artifact["type_s_result_claimed"] is False


def test_committed_stage1_pilot_artifact_status_counts_match_attempts() -> None:
    artifact = json.loads(ARTIFACT_PATH.read_text(encoding="utf-8"))
    counts = Counter(attempt["source_status"] for attempt in artifact["attempts"])
    assert dict(counts) == {
        "source_supported": 4,
        "source_support_failed": 2,
    }
    assert artifact["status_counts"] == {
        "source_supported": 4,
        "source_support_failed": 2,
        "source_support_indeterminate": 0,
    }


def test_committed_stage1_pilot_directional_support_is_retained_without_inference() -> None:
    artifact = json.loads(ARTIFACT_PATH.read_text(encoding="utf-8"))
    by_p_star = {
        p_star: [attempt["source_support"] for attempt in artifact["attempts"] if attempt["p_star"] == p_star]
        for p_star in (0.25, 0.50, 0.75)
    }
    assert by_p_star == {
        0.25: [True, False],
        0.50: [False, True],
        0.75: [True, True],
    }
