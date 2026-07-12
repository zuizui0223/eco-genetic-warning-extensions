import json
from pathlib import Path

from eco_genetic_warning_extensions.protocol002_stage2_smoke import _assert_blind_artifact


ARTIFACT_PATH = Path("artifacts/protocol002/stage2_trait_loss_smoke.json")


def test_committed_stage2_smoke_artifact_is_blind_and_completed() -> None:
    artifact = json.loads(ARTIFACT_PATH.read_text(encoding="utf-8"))
    _assert_blind_artifact(artifact)
    assert artifact["status"] == "completed"
    assert artifact["trait_loss_only"] is True
    assert artifact["simulation_run_present"] is True
    assert artifact["asymmetric_protocol002_mutation_present"] is True
    assert artifact["source_support"] is True
    assert artifact["source_prepared"] is True
    assert artifact["projection_supported"] is True
    assert artifact["baseline_realised_high_trait_present"] is True
    assert artifact["eligible_for_trait_loss_denominator"] is True
    assert artifact["domain_selected"] is False
    assert artifact["type_s_result_claimed"] is False


def test_committed_stage2_smoke_does_not_overinterpret_non_event() -> None:
    artifact = json.loads(ARTIFACT_PATH.read_text(encoding="utf-8"))
    assert artifact["trait_loss_observed_post_baseline"] is False
    assert artifact["trait_loss_time_post_baseline"] is None
