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
    assert all(
        row["horizon_fraction_ci_includes_zero"] == "True"
        for row in rows.values()
    )
    assert all(
        float(row["horizon_fraction_difference_directional_minus_symmetric"]) > 0
        for row in rows.values()
    )


def test_manuscript_discloses_identification_boundary_and_uncertainty() -> None:
    text = (ROOT / "manuscript/main_text.md").read_text(encoding="utf-8")
    forbidden = (
        "altered only recurrent transition direction",
        "changing one genetic boundary condition while holding the ecological life cycle fixed",
        "shortened the intervention window in the tested closure",
    )
    for phrase in forbidden:
        assert phrase not in text
    for required in (
        "portability", "210-generation hold", "90-generation hold",
        "four of five seed-block", "weaker directional schedule",
        "0.540", "0.335", "directional-minus-symmetric",
        "all six", "41 of 81", "event-regime feasibility precedes warning comparison",
    ):
        assert required in text
