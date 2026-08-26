from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "artifacts" / "empirical" / "cross_origin_minimal_bridge_access_result.json"
PREREG = ROOT / "manuscript" / "empirical_cross_origin_minimal_bridge_preregistration.md"
ACCESS = ROOT / "manuscript" / "empirical_cross_origin_minimal_bridge_access_result.md"


def test_access_gate_is_transport_boundary_not_ecological_result() -> None:
    data = json.loads(RESULT.read_text(encoding="utf-8"))
    assert data["decision"] == "minimal_bridge_not_runnable_from_current_automated_archive_access"
    assert data["scientific_interpretation"].startswith("archive-access boundary")
    assert "No candidate reproductive outcome values were parsed" in data["response_firewall"]
    assert data["transport_diagnostic"]["candidate_count"] == 4
    assert data["transport_diagnostic"]["candidate_with_full_public_file_probe_count"] == 0
    assert data["transport_diagnostic"]["metadata_manifest_resolved_for_all"] is True


def test_candidate_lock_remains_two_per_origin() -> None:
    data = json.loads(RESULT.read_text(encoding="utf-8"))
    candidates = data["candidate_lock"]
    assert {item["id"] for item in candidates} == {
        "U1_commelina",
        "U2_chicago",
        "I1_hiraiwa2017",
        "I2_hawaii2019",
    }
    assert sum(item["origin"] == "urban" for item in candidates) == 2
    assert sum(item["origin"] == "island" for item in candidates) == 2
    assert all(item["metadata_files"] for item in candidates)


def test_preregistration_prohibits_outcome_facing_rescue() -> None:
    text = PREREG.read_text(encoding="utf-8")
    assert "do not generic z-score unlike fruit/seed/pollen outcomes".lower() in text.lower()
    assert "add a fifth study after results" in text
    assert "endpoints within one study not independent systems".lower() in text.lower()


def test_access_result_requires_verified_exact_bytes_before_schema_or_outcomes() -> None:
    text = ACCESS.read_text(encoding="utf-8")
    assert "0/4 candidates" in text
    assert "Validating..." in text
    assert "verified against the recorded Dryad size/digest metadata" in text
    assert "only then open outcome values" in text
    assert "is not evidence for or against an urban–island ecological difference" in text
