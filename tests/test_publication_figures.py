from __future__ import annotations

import csv
import json
from pathlib import Path

import pytest

from eco_genetic_warning_extensions.publication_figures import aggregate_stage1, write_stage1_outputs, write_stage3_figures

ROOT = Path(__file__).resolve().parents[1]


def _batch(index: int) -> dict:
    coordinate_index = index // 9
    kappa_values = (0.05, 0.20, 0.35)
    p_values = (0.10, 0.25, 0.50, 0.75, 0.90)
    kappa_mu = kappa_values[coordinate_index // 5]
    p_star = p_values[coordinate_index % 5]
    supported = index % 26
    return {"stage":"Protocol 002 Stage I source reconstruction batch","campaign":{"batch_index":index,"attempts_per_batch":25},"cell":{"kappa_mu":kappa_mu,"p_star":p_star},"status_counts":{"source_supported":supported,"source_prepared":supported,"projection_supported":supported,"projection_failed":0,"projection_not_run":25-supported}}


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


def test_stage1_requires_complete_batch_coverage(tmp_path: Path) -> None:
    (tmp_path / "batch.json").write_text(json.dumps(_batch(0)), encoding="utf-8")
    with pytest.raises(ValueError, match="coverage mismatch"):
        aggregate_stage1(tmp_path)


def test_stage1_aggregation_and_svg_outputs(tmp_path: Path) -> None:
    raw = tmp_path / "raw"; raw.mkdir()
    for index in range(135):
        (raw / f"batch_{index:03d}.json").write_text(json.dumps(_batch(index)), encoding="utf-8")
    out = tmp_path / "out"; result = write_stage1_outputs(raw, out)
    assert result["batch_count"] == 135
    assert result["attempt_count"] == 3375
    assert result["coordinate_count"] == 15
    assert (out / "stage1_coordinate_summary.csv").exists()
    assert "<svg" in (out / "figure2_stage1_source_feasibility.svg").read_text(encoding="utf-8")


def test_stage3_figures_from_secondary_audit(tmp_path: Path) -> None:
    source = _stage3_audit_fixture(tmp_path); write_stage3_figures(source, tmp_path)
    fig4 = (tmp_path / "figure4_stage3_cumulative_incidence.svg").read_text(encoding="utf-8")
    fig5 = (tmp_path / "figure5_stage3_availability_ordering.svg").read_text(encoding="utf-8")
    fig6 = (tmp_path / "figure6_stage3_lead_time_normalized.svg").read_text(encoding="utf-8")
    assert "Cumulative warning and functional-loss incidence" in fig4
    assert "100 attempted" in fig5
    assert "valid pairs=54/100" in fig5
    assert ">generations<" in fig6
    assert "fraction of calibrated horizon" in fig6
    assert "Recalibrated symmetric domain" in fig6
    assert "Directional calibrated domain" in fig6
    assert ">50<" in fig6 and ">100<" in fig6 and ">150<" in fig6
    assert ">37<" not in fig6 and ">74<" not in fig6
    assert "all six horizon-normalized 95% intervals include 0" in fig6
