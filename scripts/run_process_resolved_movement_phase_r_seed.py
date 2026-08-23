from __future__ import annotations

import argparse
import json
from pathlib import Path

from eco_genetic_warning_extensions.process_resolved_movement_phase_r_runner import run_phase_r_seed


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--upstream-checkout", required=True)
    parser.add_argument("--master-seed", type=int, required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    payload = run_phase_r_seed(args.upstream_checkout, args.master_seed)
    target = Path(args.output)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("PHASE_R_SEED_SUMMARY_BEGIN")
    print(json.dumps({
        "master_seed": payload["master_seed"],
        "prefix_audit_passed": payload["prefix_audit_passed"],
        "process_baseline_pairing_passed": payload["process_baseline_pairing_passed"],
        "condition_summaries": payload["condition_summaries"],
    }, sort_keys=True))
    print("PHASE_R_SEED_SUMMARY_END")


if __name__ == "__main__":
    main()
