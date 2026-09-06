from __future__ import annotations

import json
import math
from pathlib import Path

from eco_genetic_warning_extensions.density_feedback_gate_theorem import (
    barrier_schedule,
    direct_two_step_loop_gain,
    gate_certificate,
    interaction_density_derivative,
    interaction_next,
    interaction_population_derivative,
    minimum_density_for_target,
    required_density_product,
)


def test_density_to_interaction_is_strictly_positive_below_capacity() -> None:
    for q in (0.2, 0.5, 0.8, 1.0):
        for d in (0.1, 0.5, 0.9):
            assert interaction_density_derivative(q, d, 0.55, 4.5) > 0.0
    assert interaction_population_derivative(0.8, 20.0, 40.0, 0.55, 4.5) > 0.0
    assert interaction_population_derivative(0.8, 40.0, 40.0, 0.55, 4.5) == 0.0
    assert interaction_population_derivative(0.8, 50.0, 40.0, 0.55, 4.5) == 0.0


def test_exact_target_boundary_at_q_star() -> None:
    c = 0.625
    for g in (1, 20, 40):
        theta = barrier_schedule(g)
        product = required_density_product(theta, c, 4.5)
        q = 0.8
        d = product / q
        assert math.isclose(interaction_next(q, d, theta, 4.5), c, rel_tol=0.0, abs_tol=1e-12)
        assert interaction_next(q, d + 1e-6, theta, 4.5) > c
        assert interaction_next(q, d - 1e-6, theta, 4.5) < c


def test_required_headroom_rises_under_locked_forcing() -> None:
    cert = gate_certificate()
    products = cert["required_density_interaction_product"]
    assert math.isclose(products["1"], 0.6160168052813312, abs_tol=1e-12)
    assert math.isclose(products["20"], 0.6635168052813313, abs_tol=1e-12)
    assert math.isclose(products["40"], 0.7135168052813312, abs_tol=1e-12)
    assert products["1"] < products["20"] < products["40"]
    assert math.isclose(minimum_density_for_target(0.8, barrier_schedule(40)), 0.891896006601664, abs_tol=1e-12)


def test_direct_smooth_q_n_q_loop_gain_is_positive_when_density_unsaturated() -> None:
    assert direct_two_step_loop_gain(0.7, 20.0, 0.6, 40.0, 4.5, 0.4) > 0.0
    assert direct_two_step_loop_gain(0.7, 39.0, 0.6, 40.0, 4.5, 0.4) > 0.0
    assert direct_two_step_loop_gain(0.7, 40.0, 0.6, 40.0, 4.5, 0.4) == 0.0


def test_locked_density_deletion_is_system_level_failure_gate() -> None:
    root = Path(__file__).resolve().parents[1]
    derived = json.loads((root / "artifacts" / "density_feedback_gate" / "locked_derived_result.json").read_text())
    assert derived["source"]["workflow_run"] == 34014537015
    assert derived["source"]["artifact_id"] == 9983623440

    g20 = derived["generation_20"]
    assert g20["AA"]["delete_density_loss_rate"] == 0.0
    assert g20["RR"]["delete_density_loss_rate"] == 0.0
    assert g20["AA"]["paired_ci95"][0] > 0.35
    assert g20["RR"]["paired_ci95"][0] > 0.40

    g40 = derived["generation_40"]
    assert g40["AA"]["baseline_minus_deletion_risk"] > 0.57
    assert g40["RR"]["baseline_minus_deletion_risk"] > 0.59
    assert g40["AA"]["paired_ci95"][0] > 0.54
    assert g40["RR"]["paired_ci95"][0] > 0.56


def test_theorem_document_preserves_failure_gate_claim_boundary() -> None:
    root = Path(__file__).resolve().parents[1]
    text = (root / "docs" / "DENSITY_FEEDBACK_FAILURE_GATE_THEOREM_2026-09-06.md").read_text()
    assert "d_{\\min}" in text
    assert "0.1135168053" in text
    assert "positive feedback" in text
    lower = text.casefold()
    # Require both boundaries semantically, without binding to one sentence order.
    assert "sorting advantage" in lower
    assert "incorrect to call density feedback" in lower
    assert "universal natural density threshold" in lower
    assert (
        "none of these quantities is asserted" in lower
        or "does not assert a universal natural collapse threshold" in lower
    )
