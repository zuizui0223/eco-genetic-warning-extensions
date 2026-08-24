import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUMMARY = json.loads((ROOT / "artifacts" / "empirical" / "e1_izu_residual_origin_locked_summary.json").read_text(encoding="utf-8"))
DOC = (ROOT / "manuscript" / "empirical_e1_residual_origin_result.md").read_text(encoding="utf-8")


def test_e1_distance_does_not_improve_transfer_after_partial_state() -> None:
    assert SUMMARY["decision"] == "ecological_partial_state_convergence_supported"
    contrast = SUMMARY["C2_vs_C1"]
    assert contrast["C2_lower_mse_fold_count"] == 3
    assert contrast["row_weighted_mse_change_C2_minus_C1"] > 0
    assert contrast["row_weighted_mse_percent_change"] > 4.0


def test_e1_partial_state_strength_caveat_is_retained() -> None:
    assert SUMMARY["C1_vs_C0"]["C1_lower_mse_fold_count"] == 4
    assert SUMMARY["C1_vs_C0"]["row_weighted_mse_change_C1_minus_C0"] < 0
    assert "only modestly" in SUMMARY["decision_caveat"]
    assert "not a strong or complete compression" in DOC


def test_e1_source_and_analysis_are_locked() -> None:
    source = SUMMARY["source_lock"]
    analysis = SUMMARY["analysis_lock"]
    assert source["doi"] == "10.6084/m9.figshare.25025000.v1"
    assert source["discovery_workflow_run"] == 32698949654
    assert source["discovery_artifact_id"] == 9510855695
    assert source["discovery_artifact_digest"] == "sha256:5589e73dcf417122f844d8abe5583d8fa16a848838d206ef6ea4af75c987fb23"
    assert analysis["runner_blob_sha"] == "0cd94722d2559ab868c58dc46314809a68f4fd3c"
    assert analysis["row_count"] == 572
    assert analysis["site_count"] == 8


def test_e1_does_not_claim_full_ecogenetic_convergence() -> None:
    lower = SUMMARY["claim_boundary"].lower()
    assert "does not show that c1 is a complete sufficient state" in lower
    assert "g/c/r/m are not synchronized" in lower
    assert "do not yet establish full urban–island convergence" in DOC
