from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_generated_figures_have_accessible_svg_metadata() -> None:
    builder = _read("scripts/build_submission_bundle.py")
    stage_figures = _read("src/eco_genetic_warning_extensions/publication_figures.py")
    regime_map = _read("src/eco_genetic_warning_extensions/protocol002_publication_outputs.py")

    assert 'role="img"' in builder
    assert '<title id="figure1-title">' in builder
    assert '<desc id="figure1-desc">' in builder
    assert '<title id="figure4-title">' in builder
    assert '<desc id="figure4-desc">' in builder

    for identifier in ("figure2", "figure5", "figure6"):
        assert f'aria-labelledby="{identifier}-title {identifier}-desc"' in stage_figures
    assert 'aria-labelledby="figure3-title figure3-desc"' in regime_map


def test_all_colour_encodings_have_direct_text_redundancy() -> None:
    builder = _read("scripts/build_submission_bundle.py")
    stage_figures = _read("src/eco_genetic_warning_extensions/publication_figures.py")
    regime_map = _read("src/eco_genetic_warning_extensions/protocol002_publication_outputs.py")

    assert "('R', 'rapid loss'" in builder
    assert "('H', 'seed heterogeneous'" in builder
    assert "('P', 'persistence'" in builder
    assert "Direct labels R, H, and P" in builder

    assert "supported/planned attempts" in stage_figures
    assert "Every segment is directly labelled" in stage_figures
    assert 'codes = ["S", "D"]' in stage_figures
    assert '"rapid-loss": "R"' in regime_map
    assert '"seed-heterogeneous": "H"' in regime_map
    assert '"persistence": "P"' in regime_map


def test_publication_figure_titles_use_biological_language() -> None:
    stage_figures = _read("src/eco_genetic_warning_extensions/publication_figures.py")
    regime_map = _read("src/eco_genetic_warning_extensions/protocol002_publication_outputs.py")

    for stale_title in (
        "Stage I source-feasibility map",
        "Stage III warning ordering across six endpoints",
        "Stage III median positive lead time",
        "Protocol 002 trait-loss regimes",
    ):
        assert stale_title not in stage_figures
        assert stale_title not in regime_map

    assert "Source feasibility across transition coordinates" in stage_figures
    assert "Warning ordering in calibrated domains" in stage_figures
    assert "Median positive warning lead time" in stage_figures
    assert "Functional-loss regimes across transition coordinates" in regime_map


def test_bundle_includes_accessibility_and_metadata_documents() -> None:
    builder = _read("scripts/build_submission_bundle.py")
    review = _read("manuscript/figure_accessibility_review.md")
    metadata = _read("manuscript/submission_metadata.md")
    assert "figure_accessibility_review.md" in builder
    assert "submission_metadata.md" in builder
    assert "Every figure must remain interpretable without colour alone" in review
    assert "Data availability" in metadata
    assert "Code availability" in metadata
    assert "CRediT" in metadata
    assert "permanent archived release and DOI" in metadata
