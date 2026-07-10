"""Minimal deterministic life-cycle fixtures for Protocol 002.

This module fixes the ordering around the mutation slot without running the full
eco-genetic simulator. It is a regression fixture, not Stage I source
reconstruction.
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

FrequencyTransform = Callable[[float], float]


def identity_transform(frequency: float) -> float:
    """Return the input frequency unchanged."""
    return float(frequency)


@dataclass(frozen=True)
class MinimalLifeCycleFixture:
    """A deterministic fixture for the ordered allele-frequency life cycle.

    The fixture records only allele-frequency transformations. It does not model
    ecological interaction, trait recruitment, stochastic drift, or event
    semantics.
    """

    initial_frequency: float
    generations: int

    def __post_init__(self) -> None:
        validate_frequency_sequence((self.initial_frequency,))
        if self.generations < 0:
            raise ValueError("generations must be non-negative")


@dataclass(frozen=True)
class MinimalLifeCycleStep:
    """One fully auditable generation in the minimal fixture."""

    generation: int
    resident_frequency: float
    after_selection: float
    after_migration: float
    after_mutation: float
    after_drift: float

    def as_tuple(self) -> tuple[float, float, float, float, float]:
        """Return numerical states without the generation label."""
        return (
            self.resident_frequency,
            self.after_selection,
            self.after_migration,
            self.after_mutation,
            self.after_drift,
        )


def _checked_transform(transform: FrequencyTransform, frequency: float) -> float:
    value = float(transform(float(frequency)))
    validate_frequency_sequence((value,))
    return value


def run_minimal_life_cycle(
    fixture: MinimalLifeCycleFixture,
    *,
    selection: FrequencyTransform = identity_transform,
    migration: FrequencyTransform = identity_transform,
    mutation: FrequencyTransform,
    drift: FrequencyTransform = identity_transform,
) -> tuple[MinimalLifeCycleStep, ...]:
    """Run the ordered deterministic fixture.

    Per generation, the order is:

    resident -> selection -> migration -> mutation -> deterministic/no-op drift
    """
    resident = float(fixture.initial_frequency)
    steps: list[MinimalLifeCycleStep] = []
    for generation in range(1, fixture.generations + 1):
        after_selection = _checked_transform(selection, resident)
        after_migration = _checked_transform(migration, after_selection)
        after_mutation = _checked_transform(mutation, after_migration)
        after_drift = _checked_transform(drift, after_mutation)
        steps.append(
            MinimalLifeCycleStep(
                generation=generation,
                resident_frequency=resident,
                after_selection=after_selection,
                after_migration=after_migration,
                after_mutation=after_mutation,
                after_drift=after_drift,
            )
        )
        resident = after_drift
    return tuple(steps)


def run_protocol002_minimal_life_cycle(
    fixture: MinimalLifeCycleFixture,
    coordinate: MutationCoordinates,
    *,
    selection: FrequencyTransform = identity_transform,
    migration: FrequencyTransform = identity_transform,
    drift: FrequencyTransform = identity_transform,
) -> tuple[MinimalLifeCycleStep, ...]:
    """Run the minimal fixture with a Protocol 002 mutation coordinate."""
    return run_minimal_life_cycle(
        fixture,
        selection=selection,
        migration=migration,
        mutation=lambda value: apply_protocol002_mutation((value,), coordinate)[0],
        drift=drift,
    )


def run_upstream_symmetric_minimal_life_cycle(
    fixture: MinimalLifeCycleFixture,
    *,
    symmetric_mutation_rate: float,
    selection: FrequencyTransform = identity_transform,
    migration: FrequencyTransform = identity_transform,
    drift: FrequencyTransform = identity_transform,
) -> tuple[MinimalLifeCycleStep, ...]:
    """Run the minimal fixture with the pinned upstream symmetric mutation map."""
    return run_minimal_life_cycle(
        fixture,
        selection=selection,
        migration=migration,
        mutation=lambda value: upstream_symmetric_reference(value, symmetric_mutation_rate=symmetric_mutation_rate),
        drift=drift,
    )


def symmetric_minimal_life_cycle_differences(
    fixture: MinimalLifeCycleFixture,
    *,
    symmetric_mutation_rate: float,
    selection: FrequencyTransform = identity_transform,
    migration: FrequencyTransform = identity_transform,
    drift: FrequencyTransform = identity_transform,
) -> tuple[tuple[float, float, float, float, float], ...]:
    """Return Protocol 002 SYM minus upstream symmetric states per generation."""
    coordinate = MutationCoordinates(kappa_mu=2.0 * symmetric_mutation_rate, p_star=0.5)
    protocol = run_protocol002_minimal_life_cycle(
        fixture,
        coordinate,
        selection=selection,
        migration=migration,
        drift=drift,
    )
    upstream = run_upstream_symmetric_minimal_life_cycle(
        fixture,
        symmetric_mutation_rate=symmetric_mutation_rate,
        selection=selection,
        migration=migration,
        drift=drift,
    )
    return tuple(
        tuple(left - right for left, right in zip(p_step.as_tuple(), u_step.as_tuple(), strict=True))
        for p_step, u_step in zip(protocol, upstream, strict=True)
    )
