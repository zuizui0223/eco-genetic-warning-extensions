import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUMMARY = json.loads((ROOT / "artifacts" / "cross_layer_alignment" / "phase_v_locked_summary.json").read_text(encoding="utf-8"))
DOC = (ROOT / "docs" / "CROSS_LAYER_ALIGNMENT_PHASE_V_STATUS.md").read_text(encoding="utf-8")


def test_alignment_changes_transition_with_identical_coarse_marginals() -> None:
    opening = SUMMARY["opening_certificate"]
    assert opening["coarse_marginal_signatures_identical"] is True
    assert opening["coarse_marginals_are_transition_sufficient"] is False
    assert opening["maximum_patchwise_generation1_difference"] > 0.25
    assert opening["aligned_cross_layer_covariance"] > 0
    assert opening["anti_aligned_cross_layer_covariance"] < 0


def test_alignment_does_not_overclaim_long_horizon_loss_effect() -> None:
    assert SUMMARY["aligned"]["pooled_trait_loss_rate"] == 0.678
    assert SUMMARY["anti_aligned"]["pooled_trait_loss_rate"] == 0.722
    assert SUMMARY["paired"]["mcnemar_exact_p"] > 0.05
    assert SUMMARY["decision"] == "coarse_marginals_not_transition_sufficient_but_no_detected_loss_incidence_effect"
    assert "not supported" in DOC
    assert "not be treated as a universally directional risk score" in DOC


def test_alignment_provenance_and_stop_rule_are_locked() -> None:
    assert SUMMARY["workflow_run_id"] == 32636913615
    assert SUMMARY["artifact_id"] == 9492558602
    assert SUMMARY["artifact_digest"] == "sha256:a5754ab2d54dea868a72fed582a9862cbc88b83510e1cf81e0a872f56b70a1bd"
    assert "No replacement seeds" in SUMMARY["stop_rule"]
