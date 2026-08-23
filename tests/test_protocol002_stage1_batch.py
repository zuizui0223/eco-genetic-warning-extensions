import pytest

from eco_genetic_warning_extensions.protocol002_stage1_batch import (
    _batch_artifact,
    default_stage1_batch_path,
    stage1_batch_cell,
    stage1_batch_cells,
)


def test_stage1_campaign_has_135_stable_unique_batches() -> None:
    cells = stage1_batch_cells()
    assert len(cells) == 135
    assert [cell.batch_index for cell in cells] == list(range(135))
    identities = {
        (
            cell.coordinate.kappa_mu,
            cell.coordinate.p_star,
            cell.area_reference,
            cell.kappa,
        )
        for cell in cells
    }
    assert len(identities) == 135


def test_stage1_batch_zero_is_first_declared_phase_cell() -> None:
    cell = stage1_batch_cell(0)
    assert cell.identity() == {
        "batch_index": 0,
        "kappa_mu": 0.05,
        "p_star": 0.10,
        "area_reference": 0.8,
        "kappa": 3.0,
    }


def test_stage1_batch_last_is_last_declared_phase_cell() -> None:
    cell = stage1_batch_cell(134)
    assert cell.identity() == {
        "batch_index": 134,
        "kappa_mu": 0.35,
        "p_star": 0.90,
        "area_reference": 1.2,
        "kappa": 6.0,
    }


def test_stage1_batch_index_validation() -> None:
    with pytest.raises(ValueError, match="batch_index"):
        stage1_batch_cell(-1)
    with pytest.raises(ValueError, match="batch_index"):
        stage1_batch_cell(135)


def test_default_stage1_batch_path_is_zero_padded() -> None:
    assert default_stage1_batch_path(0).as_posix().endswith("stage1_batches/batch_000.json")
    assert default_stage1_batch_path(42).as_posix().endswith("stage1_batches/batch_042.json")


def test_batch_artifact_locks_campaign_denominators() -> None:
    batch = stage1_batch_cell(0)
    attempts = []
    for index in range(25):
        attempts.append(
            {
                "source_support": index < 10,
                "source_prepared": index < 8,
                "projection_status": "projection_supported" if index < 7 else ("projection_failed" if index == 7 else "not_run"),
            }
        )
    artifact = _batch_artifact(batch, attempts)
    assert artifact["campaign"] == {
        "batch_index": 0,
        "batch_count": 135,
        "attempts_per_batch": 25,
        "full_campaign_attempt_count": 3375,
        "resumable_unit": "one mutation coordinate x one area_reference x one kappa",
    }
    assert artifact["status_counts"] == {
        "source_supported": 10,
        "source_prepared": 8,
        "projection_supported": 7,
        "projection_failed": 1,
        "projection_not_run": 17,
    }


def test_batch_artifact_requires_all_25_attempts() -> None:
    with pytest.raises(RuntimeError, match="25 attempts"):
        _batch_artifact(stage1_batch_cell(0), [])
