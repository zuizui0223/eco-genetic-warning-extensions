import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUMMARY = json.loads((ROOT / "artifacts" / "empirical" / "oenothera_mating_state_locked_summary.json").read_text(encoding="utf-8"))
DOC = (ROOT / "manuscript" / "empirical_oenothera_mating_state_result.md").read_text(encoding="utf-8")


def test_locked_oenothera_decision_and_source() -> None:
    assert SUMMARY["decision"] == "residual_isolation_detected"
    assert SUMMARY["source_lock"]["dataset_doi"] == "10.5061/dryad.p24q3"
    assert SUMMARY["source_lock"]["observed_md5"] == "600f6f370ffa8ad205d0ccb6bc92ab65"
    assert SUMMARY["source_lock"]["observed_md5"] == SUMMARY["source_lock"]["published_md5"]


def test_locked_oenothera_schema_and_validation_units() -> None:
    assert SUMMARY["schema"]["n_seed_family_rows"] == 60
    assert SUMMARY["schema"]["n_maternal_plants"] == 23
    assert SUMMARY["schema"]["repeated_plant_rows"] == 37
    assert SUMMARY["schema"]["treatment_profile_counts"] == {
        "c/de": 4,
        "c/de/ne": 14,
        "c/ne": 3,
        "de/ne": 2,
    }
    assert "maternal plant" in SUMMARY["schema"]["validation_unit"]
    assert "treatment-profile" in SUMMARY["schema"]["permutation_unit"]


def test_isolation_improves_held_out_prediction_and_is_positive() -> None:
    m0 = SUMMARY["models"]["M0"]
    m1 = SUMMARY["models"]["M1"]
    inc = SUMMARY["incremental_isolation"]
    assert m1["loo_mse"] < m0["loo_mse"]
    assert m1["loo_mae"] < m0["loo_mae"]
    assert m1["isolation_beta"] > 0
    assert inc["loo_mse_percent_change"] < -20
    assert inc["treatment_profile_stratified_plant_permutation_p"] < 0.05
    assert inc["permutations"] == 10000
    assert inc["rng_seed"] == 20260824


def test_result_claim_ceiling_remains_mating_state_only() -> None:
    assert "contemporary mating-state (`G_mating/C_pollen`) result" in DOC
    assert "not a direct ecological-function or functional-loss result" in DOC
    assert "20.93% improvement" in DOC
    assert "0.00129987" in DOC
    assert "universal fragmentation threshold" in DOC
    assert "No third-party raw data are committed" in DOC


def test_workflow_provenance_is_locked() -> None:
    p = SUMMARY["workflow_provenance"]
    assert p["run_id"] == 32721630217
    assert p["job_id"] == 97414084955
    assert p["head_sha"] == "d9688dae3ec609376d36ee4a7df9b193137938fb"
    assert p["artifact_id"] == 9519204842
    assert p["artifact_digest"] == "sha256:97a2b2359ec44b2fbd94ecd54975f206f240be3c994ef2a50c636678ee882eb1"
