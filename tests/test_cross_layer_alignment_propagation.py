from __future__ import annotations

import json
from pathlib import Path
from types import SimpleNamespace

import pytest

np = pytest.importorskip("numpy")

from eco_genetic_warning_extensions.cross_layer_alignment_phase_v import (
    one_step_state_sufficiency_certificate,
    signatures_match,
)
from eco_genetic_warning_extensions.cross_layer_alignment_propagation import (
    PROPAGATION_HORIZONS,
    bootstrap_median_curve,
    classify_interaction_memory,
    reproduction_gate,
    simultaneous_risk_difference_band,
    snapshot_distances,
    trajectory_seed,
)

ROOT = Path(__file__).resolve().parents[1]
LOCKED = ROOT / "artifacts" / "cross_layer_alignment" / "phase_v_locked_summary.json"


def _snapshot(
    generation: int,
    *,
    interaction=(0.1, 0.2, 0.3, 0.4),
    population=(10, 20, 30, 40),
    effective_size=(6.0, 12.0, 18.0, 24.0),
    frequency=(0.2, 0.4, 0.6, 0.8),
    high_mass=(0.1, 0.3, 0.5, 0.7),
    h_alpha=0.4,
    h_gamma=0.5,
    fst=0.2,
):
    return SimpleNamespace(
        generation=generation,
        interaction=interaction,
        population=population,
        effective_size=effective_size,
        high_allele_frequency=frequency,
        trait_occupancy=tuple(SimpleNamespace(high_trait_mass=value) for value in high_mass),
        h_alpha=h_alpha,
        h_gamma=h_gamma,
        fst=fst,
    )


def test_horizon_grid_and_historical_seed_map_are_fixed():
    assert PROPAGATION_HORIZONS == (1, 2, 5, 10, 20, 40, 60)
    assert trajectory_seed(20300110, 0) == 7_985_256
    assert trajectory_seed(20300110, 99) == 7_995_255
    assert trajectory_seed(20300114, 0) == 11_985_268
    assert trajectory_seed(20300114, 99) == 11_995_267


def test_restored_phase_v_certificate_matches_locked_number():
    assert signatures_match() is True
    certificate = one_step_state_sufficiency_certificate()
    assert certificate["coarse_marginal_signatures_identical"] is True
    assert certificate["coarse_marginals_are_transition_sufficient"] is False
    assert abs(certificate["maximum_patchwise_generation1_difference"] - 0.25433292878878405) < 1e-15


def test_snapshot_distance_uses_declared_patch_identity_without_sorting():
    left = _snapshot(5)
    right = _snapshot(
        5,
        interaction=(0.4, 0.2, 0.3, 0.1),
        population=(40, 20, 30, 10),
        effective_size=(24.0, 12.0, 18.0, 6.0),
        frequency=(0.8, 0.4, 0.6, 0.2),
        high_mass=(0.7, 0.3, 0.5, 0.1),
        h_alpha=0.3,
        h_gamma=0.45,
        fst=None,
    )
    distances = snapshot_distances(left, right)
    assert distances["interaction_max_abs"] == 0.30000000000000004
    assert abs(distances["interaction_mean_abs"] - 0.15) < 1e-15
    assert distances["population_mean_abs"] == 15.0
    assert distances["effective_size_mean_abs"] == 9.0
    assert abs(distances["high_allele_frequency_mean_abs"] - 0.3) < 1e-15
    assert abs(distances["high_trait_mass_mean_abs"] - 0.3) < 1e-15
    assert abs(distances["h_alpha_abs"] - 0.1) < 1e-15
    assert abs(distances["h_gamma_abs"] - 0.05) < 1e-15
    assert distances["fst_abs"] is None


def test_memory_classification_covers_all_preregistered_branches():
    short = {1: 1.0, 2: 0.4, 5: 0.3, 10: 0.2, 20: 0.2, 40: 0.1, 60: 0.1}
    assert classify_interaction_memory(short) == {
        "classification": "short_representation_memory",
        "half_retention_horizon": 2,
        "half_level": 0.5,
    }

    late = {1: 1.0, 2: 0.9, 5: 0.8, 10: 0.7, 20: 0.6, 40: 0.55, 60: 0.49}
    result = classify_interaction_memory(late)
    assert result["classification"] == "attenuating_representation_memory"
    assert result["half_retention_horizon"] == 60

    persistent = {1: 1.0, 2: 0.9, 5: 0.8, 10: 0.7, 20: 0.6, 40: 0.55, 60: 0.51}
    assert classify_interaction_memory(persistent)["classification"] == "persistent_representation_memory"

    rebound = {1: 1.0, 2: 0.4, 5: 0.6, 10: 0.3, 20: 0.2, 40: 0.2, 60: 0.2}
    result = classify_interaction_memory(rebound)
    assert result["classification"] == "nonmonotone_representation_memory"
    assert result["first_below_half_horizon"] == 2

    unidentified = {horizon: 0.0 for horizon in PROPAGATION_HORIZONS}
    assert classify_interaction_memory(unidentified)["classification"] == "representation_memory_not_identifiable"


def test_bootstrap_helpers_preserve_pair_cluster_and_family_logic():
    rng = np.random.default_rng(1)
    indices = rng.integers(0, 20, size=(200, 20), dtype=np.int32)

    zero_loss_difference = np.zeros((20, len(PROPAGATION_HORIZONS)), dtype=float)
    band = simultaneous_risk_difference_band(zero_loss_difference, indices)
    assert band["classification"] == "no_detected_horizon_family_loss_incidence_separation"
    assert band["simultaneous_half_width_95"] == 0.0

    certain_loss_difference = np.ones((20, len(PROPAGATION_HORIZONS)), dtype=float)
    band = simultaneous_risk_difference_band(certain_loss_difference, indices)
    assert band["classification"] == "horizon_family_loss_incidence_separation_detected"
    assert np.all(band["excludes_zero"])

    values = np.tile(np.arange(20, dtype=float)[:, None], (1, len(PROPAGATION_HORIZONS)))
    medians = bootstrap_median_curve(values, indices, batch_size=50)
    assert medians["observed_median"].shape == (len(PROPAGATION_HORIZONS),)
    assert np.all(medians["finite_pair_count"] == 20)
    assert np.all(medians["valid_bootstrap_draws"] == 200)


def test_reproduction_gate_is_anchored_to_locked_phase_v_counts():
    locked = json.loads(LOCKED.read_text(encoding="utf-8"))
    keys = [
        (seed, replicate)
        for seed in (20300110, 20300111, 20300112, 20300113, 20300114)
        for replicate in range(100)
    ]
    statuses = (
        [(True, True)] * 247
        + [(False, False)] * 47
        + [(True, False)] * 92
        + [(False, True)] * 114
    )
    records = []
    for (seed, replicate), (aligned_loss, anti_loss) in zip(keys, statuses):
        records.append(
            {
                "master_seed": seed,
                "replicate": replicate,
                "horizons": {
                    "60": {
                        "aligned_cumulative_loss": aligned_loss,
                        "anti_aligned_cumulative_loss": anti_loss,
                    }
                },
            }
        )
    gate = reproduction_gate(records, locked, one_step_state_sufficiency_certificate())
    assert gate["passed"] is True
    assert gate["decision"] == "reproduction_gate_passed"
