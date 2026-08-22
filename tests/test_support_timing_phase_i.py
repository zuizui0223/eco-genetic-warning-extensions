import pytest

from eco_genetic_warning_extensions.support_timing_phase_i import (
    PHASE_I_MASTER_SEEDS,
    PHASE_I_REPLICATES_PER_SEED,
    effective_support_at_generation,
    phase_i_conditions,
    phase_i_manifest,
    phase_i_schedule,
)


def _condition(name: str):
    return next(condition for condition in phase_i_conditions() if condition.name == name)


def test_phase_i_manifest_is_warning_blind_and_paired() -> None:
    manifest = phase_i_manifest()
    assert manifest["blinding_scope"] == "source_network_and_trait_loss_only"
    assert manifest["paired_across_conditions"] is True
    assert manifest["prepared_source_count"] == len(PHASE_I_MASTER_SEEDS) * PHASE_I_REPLICATES_PER_SEED
    assert manifest["trajectory_count"] == 7 * len(PHASE_I_MASTER_SEEDS) * PHASE_I_REPLICATES_PER_SEED
    assert "Do not tune" in manifest["stop_rule"]


def test_phase_i_condition_set_is_fixed() -> None:
    assert [condition.name for condition in phase_i_conditions()] == [
        "intact_control",
        "partner_loss_no_rescue",
        "topology_only_null",
        "partial_support_only",
        "coupled_rewiring_replay",
        "full_support_delayed",
        "full_support_immediate",
    ]


def test_topology_only_null_changes_topology_but_not_effective_support() -> None:
    loss = _condition("partner_loss_no_rescue")
    topology = _condition("topology_only_null")
    for generation in (1, 5, 10, 120):
        assert effective_support_at_generation(topology, 0, generation) == pytest.approx(
            effective_support_at_generation(loss, 0, generation)
        )
    loss_final = phase_i_schedule(loss, 0, 120)[-1]
    topology_final = phase_i_schedule(topology, 0, 120)[-1]
    assert topology_final["active_edge_count"] > loss_final["active_edge_count"]
    assert topology_final["realised_connectance"] > loss_final["realised_connectance"]


def test_partial_support_only_matches_coupled_effective_support_but_not_topology() -> None:
    partial = _condition("partial_support_only")
    coupled = _condition("coupled_rewiring_replay")
    for generation in (1, 5, 10, 120):
        assert effective_support_at_generation(partial, 1, generation) == pytest.approx(
            effective_support_at_generation(coupled, 1, generation)
        )
    partial_final = phase_i_schedule(partial, 1, 120)[-1]
    coupled_final = phase_i_schedule(coupled, 1, 120)[-1]
    assert partial_final["active_edge_count"] < coupled_final["active_edge_count"]


def test_delayed_full_support_has_same_start_and_reaches_one_by_generation_ten() -> None:
    loss = _condition("partner_loss_no_rescue")
    delayed = _condition("full_support_delayed")
    start = effective_support_at_generation(loss, 2, 1)
    assert effective_support_at_generation(delayed, 2, 1) == pytest.approx(start)
    values = [effective_support_at_generation(delayed, 2, generation) for generation in range(1, 11)]
    assert values == sorted(values)
    assert values[-1] == pytest.approx(1.0)
    assert effective_support_at_generation(delayed, 2, 120) == pytest.approx(1.0)


def test_immediate_full_support_is_one_despite_loss_topology() -> None:
    immediate = _condition("full_support_immediate")
    for generation in (1, 2, 10, 120):
        assert effective_support_at_generation(immediate, 3, generation) == pytest.approx(1.0)
    final = phase_i_schedule(immediate, 3, 120)[-1]
    assert final["active_edge_count"] == 3
    assert final["effective_support_multiplier"] == pytest.approx(1.0)


def test_partial_recovery_stays_below_or_equal_to_full_delayed_after_window() -> None:
    partial = _condition("partial_support_only")
    delayed = _condition("full_support_delayed")
    for replicate in range(4):
        assert effective_support_at_generation(partial, replicate, 120) <= effective_support_at_generation(delayed, replicate, 120)
