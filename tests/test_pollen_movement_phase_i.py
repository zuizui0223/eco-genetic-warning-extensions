import pytest

from eco_genetic_warning_extensions.pollen_movement_phase_i import (
    PHASE_I_EQUIVALENT_GLOBAL_MIGRATION_RATE,
    PHASE_I_MASTER_SEEDS,
    PHASE_I_POLLEN_POOL_FRACTION,
    PHASE_I_REPLICATES_PER_SEED,
    census_weighted_regional_pool,
    census_weighted_ring_pool,
    equivalent_global_migration_rate,
    global_pollen_equals_legacy_mixing,
    offspring_allele_frequency,
    phase_i_conditions,
    phase_i_manifest,
    pollen_offspring_frequencies,
)


def test_phase_i_manifest_freezes_process_resolved_movement_and_blinding() -> None:
    manifest = phase_i_manifest()
    assert manifest["calibration_scope"] == "source_and_trait_loss_only"
    assert manifest["blinding_scope"] == "source_movement_and_trait_loss_only"
    assert manifest["prepared_source_count"] == len(PHASE_I_MASTER_SEEDS) * PHASE_I_REPLICATES_PER_SEED
    assert manifest["trajectory_count"] == 4 * len(PHASE_I_MASTER_SEEDS) * PHASE_I_REPLICATES_PER_SEED
    assert manifest["paired_across_movement_conditions"] is True
    assert manifest["pollen_pool_fraction"] == pytest.approx(0.20)
    assert manifest["exact_global_equivalence"]["legacy_migration_rate"] == pytest.approx(0.10)
    assert "Do not tune" in manifest["stop_rule"]


def test_phase_i_conditions_keep_pollen_and_legacy_mixing_separate() -> None:
    conditions = phase_i_conditions()
    assert [condition.name for condition in conditions] == [
        "no_pollen_control",
        "regional_pollen_pool_g020",
        "legacy_allele_mixing_m010",
        "ring_pollen_pool_g020",
    ]
    regional = conditions[1]
    legacy = conditions[2]
    ring = conditions[3]
    assert regional.pollen_pool_fraction == pytest.approx(PHASE_I_POLLEN_POOL_FRACTION)
    assert regional.legacy_migration_rate == 0.0
    assert ring.pollen_pool_fraction == pytest.approx(PHASE_I_POLLEN_POOL_FRACTION)
    assert ring.legacy_migration_rate == 0.0
    assert legacy.pollen_pool_fraction == 0.0
    assert legacy.legacy_migration_rate == pytest.approx(PHASE_I_EQUIVALENT_GLOBAL_MIGRATION_RATE)


def test_diploid_pollen_identity_maps_g_to_m_over_two() -> None:
    assert equivalent_global_migration_rate(0.20) == pytest.approx(0.10)
    local = 0.8
    pool = 0.2
    g = 0.20
    expected = (1.0 - 0.10) * local + 0.10 * pool
    assert offspring_allele_frequency(local, pool, g) == pytest.approx(expected)


def test_regional_pollen_is_exactly_legacy_global_mixing_for_arbitrary_state() -> None:
    selected = (0.1, 0.3, 0.7, 0.9)
    weights = (5.0, 20.0, 10.0, 15.0)
    assert global_pollen_equals_legacy_mixing(selected, weights, 0.20)
    regional_pool = census_weighted_regional_pool(selected, weights)
    regional = pollen_offspring_frequencies(selected, weights, pollen_pool_fraction=0.20, kernel="regional")
    mean = regional_pool[0]
    legacy = tuple(0.9 * p + 0.1 * mean for p in selected)
    assert regional == pytest.approx(legacy)


def test_ring_pool_uses_only_circular_neighbours_and_census_weights() -> None:
    selected = (0.1, 0.2, 0.8, 0.9)
    weights = (10.0, 20.0, 30.0, 40.0)
    pools = census_weighted_ring_pool(selected, weights)
    assert pools[0] == pytest.approx((20.0 * 0.2 + 40.0 * 0.9) / 60.0)
    assert pools[1] == pytest.approx((10.0 * 0.1 + 30.0 * 0.8) / 40.0)
    assert pools[2] == pytest.approx((20.0 * 0.2 + 40.0 * 0.9) / 60.0)
    assert pools[3] == pytest.approx((30.0 * 0.8 + 10.0 * 0.1) / 40.0)


def test_same_g_can_generate_different_offspring_under_different_spatial_kernels() -> None:
    selected = (0.1, 0.2, 0.8, 0.9)
    weights = (10.0, 20.0, 30.0, 40.0)
    regional = pollen_offspring_frequencies(selected, weights, pollen_pool_fraction=0.20, kernel="regional")
    ring = pollen_offspring_frequencies(selected, weights, pollen_pool_fraction=0.20, kernel="ring")
    assert regional != pytest.approx(ring)
