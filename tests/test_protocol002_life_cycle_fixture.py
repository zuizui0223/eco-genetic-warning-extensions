import pytest

from eco_genetic_warning_extensions.mutation_coordinates import MutationCoordinates
from eco_genetic_warning_extensions.protocol002_life_cycle_fixture import (
    MinimalLifeCycleFixture,
    identity_transform,
    run_minimal_life_cycle,
    run_protocol002_minimal_life_cycle,
    run_upstream_symmetric_minimal_life_cycle,
    symmetric_minimal_life_cycle_differences,
)


def test_minimal_life_cycle_orders_selection_migration_mutation_drift() -> None:
    fixture = MinimalLifeCycleFixture(initial_frequency=0.20, generations=1)
    steps = run_minimal_life_cycle(
        fixture,
        selection=lambda value: value + 0.10,
        migration=lambda value: value + 0.05,
        mutation=lambda value: value + 0.20,
        drift=lambda value: value - 0.05,
    )
    assert len(steps) == 1
    assert steps[0].as_tuple() == pytest.approx((0.20, 0.30, 0.35, 0.55, 0.50))


def test_protocol002_minimal_life_cycle_applies_mutation_between_migration_and_drift() -> None:
    fixture = MinimalLifeCycleFixture(initial_frequency=0.40, generations=1)
    coordinate = MutationCoordinates(kappa_mu=0.20, p_star=0.75)
    steps = run_protocol002_minimal_life_cycle(
        fixture,
        coordinate,
        selection=lambda value: value + 0.10,
        migration=lambda value: value - 0.05,
        drift=identity_transform,
    )
    expected_migrated = 0.45
    expected_mutated = 0.20 * 0.75 + 0.80 * expected_migrated
    assert steps[0].resident_frequency == pytest.approx(0.40)
    assert steps[0].after_selection == pytest.approx(0.50)
    assert steps[0].after_migration == pytest.approx(expected_migrated)
    assert steps[0].after_mutation == pytest.approx(expected_mutated)
    assert steps[0].after_drift == pytest.approx(expected_mutated)


def test_symmetric_minimal_life_cycle_matches_upstream_with_noop_selection_migration_drift() -> None:
    fixture = MinimalLifeCycleFixture(initial_frequency=0.73, generations=10)
    differences = symmetric_minimal_life_cycle_differences(fixture, symmetric_mutation_rate=0.10)
    assert differences == pytest.approx(((0.0, 0.0, 0.0, 0.0, 0.0),) * 10)


def test_symmetric_minimal_life_cycle_matches_upstream_with_shared_deterministic_transforms() -> None:
    fixture = MinimalLifeCycleFixture(initial_frequency=0.31, generations=6)
    selection = lambda value: 0.95 * value + 0.02
    migration = lambda value: 0.90 * value + 0.04
    drift = lambda value: value
    protocol = run_protocol002_minimal_life_cycle(
        fixture,
        MutationCoordinates(kappa_mu=0.20, p_star=0.50),
        selection=selection,
        migration=migration,
        drift=drift,
    )
    upstream = run_upstream_symmetric_minimal_life_cycle(
        fixture,
        symmetric_mutation_rate=0.10,
        selection=selection,
        migration=migration,
        drift=drift,
    )
    assert [step.as_tuple() for step in protocol] == pytest.approx([step.as_tuple() for step in upstream])


def test_minimal_life_cycle_validates_state_after_each_transform() -> None:
    fixture = MinimalLifeCycleFixture(initial_frequency=0.95, generations=1)
    with pytest.raises(ValueError, match="\[0, 1\]"):
        run_minimal_life_cycle(
            fixture,
            selection=lambda value: value,
            migration=lambda value: value,
            mutation=lambda value: value + 0.10,
            drift=lambda value: value,
        )
    with pytest.raises(ValueError, match="non-negative"):
        MinimalLifeCycleFixture(initial_frequency=0.2, generations=-1)
