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
        1: ("eco-genetic causal architecture and four-question hierarchy", "Eco-genetic causal architecture and four-question hierarchy"),
        2: ("fragmentation creates vulnerability; event-only warning ordering lacks discrimination", "Fragmentation creates vulnerability; event-only warning ordering lacks discrimination"),
        3: ("recurrent state turnover reorganises source feasibility and historical loss-screen placement", "Recurrent state turnover reorganises source feasibility and historical loss-screen placement"),
        4: ("high-precision recurrent-turnover incidence frontier", "High-precision recurrent-turnover incidence frontier"),
        5: ("historical allele-mixing heterogeneity and fresh non-replication", "Historical allele-mixing heterogeneity failed fresh-seed replication"),
        6: ("portability after downstream loss conditions are separately recovered", "Portability after downstream loss conditions are separately recovered"),
    }
    for number, (allocation_title, caption_title) in expected.items():
        assert f"### Figure {number} — {allocation_title}" in allocation
        assert f"## Figure {number}. {caption_title}" in captions


def test_supplementary_table_links_follow_current_figure_spine() -> None:
    allocation = _read("manuscript/display_allocation.md")
    assert "Table S1 retains the paired fragmentation effect sizes" in allocation
    assert "Tables S3–S4 retain the coordinate and candidate records" in allocation
    assert "Table S6 retains the high-precision frontier records" in allocation
    assert "Table S6 retains both historical and fresh connectivity records" in allocation
    assert "Table S5 retains the endpoint, censoring and timing audit" in allocation
    assert "Table S7 retains warning validity" in allocation
    assert "Table S8 retains the exploratory continuous landmark audit" in allocation
