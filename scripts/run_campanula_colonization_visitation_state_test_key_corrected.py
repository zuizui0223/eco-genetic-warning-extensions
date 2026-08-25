from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

BASE_PATH = Path(__file__).with_name("run_campanula_colonization_visitation_state_test.py")
spec = importlib.util.spec_from_file_location("campanula_visitation_base", BASE_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError("could not load preregistered Campanula analysis module")
base = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = base
spec.loader.exec_module(base)

_original_prepare = base._prepare


def _prepare_response_bearing_populations(source_lock, seed, poll):
    """Permit predictor-only populations without changing scientific logic.

    The first locked run stopped before outcome construction because the base
    implementation required equality of the entire seed and pollinator population
    sets. The preregistration only requires every response-bearing seed population
    to have its unique declared pollinator state. Extra pollinator-only populations
    cannot contribute to either PL_abs or F_control and are therefore retained only
    as source-provenance diagnostics.
    """
    seed_ids = seed["experimental.population"].astype("string").str.strip()
    poll_ids = poll["experimental.population"].astype("string").str.strip()
    seed_set = set(seed_ids.dropna().tolist())
    poll_set = set(poll_ids.dropna().tolist())
    extras = sorted(poll_set - seed_set)

    # Never drop a response-bearing population. If a seed population lacks a
    # pollinator row, the original _prepare gate still returns not-identifiable.
    poll_subset = poll.loc[poll_ids.isin(seed_set)].copy()
    result = _original_prepare(source_lock, seed, poll_subset)
    if isinstance(result, tuple):
        paired, prepared_poll, diagnostics = result
        diagnostics = dict(diagnostics)
        diagnostics["pollinator_only_populations_excluded_from_response_fitting"] = extras
        diagnostics["n_pollinator_only_populations"] = len(extras)
        return paired, prepared_poll, diagnostics
    result = dict(result)
    details = dict(result.get("details", {}))
    details["pollinator_only_populations_excluded_from_response_fitting"] = extras
    result["details"] = details
    return result


base._prepare = _prepare_response_bearing_populations


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="artifacts/empirical/campanula_colonization_visitation_result.json")
    args = parser.parse_args()
    result = base.run()
    result["population_key_gate_correction"] = {
        "policy": "all seed-response populations require pollinator state; predictor-only populations retained as provenance only",
        "correction_note": "manuscript/empirical_campanula_population_key_gate_correction.md",
        "first_run": 32819915952,
        "first_run_outcome_model_fitted": False,
    }
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "decision": result.get("decision"),
                "reason": result.get("reason"),
                "PL_process": result.get("PL_abs", {}).get("comparisons", {}).get("S0_to_S1"),
                "PL_size": result.get("PL_abs", {}).get("comparisons", {}).get("S1_to_S2"),
                "PL_autonomy": result.get("PL_abs", {}).get("comparisons", {}).get("S2_to_S3"),
                "F_process": result.get("F_control", {}).get("comparisons", {}).get("S0_to_S1"),
                "key_gate_correction": result.get("population_key_gate_correction"),
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
