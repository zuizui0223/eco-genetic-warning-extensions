from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREREG = (ROOT / "manuscript" / "empirical_e2_zurich_residual_context_preregistration.md").read_text(encoding="utf-8")
SCRIPT = (ROOT / "scripts" / "run_e2_zurich_residual_context.py").read_text(encoding="utf-8")
WORKFLOW = (ROOT / ".github" / "workflows" / "e2-zurich-envidat-audit.yml").read_text(encoding="utf-8")


def test_e2_sources_are_locked_before_new_fit() -> None:
    assert "before downloading or fitting the EnviDat pollination-success observations" in PREREG
    assert "10.16904/envidat.676" in PREREG
    assert "d6361f6874398e797322afe07a8fea85a3c7e927" in PREREG
    assert 'SOURCE_COMMIT = "d6361f6874398e797322afe07a8fea85a3c7e927"' in SCRIPT


def test_six_focal_functions_are_immutable() -> None:
    for token in (
        "daucus_seed_set",
        "raphanus_fruit_set",
        "raphanus_seed_set",
        "onobrychis_fruit_set",
        "symphytum_fruit_set",
        "symphytum_seed_set",
    ):
        assert token in SCRIPT
    assert "No endpoint is removed because its urban or interaction result is weak" in PREREG


def test_interaction_predictors_are_source_derived_not_searched() -> None:
    for token in (
        "A_Apis_Carrot",
        "A_socialBees_Carrot",
        "A_solitaryBees_Carrot",
        "A_otherAculeata_Carrot",
        "A_Syrphidae_Carrot",
        "A_Coleoptera_Carrot",
        "A_Apis_Radish",
        "A_Bombus_Sainfoin",
        "A_Bombus_Comfrey",
    ):
        assert token in SCRIPT
    assert "No interaction guild is added or dropped after viewing E2 results" in PREREG


def test_context_is_added_last_and_urban_scale_is_fixed() -> None:
    assert "E2-S1 — measured interaction-state model" in PREREG
    assert "E2-S2 — residual-context model" in PREREG
    assert "PlantS + Urban_500 + PlantS × Urban_500" in PREREG
    assert "Primary comparison: **E2-S2 versus E2-S1**" in PREREG
    assert "Urban_500" in SCRIPT
    assert "tune an urban buffer scale" in PREREG


def test_validation_holds_out_whole_gardens_and_scales_in_training_only() -> None:
    assert "leave-one-garden-out" in PREREG
    assert "Every reproductive observation from the held-out garden is excluded" in PREREG
    assert "inside each training fold only" in PREREG
    assert '"validation": "leave_one_garden_out"' in SCRIPT
    assert "train[column]" in SCRIPT
    assert "test[column]" in SCRIPT


def test_decision_is_predictive_and_not_equivalence_by_null_p_value() -> None:
    assert "Delta_g = NLL_S1,g - NLL_S2,g" in PREREG
    assert "ecological_partial_state_incomplete" in PREREG
    assert "no_detected_residual_urban_information" in PREREG
    assert "not_identifiable_from_archive" in PREREG
    assert "not** proof of equivalence" in PREREG
    assert "garden-bootstrap 95% interval" in PREREG


def test_raw_third_party_data_are_not_committed() -> None:
    assert "raw_data_committed_here" in WORKFLOW
    assert "False" in WORKFLOW
    assert "actions/upload-artifact@v4" in WORKFLOW
    assert "_external/envidat" not in WORKFLOW.split("path: |", 1)[-1]
    assert "git push" not in WORKFLOW
    assert "git commit" not in WORKFLOW
