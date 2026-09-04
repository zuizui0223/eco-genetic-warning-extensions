from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCKED = ROOT / "artifacts" / "alignment_propagation" / "locked_summary.json"
DOC = ROOT / "docs" / "ALIGNMENT_PROPAGATION_RESULT_2026-09-04.md"
STATE = ROOT / "manuscript" / "state_validity_and_empirical_measurement_gates.md"


def _payload() -> dict:
    return json.loads(LOCKED.read_text(encoding="utf-8"))


def test_result_provenance_is_frozen_to_successful_workflow() -> None:
    payload = _payload()
    assert payload["status"] == "locked_from_successful_workflow_artifact"
    assert payload["source_run_id"] == 33839184864
    assert payload["source_head_sha"] == "27f73ce621fc687369e529d736a381c03ce4986a"
    assert payload["source_artifact_id"] == 9924340712
    assert payload["source_artifact_digest"] == "sha256:92332ec3fb0ac04d7bfcab6b7ab56dbb2aac65d7021ae6aa71523bcfdca4fb52"


def test_primary_1500_pair_horizon_curve_is_exact() -> None:
    result = _payload()["result"]
    cells = {row["horizon"]: row for row in result["primary_horizon_cells"]}
    assert set(cells) == {5, 10, 20, 40}
    expected = {
        5: (0.0, 0.0, 0.0),
        10: (0.0033333333333333335, -0.004395170139262505, 0.01106183680592917),
        20: (0.05333333333333334, 0.020439227320699846, 0.08622743934596683),
        40: (0.052, 0.019623552659379068, 0.08437644734062093),
    }
    for horizon, (estimate, lower, upper) in expected.items():
        cell = cells[horizon]
        assert cell["n_pairs"] == 1500
        assert math.isclose(cell["risk_difference_anti_minus_aligned"], estimate, abs_tol=1e-15)
        assert math.isclose(cell["ci95_lower"], lower, abs_tol=1e-15)
        assert math.isclose(cell["ci95_upper"], upper, abs_tol=1e-15)


def test_all_nested_cells_are_retained_and_not_independent_experiments() -> None:
    result = _payload()["result"]
    cells = result["cells"]
    assert len(cells) == 12
    assert {(c["horizon"], c["n_pairs"]) for c in cells} == {
        (h, n) for h in (5, 10, 20, 40) for n in (500, 1000, 1500)
    }
    assert any("Do not pool nested pair-count prefixes" in rule for rule in result["interpretation_rule"]["forbidden"])


def test_manuscript_uses_effect_size_timescale_not_significance_cutoff() -> None:
    doc = DOC.read_text(encoding="utf-8")
    state = STATE.read_text(encoding="utf-8")
    for text in (doc, state):
        assert "+5.33" in text or "+5.3" in text
        assert "+5.20" in text or "+5.2" in text
        assert "10" in text and "20" in text and "40" in text
    flat = " ".join(state.lower().split())
    # The manuscript may mention a cutoff only to reject that interpretation.
    assert "does not establish generation 20 as a true cutoff" in flat
    assert "does not establish a universal temporal cutoff" in flat
    assert "generation 20 is the true cutoff" not in flat
    assert "generation 20 is a universal onset" not in flat
