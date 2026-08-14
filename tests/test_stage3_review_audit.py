from __future__ import annotations

import csv
import json
import statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _rows():
    with (ROOT / "manuscript/tables/stage3_review_summary.csv").open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def test_secondary_audit_locks_domain_differences_and_uncertainty() -> None:
    lock = json.loads((ROOT / "reproducibility/upstream-lock.json").read_text(encoding="utf-8"))
    review = lock["secondary_review_audit"]
    sym = review["corrected_publication_timing"]["recalibrated_symmetric_domain"]
    directional = review["corrected_publication_timing"]["directional_calibrated_domain"]
    assert sym["horizon"] == 240
    assert directional["horizon"] == 120
    assert max(sym["median_positive_lead_fraction_horizon_range"]) < min(directional["median_positive_lead_fraction_horizon_range"])
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


def test_manuscript_discloses_identification_boundary() -> None:
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
        "0.540", "0.335", "horizon-normalized",
    ):
        assert required in text
