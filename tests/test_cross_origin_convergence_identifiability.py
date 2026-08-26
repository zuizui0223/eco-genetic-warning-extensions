import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_cross_origin_identifiability_result_is_locked():
    result = json.loads(
        (ROOT / "artifacts/empirical/cross_origin_convergence_identifiability.json").read_text(
            encoding="utf-8"
        )
    )
    assert result["decision"] == "cross_origin_convergence_not_identifiable_from_existing_archives"
    assert result["pooled_outcome_model_fitted"] is False
    assert all(not gate["pass"] for gate in result["gates"].values())
    assert result["stop_rules"]["generic_zscore_harmonization"] == "prohibited"
    assert result["stop_rules"]["origin_effect_when_origin_equals_study"] == "prohibited"


def test_cross_origin_story_preserves_claim_ceiling():
    prereg = (ROOT / "manuscript/empirical_cross_origin_convergence_preregistration.md").read_text(
        encoding="utf-8"
    )
    result = (ROOT / "manuscript/empirical_cross_origin_convergence_result.md").read_text(
        encoding="utf-8"
    )
    story = (ROOT / "manuscript/main_story_revision.md").read_text(encoding="utf-8")

    assert "origin is not perfectly confounded with study identity" in prereg
    assert "cross_origin_convergence_not_identifiable_from_existing_archives" in result
    assert "origin == study/protocol identity" in result
    assert "at least two independent island systems and two independent urban systems" in result
    assert "not identifiable from the current Honshu–Izu and Zurich archives" in story
    assert "design boundary, not evidence against convergence" in story
