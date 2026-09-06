from __future__ import annotations

import math
import random

from eco_genetic_warning_extensions.headroom_budget import (
    HeadroomState,
    accumulated_budget,
    budget_terms,
)


def test_budget_closes_exactly_for_random_state_changes() -> None:
    rng = random.Random(20260906)
    for _ in range(500):
        before = HeadroomState(
            q=rng.random(),
            trait=rng.random(),
            allele=rng.random(),
            density=rng.random(),
            theta=rng.uniform(0.4, 0.7),
        )
        after = HeadroomState(
            q=rng.random(),
            trait=rng.random(),
            allele=rng.random(),
            density=rng.random(),
            theta=rng.uniform(0.4, 0.7),
        )
        row = budget_terms(before, after)
        assert math.isclose(row["sum"], row["direct_delta_headroom"], abs_tol=1e-12)
        assert abs(row["closure_error"]) < 1e-12


def test_each_component_has_expected_sign_in_isolation() -> None:
    base = HeadroomState(q=0.7, trait=0.5, allele=0.5, density=0.8, theta=0.55)
    q_up = budget_terms(base, HeadroomState(q=0.8, trait=0.5, allele=0.5, density=0.8, theta=0.55))
    t_up = budget_terms(base, HeadroomState(q=0.7, trait=0.6, allele=0.5, density=0.8, theta=0.55))
    g_up = budget_terms(base, HeadroomState(q=0.7, trait=0.5, allele=0.6, density=0.8, theta=0.55))
    d_up = budget_terms(base, HeadroomState(q=0.7, trait=0.5, allele=0.5, density=0.9, theta=0.55))
    forcing = budget_terms(base, HeadroomState(q=0.7, trait=0.5, allele=0.5, density=0.8, theta=0.56))
    assert q_up["interaction"] > 0 and math.isclose(q_up["sum"], q_up["interaction"], abs_tol=1e-12)
    assert t_up["trait"] > 0 and math.isclose(t_up["sum"], t_up["trait"], abs_tol=1e-12)
    assert g_up["allele"] > 0 and math.isclose(g_up["sum"], g_up["allele"], abs_tol=1e-12)
    assert d_up["density"] > 0 and math.isclose(d_up["sum"], d_up["density"], abs_tol=1e-12)
    assert forcing["forcing"] < 0 and math.isclose(forcing["sum"], forcing["forcing"], abs_tol=1e-12)


def test_accumulated_budget_telescopes_without_residual() -> None:
    states = [
        HeadroomState(0.8, 0.7, 0.6, 1.0, 0.50),
        HeadroomState(0.75, 0.72, 0.63, 0.95, 0.52),
        HeadroomState(0.70, 0.74, 0.66, 0.90, 0.55),
        HeadroomState(0.68, 0.76, 0.69, 0.86, 0.58),
    ]
    total = accumulated_budget(states)
    assert math.isclose(total["sum"], total["direct_delta_headroom"], abs_tol=1e-12)
    assert abs(total["accumulated_closure_error"]) < 1e-12
    assert total["max_abs_step_closure_error"] < 1e-12
