"""Scaling regimes for finite trait-bin mutation.

The same discrete radius-J mutation operator has different continuum limits
depending on how bin radius J, grid spacing h and time step Delta t scale.

Regime A: fixed J, h -> 0, Delta t proportional to h^2
    -> local diffusion with vanishing higher-order corrections.

Regime B: fixed physical radius rho=J h, J -> infinity, h -> 0 at fixed Delta t
    -> a finite-range nonlocal uniform-jump generator, not local diffusion.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import isfinite

from .general_radius_diffusion import continuum_coefficients


@dataclass(frozen=True)
class FixedRangeMomentLimit:
    mutation_rate: float
    physical_radius: float
    time_step: float
    limiting_diffusion_coefficient: float
    limiting_fourth_derivative_coefficient: float
    fourth_to_second_scale_ratio: float


def fixed_range_moment_limit(
    *,
    mutation_rate: float,
    physical_radius: float,
    time_step: float,
) -> FixedRangeMomentLimit:
    """Moment coefficients when ``rho=J h`` stays positive under refinement.

    Uniform jumps over the physical interval ``[-rho,rho]`` have

        E[S^2] = rho^2/3,
        E[S^4] = rho^4/5.

    Therefore the formal Taylor coefficients of the jump generator are

        D  = mu rho^2/(6 Delta t),
        C4 = mu rho^4/(120 Delta t).

    Since C4 remains positive for fixed rho, the local diffusion truncation is
    not an asymptotically exact description of this scaling regime.
    """
    mu = float(mutation_rate)
    rho = float(physical_radius)
    dt = float(time_step)
    if not 0.0 <= mu <= 1.0:
        raise ValueError("mutation_rate must lie in [0, 1]")
    if not isfinite(rho) or rho <= 0.0 or not isfinite(dt) or dt <= 0.0:
        raise ValueError("physical_radius and time_step must be finite and positive")
    D = mu * rho * rho / (6.0 * dt)
    c4 = mu * rho**4 / (120.0 * dt)
    ratio = 0.0 if D == 0.0 else c4 / D
    return FixedRangeMomentLimit(mu, rho, dt, D, c4, ratio)


def discrete_fixed_range_coefficients(
    *,
    mutation_rate: float,
    physical_radius: float,
    radius_bins: int,
    time_step: float,
):
    """Finite-J coefficients with ``h=rho/J`` for the fixed-range sequence."""
    J = int(radius_bins)
    if J < 1:
        raise ValueError("radius_bins must be at least 1")
    rho = float(physical_radius)
    if not isfinite(rho) or rho <= 0.0:
        raise ValueError("physical_radius must be finite and positive")
    return continuum_coefficients(
        mutation_rate=mutation_rate,
        radius_bins=J,
        grid_spacing=rho / J,
        time_step=time_step,
    )


def nonlocal_uniform_generator_value(
    *,
    local_value: float,
    neighbourhood_average: float,
    mutation_rate: float,
    time_step: float,
) -> float:
    """Continuum fixed-range jump generator from the uniform neighbourhood mean.

    In Regime B the limiting generator is

        L_rho f(z)
        = (mu/Delta t) [ (1/(2rho)) integral_{-rho}^{rho} f(z+s) ds - f(z) ].

    This helper evaluates that expression once the neighbourhood integral has
    been supplied as its uniform average.  It deliberately does not approximate
    the average by a second derivative.
    """
    mu = float(mutation_rate)
    dt = float(time_step)
    if not 0.0 <= mu <= 1.0:
        raise ValueError("mutation_rate must lie in [0, 1]")
    if not isfinite(dt) or dt <= 0.0:
        raise ValueError("time_step must be finite and positive")
    a = float(local_value)
    avg = float(neighbourhood_average)
    if not isfinite(a) or not isfinite(avg):
        raise ValueError("values must be finite")
    return mu * (avg - a) / dt
