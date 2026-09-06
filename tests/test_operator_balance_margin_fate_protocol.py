from __future__ import annotations

import json
from pathlib import Path

from eco_genetic_warning_extensions.operator_balance_margin_fate import load_protocol


def test_protocol_is_prospectively_locked_with_fresh_replication() -> None:
    protocol = load_protocol()
    assert protocol["experiment_id"] == "operator_balance_margin_fate_v1"
    assert protocol["status"] == "prospective_locked_before_run"
    assert protocol["forcing"]["generations"] == 40
    assert protocol["forcing"]["primary_marker_generation"] == 20
    assert protocol["forcing"]["endpoint_generation"] == 40
    assert protocol["replication"]["paired_keys_per_condition"] == 3000
    assert protocol["replication"]["total_trajectories"] == 12000
    assert protocol["replication"]["master_seeds"] == [203601, 203602, 203603, 203604, 203605, 203606]


def test_conditions_are_exactly_the_predeclared_four() -> None:
    protocol = load_protocol()
    assert set(protocol["conditions"]) == {"AA_full", "RR_full", "AA_q_only", "RR_q_only"}
    assert protocol["conditions"]["AA_full"]["q_feedback"] == [0.6, 0.3, 0.1]
    assert protocol["conditions"]["RR_full"]["q_feedback"] == [0.6, 0.3, 0.1]
    assert protocol["conditions"]["AA_q_only"]["q_feedback"] == [1.0, 0.0, 0.0]
    assert protocol["conditions"]["RR_q_only"]["q_feedback"] == [1.0, 0.0, 0.0]


def test_primary_decision_rule_is_direction_fixed_before_outcomes() -> None:
    protocol = load_protocol()
    primary = protocol["primary_estimands"]
    assert "RR direct-feedback extension minus AA direct-feedback extension" in primary["primary_DID"]
    decisions = protocol["decision_rules"]
    assert "strictly above zero" in decisions["route_repair_resolved"]
    assert "strictly below zero" in decisions["route_repair_opposite"]
    assert "contains zero" in decisions["route_repair_unresolved"]


def test_full_denominator_marker_has_no_success_threshold() -> None:
    protocol = load_protocol()
    marker = protocol["primary_estimands"]["full_denominator_marker"]
    assert "sensitivity" in marker
    assert "specificity" in marker
    assert "binary-marker AUC" in marker
    assert "No minimum performance is required" in marker


def test_stop_rules_prevent_post_result_search() -> None:
    protocol = load_protocol()
    text = " ".join(protocol["stop_rules"]).casefold()
    for token in ("seeds", "horizons", "margin thresholds", "endpoint definitions", "barrier schedules", "feedback weights"):
        assert token in text
    assert "do not tune the generation-20 marker" in text


def test_protocol_file_contains_no_outcomes() -> None:
    root = Path(__file__).resolve().parents[1]
    raw = json.loads((root / "experiments" / "operator_balance_margin_fate_protocol.json").read_text())
    assert "results" not in raw
    assert "outcome" not in raw
