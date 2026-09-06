"""Exact interior finite-difference bridge from radius-one mutation to diffusion."""
from __future__ import annotations

from dataclasses import dataclass
from math import isfinite
from typing import Sequence

from eco_genetic_warning_extensions.small_jump_trait_bins import (
    diffusion_coefficient_from_small_jump,
    local_trait_mutation,
    normalise_distribution,
)


def diffusive_time_step(
    *, mutation_rate: float, grid_spacing: float, target_diffusion: float
) -> float:
    """Return Delta t that preserves a target radius-one diffusion coefficient."""
    mu = float(mutation_rate)
    h = float(grid_spacing)
    D = float(target_diffusion)
    if not 0.0 < mu <= 1.0:
        raise ValueError("mutation_rate must lie in (0, 1]")
    if not isfinite(h) or h <= 0.0:
        raise ValueError("grid_spacing must be finite and positive")
    if not isfinite(D) or D <= 0.0:
        raise ValueError("target_diffusion must be finite and positive")
    return mu * h * h / (2.0 * D)


def discrete_laplacian(values: Sequence[float], *, grid_spacing: float) -> tuple[float, ...]:
    """Return the centered second difference on interior indices.

    Boundary entries are NaN because this module does not silently choose a
    continuum boundary condition for the parent finite-bin closure.
    """
    vals = tuple(float(v) for v in values)
    h = float(grid_spacing)
    if len(vals) < 3:
        raise ValueError("values must contain at least three bins")
    if any(not isfinite(v) for v in vals):
        raise ValueError("values must be finite")
    if not isfinite(h) or h <= 0.0:
        raise ValueError("grid_spacing must be finite and positive")
    out = [float("nan")] * len(vals)
    scale = h * h
    for i in range(1, len(vals) - 1):
        out[i] = (vals[i - 1] - 2.0 * vals[i] + vals[i + 1]) / scale
    return tuple(out)


def mutation_generator(
    distribution: Sequence[float], *, mutation_rate: float, time_step: float
) -> tuple[float, ...]:
    """Return (M_mu f - f)/Delta t for the radius-one mutation operator."""
    f = normalise_distribution(distribution)
    dt = float(time_step)
    if not isfinite(dt) or dt <= 0.0:
        raise ValueError("time_step must be finite and positive")
    after = local_trait_mutation(f, mutation_rate=mutation_rate, radius_bins=1)
    return tuple((b - a) / dt for a, b in zip(f, after))


@dataclass(frozen=True)
class DiffusionIdentityAudit:
    diffusion_coefficient: float
    checked_indices: tuple[int, ...]
    generator: tuple[float, ...]
    diffusion_rhs: tuple[float, ...]
    residuals: tuple[float, ...]
    max_abs_residual: float


def audit_radius_one_diffusion_identity(
    distribution: Sequence[float],
    *,
    mutation_rate: float,
    grid_spacing: float,
    time_step: float,
) -> DiffusionIdentityAudit:
    """Verify the exact strict-interior discrete diffusion identity.

    With the current boundary-renormalised mutation operator, indices adjacent
    to a finite boundary receive asymmetric inflow from the endpoint bin. The
    exact centered-laplacian identity is therefore checked only on indices
    ``2..n-3``. No continuum boundary condition is inferred here.
    """
    f = normalise_distribution(distribution)
    if len(f) < 5:
        raise ValueError("at least five bins are required for a strict interior")
    generator = mutation_generator(
        f, mutation_rate=mutation_rate, time_step=time_step
    )
    lap = discrete_laplacian(f, grid_spacing=grid_spacing)
    D = diffusion_coefficient_from_small_jump(
        mutation_rate=mutation_rate,
        radius_bins=1,
        grid_spacing=grid_spacing,
        time_step=time_step,
    )
    rhs = tuple(
        float("nan") if value != value else D * value
        for value in lap
    )
    checked = tuple(range(2, len(f) - 2))
    residuals = tuple(generator[i] - rhs[i] for i in checked)
    max_abs = max((abs(value) for value in residuals), default=0.0)
    return DiffusionIdentityAudit(
        diffusion_coefficient=D,
        checked_indices=checked,
        generator=generator,
        diffusion_rhs=rhs,
        residuals=residuals,
        max_abs_residual=max_abs,
    )
