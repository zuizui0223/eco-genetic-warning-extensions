"""Small-jump mutation bridge for finite eco-genetic trait-bin states.

This extension intentionally does not modify the locked parent simulator.
It supplies a local mutation operator that can be composed prospectively with
trait-bin selection in separately declared extension experiments.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import isfinite
from typing import Sequence


def normalise_distribution(values: Sequence[float]) -> tuple[float, ...]:
    vals = tuple(float(v) for v in values)
    if not vals:
        raise ValueError("distribution must be non-empty")
    if any((not isfinite(v)) or v < 0.0 for v in vals):
        raise ValueError("distribution must be finite and non-negative")
    total = sum(vals)
    if total <= 0.0:
        raise ValueError("distribution must have positive mass")
    return tuple(v / total for v in vals)


def local_trait_mutation(
    distribution: Sequence[float],
    *,
    mutation_rate: float,
    radius_bins: int = 1,
) -> tuple[float, ...]:
    """Move mutated mass only to neighbouring trait bins.

    The kernel is symmetric in the interior and truncated/renormalised at the
    finite trait boundaries. No mass leaks outside the represented trait grid.
    """
    f = normalise_distribution(distribution)
    if not 0.0 <= mutation_rate <= 1.0:
        raise ValueError("mutation_rate must lie in [0, 1]")
    if radius_bins < 0:
        raise ValueError("radius_bins must be non-negative")
    if mutation_rate == 0.0 or radius_bins == 0:
        return f

    out = [0.0] * len(f)
    for i, mass in enumerate(f):
        out[i] += (1.0 - mutation_rate) * mass
        neighbours = [
            j
            for j in range(max(0, i - radius_bins), min(len(f), i + radius_bins + 1))
            if j != i
        ]
        if not neighbours:
            out[i] += mutation_rate * mass
            continue
        share = mutation_rate * mass / len(neighbours)
        for j in neighbours:
            out[j] += share
    return normalise_distribution(out)


def viability_selection(
    distribution: Sequence[float],
    fitness: Sequence[float],
    *,
    floor: float = 1e-12,
) -> tuple[float, ...]:
    """Parent-compatible multiplicative viability-selection form."""
    f = normalise_distribution(distribution)
    w = tuple(float(x) for x in fitness)
    if len(f) != len(w):
        raise ValueError("distribution and fitness must have equal length")
    if floor <= 0.0:
        raise ValueError("floor must be positive")
    if any(not isfinite(x) for x in w):
        raise ValueError("fitness must be finite")
    weighted = tuple(mass * max(floor, value) for mass, value in zip(f, w))
    return normalise_distribution(weighted)


@dataclass(frozen=True)
class TraitBinStep:
    before: tuple[float, ...]
    after_selection: tuple[float, ...]
    after_mutation: tuple[float, ...]
    mutation_rate: float
    radius_bins: int


def selection_mutation_step(
    distribution: Sequence[float],
    fitness: Sequence[float],
    *,
    mutation_rate: float,
    radius_bins: int = 1,
    floor: float = 1e-12,
) -> TraitBinStep:
    before = normalise_distribution(distribution)
    selected = viability_selection(before, fitness, floor=floor)
    mutated = local_trait_mutation(
        selected, mutation_rate=mutation_rate, radius_bins=radius_bins
    )
    return TraitBinStep(
        before=before,
        after_selection=selected,
        after_mutation=mutated,
        mutation_rate=float(mutation_rate),
        radius_bins=int(radius_bins),
    )


def interior_jump_variance(
    *,
    mutation_rate: float,
    radius_bins: int,
    grid_spacing: float,
) -> float:
    """Expected squared trait displacement for an interior source bin.

    Conditional mutated jumps are uniform over +/-1,...,+/-radius_bins.
    The returned value includes the probability of no mutation.
    """
    if not 0.0 <= mutation_rate <= 1.0:
        raise ValueError("mutation_rate must lie in [0, 1]")
    if radius_bins < 0:
        raise ValueError("radius_bins must be non-negative")
    if grid_spacing <= 0.0:
        raise ValueError("grid_spacing must be positive")
    if radius_bins == 0 or mutation_rate == 0.0:
        return 0.0
    mean_square_bins = sum(k * k for k in range(1, radius_bins + 1)) / radius_bins
    return mutation_rate * mean_square_bins * grid_spacing * grid_spacing


def diffusion_coefficient_from_small_jump(
    *,
    mutation_rate: float,
    radius_bins: int,
    grid_spacing: float,
    time_step: float = 1.0,
) -> float:
    """Interior diffusion diagnostic D = E[(Delta z)^2]/(2 Delta t).

    This is a scaling diagnostic only; it does not assert that the finite
    parent simulator already obeys a Fokker--Planck PDE.
    """
    if time_step <= 0.0:
        raise ValueError("time_step must be positive")
    return interior_jump_variance(
        mutation_rate=mutation_rate,
        radius_bins=radius_bins,
        grid_spacing=grid_spacing,
    ) / (2.0 * time_step)
