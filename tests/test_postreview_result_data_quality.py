import csv
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTINUOUS_JSON = ROOT / "artifacts/prepublication_review/continuous_warning_landmark_auc.json"
CONTINUOUS_CSV = ROOT / "manuscript/tables/continuous_warning_landmark_auc.csv"
ESCH_JSON = ROOT / "artifacts/empirical/eschscholzia_f_full_metadata_repair_result.json"


def test_continuous_table_has_complete_unique_fixed_grain() -> None:
    with CONTINUOUS_CSV.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    keys = {
        (row["ensemble"], row["diversity_id"], int(row["landmark"])) for row in rows
    }
    expected = {
        (ensemble, diversity, landmark)
        for ensemble in ("inherited_202611", "fresh_202911")
        for diversity in ("H_alpha", "H_gamma")
        for landmark in (30, 60, 90)
    }
    assert len(rows) == len(keys) == 12
    assert keys == expected


def test_continuous_denominators_reconcile_at_trajectory_grain() -> None:
    expected = {
        "inherited_202611": {"eligible": 83, "events": 35, "controls": 48},
        "fresh_202911": {"eligible": 82, "events": 33, "controls": 49},
    }
    with CONTINUOUS_CSV.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    for row in rows:
        counts = expected[row["ensemble"]]
        risk_set = int(row["risk_set"])
        future_cases = int(row["future_cases"])
        controls = int(row["dynamic_controls"])
        prior_losses = int(row["excluded_losses_at_or_before_landmark"])
        assert risk_set + prior_losses == counts["eligible"]
        assert future_cases + prior_losses == counts["events"]
        assert controls == counts["controls"]
        assert risk_set == future_cases + controls


def test_continuous_auc_and_uncertainty_are_valid_and_json_aligned() -> None:
    result = json.loads(CONTINUOUS_JSON.read_text(encoding="utf-8"))
    json_cells = {
        (ensemble, cell["diversity_id"], int(cell["landmark"])): cell
        for ensemble, item in result["ensembles"].items()
        for cell in item["cells"]
    }
    seeds = set()
    with CONTINUOUS_CSV.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            key = (row["ensemble"], row["diversity_id"], int(row["landmark"]))
            cell = json_cells[key]
            auc = float(row["auc"])
            lower = float(row["auc_ci95_lower"])
            upper = float(row["auc_ci95_upper"])
            assert all(math.isfinite(value) for value in (auc, lower, upper))
            assert 0 <= lower <= auc <= upper <= 1
            assert auc == cell["auc"]
            assert [lower, upper] == cell["auc_ci95_percentile"]
            assert int(row["bootstrap_replicates"]) == 10_000
            seeds.add(int(row["bootstrap_seed"]))
    assert len(seeds) == 12
    assert result["source_manifest"]["inherited_202611"][
        "raw_member_sha256_verified"
    ] == "c1552616a94b23ffc1340580231d7d1b16bc7d84c951c3d2606cc437fb15673e"
    assert result["source_manifest"]["fresh_202911"][
        "raw_member_sha256_verified"
    ] == "1674c817b760f5a20320ffdf775181f3c3134d60cc977feffe76c9296c253fb9"


def test_eschscholzia_stop_has_complete_source_and_information_barriers() -> None:
    result = json.loads(ESCH_JSON.read_text(encoding="utf-8"))
    assert result["correction"]["corrected_rows_by_key"] == {"1||3": 3, "1||4": 3}
    assert result["correction"]["mismatch_count_after"] == 0
    assert result["source_lock"]["pollinator"]["csv_sha256"] == (
        "db063840850fb4f358db7e99271feb9b9a92f6701b889d1b59a1348ffada89ef"
    )
    assert result["source_lock"]["f_seed"]["csv_sha256"] == (
        "83ab56cc8b3e4b2ae2b7141e55683b1cff2734006d4fa4f6735605d3a2be379f"
    )
    boundary = result["information_boundary"]
    for field in (
        "f_preparation_completed",
        "f_model_fitted",
        "model_score_calculated",
        "bootstrap_run",
        "other_endpoints_rerun",
    ):
        assert boundary[field] is False
    assert "F_seed_descriptive_reconstruction" not in result
