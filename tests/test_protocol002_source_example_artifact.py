import json
from pathlib import Path

from eco_genetic_warning_extensions.protocol002_source_example import example_source_skeleton_artifact


ARTIFACT_PATH = Path("artifacts/protocol002/source_skeleton_example_manifest.json")


def test_committed_source_skeleton_example_matches_writer() -> None:
    committed = json.loads(ARTIFACT_PATH.read_text(encoding="utf-8"))
    assert committed == example_source_skeleton_artifact()


def test_committed_source_skeleton_example_contains_no_simulation_result() -> None:
    committed = json.loads(ARTIFACT_PATH.read_text(encoding="utf-8"))
    assert committed["simulation_result_present"] is False
    assert committed["record_count"] == 1
    assert committed["status_counts"] == {
        "not_run": 1,
        "preparation_failed": 0,
        "projection_failed": 0,
        "source_support_failed": 0,
        "success": 0,
    }
    assert committed["records"][0]["status"] == "not_run"
