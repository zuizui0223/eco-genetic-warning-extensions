from __future__ import annotations

import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "artifacts" / "empirical" / "n2_open_data_state_layer_registry.json"
SUMMARY = ROOT / "artifacts" / "empirical" / "n2_open_data_state_layer_summary.json"
SCRIPT = ROOT / "scripts" / "summarize_n2_state_layer_registry.py"
PREREG = ROOT / "manuscript" / "N2_OPEN_DATA_STATE_LAYER_AUDIT_PREREGISTRATION.md"


def _module():
    spec = importlib.util.spec_from_file_location("n2_summary", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_committed_n2_summary_is_exactly_regenerated_from_registry() -> None:
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    committed = json.loads(SUMMARY.read_text(encoding="utf-8"))
    regenerated = _module().summarize(registry)
    assert regenerated == committed


def test_n2_response_firewall_and_candidate_lock() -> None:
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    assert registry["search_cutoff"] == "2026-08-26"
    systems = registry["systems"]
    assert len(systems) == 10
    assert sum(x["origin_family"] == "urban" for x in systems) == 5
    assert sum(x["origin_family"] == "island" for x in systems) == 5
    text = json.dumps(registry).lower()
    for forbidden in ("p_value", "pvalue", "effect_direction", "effect_size", "coefficient"):
        assert forbidden not in text


def test_n2_current_boundary_is_measurement_representation_not_ecological_null() -> None:
    summary = json.loads(SUMMARY.read_text(encoding="utf-8"))
    assert summary["by_origin"]["urban"]["direct_I_and_F_public_yes"] == 3
    assert summary["by_origin"]["island"]["direct_I_and_F_public_yes"] == 0
    assert summary["full_proximal_state_public_yes_all_systems"] == 0
    assert summary["public_connectivity_C_yes_all_systems"] == 0
    assert summary["public_genetic_G_yes_all_systems"] == 0
    assert summary["direct_cross_origin_residual_context_ready"] is False
    assert summary["decision"] == "N2_measurement_representation_gap_prevents_direct_cross_origin_test"
    assert "not ecological absence" in summary["claim_ceiling"]


def test_n2_preregistration_prevents_rescue_by_relabelling_or_study_replacement() -> None:
    text = PREREG.read_text(encoding="utf-8")
    assert "Published effect directions, p-values" in text
    assert "call pollen receipt, pollinator abundance, richness and direct flower visitation the same `I` coordinate" in text
    assert "add a new system after N2 scoring merely to restore a desired two-versus-two comparison" in text
    assert "interpret missing archive layers as evidence that the biological mechanism was absent" in text
