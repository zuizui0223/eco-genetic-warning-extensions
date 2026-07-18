from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_generated_figures_have_accessible_svg_metadata(tmp_path: Path) -> None:
    builder = _read("scripts/build_submission_bundle.py")
    assert 'role="img"' in builder
    assert '<title id="figure1-title">' in builder
    assert '<desc id="figure1-desc">' in builder
    assert '<title id="figure4-title">' in builder
    assert '<desc id="figure4-desc">' in builder

    from eco_genetic_warning_extensions.publication_figures import (
        _stage1_svg,
        write_stage3_figures,
    )
    from eco_genetic_warning_extensions.protocol002_publication_outputs import write_regime_svg

    stage1_rows = [
        {
            "kappa_mu": kappa,
            "p_star": p_star,
            "projection_supported_rate": 0.5,
            "projection_supported": 10,
            "attempted": 20,
        }
        for kappa in (0.05, 0.20, 0.35)
        for p_star in (0.10, 0.25, 0.50, 0.75, 0.90)
    ]
    rendered = {"figure2": _stage1_svg(stage1_rows)}

    endpoints = (
        "H_alpha_0.05", "H_alpha_0.10", "H_alpha_0.20",
        "H_gamma_0.05", "H_gamma_0.10", "H_gamma_0.20",
    )
    summary = {
        "domains": [
            {
                "domain": {"label": "symmetric_bridge"},
                "aggregate_ordering_across_six_endpoints": {"valid_pairs": 6, "lead": 5, "tie": 1, "lag": 0},
                "endpoint_summary": {key: {"median_positive_lead_time": 10} for key in endpoints},
            },
            {
                "domain": {"label": "directional_transition"},
                "aggregate_ordering_across_six_endpoints": {"valid_pairs": 6, "lead": 4, "tie": 1, "lag": 1},
                "endpoint_summary": {key: {"median_positive_lead_time": 5} for key in endpoints},
            },
        ]
    }
    summary_path = tmp_path / "summary.json"
    summary_path.write_text(json.dumps(summary), encoding="utf-8")
    write_stage3_figures(summary_path, tmp_path)
    rendered["figure5"] = (tmp_path / "figure5_stage3_ordering.svg").read_text(encoding="utf-8")
    rendered["figure6"] = (tmp_path / "figure6_stage3_lead_time.svg").read_text(encoding="utf-8")

    regime_rows = [
        {
            "kappa_mu": kappa,
            "p_star": p_star,
            "dominant_regime": "rapid-loss",
            "closest_pooled_trait_loss_rate": 0.8,
            "complete_candidate_count": 12,
        }
        for kappa in (0.05, 0.20, 0.35)
        for p_star in (0.10, 0.25, 0.50, 0.75, 0.90)
    ]
    figure3_path = tmp_path / "figure3.svg"
    write_regime_svg(regime_rows, figure3_path)
    rendered["figure3"] = figure3_path.read_text(encoding="utf-8")

    for identifier, svg in rendered.items():
        assert 'role="img"' in svg
        assert f'aria-labelledby="{identifier}-title {identifier}-desc"' in svg
        assert f'<title id="{identifier}-title">' in svg
        assert f'<desc id="{identifier}-desc">' in svg


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
