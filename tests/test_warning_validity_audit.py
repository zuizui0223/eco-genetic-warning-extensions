from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

from eco_genetic_warning_extensions.warning_validity_audit import audit, load_records

ROOT = Path(__file__).resolve().parents[1]
RECORDS = ROOT / "artifacts/warning_validity/trajectory_endpoint_records.csv"
RESULT = ROOT / "artifacts/prepublication_review/warning_validity_audit.json"


def test_compact_record_checksum_matches_immutable_source_manifest() -> None:
    manifest = json.loads(
        (ROOT / "artifacts/warning_validity/source_manifest.json").read_text(encoding="utf-8")
    )
    observed = hashlib.sha256(RECORDS.read_bytes()).hexdigest()
    assert observed == manifest["record_table"]["sha256"]
    assert manifest["record_table"]["rows"] == 1_200


def test_compact_records_retain_attempts_endpoints_and_non_events() -> None:
    rows = load_records(RECORDS)
    assert len(rows) == 1_200
    assert {row["ensemble"] for row in rows} == {"inherited_202611", "fresh_202911"}
    assert sum(row["baseline_eligible"] for row in rows) == (83 + 82) * 6
    for ensemble, available, losses in (
        ("inherited_202611", 83, 35),
        ("fresh_202911", 82, 33),
    ):
        endpoint_rows = [
            row
            for row in rows
            if row["ensemble"] == ensemble and row["endpoint"] == "H_alpha_0.05"
        ]
        assert sum(row["baseline_eligible"] for row in endpoint_rows) == available
        assert sum(row["trait_loss_time"] is not None for row in endpoint_rows) == losses


def test_all_six_thresholds_fire_in_every_non_event_trajectory() -> None:
    result = audit(load_records(RECORDS))
    for ensemble, non_events in (("inherited_202611", 48), ("fresh_202911", 49)):
        endpoints = result["ensembles"][ensemble]["endpoints"]
        assert len(endpoints) == 6
        for endpoint in endpoints.values():
            fpr = endpoint["non_event_false_positive_rate"]
            assert (fpr["successes"], fpr["total"], fpr["estimate"]) == (
                non_events,
                non_events,
                1.0,
            )
            assert endpoint["lead_sensitivity"]["estimate"] == 1.0
            assert endpoint["full_horizon_classification"]["specificity"]["estimate"] == 0.0
            assert endpoint["full_horizon_classification"]["binary_marker_auc"] == 0.5


def test_ramp_end_landmark_uses_only_trajectories_still_at_risk() -> None:
    result = json.loads(RESULT.read_text(encoding="utf-8"))
    inherited = result["ensembles"]["inherited_202611"]["endpoints"]["H_gamma_0.20"]
    ramp = inherited["landmark_dynamic_classification"]["30"]
    assert ramp["risk_set"] == 81
    assert ramp["future_cases"] == 33
    assert ramp["confusion"] == {
        "false_negative": 3,
        "false_positive": 40,
        "true_negative": 8,
        "true_positive": 30,
    }
    assert 0.53 < ramp["binary_marker_auc"] < 0.54


def test_publication_table_keeps_ensembles_and_endpoints_separate() -> None:
    path = ROOT / "manuscript/tables/warning_validity_audit.csv"
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == 18
    assert {row["ensemble"] for row in rows} == {
        "inherited_202611",
        "fresh_202911",
        "combined_descriptive",
    }
    assert all(float(row["non_event_false_positive_rate"]) == 1.0 for row in rows)


def test_audit_discloses_endpoint_dependence_and_auc_limit() -> None:
    result = json.loads(RESULT.read_text(encoding="utf-8"))
    assert "repeated measurements" in result["endpoint_dependence"]
    assert "not a preregistered continuous risk score" in result["auc_identifiability"]
    assert "valid pairs alone" in result["claim_rule"]
