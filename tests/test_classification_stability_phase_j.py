from eco_genetic_warning_extensions.classification_stability_phase_j import (
    PHASE_J_MASTER_SEEDS,
    PHASE_J_MIGRATION_RATE,
    PHASE_J_PANEL_SIZE,
    PHASE_J_REPLICATES_PER_SEED,
    phase_j_manifest,
    phase_j_panels,
)


def test_phase_j_fixes_one_condition_and_twenty_fresh_seed_blocks() -> None:
    manifest = phase_j_manifest()
    assert manifest["calibration_scope"] == "source_and_trait_loss_only"
    assert manifest["blinding_scope"] == "source_and_trait_loss_only"
    assert manifest["fixed_condition"]["migration_rate"] == 0.10
    assert manifest["prepared_source_count"] == len(PHASE_J_MASTER_SEEDS) * PHASE_J_REPLICATES_PER_SEED == 400
    assert manifest["trajectory_count"] == 400
    assert len(PHASE_J_MASTER_SEEDS) == 20
    assert PHASE_J_MIGRATION_RATE == 0.10


def test_phase_j_panels_are_prospectively_fixed_disjoint_and_complete() -> None:
    panels = phase_j_panels()
    assert len(panels) == 4
    assert all(len(panel) == PHASE_J_PANEL_SIZE == 5 for panel in panels)
    flattened = [seed for panel in panels for seed in panel]
    assert flattened == list(PHASE_J_MASTER_SEEDS)
    assert len(set(flattened)) == 20


def test_phase_j_historical_results_motivate_but_do_not_select_design() -> None:
    manifest = phase_j_manifest()
    context = manifest["motivation_only_not_selection_data"]
    assert context["phase_e_m010_regime"] == "R3_highrep"
    assert context["phase_i_m010_regime"] == "R4_highrep"
    assert "do not alter" in context["rule"]


def test_phase_j_stop_rule_forbids_adaptive_seed_or_panel_changes() -> None:
    stop = phase_j_manifest()["stop_rule"].lower()
    for token in ("exactly these 20", "do not add seeds", "regroup panels", "m=0.10", "r4 thresholds"):
        assert token in stop
