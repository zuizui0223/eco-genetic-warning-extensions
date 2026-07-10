"""Protocol 002 adapter contract for the pinned upstream life cycle.

This module does not import or copy the upstream simulator. It isolates the only
operation Protocol 002 is allowed to replace: the post-migration, pre-drift
allele-frequency mutation transform.
"""
from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass
from typing import Final

from .mutation_coordinates import MutationCoordinates
from .protocol002_stage0 import (
    LIFECYCLE_MUTATION_POSITION,
    UPSTREAM_COMMIT,
    UPSTREAM_MODULE,
    UPSTREAM_REPOSITORY,
)


@dataclass(frozen=True)
class UpstreamLifecycleLock:
    """Immutable provenance for the finite life-cycle contract used by Protocol 002."""

    repository: str
    commit: str
    module: str
    mutation_position: str


PINNED_UPSTREAM_LIFECYCLE: Final = UpstreamLifecycleLock(
    repository=UPSTREAM_REPOSITORY,
    commit=UPSTREAM_COMMIT,
    module=UPSTREAM_MODULE,
    mutation_position=LIFECYCLE_MUTATION_POSITION,
)


def validate_frequency_sequence(frequencies: Iterable[float]) -> tuple[float, ...]:
    """Return a tuple of allele frequencies after validating the unit interval."""
    values = tuple(float(value) for value in frequencies)
    if not values:
        raise ValueError("at least one frequency is required")
    for value in values:
        if not 0.0 <= value <= 1.0:
            raise ValueError("all frequencies must lie in [0, 1]")
    return values


def apply_protocol002_mutation(
    migrated_frequencies: Iterable[float],
    coordinate: MutationCoordinates,
) -> tuple[float, ...]:
    """Apply Protocol 002 mutation to post-migration, pre-drift frequencies.

    The caller supplies frequencies after selection and migration. This function
    performs only the affine mutation transform and returns the frequencies that
    should then be passed to finite genetic drift.
    """
    values = validate_frequency_sequence(migrated_frequencies)
    return tuple(coordinate.apply(value) for value in values)


def upstream_symmetric_reference(frequency: float, *, symmetric_mutation_rate: float) -> float:
    """Reference map from the pinned upstream symmetric mutation closure.

    The upstream closure applies ``p -> mu + (1 - 2 * mu) * p``. This function is
    deliberately tiny and auditable; it exists only to prove the SYM bridge.
    """
    p = float(frequency)
    mu = float(symmetric_mutation_rate)
    if not 0.0 <= p <= 1.0:
        raise ValueError("frequency must lie in [0, 1]")
    if not 0.0 <= mu < 0.5:
        raise ValueError("symmetric_mutation_rate must lie in [0, 0.5)")
    return mu + (1.0 - 2.0 * mu) * p


def symmetric_bridge_coordinate(*, symmetric_mutation_rate: float) -> MutationCoordinates:
    """Return the Protocol 002 coordinate equivalent to upstream symmetric mutation."""
    mu = float(symmetric_mutation_rate)
    if not 0.0 <= mu < 0.5:
        raise ValueError("symmetric_mutation_rate must lie in [0, 0.5)")
    return MutationCoordinates(kappa_mu=2.0 * mu, p_star=0.5)


def apply_symmetric_bridge(
    migrated_frequencies: Iterable[float],
    *,
    symmetric_mutation_rate: float,
) -> tuple[float, ...]:
    """Apply the Protocol 002 SYM bridge equivalent to the upstream symmetric map."""
    return apply_protocol002_mutation(
        migrated_frequencies,
        symmetric_bridge_coordinate(symmetric_mutation_rate=symmetric_mutation_rate),
    )


def symmetric_bridge_differences(
    frequencies: Iterable[float],
    *,
    symmetric_mutation_rate: float,
) -> tuple[float, ...]:
    """Return Protocol 002 minus upstream-reference values for SYM bridge checks."""
    values = validate_frequency_sequence(frequencies)
    bridged = apply_symmetric_bridge(values, symmetric_mutation_rate=symmetric_mutation_rate)
    reference = tuple(
        upstream_symmetric_reference(value, symmetric_mutation_rate=symmetric_mutation_rate)
        for value in values
    )
    return tuple(left - right for left, right in zip(bridged, reference, strict=True))
