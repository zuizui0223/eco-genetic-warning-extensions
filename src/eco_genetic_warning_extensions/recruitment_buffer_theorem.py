from __future__ import annotations

import math
from statistics import fmean
from typing import Iterable


def recruit_high_trait_mass(
    resident_high_trait_mass: float,
    high_allele_frequency: float,
    inheritance_weight: float = 0.5,
) -> float:
    """Exact high-region mass under the declared two-kernel recruitment closure.

    The parent low kernel has zero mass in the declared high-trait region and
    the high kernel has unit mass there. Hence the pre-selection high-trait mass
    is the convex combination `(1-h)*p + h*m`.
    """
    m = float(resident_high_trait_mass)
    p = float(high_allele_frequency)
    h = float(inheritance_weight)
    if not 0.0 <= m <= 1.0:
        raise ValueError("resident_high_trait_mass must lie in [0,1]")
    if not 0.0 <= p <= 1.0:
        raise ValueError("high_allele_frequency must lie in [0,1]")
    if not 0.0 <= h <= 1.0:
        raise ValueError("inheritance_weight must lie in [0,1]")
    return (1.0 - h) * p + h * m


def mismatch_after_recruitment(
    resident_high_trait_mass: float,
    high_allele_frequency: float,
    inheritance_weight: float = 0.5,
) -> float:
    """Signed recruit-trait minus allele mismatch after recruitment."""
    r = recruit_high_trait_mass(
        resident_high_trait_mass,
        high_allele_frequency,
        inheritance_weight,
    )
    return r - float(high_allele_frequency)


def spatial_mean_squared_mismatch(
    trait_masses: Iterable[float],
    allele_frequencies: Iterable[float],
) -> float:
    trait = tuple(float(x) for x in trait_masses)
    allele = tuple(float(x) for x in allele_frequencies)
    if not trait or len(trait) != len(allele):
        raise ValueError("trait and allele vectors must be nonempty and equal length")
    if any(not 0.0 <= x <= 1.0 for x in trait + allele):
        raise ValueError("trait and allele values must lie in [0,1]")
    return fmean((m - p) ** 2 for m, p in zip(trait, allele))


def contraction_certificate(inheritance_weight: float = 0.5) -> dict[str, float]:
    h = float(inheritance_weight)
    if not 0.0 <= h <= 1.0:
        raise ValueError("inheritance_weight must lie in [0,1]")
    return {
        "inheritance_weight": h,
        "absolute_mismatch_factor": h,
        "squared_mismatch_factor": h * h,
        "allele_kernel_weight": 1.0 - h,
    }


def verify_parent_recruitment(
    resident_high_trait_mass: float,
    high_allele_frequency: float,
    inheritance_weight: float = 0.5,
    trait_grid_size: int = 31,
) -> dict[str, float]:
    """Check the analytic high-mass identity against the pinned parent implementation.

    Requires the parent `causal_model` package to be installed. This helper is
    intentionally separate from the theorem formula so ordinary extension tests
    can still run without the parent checkout.
    """
    from causal_model.multipatch_criticality_dynamics import (
        DynamicsParameters,
        _kernel_distribution,
        recruit_trait_distribution,
        trait_grid,
    )

    m = float(resident_high_trait_mass)
    p = float(high_allele_frequency)
    h = float(inheritance_weight)
    params = DynamicsParameters(
        patch_areas=(1.0,),
        trait_grid_size=int(trait_grid_size),
        genotype_trait_recruitment="two_kernel_recruitment",
        inheritance_weight=h,
    )
    low = _kernel_distribution(params.low_trait_kernel_center, params)
    high = _kernel_distribution(params.high_trait_kernel_center, params)
    resident = tuple((1.0 - m) * lo + m * hi for lo, hi in zip(low, high))
    recruit = recruit_trait_distribution(resident, p, params)
    grid = trait_grid(params)
    observed = sum(value for z, value in zip(grid, recruit) if z >= params.high_trait_cutoff)
    expected = recruit_high_trait_mass(m, p, h)
    if not math.isclose(observed, expected, rel_tol=0.0, abs_tol=1e-12):
        raise RuntimeError("parent recruitment implementation drifted from analytic identity")
    return {
        "resident_high_trait_mass": m,
        "high_allele_frequency": p,
        "inheritance_weight": h,
        "observed_recruit_high_trait_mass": observed,
        "expected_recruit_high_trait_mass": expected,
    }
