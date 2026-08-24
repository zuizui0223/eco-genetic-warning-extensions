from __future__ import annotations

import json
from pathlib import Path

from eco_genetic_warning_extensions.matched_direction_identifiability_phase_w import (
    CROSS_STRENGTH_BRIDGE,
    SAME_STRENGTH_CELLS,
    TARGET_LOSS_BAND,
    extreme_clopper_pearson_reference,
    phase_w_audit,
)

ROOT = Path(__file__).resolve().parents[1]


def test_same_strength_grid_is_exact_phase_v_ecology_and_schedule() -> None:
    assert [row.p_star for row in SAME_STRENGTH_CELLS] == [0.10, 0.25, 0.50, 0.75, 0.90]
    assert {row.kappa_mu for row in SAME_STRENGTH_CELLS} == {0.20}
    assert {row.area_reference for row in SAME_STRENGTH_CELLS} == {0.8}
    assert {row.interaction_kappa for row in SAME_STRENGTH_CELLS} == {6.0}
    assert {row.ramp_generations for row in SAME_STRENGTH_CELLS} == {30}
    assert {row.hold_generations for row in SAME_STRENGTH_CELLS} == {90}
    assert {row.horizon for row in SAME_STRENGTH_CELLS} == {120}
    assert {row.normalised_barrier_increase for row in SAME_STRENGTH_CELLS} == {0.15}


def test_direction_only_grid_has_no_matched_intermediate_loss_cell() -> None:
    pooled = {row.p_star: row.pooled_loss for row in SAME_STRENGTH_CELLS}
    assert pooled == {0.10: 1.0, 0.25: 1.0, 0.50: 0.4, 0.75: 0.0, 0.90: 0.0}
    lower, upper = TARGET_LOSS_BAND
    directional_inside = [
        row.p_star for row in SAME_STRENGTH_CELLS
        if row.p_star != 0.50 and lower <= row.pooled_loss <= upper
    ]
    assert directional_inside == []


def test_extreme_reference_intervals_stay_outside_old_intermediate_band() -> None:
    lower, upper = TARGET_LOSS_BAND
    for row in SAME_STRENGTH_CELLS:
        if row.p_star == 0.50:
            continue
        interval = extreme_clopper_pearson_reference(row.trait_loss, row.baseline_eligible)
        assert interval is not None
        lo, hi = interval
        if row.trait_loss == row.baseline_eligible:
            assert lo > upper
        else:
            assert hi < lower


def test_cross_strength_bridge_is_not_direction_only() -> None:
    assert CROSS_STRENGTH_BRIDGE["pooled_loss"] == 10 / 21
    assert TARGET_LOSS_BAND[0] <= CROSS_STRENGTH_BRIDGE["pooled_loss"] <= TARGET_LOSS_BAND[1]
    assert CROSS_STRENGTH_BRIDGE["kappa_mu"] != 0.20


def test_phase_w_closes_direction_only_warning_opening() -> None:
    audit = phase_w_audit()
    assert audit["simulation_added"] is False
    assert audit["warning_outcomes_inspected"] is False
    assert audit["same_strength_directional_candidates_inside_band"] == []
    assert audit["direction_only_warning_comparison_opened"] is False
    assert audit["decision"] == "direction_only_warning_comparison_not_identifiable_under_frozen_common_schedule"
    assert "finer p_star" in audit["boundary"]


def test_committed_phase_w_audit_locks_same_decision_and_provenance() -> None:
    data = json.loads(
        (ROOT / "artifacts/matched_direction_identifiability/phase_w_locked_audit.json").read_text(encoding="utf-8")
    )
    assert data["decision"] == "direction_only_warning_comparison_not_identifiable_under_frozen_common_schedule"
    assert data["source_workflow_run"] == 29192711417
    assert data["direction_only_warning_comparison_opened"] is False
    assert [row["batch_index"] for row in data["same_strength_cells"]] == [282, 336, 390, 444, 498]
    assert [row["pooled_loss"] for row in data["same_strength_cells"]] == [1.0, 1.0, 0.4, 0.0, 0.0]
    assert data["cross_strength_bridge"]["batch_index"] == 228
