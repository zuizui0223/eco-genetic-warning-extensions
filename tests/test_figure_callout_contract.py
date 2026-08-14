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
        1: ("eco-genetic causal architecture", "Genetic warning emerges from eco-genetic closure"),
        2: ("source feasibility across recurrent-transition coordinates", "High-trait source feasibility depends on recurrent-transition coordinates"),
        3: ("functional-loss regimes plus complete-candidate composition", "The common deterioration family separates rapid-loss, heterogeneous, and persistence regimes"),
        4: ("cumulative warning and functional-loss incidence", "Cumulative warning and functional-loss incidence across calibrated horizons"),
        5: ("full attempted denominator, censoring, and ordering", "Warning availability, censoring, and ordering across the full attempted denominator"),
        6: ("absolute and horizon-normalized positive lead time", "Absolute and horizon-normalized positive warning lead time"),
    }
    for number, (allocation_title, caption_title) in expected.items():
        assert f"### Figure {number} — {allocation_title}" in allocation
        assert f"## Figure {number}. {caption_title}" in captions


def test_supplementary_table_links_use_current_figure_numbers() -> None:
    allocation = _read("manuscript/main_vs_supplement.md")
    assert "underlying Figure 2" in allocation
    assert "underlying Figures 4–6" in allocation
    assert "Table S4" in allocation
    assert "Table S5" in allocation
