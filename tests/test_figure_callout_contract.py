from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_main_text_calls_every_main_figure() -> None:
    text = _read("manuscript/main_text.md")
    for number in range(1, 7):
        assert f"Figure {number}" in text or f"Figures {number}" in text


def test_display_allocation_matches_current_figure_captions() -> None:
    allocation = _read("manuscript/display_allocation.md")
    captions = _read("manuscript/figure_captions.md")
    expected = {
        1: ("eco-genetic causal architecture from function to warning", "Eco-genetic causal architecture from function to warning"),
        2: ("fragmentation creates vulnerability and genetic warning is conditionally possible", "Fragmentation creates vulnerability and genetic warning is conditionally possible"),
        3: ("recurrent state turnover reorganises source feasibility and functional-loss outcomes", "Recurrent state turnover reorganises source feasibility and functional-loss outcomes"),
        4: ("finite calibration certificates and their sampling boundary", "Finite calibration certificates and their sampling boundary"),
        5: ("connectivity and interaction processes reshape different layers of functional loss", "Connectivity and interaction processes reshape different layers of functional loss"),
        6: ("portability after loss-process characterisation", "Portability after loss-process characterisation"),
    }
    for number, (allocation_title, caption_title) in expected.items():
        assert f"### Figure {number} — {allocation_title}" in allocation
        assert f"## Figure {number}. {caption_title}" in captions


def test_supplementary_links_follow_distributional_figure_spine() -> None:
    allocation = _read("manuscript/display_allocation.md")
    assert "Table S1 retains the paired fragmentation effect sizes underlying Figure 2" in allocation
    assert "Tables S3–S4 retain the coordinate and candidate records underlying Figure 3" in allocation
    assert "Table S6 contains the historical frontier records and Phase-J block/panel diagnostics" in allocation
    assert "Table S6 and machine-readable Phase E–J summaries retain the detailed condition records" in allocation
    assert "Table S5 contains the endpoint, censoring and timing audit underlying Figure 6" in allocation


def test_phase_j_reframes_r4_as_finite_certificate_in_display_contract() -> None:
    allocation = _read("manuscript/display_allocation.md").lower()
    captions = _read("manuscript/figure_captions.md").lower()
    for text in (allocation, captions):
        assert "finite-panel calibration certificate" in text
        assert "sample-size-invariant biological regime" in text
    assert "75%" in captions and "25%" in captions
    assert "network state, process-resolved connectivity, mean loss incidence and among-block heterogeneity" in captions
