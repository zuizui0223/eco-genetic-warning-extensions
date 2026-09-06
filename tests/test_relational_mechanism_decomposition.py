from __future__ import annotations

import math

from eco_genetic_warning_extensions.relational_mechanism_decomposition import analytic_baseline, load_protocol


def test_locked_analytic_covariance_to_support_variance_identity() -> None:
    protocol = load_protocol()
    analytic = analytic_baseline(protocol)
    aa = analytic["AA_full"]
    rr = analytic["RR_full"]

    assert math.isclose(aa["support_mean"], 0.68, abs_tol=1e-12)
    assert math.isclose(rr["support_mean"], 0.68, abs_tol=1e-12)
    assert tuple(round(x, 2) for x in aa["support"]) == (0.47, 0.61, 0.75, 0.89)
    assert tuple(round(x, 2) for x in rr["support"]) == (0.71, 0.69, 0.67, 0.65)
    assert math.isclose(aa["support_variance"], 0.0245, abs_tol=1e-12)
    assert math.isclose(rr["support_variance"], 0.0005, abs_tol=1e-12)
    assert math.isclose(aa["support_variance"] / rr["support_variance"], 49.0, abs_tol=1e-12)

    for cell in analytic.values():
        assert math.isclose(
            cell["support_variance"],
            cell["support_variance_from_covariance_identity"],
            abs_tol=1e-12,
        )


def test_q_only_intervention_removes_initial_alignment_difference() -> None:
    protocol = load_protocol()
    analytic = analytic_baseline(protocol)
    aa = analytic["AA_q_only"]
    rr = analytic["RR_q_only"]
    assert aa["support"] == rr["support"]
    assert math.isclose(aa["support_variance"], rr["support_variance"], abs_tol=1e-12)
