from __future__ import annotations

import argparse
import glob
import json
from pathlib import Path

from eco_genetic_warning_extensions.connectivity_precision_phase_m_runner import load_and_aggregate_phase_m


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-glob", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    paths = sorted(glob.glob(args.input_glob))
    if not paths:
        raise SystemExit("no Phase-M seed files matched")
    result = load_and_aggregate_phase_m(paths)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("PHASE_M_SUMMARY_BEGIN")
    print(json.dumps({
        "prefix_audit_passed": result["prefix_audit_passed"],
        "decision": result["decision"],
        "regime_by_migration_rate": result["regime_by_migration_rate"],
        "migration_condition_summaries": result["migration_condition_summaries"],
        "paired_loss_status_vs_isolation": result["paired_loss_status_vs_isolation"],
    }, sort_keys=True))
    print("PHASE_M_SUMMARY_END")


if __name__ == "__main__":
    main()
