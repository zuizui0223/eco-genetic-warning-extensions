from __future__ import annotations

import math

import pytest

from eco_genetic_warning_extensions.operator_balance_route_margin import (
    next_interaction_from_state,
    route_margin,
)

try:
    from causal_model.multipatch_criticality_dynamics import (
        DynamicsParameters,
        interaction_support_signal,
        sigmoid,
    )
except ImportError:  # Parent is intentionally absent from the lightweight repository-only CI.
    DynamicsParameters = None


@pytest.mark.skipif(DynamicsParameters is None, reason="pinned parent package not installed")
def test_route_margin_matches_parent_support_and_transition() -> None:
    params = DynamicsParameters(
        patch_areas=(1.0,),
        initial_population=(40,),
        initial_interaction=(0.7,),
        initial_high_allele_frequency=(0.4,),
        interaction_feedback=4.5,
        interaction_barrier=0.58,
        q_feedback_alpha=0.6,
        q_feedback_beta_trait=0.3,
        q_feedback_gamma_allele=0.1,
    )
    q, t, g, d, theta = 0.7, 0.8, 0.4, 0.9, 0.58
    support_parent = interaction_support_signal(q, t, g, params)
    q_parent = sigmoid(params.interaction_feedback * (d * support_parent - theta))
    q_theorem = next_interaction_from_state(q, t, g, d, theta)
    assert math.isclose(q_parent, q_theorem, abs_tol=1e-12)

    margin = route_margin(q, t, g, d, theta)
    assert (q_parent > 0.625) == (margin > 0.0)
