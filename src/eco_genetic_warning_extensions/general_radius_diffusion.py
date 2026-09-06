"""General-radius interior generator for local trait-bin mutation.

For a symmetric mutation radius J, the translation-invariant stencil is exact
only when the destination is at least ``2J`` bins from each finite boundary.
The reason is subtle but important: the implemented mutation kernel is
normalised per *source* bin.  A destination ``i`` receives mass from sources
``i-J,...,i+J``; every one of those sources must itself have a full ``2J``
neighbourhood for the inflow weights to equal ``mu/(2J)``.  Hence source-side
boundary renormalisation propagates J additional bins beyond the direct jump
radius.

Within that 2J-deep interior the finite-bin mutation operator has an exact
nonlocal stencil representation, whose leading continuum coefficient is the
jump-variance diffusion coefficient.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import isfinite
from typing import Sequence

from .small_jump_trait_bins import local_trait_mutation, normalise_distribution


@dataclass(frozen=True)
class ContinuumCoefficients:
    mutation_rate: float
    radius_bins: int
    grid_spacing: float
    time_step: float
    diffusion_coefficient: float
    fourth_derivative_coefficient: float


def diffusion_coefficient_general_radius(
    *,
    mutation_rate: float,
    radius_bins: int,
    grid_spacing: float,
    time_step: float,
) -> float:
    """Return D for the leading translation-invariant interior continuum term.

        D = mu h^2 (J+1)(2J+1) / (12 Delta t).
    """
    mu = float(mutation_rate)
    J = int(radius_bins)
    h = float(grid_spacing)
    dt = float(time_step)
    if not 0.0 <= mu <= 1.0:
        raise ValueError("mutation_rate must lie in [0, 1]")
    if J < 1:
        raise ValueError("radius_bins must be at least 1")
    if not isfinite(h) or h <= 0.0 or not isfinite(dt) or dt <= 0.0:
        raise ValueError("grid_spacing and time_step must be finite and positive")
    return mu * h * h * (J + 1) * (2 * J + 1) / (12.0 * dt)


def continuum_coefficients(
    *,
    mutation_rate: float,
    radius_bins: int,
    grid_spacing: float,
    time_step: float,
) -> ContinuumCoefficients:
    """Return the f'' and f'''' coefficients of the 2J-deep Taylor expansion."""
    mu = float(mutation_rate)
    J = int(radius_bins)
    h = float(grid_spacing)
    dt = float(time_step)
    D = diffusion_coefficient_general_radius(
        mutation_rate=mu,
        radius_bins=J,
        grid_spacing=h,
        time_step=dt,
    )
    sum_k4 = sum(k**4 for k in range(1, J + 1))
    c4 = mu * h**4 * sum_k4 / (24.0 * J * dt)
    return ContinuumCoefficients(mu, J, h, dt, D, c4)


def translation_invariant_interior(index: int, n_bins: int, radius_bins: int) -> bool:
    """Whether source-normalised mutation has a full symmetric stencil at index.

    A destination is translation invariant only if every source within J bins
    also has all 2J mutation destinations.  This requires depth >= 2J from each
    represented trait boundary.
    """
    i = int(index)
    n = int(n_bins)
    J = int(radius_bins)
    if J < 1:
        raise ValueError("radius_bins must be at least 1")
    if n < 1 or not 0 <= i < n:
        raise IndexError("index outside represented trait bins")
    return i >= 2 * J and i + 2 * J < n


def exact_interior_generator(
    distribution: Sequence[float],
    *,
    index: int,
    mutation_rate: float,
    radius_bins: int,
    time_step: float,
) -> float:
    """Exact finite-bin generator in the translation-invariant 2J-deep interior."""
    f = normalise_distribution(distribution)
    i = int(index)
    J = int(radius_bins)
    mu = float(mutation_rate)
    dt = float(time_step)
    if J < 1:
        raise ValueError("radius_bins must be at least 1")
    if not 0.0 <= mu <= 1.0:
        raise ValueError("mutation_rate must lie in [0, 1]")
    if dt <= 0.0:
        raise ValueError("time_step must be positive")
    if not translation_invariant_interior(i, len(f), J):
        raise ValueError(
            "index must be at least 2*radius_bins from both boundaries because "
            "source-side boundary renormalisation changes incoming mutation weights"
        )
    return mu / (2.0 * J * dt) * sum(
        f[i - k] + f[i + k] - 2.0 * f[i]
        for k in range(1, J + 1)
    )


def finite_operator_generator_residual(
    distribution: Sequence[float],
    *,
    index: int,
    mutation_rate: float,
    radius_bins: int,
    time_step: float,
) -> float:
    """Finite mutation update minus its exact 2J-deep interior stencil generator."""
    f = normalise_distribution(distribution)
    moved = local_trait_mutation(
        f,
        mutation_rate=mutation_rate,
        radius_bins=radius_bins,
    )
    lhs = (moved[index] - f[index]) / float(time_step)
    rhs = exact_interior_generator(
        f,
        index=index,
        mutation_rate=mutation_rate,
        radius_bins=radius_bins,
        time_step=time_step,
    )
    return lhs - rhs
