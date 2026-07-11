import json
from pathlib import Path

from eco_genetic_warning_extensions.protocol002_h1_smoke_adapter import (
    deterministic_h1_smoke_artifact,
    evaluate_h1_source_coordinate,
    h1_smoke_coordinates,
    run_h1_source_adapter,
)
from eco_genetic_warning_extensions.protocol002_source_skeleton import SourceAttemptStatus


SMOKE_ARTIFACT_PATH = Path("artifacts/protocol002/h1_adapter_smoke.json")


def test_h1_adapter_short_circuits_at_preparation_failure() -> None:
    coordinate = h1_smoke_coordinates()[0]
    evaluation = evaluate_h1_source_coordinate(
        coordinate,
        prepare_source=lambda _: False,
        source_support=lambda _: (_ for _ in ()).throw(AssertionError("source support should not run")),
        projection_support=lambda _: (_ for _ in ()).throw(AssertionError("projection should not run")),
    )
    assert evaluation.status == SourceAttemptStatus.PREPARATION_FAILED


def test_h1_adapter_short_circuits_at_source_support_failure() -> None:
    coordinate = h1_smoke_coordinates()[0]
    evaluation = evaluate_h1_source_coordinate(
        coordinate,
        prepare_source=lambda _: True,
        source_support=lambda _: False,
        projection_support=lambda _: (_ for _ in ()).throw(AssertionError("projection should not run")),
    )
    assert evaluation.status == SourceAttemptStatus.SOURCE_SUPPORT_FAILED


def test_h1_adapter_reports_projection_failure_after_prior_success() -> None:
    coordinate = h1_smoke_coordinates()[0]
    evaluation = evaluate_h1_source_coordinate(
        coordinate,
        prepare_source=lambda _: True,
        source_support=lambda _: True,
        projection_support=lambda _: False,
    )
    assert evaluation.status == SourceAttemptStatus.PROJECTION_FAILED


def test_h1_smoke_subset_is_one_coordinate_one_seed_two_replicates() -> None:
    coordinates = h1_smoke_coordinates()
    assert len(coordinates) == 2
    assert {coordinate.coordinate.kappa_mu for coordinate in coordinates} == {0.20}
    assert {coordinate.coordinate.p_star for coordinate in coordinates} == {0.50}
    assert {coordinate.master_seed for coordinate in coordinates} == {20270210}
    assert [coordinate.replicate for coordinate in coordinates] == [0, 1]


def test_deterministic_h1_smoke_runs_ordered_adapter_and_retains_both_rows() -> None:
    artifact = deterministic_h1_smoke_artifact()
    assert artifact["simulation_result_present"] is False
    assert artifact["record_count"] == 2
    assert artifact["status_counts"]["success"] == 2
    assert all(record["status"] == "success" for record in artifact["records"])


def test_run_h1_source_adapter_retains_mixed_statuses() -> None:
    coordinates = h1_smoke_coordinates()
    manifest = run_h1_source_adapter(
        coordinates,
        prepare_source=lambda coordinate: True,
        source_support=lambda coordinate: coordinate.replicate == 0,
        projection_support=lambda coordinate: True,
    )
    assert manifest.to_artifact()["status_counts"] == {
        "not_run": 0,
        "preparation_failed": 0,
        "source_support_failed": 1,
        "projection_failed": 0,
        "success": 1,
    }


def test_committed_h1_adapter_smoke_matches_generator() -> None:
    committed = json.loads(SMOKE_ARTIFACT_PATH.read_text(encoding="utf-8"))
    assert committed == deterministic_h1_smoke_artifact()
