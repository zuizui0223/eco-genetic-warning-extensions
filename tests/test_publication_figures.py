from __future__ import annotations

import json
from pathlib import Path

import pytest

from eco_genetic_warning_extensions.publication_figures import aggregate_stage1, write_stage1_outputs, write_stage3_figures


def _batch(index: int) -> dict:
    coordinate_index = index // 9
    kappa_values = (0.05, 0.20, 0.35)
    p_values = (0.10, 0.25, 0.50, 0.75, 0.90)
    kappa_mu = kappa_values[coordinate_index // 5]
    p_star = p_values[coordinate_index % 5]
    supported = index % 26
    return {
        "stage": "Protocol 002 Stage I source reconstruction batch",
        "campaign": {"batch_index": index, "attempts_per_batch": 25},
        "cell": {"kappa_mu": kappa_mu, "p_star": p_star},
        "status_counts": {
            "source_supported": supported,
            "source_prepared": supported,
            "projection_supported": supported,
            "projection_failed": 0,
            "projection_not_run": 25 - supported,
        },
    }


def test_stage1_requires_complete_batch_coverage(tmp_path: Path) -> None:
    (tmp_path / "batch.json").write_text(json.dumps(_batch(0)), encoding="utf-8")
    with pytest.raises(ValueError, match="coverage mismatch"):
        aggregate_stage1(tmp_path)


def test_stage1_aggregation_and_svg_outputs(tmp_path: Path) -> None:
    raw = tmp_path / "raw"
    raw.mkdir()
    for index in range(135):
        (raw / f"batch_{index:03d}.json").write_text(json.dumps(_batch(index)), encoding="utf-8")
    out = tmp_path / "out"
    result = write_stage1_outputs(raw, out)
    assert result["batch_count"] == 135
    assert result["attempt_count"] == 3375
    assert result["coordinate_count"] == 15
    assert (out / "stage1_coordinate_summary.csv").exists()
    assert "<svg" in (out / "figure2_stage1_source_feasibility.svg").read_text(encoding="utf-8")


def test_stage3_figures_from_locked_summary(tmp_path: Path) -> None:
    summary = {
        "domains": [
            {
                "domain": {"label": "symmetric_bridge"},
                "aggregate_ordering_across_six_endpoints": {"valid_pairs": 2, "lead": 2, "tie": 0, "lag": 0},
                "endpoint_summary": {key: {"median_positive_lead_time": 10} for key in ("H_alpha_0.05", "H_alpha_0.10", "H_alpha_0.20", "H_gamma_0.05", "H_gamma_0.10", "H_gamma_0.20")},
            },
            {
                "domain": {"label": "transition"},
                "aggregate_ordering_across_six_endpoints": {"valid_pairs": 2, "lead": 1, "tie": 0, "lag": 1},
                "endpoint_summary": {key: {"median_positive_lead_time": 5} for key in ("H_alpha_0.05", "H_alpha_0.10", "H_alpha_0.20", "H_gamma_0.05", "H_gamma_0.10", "H_gamma_0.20")},
            },
        ]
    }
    source = tmp_path / "summary.json"
    source.write_text(json.dumps(summary), encoding="utf-8")
    write_stage3_figures(source, tmp_path)
    assert "lead 2" in (tmp_path / "figure5_stage3_ordering.svg").read_text(encoding="utf-8")
    assert "symmetric_bridge" in (tmp_path / "figure6_stage3_lead_time.svg").read_text(encoding="utf-8")
