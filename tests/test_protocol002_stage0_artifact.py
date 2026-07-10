import json
from pathlib import Path

from eco_genetic_warning_extensions.protocol002_stage0 import stage0_certificate


ARTIFACT_PATH = Path("artifacts/protocol002/stage0_operator_certificate.json")


def test_committed_stage0_artifact_matches_generator() -> None:
    committed = json.loads(ARTIFACT_PATH.read_text(encoding="utf-8"))
    assert committed == stage0_certificate()


def test_committed_stage0_artifact_contains_no_simulation_result() -> None:
    committed = json.loads(ARTIFACT_PATH.read_text(encoding="utf-8"))
    assert committed["interpretation"]["simulation_result_present"] is False
    assert committed["coordinate_count"] == 15
    assert {point["p_star"] for point in committed["coordinates"]} == {0.10, 0.25, 0.50, 0.75, 0.90}
    assert {point["kappa_mu"] for point in committed["coordinates"]} == {0.05, 0.20, 0.35}
