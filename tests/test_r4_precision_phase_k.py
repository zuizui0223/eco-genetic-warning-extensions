import pytest

from eco_genetic_warning_extensions.explicit_rewiring_phase_h import post_loss_edges, support_multiplier
from eco_genetic_warning_extensions.r4_precision_phase_k import (
    PHASE_H_PREFIX_LOSS,
    PHASE_I_PREFIX_LOSS,
    PHASE_K_MIN_BASELINE_ELIGIBLE_PER_SEED,
    PHASE_K_REPLICATES_PER_SEED,
    expected_prefix,
    phase_k_manifest,
    phase_k_seed_families,
)
from eco_genetic_warning_extensions.r4_precision_phase_k_runner import _support_schedule


def test_phase_k_uses_all_conflicting_historical_master_seeds() -> None:
    families = phase_k_seed_families()
    assert families["phase_h_seed_family"] == (20290710, 20290711, 20290712, 20290713, 20290714)
    assert families["phase_i_seed_family"] == (20290810, 20290811, 20290812, 20290813, 20290814)
    assert len({seed for seeds in families.values() for seed in seeds}) == 10


def test_phase_k_increases_precision_without_changing_historical_gate() -> None:
    manifest = phase_k_manifest()
    assert PHASE_K_REPLICATES_PER_SEED == 100
    assert PHASE_K_MIN_BASELINE_ELIGIBLE_PER_SEED == 70
    assert manifest["historical_r4_rule_unchanged"] == "all five observed block loss rates inside [0.30,0.70]"
    assert manifest["seed_selection"].startswith("all five Phase-H and all five Phase-I")
    assert "Do not add replacement seeds" in manifest["stop_rule"]


def test_locked_prefix_counts_are_exposed_for_both_families() -> None:
    for seed, counts in PHASE_H_PREFIX_LOSS.items():
        assert expected_prefix(seed, "partner_loss_no_rescue") == counts
    for seed, counts in PHASE_I_PREFIX_LOSS.items():
        assert expected_prefix(seed, "partner_loss_no_rescue") == counts


def test_phase_k_replays_exact_historical_partner_loss_support_not_constant_mean() -> None:
    levels = []
    for replicate in range(4):
        expected = support_multiplier(post_loss_edges(replicate))
        schedule = _support_schedule("partner_loss_no_rescue", replicate, 120)
        assert len(set(schedule)) == 1
        assert schedule[0] == pytest.approx(expected)
        levels.append(expected)
    assert len({round(value, 12) for value in levels}) == 4
    assert sum(levels) / len(levels) == pytest.approx(0.75)
    assert any(abs(value - 0.75) > 1e-3 for value in levels)


def test_intact_support_is_exactly_one() -> None:
    for replicate in range(4):
        assert set(_support_schedule("intact_control", replicate, 120)) == {1.0}


def test_phase_k_is_warning_blind_and_only_runs_two_conditions() -> None:
    manifest = phase_k_manifest()
    assert manifest["blinding_scope"] == "source_network_and_trait_loss_only"
    assert manifest["conditions"] == ["intact_control", "partner_loss_no_rescue"]
    assert manifest["paired_conditions"] is True
    assert manifest["trajectory_count"] == 2000
    assert manifest["prepared_source_count"] == 1000
    assert "replicate-specific" in manifest["partner_loss_support_closure"]
