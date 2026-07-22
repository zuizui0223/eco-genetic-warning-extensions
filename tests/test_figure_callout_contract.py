from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_main_text_calls_every_main_figure() -> None:
    text = _read("manuscript/main_text.md")
    for number in range(1, 7):
        assert f"Figure {number}" in text or f"Figures {number}" in text


def test_display_allocation_matches_current_figure_captions() -> None:
    allocation = _read("manuscript/main_vs_supplement.md")
    captions = _read("manuscript/figure_captions.md")

    expected = {
        1: ("eco-genetic mechanism", "Genetic warning emerges from eco-genetic closure"),
        2: ("source feasibility across transition coordinates", "High-trait source feasibility depends on transition closure"),
        3: ("functional-loss regimes across transition coordinates", "Transition direction separates rapid-loss, persistence, and seed-heterogeneous regimes"),
        4: ("candidate composition within transition coordinates", "Pooled event frequency can conceal opposing seed-level regimes"),
        5: ("warning ordering in calibrated domains", "Warning ordering is closure-dependent after independent calibration"),
        6: ("usable warning lead time", "Directional transition shortens usable intervention time"),
    }

    for number, (allocation_title, caption_title) in expected.items():
        assert f"### Figure {number} — {allocation_title}" in allocation
        assert f"## Figure {number}. {caption_title}" in captions


def test_supplementary_table_links_use_current_figure_numbers() -> None:
    allocation = _read("manuscript/main_vs_supplement.md")
    assert "underlying Figure 2" in allocation
    assert "underlying Figures 3–4" in allocation
    assert "underlying Figures 5–6" in allocation
    assert "underlying Figure 3" not in allocation
