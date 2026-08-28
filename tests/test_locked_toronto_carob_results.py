from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def test_toronto_locked_result_and_claim_ceiling() -> None:
    x = _load("artifacts/empirical/toronto_residual_context_result_locked.json")
    assert x["decision"] == "no_detected_residual_urban_context_information"
    assert x["schema_audit"]["site_count"] == 10
    assert x["schema_audit"]["eligible_rows"] == 28
    assert x["delta_NLL_total_M1_minus_M0"] > 0
    lo, hi = x["garden_bootstrap_95ci"]
    assert lo > 0 and hi > 0
    assert x["provenance"]["workflow_run"] == 32993817229
    assert "not evidence that urban context is biologically irrelevant" in x["interpretation"]


def test_carob_locked_result_stops_before_context() -> None:
    x = _load("artifacts/empirical/n3_carob_predictive_result_locked.json")
    assert x["decision"] == "process_measurement_not_supported_for_primary_endpoint"
    assert x["B1_gate"] == "process_measurement_not_supported_for_primary_endpoint"
    assert x["B2_opened"] is False
    assert x["data_audit"]["orchard_count"] == 20
    assert x["data_audit"]["orchard_year_rows"] == 37
    for key in ("embedded", "joined"):
        result = x["B1"][key]
        assert result["decision"] == "no_detected_process_information"
        lo, hi = result["orchard_bootstrap_95ci"]
        assert lo < 0 < hi
    assert x["provenance"]["workflow_run"] == 33134449528
    assert x["contract_sha256"] == "61be811be8789b86a3cdb019ba8ac1dbf487a6e776775eee982d045cc076084d"


def test_natural_ledger_preserves_gate_order_and_no_cross_origin_overclaim() -> None:
    text = (ROOT / "docs/NATURAL_STATE_RECOVERY_LEDGER.md").read_text(encoding="utf-8")
    assert "endpoint-relevant predictive adequacy" in text
    assert "process_measurement_not_supported_for_primary_endpoint" in text
    assert "no_detected_residual_urban_context_information" in text
    assert "Neither is evidence for ecological equivalence or difference between urban and island systems." in text


def test_reader_story_uses_toronto_carob_as_gate_contrast() -> None:
    text = (ROOT / "manuscript/main_story_revision.md").read_text(encoding="utf-8")
    assert "Toronto–carob contrast" in text
    assert "residual-context B2 was not opened" in text
    assert "Urban–island convergence remains open" in text
