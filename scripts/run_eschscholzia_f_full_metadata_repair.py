"""Run the post-lock descriptive two-key Eschscholzia F reconstruction."""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

ADAPTER_PATH = Path(__file__).with_name(
    "run_eschscholzia_multiprocess_state_test_locked_source.py"
)
spec = importlib.util.spec_from_file_location("esch_full_repair_adapter", ADAPTER_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError("could not load locked Eschscholzia source adapter")
adapter = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = adapter
spec.loader.exec_module(adapter)
base = adapter.base

OBSERVED_VALUE = "Fallow graound"
REPLACEMENT_VALUE = "Fallow ground"
TARGET_KEYS = ("1||3", "1||4")
EXPECTED_MISMATCHES = {
    key: {"f_seed": [OBSERVED_VALUE], "pollinator": REPLACEMENT_VALUE}
    for key in TARGET_KEYS
}


def _metadata_mismatches(f_source, pstate) -> dict[str, dict[str, object]]:
    raw_map = (
        f_source.assign(Habitat=f_source["Habitat"].map(base._clean))
        .groupby("array_key_repair")["Habitat"]
        .agg(lambda values: sorted(set(values)))
    )
    pmap = pstate.set_index("array_key")["habitat"].astype(str)
    mismatches = {}
    for key, values in raw_map.items():
        pollinator_habitat = None if key not in pmap.index else str(pmap.loc[key])
        if values != [pollinator_habitat]:
            mismatches[key] = {"f_seed": values, "pollinator": pollinator_habitat}
    return mismatches


def run(protocol_commit: str) -> dict[str, object]:
    if len(protocol_commit) != 40 or any(ch not in "0123456789abcdef" for ch in protocol_commit):
        raise ValueError("protocol_commit must be a lowercase 40-character Git SHA")
    frames = {}
    source_info = {}
    for role in ("pollinator", "f_seed"):
        source = base.SOURCES[role]
        package, raw, url = adapter._download_source_member_locked(source)
        frames[role] = base._read_csv(raw)
        source_info[role] = {
            "doi": source["doi"],
            "url": url,
            "transport_package_sha256_record_only": adapter._sha256(package),
            "csv_member": source["member"],
            "csv_sha256": adapter._sha256(raw),
        }

    pstate = base._prepare_pollinator(frames["pollinator"])
    f_source = frames["f_seed"].copy()
    f_source["array_key_repair"] = [
        base._array_key(block, array)
        for block, array in zip(
            f_source["Block"], f_source["Experimental_array"], strict=True
        )
    ]
    mismatches_before = _metadata_mismatches(f_source, pstate)
    if mismatches_before != EXPECTED_MISMATCHES:
        raise base.NotIdentifiable(
            f"full-repair precondition mismatch: observed={mismatches_before!r}"
        )

    corrected_rows = {}
    for key in TARGET_KEYS:
        target = f_source["array_key_repair"] == key
        values = sorted({base._clean(value) for value in f_source.loc[target, "Habitat"]})
        if not target.any() or values != [OBSERVED_VALUE]:
            raise base.NotIdentifiable(f"repair precondition failed: {key} values={values!r}")
        corrected_rows[key] = int(target.sum())
        f_source.loc[target, "Habitat"] = REPLACEMENT_VALUE

    mismatches_after = _metadata_mismatches(f_source, pstate)
    if mismatches_after:
        raise base.NotIdentifiable(
            f"metadata mismatch remains after exact two-key correction: {mismatches_after!r}"
        )
    f_source = f_source.drop(columns=["array_key_repair"])
    try:
        f = base._prepare_f(f_source, pstate)
    except base.NotIdentifiable as exc:
        return {
            "analysis": "postlock_descriptive_full_metadata_repair",
            "decision": "postlock_descriptive_reconstruction_not_estimable",
            "prospective_protocol_commit": protocol_commit,
            "preregistration": (
                "manuscript/empirical_eschscholzia_f_full_metadata_repair_preregistration.md"
            ),
            "primary_lock": {
                "decision": "multi_endpoint_not_identifiable",
                "locked_result": (
                    "artifacts/empirical/eschscholzia_multiprocess_state_locked_result.json"
                ),
                "status": "unchanged_not_rescued_or_reclassified",
            },
            "prior_one_key_sensitivity": {
                "decision": "stop_pre_model_unexpected_second_metadata_mismatch",
                "locked_result": "artifacts/empirical/eschscholzia_f_typo_sensitivity_stop.json",
                "status": "unchanged_not_reopened_or_expanded",
            },
            "source_lock": source_info,
            "correction": {
                "source_role": "f_seed",
                "array_keys": list(TARGET_KEYS),
                "field": "Habitat",
                "observed": OBSERVED_VALUE,
                "replacement": REPLACEMENT_VALUE,
                "corrected_rows_by_key": corrected_rows,
                "mismatches_before": mismatches_before,
                "mismatch_count_after": 0,
            },
            "information_boundary": {
                "f_preparation_completed": False,
                "f_model_fitted": False,
                "model_score_calculated": False,
                "bootstrap_run": False,
                "other_endpoints_rerun": False,
                "failure_stage": "locked_prepare_f",
                "reason": str(exc),
            },
            "claim_boundary": (
                "The exact two-key metadata repair removed the cross-source Habitat mismatch, "
                "but the unchanged F preparation gate found an invalid primary response. No "
                "additional response repair, row exclusion, model, score or bootstrap is opened."
            ),
        }
    primary = base._endpoint_to_dict(base._run_primary_endpoint(f, "y_F", "continuous"))
    capacity = base._secondary_extension(f, "y_F", "continuous", "D_capacity")
    capacity["semantic_decision"] = (
        "capacity_adds_function_information"
        if capacity.get("decision") == "supported_positive_gain"
        else "no_detected_capacity_gain"
        if capacity.get("decision") == "no_detected_positive_gain"
        else "capacity_not_identifiable"
    )
    primary["capacity_extension"] = capacity

    return {
        "analysis": "postlock_descriptive_full_metadata_repair",
        "prospective_protocol_commit": protocol_commit,
        "preregistration": (
            "manuscript/empirical_eschscholzia_f_full_metadata_repair_preregistration.md"
        ),
        "primary_lock": {
            "decision": "multi_endpoint_not_identifiable",
            "locked_result": (
                "artifacts/empirical/eschscholzia_multiprocess_state_locked_result.json"
            ),
            "status": "unchanged_not_rescued_or_reclassified",
        },
        "prior_one_key_sensitivity": {
            "decision": "stop_pre_model_unexpected_second_metadata_mismatch",
            "locked_result": "artifacts/empirical/eschscholzia_f_typo_sensitivity_stop.json",
            "status": "unchanged_not_reopened_or_expanded",
        },
        "source_lock": source_info,
        "correction": {
            "source_role": "f_seed",
            "array_keys": list(TARGET_KEYS),
            "field": "Habitat",
            "observed": OBSERVED_VALUE,
            "replacement": REPLACEMENT_VALUE,
            "corrected_rows_by_key": corrected_rows,
            "mismatches_before": mismatches_before,
            "mismatch_count_after": 0,
        },
        "frozen_analysis": {
            "endpoint": "F_seed",
            "held_out_unit": "Experimental array",
            "model_sequence": ["S0", "S1", "S2"],
            "regularization": "Ridge(alpha=1.0)",
            "bootstrap_replicates": base.N_BOOT,
            "bootstrap_rng_seed": base.RNG_SEED,
            "other_endpoints_rerun": False,
        },
        "F_seed_descriptive_reconstruction": primary,
        "claim_boundary": (
            "Post-lock descriptive information recovery only. This result cannot replace, rescue, "
            "weaken or relabel either locked prior decision and cannot establish multi-endpoint "
            "state adequacy."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--protocol-commit", required=True)
    parser.add_argument(
        "--output",
        default="artifacts/empirical/eschscholzia_f_full_metadata_repair_result.json",
    )
    args = parser.parse_args()
    result = run(args.protocol_commit)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if result.get("decision") == "postlock_descriptive_reconstruction_not_estimable":
        summary = {
            "analysis": result["analysis"],
            "decision": result["decision"],
            "information_boundary": result["information_boundary"],
        }
    else:
        summary = {
            "analysis": result["analysis"],
            "F_decision": result["F_seed_descriptive_reconstruction"]["decision"],
            "F_process": result["F_seed_descriptive_reconstruction"]["comparisons"][
                "S0_to_S1"
            ],
            "F_habitat": result["F_seed_descriptive_reconstruction"]["comparisons"][
                "S1_to_S2"
            ],
        }
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
