import json
from pathlib import Path

import pytest

from eco_genetic_warning_extensions.mutation_coordinates import MutationCoordinates
from eco_genetic_warning_extensions.protocol002_calibration_grid import (
    artifact_sha256,
    planned_calibration_grid_artifact,
    planned_calibration_grid_lock_artifact,
    protocol002_calibration_grid,
    write_planned_calibration_grid_lock,
)


LOCK_PATH = Path("artifacts/protocol002/stage2_calibration_planned_lock.json")
EXPECTED_CANDIDATE_CELLS = 15 * 3 * 3 * 2 * 3
EXPECTED_ATTEMPTS = EXPECTED_CANDIDATE_CELLS * 5 * 5


def test_default_calibration_grid_has_declared_size_and_unique_attempts() -> None:
    attempts = protocol002_calibration_grid()
    assert len(attempts) == EXPECTED_ATTEMPTS
    assert len({tuple(attempt.identity().items()) for attempt in attempts}) == EXPECTED_ATTEMPTS


def test_calibration_grid_can_be_restricted_for_tiny_fixture() -> None:
    attempts = protocol002_calibration_grid(
        coordinates=(MutationCoordinates(kappa_mu=0.20, p_star=0.75),),
        area_references=(1.0,),
        kappas=(4.5,),
        hold_generations=(90,),
        barrier_increases=(0.30,),
        master_seeds=(20270310,),
        replicates_per_cell=2,
    )
    assert len(attempts) == 2
    assert [attempt.replicate for attempt in attempts] == [0, 1]
    assert all(attempt.horizon == 120 for attempt in attempts)


def test_planned_calibration_artifact_is_blind_and_no_simulation() -> None:
    artifact = planned_calibration_grid_artifact()
    assert artifact["candidate_cell_count"] == EXPECTED_CANDIDATE_CELLS
    assert artifact["attempt_count"] == EXPECTED_ATTEMPTS
    assert artifact["attempts_per_candidate_cell"] == 25
    assert artifact["simulation_result_present"] is False
    assert artifact["warning_fields_present"] is False
    forbidden = ("warning", "lead", "lag", "diversity", "heterozygosity", "h_alpha", "h_gamma")
    for row in artifact["attempts"][:50]:
        lowered = tuple(key.lower() for key in row)
        assert not any(token in key for key in lowered for token in forbidden)


def test_committed_calibration_grid_lock_matches_generator() -> None:
    committed = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
    assert committed == planned_calibration_grid_lock_artifact()


def test_calibration_grid_lock_hash_matches_full_manifest() -> None:
    lock = planned_calibration_grid_lock_artifact()
    assert lock["full_manifest_sha256"] == artifact_sha256(planned_calibration_grid_artifact())


def test_write_calibration_grid_lock(tmp_path) -> None:
    output = write_planned_calibration_grid_lock(tmp_path / "stage2_lock.json")
    assert json.loads(output.read_text(encoding="utf-8")) == planned_calibration_grid_lock_artifact()


def test_calibration_grid_rejects_non_positive_replicate_count() -> None:
    with pytest.raises(ValueError, match="replicates_per_cell"):
        protocol002_calibration_grid(replicates_per_cell=0)
