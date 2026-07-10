import json

from eco_genetic_warning_extensions.protocol002_source_example import (
    example_source_coordinate,
    example_source_skeleton_artifact,
    example_source_skeleton_manifest,
    write_source_skeleton_example,
)


def test_example_source_coordinate_is_declared_fixture() -> None:
    coordinate = example_source_coordinate()
    assert coordinate.identity() == {
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


def test_example_manifest_contains_one_not_run_record_and_no_result() -> None:
    artifact = example_source_skeleton_artifact()
    assert artifact["simulation_result_present"] is False
    assert artifact["record_count"] == 1
    assert artifact["status_counts"]["not_run"] == 1
    assert artifact["status_counts"]["success"] == 0
    assert artifact["records"][0]["status"] == "not_run"
    assert artifact["records"][0]["reason"] == "source reconstruction not run in skeleton stage"


def test_example_manifest_object_matches_artifact() -> None:
    manifest = example_source_skeleton_manifest()
    assert manifest.to_artifact() == example_source_skeleton_artifact()


def test_write_source_skeleton_example(tmp_path) -> None:
    output = write_source_skeleton_example(tmp_path / "source_skeleton_example.json")
    payload = json.loads(output.read_text(encoding="utf-8"))
    assert payload == example_source_skeleton_artifact()
