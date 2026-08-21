from types import SimpleNamespace

import pytest

from eco_genetic_warning_extensions.explicit_rewiring_phase_h import (
    PHASE_H_EDGE_CAPACITIES,
    PHASE_H_INITIAL_EDGE_STRENGTHS,
    PHASE_H_MASTER_SEEDS,
    PHASE_H_PARTNER_POOL_SIZE,
    PHASE_H_PRIMARY_PARTNER_COUNT,
    PHASE_H_REPLICATES_PER_SEED,
    PHASE_H_REWIRING_FRACTION,
    PHASE_H_REWIRING_WINDOW_GENERATIONS,
    active_edge_count,
    intact_edges,
    lost_primary_partner_index,
    network_edges_at_generation,
    network_schedule,
    phase_h_conditions,
    phase_h_manifest,
    post_loss_edges,
    rewired_target_edges,
    support_multiplier,
)
from eco_genetic_warning_extensions.explicit_rewiring_phase_h_runner import patched_interaction_support_schedule


def test_phase_h_manifest_freezes_network_and_warning_blind_opening_rule() -> None:
    manifest = phase_h_manifest()
    assert manifest["calibration_scope"] == "source_and_trait_loss_only"
    assert manifest["blinding_scope"] == "source_network_and_trait_loss_only"
    assert manifest["prepared_source_count"] == len(PHASE_H_MASTER_SEEDS) * PHASE_H_REPLICATES_PER_SEED
    assert manifest["trajectory_count"] == 3 * len(PHASE_H_MASTER_SEEDS) * PHASE_H_REPLICATES_PER_SEED
    assert manifest["paired_across_rewiring_conditions"] is True
    assert "intact control is R4_highrep" in manifest["opening_rule"]
    assert "partner-loss/no-rewiring condition is R3_highrep" in manifest["opening_rule"]
    assert "Do not tune" in manifest["stop_rule"]


def test_phase_h_conditions_change_only_loss_and_rewiring_rule() -> None:
    conditions = phase_h_conditions()
    assert [condition.name for condition in conditions] == [
        "intact_control",
        "partner_loss_no_rewiring",
        "partner_loss_trait_capacity_rewiring",
    ]
    assert conditions[0].remove_primary_partner is False
    assert conditions[1].remove_primary_partner is True
    assert conditions[2].remove_primary_partner is True
    assert conditions[1].rewiring_rule == "none"
    assert conditions[2].rewiring_rule == "trait_capacity"


def test_initial_network_has_four_active_edges_in_six_partner_pool() -> None:
    edges = intact_edges()
    assert len(edges) == PHASE_H_PARTNER_POOL_SIZE == 6
    assert tuple(edges) == PHASE_H_INITIAL_EDGE_STRENGTHS
    assert active_edge_count(edges) == PHASE_H_PRIMARY_PARTNER_COUNT == 4
    assert all(edge <= capacity for edge, capacity in zip(edges, PHASE_H_EDGE_CAPACITIES))
    assert support_multiplier(edges) == pytest.approx(1.0)


def test_partner_loss_identity_is_balanced_per_seed_block() -> None:
    counts = {index: 0 for index in range(PHASE_H_PRIMARY_PARTNER_COUNT)}
    for replicate in range(PHASE_H_REPLICATES_PER_SEED):
        counts[lost_primary_partner_index(replicate)] += 1
    assert counts == {0: 5, 1: 5, 2: 5, 3: 5}


def test_no_rewiring_and_rewiring_start_from_same_post_loss_network() -> None:
    no_rewire = phase_h_conditions()[1]
    rewire = phase_h_conditions()[2]
    for replicate in range(PHASE_H_PRIMARY_PARTNER_COUNT):
        base = post_loss_edges(replicate)
        assert network_edges_at_generation(no_rewire, replicate, 1) == base
        assert network_edges_at_generation(rewire, replicate, 1) == base
        assert active_edge_count(base) == 3
        assert base[lost_primary_partner_index(replicate)] == 0.0


def test_trait_capacity_rewiring_activates_latent_edges_and_respects_caps() -> None:
    rewire = phase_h_conditions()[2]
    for replicate in range(PHASE_H_PRIMARY_PARTNER_COUNT):
        target = rewired_target_edges(replicate)
        lost = lost_primary_partner_index(replicate)
        assert target[lost] == 0.0
        assert active_edge_count(target) == 5
        assert target[4] > 0.0 and target[5] > 0.0
        assert all(edge <= capacity + 1e-12 for edge, capacity in zip(target, PHASE_H_EDGE_CAPACITIES))
        assert sum(target) == pytest.approx(1.0 - 0.25 + PHASE_H_REWIRING_FRACTION * 0.25)
        assert support_multiplier(target) > support_multiplier(post_loss_edges(replicate))
        assert support_multiplier(target) <= 1.0


def test_rewiring_schedule_is_gradual_and_fixed_length() -> None:
    rewire = phase_h_conditions()[2]
    schedule = network_schedule(rewire, 0, 20)
    assert len(schedule) == 20
    assert schedule[0]["edge_strengths"] == list(post_loss_edges(0))
    assert schedule[PHASE_H_REWIRING_WINDOW_GENERATIONS - 1]["edge_strengths"] == pytest.approx(list(rewired_target_edges(0)))
    assert schedule[-1]["edge_strengths"] == pytest.approx(list(rewired_target_edges(0)))
    multipliers = [row["support_multiplier"] for row in schedule[:PHASE_H_REWIRING_WINDOW_GENERATIONS]]
    assert multipliers == sorted(multipliers)


def test_support_schedule_patch_is_scoped_generation_aware_and_restored() -> None:
    module = SimpleNamespace()
    module.interaction_support_signal = lambda q, trait, allele, parameters: q + trait + allele
    original = module.interaction_support_signal
    with patched_interaction_support_schedule(module, (0.5, 0.75), patch_count=2) as state:
        assert module.interaction_support_signal(0.2, 0.3, 0.1, None) == pytest.approx(0.3)
        assert module.interaction_support_signal(0.2, 0.3, 0.1, None) == pytest.approx(0.3)
        assert module.interaction_support_signal(0.2, 0.3, 0.1, None) == pytest.approx(0.45)
        assert module.interaction_support_signal(0.2, 0.3, 0.1, None) == pytest.approx(0.45)
        assert state["calls"] == 4
    assert module.interaction_support_signal is original
