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
    text = _read("manuscript/integrated_claim_evidence_map.md").lower()
    assert "not a universal" in text
    assert "not evidence that warning failed" in text
    assert "endpoint counts correlated within trajectories" in text
    assert "retrospective modification" in text
    assert "not pooled" in text or "pooled statistical test" in text


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
    assert "eco-genetic closure" in text.lower()


def test_main_text_uses_closure_first_identity() -> None:
    text = _read("manuscript/main_text.md")
    first_line = text.splitlines()[0]
    assert "Genetic warning emerges from eco-genetic closure" in first_line
    assert "### Stage I" not in text
    assert "### Stage II" not in text
    assert "### Stage III" not in text
    assert "not a portable property" in text


def test_workspace_does_not_present_mutation_direction_as_sole_novelty() -> None:
    text = _read("manuscript/README.md")
    assert "Genetic-warning reliability is not a portable property" in text
    assert "one mechanism that reshapes this closure" in text
    assert "Mutation direction governs genetic early-warning reliability" not in text


def test_submission_figure_one_is_closure_first() -> None:
    text = _read("scripts/build_submission_bundle.py")
    assert "Genetic warning emerges from eco-genetic closure" in text
    assert "figure1_eco_genetic_closure.svg" in text
    assert "figure1_mutation_coordinates.svg" not in text
    assert "Stage II candidate-regime composition" not in text
