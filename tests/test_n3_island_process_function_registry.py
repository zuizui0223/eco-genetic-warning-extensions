from __future__ import annotations

import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "artifacts" / "empirical" / "n3_island_process_function_registry.json"
SUMMARY = ROOT / "artifacts" / "empirical" / "n3_island_process_function_summary.json"
SCRIPT = ROOT / "scripts" / "summarize_n3_island_process_function_registry.py"
PREREG = ROOT / "manuscript" / "N3_ISLAND_PROCESS_FUNCTION_ARCHIVE_PREREGISTRATION.md"


def _module():
    spec = importlib.util.spec_from_file_location("n3_summary", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_n3_summary_regenerates_from_locked_registry() -> None:
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    committed = json.loads(SUMMARY.read_text(encoding="utf-8"))
    assert _module().summarize(registry) == committed


def test_n3_is_response_firewalled_and_distinct_from_n2_rescue() -> None:
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    assert registry["search_cutoff"] == "2026-08-27"
    assert len(registry["systems"]) == 4
    text = json.dumps(registry).lower()
    for forbidden in ("p_value", "pvalue", "effect_direction", "effect_size", "coefficient"):
        assert forbidden not in text
    prereg = PREREG.read_text(encoding="utf-8")
    assert "N3 is a new prospective programme" in prereg
    assert "does not replace, add to, or rescue the N2 candidate registry" in prereg


def test_n3_corrects_scope_without_opening_outcome_models() -> None:
    summary = json.loads(SUMMARY.read_text(encoding="utf-8"))
    assert summary["n_systems"] == 4
    assert summary["study_level_direct_I_and_F_yes"] == 4
    assert summary["public_reusable_direct_I_and_F_both_yes"] == 1
    assert summary["public_reusable_direct_I_and_F_both_yes_systems"] == ["I3_MALLORCA_CNEORUM_2020"]
    assert summary["process_function_gate_yes"] == 0
    assert summary["process_function_gate_partial"] == 4
    assert summary["residual_context_gate_yes"] == 0
    assert summary["residual_context_gate_partial"] == 2
    assert summary["decision"] == "island_process_function_archives_recovered_but_schema_alignment_still_required"
    assert "not a general absence" in summary["interpretation"]
