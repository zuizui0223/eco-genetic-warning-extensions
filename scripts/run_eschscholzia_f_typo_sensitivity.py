"""Prospectively fixed F-only sensitivity for one literal source typo.

The locked primary non-identifiability is immutable. This script changes one
declared metadata value, reruns only the original F model, and cannot construct
a replacement F+G primary decision.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

ADAPTER_PATH = Path(__file__).with_name(
    "run_eschscholzia_multiprocess_state_test_locked_source.py"
)
spec = importlib.util.spec_from_file_location("esch_locked_adapter", ADAPTER_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError("could not load locked Eschscholzia source adapter")
adapter = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = adapter
spec.loader.exec_module(adapter)
base = adapter.base

TARGET_KEY = "1||3"
OBSERVED_VALUE = "Fallow graound"
REPLACEMENT_VALUE = "Fallow ground"


def run() -> dict[str, object]:
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
    pollinator_row = pstate[pstate["array_key"] == TARGET_KEY]
    if len(pollinator_row) != 1:
        raise base.NotIdentifiable(f"expected one pollinator state for {TARGET_KEY}")
    pollinator_value = str(pollinator_row.iloc[0]["habitat"])
    if pollinator_value != REPLACEMENT_VALUE:
        raise base.NotIdentifiable(
            f"pollinator precondition failed: {TARGET_KEY}={pollinator_value!r}"
        )

    f_source = frames["f_seed"].copy()
    f_source["array_key_sensitivity"] = [
        base._array_key(block, array)
        for block, array in zip(
            f_source["Block"], f_source["Experimental_array"], strict=True
        )
    ]
    target = f_source["array_key_sensitivity"] == TARGET_KEY
    if not target.any():
        raise base.NotIdentifiable(f"F source lacks declared target {TARGET_KEY}")
    target_values = sorted({base._clean(value) for value in f_source.loc[target, "Habitat"]})
    if target_values != [OBSERVED_VALUE]:
        raise base.NotIdentifiable(
            f"F correction precondition failed: {TARGET_KEY} values={target_values!r}"
        )

    # Verify that the declared typo is the one and only cross-source metadata mismatch.
    raw_map = (
        f_source.assign(Habitat=f_source["Habitat"].map(base._clean))
        .groupby("array_key_sensitivity")["Habitat"]
        .agg(lambda values: sorted(set(values)))
    )
    pmap = pstate.set_index("array_key")["habitat"].astype(str)
    mismatches = {}
    for key, values in raw_map.items():
        pollinator_habitat = None if key not in pmap.index else str(pmap.loc[key])
        if values != [pollinator_habitat]:
            mismatches[key] = {
                "f_seed": values,
                "pollinator": pollinator_habitat,
            }
    expected_mismatch = {
        TARGET_KEY: {"f_seed": [OBSERVED_VALUE], "pollinator": REPLACEMENT_VALUE}
    }
    if mismatches != expected_mismatch:
        raise base.NotIdentifiable(f"unexpected metadata mismatch set: {mismatches!r}")

    corrected_rows = int(target.sum())
    f_source.loc[target, "Habitat"] = REPLACEMENT_VALUE
    f_source = f_source.drop(columns=["array_key_sensitivity"])
    f = base._prepare_f(f_source, pstate)
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
        "analysis": "postreview_secondary_typo_sensitivity",
        "primary_lock": {
            "decision": "multi_endpoint_not_identifiable",
            "locked_result": "artifacts/empirical/eschscholzia_multiprocess_state_locked_result.json",
            "status": "unchanged_not_rescued_or_reclassified",
        },
        "preregistration": "manuscript/empirical_eschscholzia_f_typo_sensitivity_preregistration.md",
        "source_lock": source_info,
        "correction": {
            "source_role": "f_seed",
            "array_key": TARGET_KEY,
            "field": "Habitat",
            "observed": OBSERVED_VALUE,
            "replacement": REPLACEMENT_VALUE,
            "corrected_rows": corrected_rows,
            "mismatch_count_before": 1,
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
        "F_seed_secondary_sensitivity": primary,
        "claim_boundary": (
            "This F-only result is a post-review secondary sensitivity. It cannot replace, "
            "rescue, or relabel the locked multi-endpoint primary decision."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default="artifacts/empirical/eschscholzia_f_typo_sensitivity_result.json",
    )
    args = parser.parse_args()
    result = run()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "analysis": result["analysis"],
                "primary_lock": result["primary_lock"],
                "correction": result["correction"],
                "F_decision": result["F_seed_secondary_sensitivity"]["decision"],
                "F_process": result["F_seed_secondary_sensitivity"]["comparisons"]["S0_to_S1"],
                "F_habitat": result["F_seed_secondary_sensitivity"]["comparisons"]["S1_to_S2"],
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
