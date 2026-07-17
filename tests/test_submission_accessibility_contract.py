from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_generated_figures_have_accessible_svg_metadata() -> None:
    builder = _read("scripts/build_submission_bundle.py")
    assert 'role="img"' in builder
    assert '<title id="figure1-title">' in builder
    assert '<desc id="figure1-desc">' in builder
    assert '<title id="figure4-title">' in builder
    assert '<desc id="figure4-desc">' in builder


def test_regime_composition_has_non_colour_encoding() -> None:
    builder = _read("scripts/build_submission_bundle.py")
    assert "('R', 'rapid loss'" in builder
    assert "('H', 'seed heterogeneous'" in builder
    assert "('P', 'persistence'" in builder
    assert "Direct labels R, H, and P" in builder


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
