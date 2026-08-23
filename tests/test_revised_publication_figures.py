from __future__ import annotations

import csv
import json
from pathlib import Path

from eco_genetic_warning_extensions.revised_publication_figures import (
    figure2_parent_bridge_svg,
    figure3_source_regime_svg,
    figure4_r4_recovery_svg,
    figure5_connectivity_svg,
    figure6_portability_svg,
)

ROOT = Path(__file__).resolve().parents[1]


def _csv(path: Path):
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def _audit_fixture():
    rows = _csv(ROOT / "manuscript/tables/stage3_review_summary.csv")
    domains = {}
    for domain, horizon in (("recalibrated_symmetric_domain", 240), ("directional_calibrated_domain", 120)):
        cumulative = {}
        for row in (r for r in rows if r["domain"] == domain):
            endpoint = row["endpoint"]
            cumulative[endpoint] = {
                "baseline_eligible_completed": 82 if domain.startswith("recalibrated") else 81,
                "series": [
                    {"generation": 0, "warning_incidence": 0.0, "trait_loss_incidence": 0.0},
                    {"generation": horizon, "warning_incidence": 0.95 if domain.startswith("recalibrated") else 0.51, "trait_loss_incidence": 0.66 if domain.startswith("recalibrated") else 0.64},
                ],
            }
        domains[domain] = {"schedule": {"horizon": horizon}, "cumulative_event_incidence": cumulative}
    return {"domains": domains}


def test_figure2_uses_locked_parent_effects_and_warning_counts() -> None:
    svg = figure2_parent_bridge_svg(
        _csv(ROOT / "manuscript/tables/inherited_h3_effect_summary.csv"),
        _csv(ROOT / "manuscript/tables/inherited_h2_warning_summary.csv"),
    )
    assert "1,055 H1-qualified" in svg
    assert "99.86% median reduction" in svg
    assert "Relative Hα 5/10/20%" in svg
    assert "Lead 14" in svg and "Lag 6" in svg
    assert 'aria-labelledby="figure2-title figure2-desc"' in svg


def test_figure3_combines_source_and_loss_regime_maps() -> None:
    stage1 = []
    stage2 = []
    regimes = ("rapid-loss", "seed-heterogeneous", "persistence")
    for i, k in enumerate((0.05, 0.20, 0.35)):
        for j, p in enumerate((0.10, 0.25, 0.50, 0.75, 0.90)):
            stage1.append({"kappa_mu": k, "p_star": p, "projection_supported_rate": 0.45 + 0.02*j + 0.03*i, "projection_supported": 100, "attempted": 225})
            regime = regimes[min(2, (i+j)//3)]
            stage2.append({
                "kappa_mu": k, "p_star": p, "dominant_regime": regime,
                "closest_pooled_trait_loss_rate": 0.8 if regime == "rapid-loss" else 0.5 if regime == "seed-heterogeneous" else 0.1,
                "complete_candidate_count": 40,
                "rapid_loss_candidate_count": 22,
                "seed_heterogeneous_candidate_count": 6,
                "persistence_candidate_count": 12,
            })
    svg = figure3_source_regime_svg(stage1, stage2)
    assert "A. Source feasibility" in svg
    assert "B. Functional-loss regime" in svg
    assert "Original strict R4 candidates = 0" in svg
    assert 'aria-labelledby="figure3-title figure3-desc"' in svg


def test_figure4_renders_independent_r4_recovery() -> None:
    svg = figure4_r4_recovery_svg(
        _json(ROOT / "artifacts/frontier_refinement/phase_b_summary.json"),
        _json(ROOT / "artifacts/frontier_refinement/phase_c_summary.json"),
        _json(ROOT / "artifacts/frontier_refinement/phase_d_summary.json"),
    )
    assert "R4 operational band 0.30–0.70" in svg
    assert "0.350 C" in svg and "0.350 D" in svg
    assert "R4" in svg and "R3" in svg
    assert 'aria-labelledby="figure4-title figure4-desc"' in svg


def test_figure5_renders_connectivity_regimes_and_bidirectional_switches() -> None:
    svg = figure5_connectivity_svg(_json(ROOT / "artifacts/migration_condition/phase_e_summary.json"))
    assert "m=0.1" in svg and "m=0.2" in svg
    assert "switch 25/91" in svg
    assert "loss→no loss" in svg and "no loss→loss" in svg
    assert "allele-frequency mixing only" in svg
    assert 'aria-labelledby="figure5-title figure5-desc"' in svg


def test_figure6_retains_full_denominator_and_incidence() -> None:
    svg = figure6_portability_svg(
        _csv(ROOT / "manuscript/tables/stage3_review_summary.csv"),
        _audit_fixture(),
    )
    assert "valid 54/100" in svg
    assert "Hγ 20% warning" in svg
    assert "Recalibrated symmetric" in svg
    assert "Directional calibrated" in svg
    assert 'aria-labelledby="figure6-title figure6-desc"' in svg
