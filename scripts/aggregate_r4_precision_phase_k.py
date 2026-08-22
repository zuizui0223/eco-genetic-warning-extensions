from __future__ import annotations

import argparse
import glob
import json
from pathlib import Path

from eco_genetic_warning_extensions.r4_precision_phase_k_runner import load_and_aggregate_phase_k


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-glob", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    paths = sorted(glob.glob(args.input_glob))
    if not paths:
        raise SystemExit("no Phase-K seed artifacts matched")
    result = load_and_aggregate_phase_k(paths)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(output)
    print("PHASE_K_SUMMARY_BEGIN")
    print(json.dumps({
        "prefix_audit_passed": result["prefix_audit_passed"],
        "decision": result["decision"],
        "partner_loss_regime_by_seed_family": result["partner_loss_regime_by_seed_family"],
        "family_condition_summaries": result["family_condition_summaries"],
    }, sort_keys=True))
    print("PHASE_K_SUMMARY_END")


if __name__ == "__main__":
    main()
