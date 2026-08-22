from eco_genetic_warning_extensions.connectivity_precision_phase_m import (
    PHASE_M_MIN_BASELINE_ELIGIBLE_PER_SEED,
    PHASE_M_REPLICATES_PER_SEED,
    expected_prefix,
    phase_m_manifest,
)
from eco_genetic_warning_extensions.migration_condition_phase_e import PHASE_E_MASTER_SEEDS, PHASE_E_MIGRATION_RATES


def test_phase_m_reuses_all_historical_phase_e_seeds_and_rates() -> None:
    manifest = phase_m_manifest()
    assert tuple(manifest["master_seeds"]) == PHASE_E_MASTER_SEEDS
    assert tuple(manifest["migration_rates"]) == PHASE_E_MIGRATION_RATES
    assert PHASE_M_REPLICATES_PER_SEED == 100
    assert PHASE_M_MIN_BASELINE_ELIGIBLE_PER_SEED == 70
    assert manifest["seed_selection"].startswith("all five locked Phase-E")


def test_phase_m_prefix_counts_lock_historical_phase_e() -> None:
    assert expected_prefix(20290410, 0.0) == (15, 7)
    assert expected_prefix(20290410, 0.10) == (15, 10)
    assert expected_prefix(20290411, 0.20) == (18, 13)
    assert expected_prefix(20290412, 0.025) == (20, 9)
    assert expected_prefix(20290413, 0.05) == (18, 12)
    assert expected_prefix(20290414, 0.20) == (20, 12)


def test_phase_m_does_not_change_gate_or_biological_scope() -> None:
    manifest = phase_m_manifest()
    assert manifest["historical_r4_rule_unchanged"] == "all five observed block loss rates inside [0.30,0.70]"
    assert manifest["paired_across_migration_rates"] is True
    assert manifest["trajectory_count"] == 2500
    assert manifest["prepared_source_count"] == 500
    assert "allele-frequency mixing only" in manifest["interpretation_boundary"]
    assert "Do not add replacement" in manifest["stop_rule"]


def test_phase_m_is_warning_blind() -> None:
    manifest = phase_m_manifest()
    assert manifest["blinding_scope"] == "source_and_trait_loss_only"
    assert "warning" not in manifest["primary_question"].lower()
