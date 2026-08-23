from __future__ import annotations

import argparse
import glob
import json
from pathlib import Path

from eco_genetic_warning_extensions.process_resolved_pollen_phase_s_runner import load_and_aggregate_phase_s


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-glob", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    paths = sorted(glob.glob(args.input_glob))
    if not paths:
        raise SystemExit("no Phase-S seed files matched")
    result = load_and_aggregate_phase_s(paths)
    target = Path(args.output)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("PHASE_S_SUMMARY_BEGIN")
    print(json.dumps({
        "opening": result["opening"],
        "decision": result["decision"],
        "condition_summaries": result["condition_summaries"],
        "paired_pollen_vs_no_connectivity": result["paired_pollen_vs_no_connectivity"],
        "paired_pollen_vs_allele_only_m010": result["paired_pollen_vs_allele_only_m010"],
        "interpretation": result["interpretation"],
    }, sort_keys=True))
    print("PHASE_S_SUMMARY_END")


if __name__ == "__main__":
    main()
