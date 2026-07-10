import json

import pytest

from eco_genetic_warning_extensions.mutation_coordinates import MutationCoordinates
from eco_genetic_warning_extensions.protocol002_source_grid import (
    SOURCE_AREA_REFERENCES,
    SOURCE_HOLD_GENERATIONS,
    SOURCE_KAPPAS,
    SOURCE_MASTER_SEEDS,
    SOURCE_NESTED_BARRIER_GRIDS,
    SOURCE_REPLICATES_PER_CELL,
    SOURCE_STAGE_GENERATIONS,
    planned_source_grid_artifact,
    planned_source_grid_manifest,
    protocol002_source_grid,
    write_planned_source_grid,
)


EXPECTED_DEFAULT_ROW_COUNT = 15 * 3 * 3 * 3 * 5 * 5


def test_default_source_grid_has_declared_row_count() -> None:
    rows = protocol002_source_grid()
    assert len(rows) == EXPECTED_DEFAULT_ROW_COUNT
    assert len({tuple(row.identity().items()) for row in rows}) == EXPECTED_DEFAULT_ROW_COUNT


def test_default_source_grid_constants_match_protocol_declaration() -> None:
    assert SOURCE_AREA_REFERENCES == (0.8, 1.0, 1.2)
    assert SOURCE_KAPPAS == (3.0, 4.5, 6.0)
    assert SOURCE_MASTER_SEEDS == (20270210, 20270211, 20270212, 20270213, 20270214)
    assert SOURCE_REPLICATES_PER_CELL == 5
    assert SOURCE_NESTED_BARRIER_GRIDS == (25, 49, 97)
    assert SOURCE_STAGE_GENERATIONS == 30
    assert SOURCE_HOLD_GENERATIONS == 30


def test_source_grid_can_be_restricted_for_small_fixture() -> None:
    rows = protocol002_source_grid(
        coordinates=(MutationCoordinates(kappa_mu=0.20, p_star=0.75),),
        area_references=(1.0,),
        kappas=(4.5,),
        nested_barrier_grids=(49,),
        master_seeds=(20270210,),
        replicates_per_cell=2,
    )
    assert len(rows) == 2
    assert [row.replicate for row in rows] == [0, 1]
    assert rows[0].identity()["kappa_mu"] == pytest.approx(0.20)
    assert rows[0].identity()["p_star"] == pytest.approx(0.75)


def test_planned_source_grid_manifest_has_no_simulation_result_and_all_not_run() -> None:
    artifact = planned_source_grid_artifact()
    assert artifact["simulation_result_present"] is False
    assert artifact["record_count"] == EXPECTED_DEFAULT_ROW_COUNT
    assert artifact["status_counts"] == {
        "not_run": EXPECTED_DEFAULT_ROW_COUNT,
        "preparation_failed": 0,
        "source_support_failed": 0,
        "projection_failed": 0,
        "success": 0,
    }
    assert all(record["status"] == "not_run" for record in artifact["records"])
    assert all(record["source_prepared"] is False for record in artifact["records"])
    assert all(record["source_supported"] is False for record in artifact["records"])
    assert all(record["projection_supported"] is False for record in artifact["records"])


def test_planned_source_grid_manifest_object_matches_artifact() -> None:
    manifest = planned_source_grid_manifest()
    assert manifest.to_artifact() == planned_source_grid_artifact()


def test_write_planned_source_grid(tmp_path) -> None:
    output = write_planned_source_grid(tmp_path / "source_grid_planned_manifest.json")
    payload = json.loads(output.read_text(encoding="utf-8"))
    assert payload == planned_source_grid_artifact()


def test_source_grid_rejects_non_positive_replicate_count() -> None:
    with pytest.raises(ValueError, match="replicates_per_cell"):
        protocol002_source_grid(replicates_per_cell=0)
