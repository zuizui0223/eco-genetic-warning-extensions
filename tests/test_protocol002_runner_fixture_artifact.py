import json
from pathlib import Path

from eco_genetic_warning_extensions.protocol002_runner_fixture_artifact import write_runner_fixture_artifact
from eco_genetic_warning_extensions.protocol002_source_runner import deterministic_fixture_source_artifact


ARTIFACT_PATH = Path("artifacts/protocol002/source_runner_fixture.json")


def test_committed_runner_fixture_matches_generator() -> None:
    committed = json.loads(ARTIFACT_PATH.read_text(encoding="utf-8"))
    assert committed == deterministic_fixture_source_artifact()


def test_committed_runner_fixture_covers_all_statuses_without_simulation_claim() -> None:
    committed = json.loads(ARTIFACT_PATH.read_text(encoding="utf-8"))
    assert committed["simulation_result_present"] is False
    assert committed["record_count"] == 5
    assert committed["status_counts"] == {
        "not_run": 1,
        "preparation_failed": 1,
        "projection_failed": 1,
        "source_support_failed": 1,
        "success": 1,
    }


def test_write_runner_fixture_artifact(tmp_path) -> None:
    output = write_runner_fixture_artifact(tmp_path / "source_runner_fixture.json")
    payload = json.loads(output.read_text(encoding="utf-8"))
    assert payload == deterministic_fixture_source_artifact()
