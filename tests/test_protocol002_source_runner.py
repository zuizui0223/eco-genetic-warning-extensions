import pytest

from eco_genetic_warning_extensions.protocol002_source_runner import (
    SourceAttemptEvaluation,
    deterministic_fixture_evaluator,
    deterministic_fixture_source_artifact,
    deterministic_fixture_source_coordinates,
    deterministic_fixture_source_manifest,
    evaluate_source_attempts,
    not_run_evaluator,
)
from eco_genetic_warning_extensions.protocol002_source_skeleton import SourceAttemptStatus


def test_not_run_evaluator_retains_explicit_not_run_record() -> None:
    coordinate = deterministic_fixture_source_coordinates()[0]
    record = not_run_evaluator(coordinate).to_record(coordinate)
    row = record.to_artifact_row()
    assert row["status"] == "not_run"
    assert row["source_prepared"] is False
    assert row["source_supported"] is False
    assert row["projection_supported"] is False
    assert row["reason"] == "source reconstruction not run by runner interface"


def test_deterministic_fixture_coordinates_cover_five_replicates() -> None:
    coordinates = deterministic_fixture_source_coordinates()
    assert len(coordinates) == 5
    assert [coordinate.replicate for coordinate in coordinates] == [0, 1, 2, 3, 4]


def test_deterministic_fixture_manifest_covers_all_statuses_once() -> None:
    artifact = deterministic_fixture_source_artifact()
    assert artifact["simulation_result_present"] is False
    assert artifact["record_count"] == 5
    assert artifact["status_counts"] == {
        "not_run": 1,
        "preparation_failed": 1,
        "source_support_failed": 1,
        "projection_failed": 1,
        "success": 1,
    }
    assert [record["status"] for record in artifact["records"]] == [
        "success",
        "preparation_failed",
        "source_support_failed",
        "projection_failed",
        "not_run",
    ]


def test_deterministic_fixture_status_flags_are_consistent() -> None:
    rows = deterministic_fixture_source_artifact()["records"]
    assert rows[0]["status"] == "success"
    assert rows[0]["source_prepared"] is True
    assert rows[0]["source_supported"] is True
    assert rows[0]["projection_supported"] is True

    assert rows[1]["status"] == "preparation_failed"
    assert rows[1]["source_prepared"] is False
    assert rows[1]["source_supported"] is False
    assert rows[1]["projection_supported"] is False

    assert rows[2]["status"] == "source_support_failed"
    assert rows[2]["source_prepared"] is True
    assert rows[2]["source_supported"] is False
    assert rows[2]["projection_supported"] is False

    assert rows[3]["status"] == "projection_failed"
    assert rows[3]["source_prepared"] is True
    assert rows[3]["source_supported"] is True
    assert rows[3]["projection_supported"] is False

    assert rows[4]["status"] == "not_run"
    assert rows[4]["source_prepared"] is False
    assert rows[4]["source_supported"] is False
    assert rows[4]["projection_supported"] is False


def test_evaluate_source_attempts_retains_every_coordinate() -> None:
    coordinates = deterministic_fixture_source_coordinates()
    manifest = evaluate_source_attempts(coordinates, not_run_evaluator)
    artifact = manifest.to_artifact()
    assert artifact["record_count"] == len(coordinates)
    assert artifact["status_counts"] == {
        "not_run": 5,
        "preparation_failed": 0,
        "source_support_failed": 0,
        "projection_failed": 0,
        "success": 0,
    }


def test_fixture_manifest_object_matches_artifact() -> None:
    assert deterministic_fixture_source_manifest().to_artifact() == deterministic_fixture_source_artifact()


def test_invalid_evaluation_is_rejected_by_record_consistency() -> None:
    coordinate = deterministic_fixture_source_coordinates()[0]
    evaluation = SourceAttemptEvaluation(
        status=SourceAttemptStatus.SUCCESS,
        source_prepared=True,
        source_supported=False,
        projection_supported=False,
        reason="invalid success fixture",
    )
    with pytest.raises(ValueError, match="success requires"):
        evaluation.to_record(coordinate)


def test_deterministic_evaluator_cycles_for_larger_replicates() -> None:
    coordinate = deterministic_fixture_source_coordinates()[0]
    coordinate_5 = type(coordinate)(
        coordinate=coordinate.coordinate,
        area_reference=coordinate.area_reference,
        kappa=coordinate.kappa,
        nested_barrier_grid=coordinate.nested_barrier_grid,
        stage_generations=coordinate.stage_generations,
        hold_generations=coordinate.hold_generations,
        master_seed=coordinate.master_seed,
        replicate=5,
    )
    assert deterministic_fixture_evaluator(coordinate_5).status == SourceAttemptStatus.SUCCESS
