from eco_genetic_warning_extensions.interaction_support_phase_f import (
    PHASE_F_AREA_REFERENCE,
    PHASE_F_INTERACTION_KAPPAS,
    PHASE_F_KAPPA_MU,
    PHASE_F_MIGRATION_RATE,
    PHASE_F_P_STAR,
    PHASE_F_REPLICATES_PER_SEED,
    phase_f_manifest,
)


def test_phase_f_reuses_original_protocol002_kappa_levels() -> None:
    assert PHASE_F_INTERACTION_KAPPAS == (3.0, 4.5, 6.0)
    assert PHASE_F_AREA_REFERENCE == 1.0
    assert PHASE_F_KAPPA_MU == 0.35
    assert PHASE_F_P_STAR == 0.35
    assert PHASE_F_MIGRATION_RATE == 0.0
    assert PHASE_F_REPLICATES_PER_SEED == 20


def test_phase_f_manifest_is_warning_blind_and_bounded() -> None:
    manifest = phase_f_manifest()
    assert manifest["calibration_scope"] == "source_and_trait_loss_only"
    assert manifest["warning_blind"] is True
    assert manifest["interaction_kappa_provenance"] == "original_protocol002_source_grid_values"
    assert manifest["condition_count"] == 3
    assert "do not refine kappa" in manifest["stop_rule"]


def test_phase_f_does_not_claim_network_simplification() -> None:
    boundary = phase_f_manifest()["interpretation_boundary"]
    assert "not partner richness" in boundary
    assert "network dimensionality" in boundary
    assert "pollinator diversity" in boundary
