from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREREG = (
    ROOT / "manuscript/empirical_eschscholzia_f_typo_sensitivity_preregistration.md"
).read_text(encoding="utf-8")
SCRIPT = (ROOT / "scripts/run_eschscholzia_f_typo_sensitivity.py").read_text(
    encoding="utf-8"
)
WORKFLOW = (ROOT / ".github/workflows/eschscholzia-f-typo-sensitivity.yml").read_text(
    encoding="utf-8"
)


def test_sensitivity_cannot_rescue_primary() -> None:
    assert "primary result remains permanently `multi_endpoint_not_identifiable`" in PREREG
    assert '"decision": "multi_endpoint_not_identifiable"' in SCRIPT
    assert '"status": "unchanged_not_rescued_or_reclassified"' in SCRIPT
    assert '"other_endpoints_rerun": False' in SCRIPT


def test_only_one_literal_correction_is_available() -> None:
    for token in ("1||3", "Fallow graound", "Fallow ground"):
        assert token in PREREG
        assert token in SCRIPT
    assert "No fuzzy matching" in PREREG
    assert "unexpected metadata mismatch set" in SCRIPT


def test_original_model_and_bootstrap_are_reused() -> None:
    assert 'base._run_primary_endpoint(f, "y_F", "continuous")' in SCRIPT
    assert 'base._secondary_extension(f, "y_F", "continuous", "D_capacity")' in SCRIPT
    assert '"bootstrap_replicates": base.N_BOOT' in SCRIPT
    assert '"bootstrap_rng_seed": base.RNG_SEED' in SCRIPT


def test_workflow_is_manual_and_uploads_only_secondary_result() -> None:
    assert "workflow_dispatch:" in WORKFLOW
    assert "pull_request:" not in WORKFLOW
    assert "Upload secondary result only" in WORKFLOW
