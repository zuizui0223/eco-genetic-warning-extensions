from __future__ import annotations

import math

import pytest

from eco_genetic_warning_extensions.coherence_switch_theorem import (
    allele_log_odds_increment,
    boundary_sensitivities,
    coherence_switch_certificate,
    high_allele_relative_fitness,
    high_trait_margin,
    q_from_headroom,
    selected_high_allele_frequency,
)


def test_headroom_sign_switches_interaction_trait_and_allele_direction_together() -> None:
    for h in (-0.2, -0.05, -1e-6, 0.0, 1e-6, 0.05, 0.2):
        cert = coherence_switch_certificate(h, p=0.37)
        nonnegative = h >= 0.0
        assert cert["interaction_high_side"] == nonnegative
        assert cert["trait_potential_viable_at_z1"] == nonnegative
        assert cert["high_allele_non_decreasing"] == nonnegative
        if h < 0:
            assert cert["allele_selection_change"] < 0.0
        elif h > 0:
            assert cert["allele_selection_change"] > 0.0
        else:
            assert math.isclose(cert["allele_selection_change"], 0.0, abs_tol=1e-15)


def test_exact_boundary_values() -> None:
    q = q_from_headroom(0.0)
    assert math.isclose(q, 0.625, abs_tol=1e-15)
    assert math.isclose(high_trait_margin(q), 0.0, abs_tol=1e-15)
    assert math.isclose(high_allele_relative_fitness(q), 1.0, abs_tol=1e-15)
    assert math.isclose(allele_log_odds_increment(q), 0.0, abs_tol=1e-15)
    for p in (0.1, 0.5, 0.9):
        assert math.isclose(selected_high_allele_frequency(p, q), p, abs_tol=1e-15)


def test_boundary_sensitivity_values() -> None:
    s = boundary_sensitivities()
    assert math.isclose(s["dq_next_dH_at_boundary"], 1.0546875, abs_tol=1e-12)
    assert math.isclose(s["d_high_trait_margin_dH_at_boundary"], 0.84375, abs_tol=1e-12)
    assert math.isclose(s["d_high_allele_relative_fitness_dH_at_boundary"], 0.421875, abs_tol=1e-12)
    assert math.isclose(s["d_allele_log_odds_increment_dH_at_boundary"], 0.421875, abs_tol=1e-12)


def test_parent_trait_and_selection_equations_when_parent_is_installed() -> None:
    parent = pytest.importorskip("causal_model.multipatch_criticality_dynamics")
    params = parent.DynamicsParameters(patch_areas=(1.0,), selection_strength=0.5)
    for q in (0.4, 0.625, 0.9):
        parent_margin = parent.trait_fitness(1.0, q, params) - params.viability_threshold
        assert math.isclose(parent_margin, high_trait_margin(q), abs_tol=1e-12)
        parent_w = 1.0 + params.selection_strength * parent_margin
        assert math.isclose(parent_w, high_allele_relative_fitness(q), abs_tol=1e-12)
        for p in (0.2, 0.5, 0.8):
            parent_selected = p * parent_w / (p * parent_w + 1.0 - p)
            assert math.isclose(parent_selected, selected_high_allele_frequency(p, q), abs_tol=1e-12)
