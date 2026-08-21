from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_main_manuscript_states_gap_and_identification_boundary() -> None:
    text = _read("manuscript/main_text.md")
    lower = text.lower()
    for token in (
        "functional-trait loss",
        "warning estimability",
        "no_domain_selected",
        "not a single-factor effect of transition direction",
        "eco-genetic",
    ):
        assert token in lower


def test_main_discussion_keeps_calibration_and_portability_limits() -> None:
    text = _read("manuscript/main_text.md")
    lower = text.lower()
    for token in (
        "warning-blind",
        "candidate family",
        "horizon",
        "not a single-factor effect of transition direction",
        "trajectory",
        "right-censored",
    ):
        assert token in lower


def test_main_manuscript_does_not_mislabel_effective_transition_parameter() -> None:
    text = _read("manuscript/main_text.md")
    lower = text.lower()
    assert "not an empirical mutation-rate estimate" in lower
    assert "directed adaptive mutation" not in lower
