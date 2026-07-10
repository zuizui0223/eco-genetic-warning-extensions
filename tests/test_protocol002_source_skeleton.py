import pytest

from eco_genetic_warning_extensions.mutation_coordinates import MutationCoordinates
from eco_genetic_warning_extensions.protocol002_source_skeleton import (
    Protocol002SourceCoordinate,
    SourceAttemptRecord,
    SourceAttemptStatus,
    SourceSkeletonManifest,
    skeleton_record,
    status_counts,
)


def make_coordinate() -> Protocol002SourceCoordinate:
    return Protocol002SourceCoordinate(
        coordinate=MutationCoordinates(kappa_mu=0.20, p_star=0.75),
        area_reference=1.0,
        kappa=4.5,
        nested_barrier_grid=49,
        stage_generations=30,
        hold_generations=30,
        master_seed=20270210,
        replicate=0,
    )


def test_source_coordinate_identity_is_flat_and_stable() -> None:
    identity = make_coordinate().identity()
    assert identity == {
        "kappa_mu": 0.20,
        "p_star": 0.75,
        "area_reference": 1.0,
        "kappa": 4.5,
        "nested_barrier_grid": 49,
        "stage_generations": 30,
        "hold_generations": 30,
        "master_seed": 20270210,
        "replicate": 0,
    }


def test_skeleton_record_retains_not_run_attempts() -> None:
    record = skeleton_record(make_coordinate())
    row = record.to_artifact_row()
    assert row["status"] == "not_run"
    assert row["source_prepared"] is False
    assert row["source_supported"] is False
    assert row["projection_supported"] is False
    assert row["reason"] == "source reconstruction not run in skeleton stage"


def test_manifest_includes_zero_counts_for_all_statuses() -> None:
    record = skeleton_record(make_coordinate())
    manifest = SourceSkeletonManifest(records=(record,)).to_artifact()
    assert manifest["simulation_result_present"] is False
    assert manifest["record_count"] == 1
    assert manifest["status_counts"] == {
        "not_run": 1,
        "preparation_failed": 0,
        "source_support_failed": 0,
        "projection_failed": 0,
        "success": 0,
    }


def test_success_record_requires_all_support_flags() -> None:
    with pytest.raises(ValueError, match="success requires"):
        SourceAttemptRecord(
            source_coordinate=make_coordinate(),
            status=SourceAttemptStatus.SUCCESS,
            source_prepared=True,
            source_supported=True,
            projection_supported=False,
            reason="inconsistent success fixture",
        )


def test_unprepared_record_cannot_skip_to_late_failure() -> None:
    with pytest.raises(ValueError, match="unprepared"):
        SourceAttemptRecord(
            source_coordinate=make_coordinate(),
            status=SourceAttemptStatus.PROJECTION_FAILED,
            source_prepared=False,
            source_supported=False,
            projection_supported=False,
            reason="projection cannot fail before preparation",
        )


def test_manifest_rejects_simulation_claims_and_empty_records() -> None:
    record = skeleton_record(make_coordinate())
    with pytest.raises(ValueError, match="simulation"):
        SourceSkeletonManifest(records=(record,), simulation_result_present=True)
    with pytest.raises(ValueError, match="at least one"):
        SourceSkeletonManifest(records=())


def test_status_counts_reports_all_declared_statuses() -> None:
    coordinate = make_coordinate()
    records = (
        skeleton_record(coordinate),
        SourceAttemptRecord(
            source_coordinate=coordinate,
            status=SourceAttemptStatus.PREPARATION_FAILED,
            source_prepared=False,
            source_supported=False,
            projection_supported=False,
            reason="fixture preparation failed",
        ),
    )
    counts = status_counts(records)
    assert counts["not_run"] == 1
    assert counts["preparation_failed"] == 1
    assert counts["source_support_failed"] == 0
    assert counts["projection_failed"] == 0
    assert counts["success"] == 0
