from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_introduction_states_gap_and_nonportable_warning_claim() -> None:
    text = _read("manuscript/integrated_introduction.md")
    required = (
        "functional persistence",
        "same trajectory",
        "independent seed families",
        "genetic-warning reliability is an emergent property",
        "not portable statistics",
    )
    for token in required:
        assert token in text


def test_discussion_contains_locked_stage3_contrast_and_limits() -> None:
    text = _read("manuscript/integrated_discussion.md")
    required = (
        "323 leads",
        "12 lags",
        "106–112",
        "74–81",
        "not independent replicates",
        "finite Type S evidence",
        "does not establish a universal theorem",
    )
    for token in required:
        assert token in text


def test_discussion_does_not_mislabel_effective_transition_parameter() -> None:
    text = _read("manuscript/integrated_discussion.md")
    assert "should not be interpreted as an empirically estimated nucleotide mutation rate" in text
    assert "directed adaptive mutation" in text
