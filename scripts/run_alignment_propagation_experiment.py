from __future__ import annotations

import argparse
import json
from pathlib import Path

from eco_genetic_warning_extensions.alignment_propagation_experiment import write_experiment


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--summary", default="artifacts/alignment_propagation/alignment_propagation_summary.json")
    parser.add_argument("--attempts", default="artifacts/alignment_propagation/alignment_propagation_attempts.json")
    args = parser.parse_args()
    summary_path, attempts_path = write_experiment(args.summary, args.attempts)
    payload = json.loads(Path(summary_path).read_text(encoding="utf-8"))
    print(json.dumps(payload, indent=2, sort_keys=True))
    print(f"summary={summary_path}")
    print(f"attempts={attempts_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
