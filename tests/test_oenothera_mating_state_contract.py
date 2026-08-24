from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = (ROOT / "manuscript" / "empirical_oenothera_mating_state_preregistration.md").read_text(encoding="utf-8")
SCRIPT = (ROOT / "scripts" / "run_oenothera_mating_state_residual_isolation.py").read_text(encoding="utf-8")


def test_source_and_primary_variables_are_locked() -> None:
    assert "10.5061/dryad.p24q3" in DOC
    assert "4942351" in DOC
    assert "600f6f370ffa8ad205d0ccb6bc92ab65" in DOC
    for token in ("plantID", "treatment", "isolation20", "correlatedPaternity"):
        assert token in DOC
        assert token in SCRIPT


def test_model_sequence_is_incremental_isolation_after_pollinator_state() -> None:
    assert "correlatedPaternity ~ treatment" in DOC
    assert "correlatedPaternity ~ treatment + z(isolation20)" in DOC
    assert "No treatment × isolation interaction is opened for the primary test" in DOC
    assert "leave-one-maternal-plant-out" in DOC
    assert "all rows sharing one `plantID` are held out together" in DOC
    assert "rows are not averaged or removed" in DOC


def test_schema_correction_precedes_outcome_analysis() -> None:
    assert "before fitting M0/M1, permutation testing or producing an outcome summary" in DOC
    assert "first detected duplicate: `5854`" in DOC
    assert "repeated plantID disagrees on isolation20" in SCRIPT
    assert "treatment` is allowed to differ" in DOC
    assert "validation_unit" in SCRIPT


def test_permutation_and_decision_rules_are_fixed() -> None:
    assert "10,000-permutation" in DOC
    assert "20260824" in DOC
    assert "treatment profile" in DOC
    assert "identical treatment profiles" in DOC
    assert "treatment_profile_stratified_plant_permutation_p" in SCRIPT
    for decision in (
        "residual_isolation_detected",
        "predictive_residual_isolation_only",
        "model_residual_isolation_only",
        "no_detected_residual_isolation",
        "not_identifiable_from_archive",
    ):
        assert decision in DOC
    assert "N_PERMUTATIONS = 10_000" in SCRIPT
    assert "RNG_SEED = 20260824" in SCRIPT


def test_claim_is_mating_state_not_direct_function() -> None:
    assert "not** realised ecological function `F`" in DOC
    assert "does **not** establish a general fragmentation threshold" in DOC
    assert "G_mating/C_pollen" in SCRIPT
