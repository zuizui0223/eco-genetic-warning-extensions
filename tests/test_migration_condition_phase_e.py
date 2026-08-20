import pytest

from eco_genetic_warning_extensions.migration_condition_phase_e import (
    PHASE_E_MASTER_SEEDS,
    PHASE_E_MIGRATION_RATES,
    PHASE_E_REPLICATES_PER_SEED,
    deviation_contraction_factor,
    phase_e_manifest,
    variance_contraction_factor,
)


def test_phase_e_manifest_is_fixed_and_paired() -> None:
    manifest = phase_e_manifest()
    assert manifest["migration_rates"] == list(PHASE_E_MIGRATION_RATES)
    assert manifest["master_seeds"] == list(PHASE_E_MASTER_SEEDS)
    assert manifest["replicates_per_seed"] == PHASE_E_REPLICATES_PER_SEED == 20
    assert manifest["prepared_source_count"] == 100
    assert manifest["trajectory_count"] == 500
    assert manifest["paired_across_migration_rates"] is True
    assert manifest["calibration_scope"] == "trait_loss_only"
    assert manifest["coordinate"] == {"kappa_mu": 0.35, "p_star": 0.35}
    assert manifest["ecological_anchor"]["area_reference"] == 1.0
    assert manifest["ecological_anchor"]["interaction_kappa"] == 4.5
    assert manifest["ecological_anchor"]["normalised_barrier_increase"] == 0.30


def test_migration_exactly_contracts_deviations_and_variance() -> None:
    assert deviation_contraction_factor(0.0) == pytest.approx(1.0)
    assert deviation_contraction_factor(0.1) == pytest.approx(0.9)
    assert variance_contraction_factor(0.1) == pytest.approx(0.81)
    assert variance_contraction_factor(0.2) == pytest.approx(0.64)


def test_invalid_migration_rate_is_rejected() -> None:
    with pytest.raises(ValueError, match="migration_rate"):
        deviation_contraction_factor(-0.01)
    with pytest.raises(ValueError, match="migration_rate"):
        deviation_contraction_factor(1.01)
