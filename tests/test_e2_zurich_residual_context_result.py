import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUMMARY = json.loads((ROOT / "artifacts" / "empirical" / "e2_zurich_residual_context_locked_summary.json").read_text(encoding="utf-8"))
DOC = (ROOT / "manuscript" / "empirical_e2_zurich_residual_context_result.md").read_text(encoding="utf-8")


def test_all_fixed_zurich_endpoints_lack_detected_residual_context_information() -> None:
    assert SUMMARY["decision_counts"] == {
        "ecological_partial_state_incomplete": 0,
        "no_detected_residual_urban_information": 6,
    }
    assert len(SUMMARY["endpoint_results"]) == 6
    assert all(row["decision"] == "no_detected_residual_urban_information" for row in SUMMARY["endpoint_results"])


def test_zurich_result_keeps_equivalence_boundary() -> None:
    assert "not proof that the interaction state is sufficient" in SUMMARY["claim_boundary"].lower()
    assert "does **not** prove ecological equivalence" in DOC
    assert "absence of detected residual urban information" in DOC


def test_two_endpoints_show_context_augmented_prediction_worsened() -> None:
    wholly_negative = [
        row["endpoint"]
        for row in SUMMARY["endpoint_results"]
        if row["bootstrap_95_interval_mean_delta"][1] < 0
    ]
    assert wholly_negative == ["daucus_seed_set", "raphanus_seed_set"]


def test_zurich_empirical_provenance_is_locked() -> None:
    provenance = SUMMARY["provenance"]
    assert provenance["dataset_doi"] == "10.16904/envidat.676"
    assert provenance["workflow_run"] == 32701131992
    assert provenance["artifact_id"] == 9511364032
    assert provenance["artifact_digest"] == "sha256:7023a893fc63777790d1fc885f9adb62a5c80d74deae968619bce0df77313ed0"
