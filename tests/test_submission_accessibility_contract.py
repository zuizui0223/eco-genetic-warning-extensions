from pathlib import Path
import csv
import json


ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def _csv(path: str):
    with (ROOT / path).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _stage3_audit_fixture():
    rows = _csv("manuscript/tables/stage3_review_summary.csv")
    domains = {}
    for domain, horizon in (("recalibrated_symmetric_domain", 240), ("directional_calibrated_domain", 120)):
        cumulative = {}
        for row in (r for r in rows if r["domain"] == domain):
            cumulative[row["endpoint"]] = {
                "baseline_eligible_completed": 82 if domain.startswith("recalibrated") else 81,
                "series": [
                    {"generation": 0, "warning_incidence": 0.0, "trait_loss_incidence": 0.0},
                    {"generation": horizon, "warning_incidence": 0.95 if domain.startswith("recalibrated") else 0.51, "trait_loss_incidence": 0.66 if domain.startswith("recalibrated") else 0.64},
                ],
            }
        domains[domain] = {"schedule": {"horizon": horizon}, "cumulative_event_incidence": cumulative}
    return {"domains": domains}


def test_revised_generated_figures_have_accessible_svg_metadata() -> None:
    from eco_genetic_warning_extensions.condition_figure1 import figure1_estimability_svg
    from eco_genetic_warning_extensions.revised_publication_figures import (
        figure2_parent_bridge_svg,
        figure3_source_regime_svg,
        figure4_r4_recovery_svg,
        figure5_connectivity_svg,
        figure6_portability_svg,
    )

    stage1_rows = []
    stage2_rows = []
    for i, kappa in enumerate((0.05, 0.20, 0.35)):
        for j, p_star in enumerate((0.10, 0.25, 0.50, 0.75, 0.90)):
            stage1_rows.append({"kappa_mu": kappa, "p_star": p_star, "projection_supported_rate": 0.5, "projection_supported": 100, "attempted": 225})
            stage2_rows.append({
                "kappa_mu": kappa, "p_star": p_star,
                "dominant_regime": "seed-heterogeneous",
                "closest_pooled_trait_loss_rate": 0.5,
                "complete_candidate_count": 40,
                "rapid_loss_candidate_count": 22,
                "seed_heterogeneous_candidate_count": 6,
                "persistence_candidate_count": 12,
            })

    rendered = {
        "figure1": figure1_estimability_svg(),
        "figure2": figure2_parent_bridge_svg(
            _csv("manuscript/tables/inherited_h3_effect_summary.csv"),
            _csv("manuscript/tables/inherited_h2_warning_summary.csv"),
        ),
        "figure3": figure3_source_regime_svg(stage1_rows, stage2_rows),
        "figure4": figure4_r4_recovery_svg(
            json.loads((ROOT / "artifacts/frontier_refinement/phase_b_summary.json").read_text()),
            json.loads((ROOT / "artifacts/frontier_refinement/phase_c_summary.json").read_text()),
            json.loads((ROOT / "artifacts/frontier_refinement/phase_d_summary.json").read_text()),
        ),
        "figure5": figure5_connectivity_svg(
            json.loads((ROOT / "artifacts/migration_condition/phase_e_summary.json").read_text())
        ),
        "figure6": figure6_portability_svg(
            _csv("manuscript/tables/stage3_review_summary.csv"), _stage3_audit_fixture()
        ),
    }
    for identifier, svg in rendered.items():
        assert 'role="img"' in svg
        assert f'aria-labelledby="{identifier}-title {identifier}-desc"' in svg
        assert f'<title id="{identifier}-title">' in svg
        assert f'<desc id="{identifier}-desc">' in svg


def test_revised_colour_encodings_have_direct_text_redundancy() -> None:
    source = _read("src/eco_genetic_warning_extensions/revised_publication_figures.py")
    figure1 = _read("src/eco_genetic_warning_extensions/condition_figure1.py")
    assert "R1/R2/R3/R4" in figure1
    assert "median reduction" in source
    assert "closest P=" in source
    assert '"R"' in source and '"H"' in source and '"P"' in source
    assert "R4 operational band 0.30–0.70" in source
    assert "loss→no loss" in source and "no loss→loss" in source
    assert "valid " in source


def test_revised_publication_figure_titles_use_biological_language() -> None:
    source = _read("src/eco_genetic_warning_extensions/revised_publication_figures.py")
    figure1 = _read("src/eco_genetic_warning_extensions/condition_figure1.py")
    expected = (
        "Eco-genetic causal architecture and four-question hierarchy",
        "Fragmentation creates vulnerability; event-only warning ordering lacks discrimination",
        "Recurrent state turnover reorganises source feasibility and functional-loss regime",
        "Warning-blind recovery of a narrow reproducible event regime",
        "Effective genetic connectivity changes event-regime estimability",
        "Portability after evaluability is separately recovered",
    )
    combined = figure1 + source
    for title in expected:
        assert title in combined
    for stale_title in (
        "Stage I source-feasibility map",
        "Stage III warning ordering across six endpoints",
        "Stage III median positive lead time",
    ):
        assert stale_title not in combined


def test_bundle_replacement_declares_main_and_supplementary_figure_sets() -> None:
    replacement = _read("scripts/replace_submission_figures.py")
    workflow = _read(".github/workflows/paper-completion-sprint.yml")
    assert "figure1_eco_genetic_estimability.svg" in replacement
    assert "figure4_r4_recovery.svg" in replacement
    assert "figure5_connectivity_estimability.svg" in replacement
    assert "figure6_portability.svg" in replacement
    assert "figure_s3_stage3_lead_time_normalized.svg" in replacement
    assert 'wc -l)" -eq 6' in workflow
    assert 'submission_bundle/supplement' in workflow


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
