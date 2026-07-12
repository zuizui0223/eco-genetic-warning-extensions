import json
from pathlib import Path

from eco_genetic_warning_extensions.protocol002_source_grid import (
    artifact_sha256,
    planned_source_grid_artifact,
    planned_source_grid_lock_artifact,
    write_planned_source_grid_lock,
)


LOCK_PATH = Path("artifacts/protocol002/source_grid_planned_lock.json")


def test_committed_source_grid_lock_matches_writer() -> None:
    committed = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
    assert committed == planned_source_grid_lock_artifact()


def test_committed_source_grid_lock_contains_no_simulation_result() -> None:
    committed = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
    assert committed["simulation_result_present"] is False
    assert committed["record_count"] == 3375
    assert committed["status_counts"] == {
        "not_run": 3375,
        "preparation_failed": 0,
        "projection_failed": 0,
        "source_support_failed": 0,
        "success": 0,
    }
    assert committed["grid"]["nested_barrier_grids_form_one_resolution_set"] is True
    assert committed["interpretation"] == {
        "planned_rows_only": True,
        "source_reconstruction_run": False,
        "type_s_result_present": False,
    }


def test_source_grid_lock_hash_matches_full_manifest() -> None:
    lock = planned_source_grid_lock_artifact()
    assert lock["full_manifest_sha256"] == artifact_sha256(planned_source_grid_artifact())


def test_write_planned_source_grid_lock(tmp_path) -> None:
    output = write_planned_source_grid_lock(tmp_path / "source_grid_planned_lock.json")
    payload = json.loads(output.read_text(encoding="utf-8"))
    assert payload == planned_source_grid_lock_artifact()
