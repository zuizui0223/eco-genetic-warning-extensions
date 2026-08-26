import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREREG = (
    ROOT / "manuscript/empirical_eschscholzia_f_full_metadata_repair_preregistration.md"
).read_text(encoding="utf-8")
SCRIPT = (ROOT / "scripts/run_eschscholzia_f_full_metadata_repair.py").read_text(
    encoding="utf-8"
)
WORKFLOW = (ROOT / ".github/workflows/eschscholzia-f-full-metadata-repair.yml").read_text(
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


def test_locked_preparation_failure_is_recorded_without_rescue() -> None:
    assert "except base.NotIdentifiable as exc" in SCRIPT
    assert '"decision": "postlock_descriptive_reconstruction_not_estimable"' in SCRIPT
    assert '"f_model_fitted": False' in SCRIPT
    assert '"model_score_calculated": False' in SCRIPT
    assert '"bootstrap_run": False' in SCRIPT
    assert "additional response repair, row exclusion" in SCRIPT


def test_committed_result_preserves_information_barrier() -> None:
    result = json.loads(
        (ROOT / "artifacts/empirical/eschscholzia_f_full_metadata_repair_result.json").read_text(
            encoding="utf-8"
        )
    )
    assert result["prospective_protocol_commit"] == (
        "bf9f492996cfb57718e03edd4a3620c0756b32c4"
    )
    assert result["decision"] == "postlock_descriptive_reconstruction_not_estimable"
    assert result["correction"]["array_keys"] == ["1||3", "1||4"]
    assert result["correction"]["mismatch_count_after"] == 0
    assert result["information_boundary"] == {
        "bootstrap_run": False,
        "f_model_fitted": False,
        "f_preparation_completed": False,
        "failure_stage": "locked_prepare_f",
        "model_score_calculated": False,
        "other_endpoints_rerun": False,
        "reason": "F primary response has missing/non-finite/negative value",
    }
    assert "F_seed_descriptive_reconstruction" not in result


def test_workflow_uses_post_stop_recorder_but_verifies_protocol_ancestry() -> None:
    assert "fetch-depth: 0" in WORKFLOW
    assert "git merge-base --is-ancestor" in WORKFLOW
    assert "Checkout prospective protocol commit" not in WORKFLOW
    assert "ref: ${{ inputs.protocol_commit }}" not in WORKFLOW
