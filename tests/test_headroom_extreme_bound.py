from __future__ import annotations

import math
import random

from eco_genetic_warning_extensions.headroom_extreme_bound import (
    aa_rr_extreme_certificate,
    guaranteed_extreme_deviation,
    population_variance,
    verify_extreme_bound,
)


def test_finite_extreme_bound_holds_for_random_vectors() -> None:
    rng = random.Random(20260906)
    for n in range(2, 11):
        for _ in range(200):
            values = [rng.uniform(-2.0, 2.0) for _ in range(n)]
            assert verify_extreme_bound(values)


def test_bound_is_sharp() -> None:
    for n in range(2, 9):
        # n-1 equal upper deviations and one compensating lower deviation attain
        # the upper-side lower bound exactly.
        values = [1.0] * (n - 1) + [-(n - 1.0)]
        mean = sum(values) / n
        bound = guaranteed_extreme_deviation(values)
        upper = max(x - mean for x in values)
        assert math.isclose(bound, upper, abs_tol=1e-12)


def test_AA_RR_49x_variance_implies_7x_guaranteed_deviation_scale() -> None:
    cert = aa_rr_extreme_certificate()
    assert math.isclose(cert["variance_ratio"], 49.0, abs_tol=1e-12)
    assert math.isclose(cert["guaranteed_deviation_ratio"], 7.0, abs_tol=1e-12)
    assert math.isclose(cert["actual_upper_deviation_ratio"], 7.0, abs_tol=1e-12)
    assert math.isclose(cert["actual_lower_deviation_ratio"], 7.0, abs_tol=1e-12)
    assert math.isclose(cert["AA"]["upper_deviation"], 0.21, abs_tol=1e-12)
    assert math.isclose(cert["RR"]["upper_deviation"], 0.03, abs_tol=1e-12)


def test_population_variance_is_translation_invariant_for_headroom() -> None:
    support = (0.47, 0.61, 0.75, 0.89)
    threshold = 0.6160168052813313
    headroom = tuple(x - threshold for x in support)
    assert math.isclose(population_variance(support), population_variance(headroom), abs_tol=1e-12)
