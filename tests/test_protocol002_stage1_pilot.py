from pathlib import Path

import pytest

from eco_genetic_warning_extensions.protocol002_stage1_pilot import (
    PILOT_COORDINATES,
    PILOT_MASTER_SEEDS,
    _support_status,
    run_stage1_source_support_pilot,
)


def test_stage1_pilot_design_is_declared() -> None:
    assert [(coordinate.kappa_mu, coordinate.p_star) for coordinate in PILOT_COORDINATES] == [
        (0.20, 0.25),
        (0.20, 0.50),
        (0.20, 0.75),
    ]
    assert PILOT_MASTER_SEEDS == (20270210, 20270211)


def test_stage1_pilot_support_status_mapping() -> None:
    assert _support_status(True) == "source_supported"
    assert _support_status(False) == "source_support_failed"
    assert _support_status(None) == "source_support_indeterminate"


def test_stage1_pilot_rejects_missing_upstream(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError, match="upstream checkout"):
        run_stage1_source_support_pilot(tmp_path / "missing")
