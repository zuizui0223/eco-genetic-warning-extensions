from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_introduction_states_gap_and_identification_boundary() -> None:
    text = _read("manuscript/integrated_introduction.md")
    required = (
        "functional-trait loss",
        "warning portability across calibrated eco-genetic domains",
        "15/15 `no_domain_selected`",
        "candidate schedules",
        "not a matched single-factor experiment",
        "genetic-warning reliability is an emergent property",
    )
    for token in required:
        assert token in text


def test_discussion_contains_locked_stage3_contrast_and_limits() -> None:
    text = _read("manuscript/integrated_discussion.md")
    required = (
        "warning-blind",
        "candidate family",
        "horizon-normalized timing result",
        "cannot identify the isolated causal contribution of transition direction",
        "trajectory",
        "finite Type S evidence",
    )
    for token in required:
        assert token in text


def test_discussion_does_not_mislabel_effective_transition_parameter() -> None:
    text = _read("manuscript/integrated_discussion.md")
    assert "not an estimated nucleotide mutation rate" in text
    assert "directed adaptive mutation" in text
