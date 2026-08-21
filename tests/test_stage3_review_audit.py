from __future__ import annotations

import csv
import json
import statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _rows():
    with (ROOT / "manuscript/tables/stage3_review_summary.csv").open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _differences():
    with (ROOT / "manuscript/tables/stage3_between_domain_differences.csv").open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def test_secondary_audit_locks_domain_differences_and_uncertainty() -> None:
    lock = json.loads((ROOT / "reproducibility/upstream-lock.json").read_text(encoding="utf-8"))
    review = lock["secondary_review_audit"]
    sym = review["corrected_publication_timing"]["recalibrated_symmetric_domain"]
    directional = review["corrected_publication_timing"]["directional_calibrated_domain"]
    assert sym["horizon"] == 240
    assert directional["horizon"] == 120
    rows = _rows()
    assert len(rows) == 12
    sym_rows = [r for r in rows if r["domain"] == "recalibrated_symmetric_domain"]
    dir_rows = [r for r in rows if r["domain"] == "directional_calibrated_domain"]
    assert sum(int(r["valid_pairs"]) for r in sym_rows) == 324
    assert sum(int(r["valid_pairs"]) for r in dir_rows) == 201
    assert sum(int(r["lag"]) for r in dir_rows) == 12


def test_historical_even_n_median_is_corrected_in_secondary_summary() -> None:
    rows = {(r["domain"], r["endpoint"]): r for r in _rows()}
    assert float(rows[("recalibrated_symmetric_domain", "H_alpha_0.20")]["median_positive_lead_time"]) == 107.5
    assert float(rows[("recalibrated_symmetric_domain", "H_gamma_0.20")]["median_positive_lead_time"]) == 106.0
    assert statistics.median([107, 108]) == 107.5


def test_direct_between_domain_bootstrap_is_reported_without_interval_overlap_heuristic() -> None:
    rows = {row["endpoint"]: row for row in _differences()}
    assert set(rows) == {
        "H_alpha_0.05", "H_alpha_0.10", "H_alpha_0.20",
        "H_gamma_0.05", "H_gamma_0.10", "H_gamma_0.20",
    }
    separated_absolute = {
        endpoint
        for endpoint, row in rows.items()
        if row["absolute_generations_ci_includes_zero"] == "False"
    }
    assert separated_absolute == {"H_alpha_0.05", "H_alpha_0.10"}
    assert all(row["horizon_fraction_ci_includes_zero"] == "True" for row in rows.values())
    assert all(
        float(row["horizon_fraction_difference_directional_minus_symmetric"]) > 0
        for row in rows.values()
    )


def test_manuscript_discloses_identification_boundary_and_uncertainty() -> None:
    text = (ROOT / "manuscript/main_text.md").read_text(encoding="utf-8")
    lower = text.lower()
    forbidden = (
        "altered only recurrent transition direction",
        "changing one genetic boundary condition while holding the ecological life cycle fixed",
        "shortened the intervention window in the tested closure",
    )
    for phrase in forbidden:
        assert phrase not in lower

    required = (
        "portability across calibrated eco-genetic domains",
        "0.540",
        "0.335",
        "conditional positive lead-time medians",
        "all six direct timing-difference intervals included zero",
        "the domains also differ in ecological parameters and deterioration schedules",
        "not a single-factor effect of transition direction",
        "full-denominator event incidence and warning availability are treated as more primary",
    )
    for phrase in required:
        assert phrase in lower or phrase in text


def test_publication_metadata_uses_one_conditional_timing_concept() -> None:
    captions = (ROOT / "manuscript/figure_captions.md").read_text(encoding="utf-8").lower()
    allocation = (ROOT / "manuscript/display_allocation.md").read_text(encoding="utf-8").lower()
    manuscript = (ROOT / "manuscript/main_text.md").read_text(encoding="utf-8").lower()
    assert "conditional positive lead-time" in manuscript
    assert "conditional positive lead-time" in allocation
    assert "positive warning lead time" in captions or "positive lead time" in captions
    assert "conditional uncertainty" not in manuscript
