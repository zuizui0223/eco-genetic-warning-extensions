from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_integrated_story_contains_locked_headline_results() -> None:
    text = _read("manuscript/integrated_story.md")
    required = (
        "2,269",
        "3,375",
        "20,250",
        "322",
        "242",
        "84",
        "323 lead",
        "12 lags",
        "106–112",
        "74–81",
    )
    for token in required:
        assert token in text


def test_integrated_claims_preserve_parent_extension_boundary() -> None:
    text = _read("manuscript/integrated_claim_evidence_map.md")
    assert "not a universal" in text.lower()
    assert "not evidence that warning failed" in text
    assert "endpoint counts correlated within trajectories" in text
    assert "retrospective modification" in text


def test_main_supplement_allocation_keeps_debug_history_out() -> None:
    text = _read("manuscript/main_vs_supplement.md")
    assert "implementation history" in text
    assert "temporary GitHub Actions outages" in text
    assert "out of both the main paper and scientific supplement" in text


def test_integrated_abstract_states_ecological_significance() -> None:
    text = _read("manuscript/integrated_abstract_and_outline.md")
    assert "functional-trait loss" in text
    assert "intervention time" in text
    assert "portable statistics" in text
