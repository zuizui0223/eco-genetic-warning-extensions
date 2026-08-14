from pathlib import Path
import csv
import json


ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def _stage3_audit_fixture(tmp_path: Path) -> Path:
    rows=list(csv.DictReader((ROOT / "manuscript/tables/stage3_review_summary.csv").open(encoding="utf-8")))
    domains={}
    for domain,horizon in (("recalibrated_symmetric_domain",240),("directional_calibrated_domain",120)):
        endpoints={}; endpoint_ci={}; cumulative={}
        for row in (r for r in rows if r["domain"]==domain):
            endpoint=row["endpoint"]
            counts={key:int(row[key]) for key in ("source_preparation_failed","baseline_ineligible","both_censored","warning_censored","trait_loss_censored","lead","tie","lag")}
            endpoints[endpoint]={"counts":counts,"attempted":100,"valid_pairs":int(row["valid_pairs"]),"positive_leads":int(row["positive_leads"]),"median_positive_lead_time":float(row["median_positive_lead_time"]),"median_positive_lead_fraction_of_horizon":float(row["median_positive_lead_fraction_of_horizon"])}
            endpoint_ci[endpoint]={"median_positive_lead_time":{"lower":float(row["median_positive_lead_time_ci_lower"]),"median":float(row["median_positive_lead_time"]),"upper":float(row["median_positive_lead_time_ci_upper"])},"median_positive_lead_fraction_of_horizon":{"lower":float(row["median_positive_lead_fraction_of_horizon_ci_lower"]),"median":float(row["median_positive_lead_fraction_of_horizon"]),"upper":float(row["median_positive_lead_fraction_of_horizon_ci_upper"])}}
            cumulative[endpoint]={"baseline_eligible_completed":82 if domain.startswith("recalibrated") else 81,"horizon":horizon,"series":[{"generation":0,"warning_incidence":0.0,"trait_loss_incidence":0.0},{"generation":horizon,"warning_incidence":1.0 if domain.startswith("recalibrated") else 0.7,"trait_loss_incidence":0.66 if domain.startswith("recalibrated") else 0.64}]}
        domains[domain]={"schedule":{"horizon":horizon},"endpoints":endpoints,"endpoint_bootstrap_95_ci":endpoint_ci,"cumulative_event_incidence":cumulative}
    path=tmp_path/"audit.json"; path.write_text(json.dumps({"domains":domains}),encoding="utf-8"); return path


def test_generated_figures_have_accessible_svg_metadata(tmp_path: Path) -> None:
    builder = _read("scripts/build_submission_bundle.py")
    assert 'role="img"' in builder
    assert '<title id="figure1-title">' in builder
    assert '<desc id="figure1-desc">' in builder

    from eco_genetic_warning_extensions.publication_figures import _stage1_svg, write_stage3_figures
    from eco_genetic_warning_extensions.protocol002_publication_outputs import write_regime_svg

    stage1_rows = [{"kappa_mu":kappa,"p_star":p_star,"projection_supported_rate":0.5,"projection_supported":10,"attempted":20} for kappa in (0.05,0.20,0.35) for p_star in (0.10,0.25,0.50,0.75,0.90)]
    rendered={"figure2":_stage1_svg(stage1_rows)}
    write_stage3_figures(_stage3_audit_fixture(tmp_path),tmp_path)
    rendered["figure4"]=(tmp_path/"figure4_stage3_cumulative_incidence.svg").read_text(encoding="utf-8")
    rendered["figure5"]=(tmp_path/"figure5_stage3_availability_ordering.svg").read_text(encoding="utf-8")
    rendered["figure6"]=(tmp_path/"figure6_stage3_lead_time_normalized.svg").read_text(encoding="utf-8")

    regime_rows=[{"kappa_mu":kappa,"p_star":p_star,"dominant_regime":"rapid-loss","closest_pooled_trait_loss_rate":0.8,"complete_candidate_count":12,"rapid_loss_candidate_count":8,"seed_heterogeneous_candidate_count":2,"persistence_candidate_count":2} for kappa in (0.05,0.20,0.35) for p_star in (0.10,0.25,0.50,0.75,0.90)]
    figure3_path=tmp_path/"figure3.svg"; write_regime_svg(regime_rows,figure3_path); rendered["figure3"]=figure3_path.read_text(encoding="utf-8")

    for identifier,svg in rendered.items():
        assert 'role="img"' in svg
        assert f'aria-labelledby="{identifier}-title {identifier}-desc"' in svg
        assert f'<title id="{identifier}-title">' in svg
        assert f'<desc id="{identifier}-desc">' in svg


def test_all_colour_encodings_have_direct_text_redundancy() -> None:
    stage_figures=_read("src/eco_genetic_warning_extensions/publication_figures.py")
    regime_map=_read("src/eco_genetic_warning_extensions/protocol002_publication_outputs.py")
    assert "supported/planned attempts" in stage_figures
    assert "valid " in stage_figures
    assert "SF" in stage_figures and "BI" in stage_figures and "WC" in stage_figures
    assert '"rapid-loss": "R"' in regime_map
    assert '"seed-heterogeneous": "H"' in regime_map
    assert '"persistence": "P"' in regime_map
    assert "Complete-candidate composition" in regime_map


def test_publication_figure_titles_use_biological_language() -> None:
    stage_figures=_read("src/eco_genetic_warning_extensions/publication_figures.py")
    regime_map=_read("src/eco_genetic_warning_extensions/protocol002_publication_outputs.py")
    for stale_title in ("Stage I source-feasibility map","Stage III warning ordering across six endpoints","Stage III median positive lead time","Protocol 002 trait-loss regimes","Warning ordering in calibrated domains"):
        assert stale_title not in stage_figures
        assert stale_title not in regime_map
    assert "Source feasibility across transition coordinates" in stage_figures
    assert "Cumulative warning and functional-loss incidence" in stage_figures
    assert "Warning availability, censoring and ordering" in stage_figures
    assert "Positive warning lead time before functional-trait loss" in stage_figures
    assert "Functional-loss regimes across transition coordinates" in regime_map


def test_bundle_includes_accessibility_and_metadata_documents() -> None:
    builder=_read("scripts/build_submission_bundle.py")
    review=_read("manuscript/figure_accessibility_review.md")
    metadata=_read("manuscript/submission_metadata.md")
    assert "figure_accessibility_review.md" in builder
    assert "submission_metadata.md" in builder
    assert "Every figure must remain interpretable without colour alone" in review
    assert "Data availability" in metadata
    assert "Code availability" in metadata
    assert "CRediT" in metadata
    assert "permanent archived release and DOI" in metadata
