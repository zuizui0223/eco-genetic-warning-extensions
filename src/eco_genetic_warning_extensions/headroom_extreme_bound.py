from __future__ import annotations

from math import sqrt
from statistics import fmean
from typing import Iterable


def population_variance(values: Iterable[float]) -> float:
    vals = tuple(float(x) for x in values)
    if not vals:
        raise ValueError("values must be non-empty")
    mean = fmean(vals)
    return fmean((x - mean) ** 2 for x in vals)


def guaranteed_extreme_deviation(values: Iterable[float]) -> float:
    """Return sqrt(v/(n-1)), the finite zero-sum extreme lower bound.

    For n>=2 values with population variance v and mean mu,
        max_i (x_i-mu) >= sqrt(v/(n-1))
    and
        max_i (mu-x_i) >= sqrt(v/(n-1)).
    """
    vals = tuple(float(x) for x in values)
    if len(vals) < 2:
        raise ValueError("at least two values are required")
    return sqrt(population_variance(vals) / (len(vals) - 1))


def verify_extreme_bound(values: Iterable[float], tolerance: float = 1e-12) -> bool:
    vals = tuple(float(x) for x in values)
    if len(vals) < 2:
        raise ValueError("at least two values are required")
    mean = fmean(vals)
    bound = guaranteed_extreme_deviation(vals)
    upper = max(x - mean for x in vals)
    lower = max(mean - x for x in vals)
    return upper + tolerance >= bound and lower + tolerance >= bound


def aa_rr_extreme_certificate() -> dict[str, object]:
    mean_h = 0.0639831947186687
    aa = (-0.1460168052813313, -0.0060168052813313, 0.1339831947186687, 0.2739831947186687)
    rr = (0.0939831947186687, 0.0739831947186687, 0.0539831947186687, 0.0339831947186687)

    def cell(values: tuple[float, ...]) -> dict[str, float | tuple[float, ...]]:
        mean = fmean(values)
        var = population_variance(values)
        bound = guaranteed_extreme_deviation(values)
        return {
            "values": values,
            "mean": mean,
            "variance": var,
            "guaranteed_extreme_deviation": bound,
            "upper_deviation": max(x - mean for x in values),
            "lower_deviation": max(mean - x for x in values),
        }

    aa_cell = cell(aa)
    rr_cell = cell(rr)
    return {
        "common_mean": mean_h,
        "AA": aa_cell,
        "RR": rr_cell,
        "variance_ratio": float(aa_cell["variance"]) / float(rr_cell["variance"]),
        "guaranteed_deviation_ratio": float(aa_cell["guaranteed_extreme_deviation"]) / float(rr_cell["guaranteed_extreme_deviation"]),
        "actual_upper_deviation_ratio": float(aa_cell["upper_deviation"]) / float(rr_cell["upper_deviation"]),
        "actual_lower_deviation_ratio": float(aa_cell["lower_deviation"]) / float(rr_cell["lower_deviation"]),
    }
