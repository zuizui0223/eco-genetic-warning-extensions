"""Deterministic mutation-slot fixtures for Protocol 002.

These fixtures exercise only the post-migration, pre-drift mutation slot. They do
not implement the ecological simulator, H1 source reconstruction, deterioration,
finite drift, or warning validation.
"""
from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass

from .mutation_coordinates import MutationCoordinates
from .protocol002_upstream_adapter import (
    apply_protocol002_mutation,
    upstream_symmetric_reference,
    validate_frequency_sequence,
)


MutationMap = Callable[[float], float]


@dataclass(frozen=True)
class MutationSlotFixture:
    """A deterministic recurrence through the mutation slot only."""

    initial_frequency: float
    generations: int

    def __post_init__(self) -> None:
        validate_frequency_sequence((self.initial_frequency,))
        if self.generations < 0:
            raise ValueError("generations must be non-negative")


def iterate_mutation_slot(fixture: MutationSlotFixture, mutation_map: MutationMap) -> tuple[float, ...]:
    """Return the inclusive deterministic trajectory under one mutation map.

    The first element is the initial post-migration frequency. Each subsequent
    element is the output of the mutation slot from the previous frequency. No
    drift, selection, migration, or trait recruitment is applied here.
    """
    trajectory = [float(fixture.initial_frequency)]
    current = trajectory[0]
    for _ in range(fixture.generations):
        current = float(mutation_map(current))
        validate_frequency_sequence((current,))
        trajectory.append(current)
    return tuple(trajectory)


def protocol002_mutation_slot_trajectory(
    fixture: MutationSlotFixture,
    coordinate: MutationCoordinates,
) -> tuple[float, ...]:
    """Return the Protocol 002 mutation-slot-only trajectory."""
    return iterate_mutation_slot(
        fixture,
        lambda value: apply_protocol002_mutation((value,), coordinate)[0],
    )


def upstream_symmetric_slot_trajectory(
    fixture: MutationSlotFixture,
    *,
    symmetric_mutation_rate: float,
) -> tuple[float, ...]:
    """Return the pinned upstream symmetric mutation-slot-only trajectory."""
    return iterate_mutation_slot(
        fixture,
        lambda value: upstream_symmetric_reference(value, symmetric_mutation_rate=symmetric_mutation_rate),
    )


def symmetric_slot_bridge_differences(
    fixture: MutationSlotFixture,
    *,
    symmetric_mutation_rate: float,
) -> tuple[float, ...]:
    """Return Protocol 002 SYM trajectory minus upstream symmetric trajectory."""
    coordinate = MutationCoordinates(kappa_mu=2.0 * symmetric_mutation_rate, p_star=0.5)
    protocol = protocol002_mutation_slot_trajectory(fixture, coordinate)
    upstream = upstream_symmetric_slot_trajectory(
        fixture,
        symmetric_mutation_rate=symmetric_mutation_rate,
    )
    return tuple(left - right for left, right in zip(protocol, upstream, strict=True))
