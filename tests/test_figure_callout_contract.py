from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_main_text_calls_every_main_figure() -> None:
    # The publication main_text remains the pre-promotion source until the
    # condition-recovered draft is fully QA'd, so keep the six-display contract
    # on that source during transition.
    text = _read("manuscript/main_text.md")
    for number in range(1, 7):
        assert f"Figure {number}" in text or f"Figures {number}" in text


def test_display_allocation_matches_current_figure_captions() -> None:
    allocation = _read("manuscript/main_vs_supplement.md")
    captions = _read("manuscript/figure_captions.md")
    expected = {
        1: ("eco-genetic causal architecture and four-question hierarchy", "Eco-genetic causal architecture and four-question hierarchy"),
        2: ("fragmentation creates vulnerability and genetic warning is conditionally possible", "Fragmentation creates vulnerability and genetic warning is conditionally possible"),
        3: ("recurrent state turnover reorganises source feasibility and functional-loss regime", "Recurrent state turnover reorganises source feasibility and functional-loss regime"),
        4: ("warning-blind recovery of a narrow R4 event regime", "Warning-blind recovery of a narrow reproducible event regime"),
        5: ("effective genetic connectivity changes event-regime estimability", "Effective genetic connectivity changes event-regime estimability"),
        6: ("portability after evaluability is separately recovered", "Portability after evaluability is separately recovered"),
    }
    for number, (allocation_title, caption_title) in expected.items():
        assert f"### Figure {number} — {allocation_title}" in allocation
        assert f"## Figure {number}. {caption_title}" in captions


def test_supplementary_table_links_follow_recovered_figure_spine() -> None:
    allocation = _read("manuscript/main_vs_supplement.md")
    assert "Table S1 retains the paired fragmentation effect sizes underlying Figure 2" in allocation
    assert "Tables S3–S4 retain the coordinate and candidate records underlying Figure 3" in allocation
    assert "Table S6 contains the high-rep frontier records underlying Figure 4" in allocation
    assert "Table S6 contains the migration-level and paired-switch records underlying Figure 5" in allocation
    assert "Table S5 contains the endpoint, censoring and timing audit underlying Figure 6" in allocation
