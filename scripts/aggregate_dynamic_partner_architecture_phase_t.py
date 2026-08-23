from __future__ import annotations

import argparse
import glob
import json
from pathlib import Path

from eco_genetic_warning_extensions.dynamic_partner_architecture_phase_t_runner import load_and_aggregate_phase_t


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-glob", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    paths = sorted(glob.glob(args.input_glob))
    if not paths:
        raise SystemExit("no Phase-T seed files matched")
    result = load_and_aggregate_phase_t(paths)
    target = Path(args.output)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("PHASE_T_SUMMARY_BEGIN")
    print(json.dumps({
        "opening": result["opening"],
        "decision": result["decision"],
        "condition_summaries": result["condition_summaries"],
        "paired_even_vs_constant": result["paired_even_vs_constant"],
        "paired_dominant_vs_constant": result["paired_dominant_vs_constant"],
        "paired_dominant_vs_even": result["paired_dominant_vs_even"],
        "effect_flags": result["effect_flags"],
    }, sort_keys=True))
    print("PHASE_T_SUMMARY_END")


if __name__ == "__main__":
    main()
