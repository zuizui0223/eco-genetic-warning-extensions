from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREREG = (
    ROOT / "manuscript/empirical_eschscholzia_f_full_metadata_repair_preregistration.md"
).read_text(encoding="utf-8")
SCRIPT = (ROOT / "scripts/run_eschscholzia_f_full_metadata_repair.py").read_text(
    encoding="utf-8"
)


def test_third_path_preserves_both_prior_decisions() -> None:
    assert "primary decision `multi_endpoint_not_identifiable`" in PREREG
    assert "`stop_pre_model_unexpected_second_metadata_mismatch`" in PREREG
    assert '"status": "unchanged_not_rescued_or_reclassified"' in SCRIPT
    assert '"status": "unchanged_not_reopened_or_expanded"' in SCRIPT


def test_only_two_exact_literal_repairs_are_permitted() -> None:
    for token in ("1||3", "1||4", "Fallow graound", "Fallow ground"):
        assert token in PREREG
        assert token in SCRIPT
    assert 'TARGET_KEYS = ("1||3", "1||4")' in SCRIPT
    assert "No fuzzy matching" in PREREG
    assert "mismatches_before != EXPECTED_MISMATCHES" in SCRIPT
    assert "if mismatches_after" in SCRIPT


def test_original_f_model_is_reused_without_other_endpoints() -> None:
    assert 'base._run_primary_endpoint(f, "y_F", "continuous")' in SCRIPT
    assert 'base._secondary_extension(f, "y_F", "continuous", "D_capacity")' in SCRIPT
    assert '"bootstrap_replicates": base.N_BOOT' in SCRIPT
    assert '"bootstrap_rng_seed": base.RNG_SEED' in SCRIPT
    assert '"other_endpoints_rerun": False' in SCRIPT


def test_analysis_is_labeled_descriptive_not_confirmatory() -> None:
    assert '"analysis": "postlock_descriptive_full_metadata_repair"' in SCRIPT
    assert "descriptive information recovery" in SCRIPT
    assert "not a confirmatory sensitivity" in PREREG
