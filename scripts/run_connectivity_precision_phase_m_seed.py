from __future__ import annotations

import argparse
import json
from pathlib import Path

from eco_genetic_warning_extensions.connectivity_precision_phase_m_runner import run_phase_m_seed


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--upstream-checkout", required=True)
    parser.add_argument("--master-seed", type=int, required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    payload = run_phase_m_seed(args.upstream_checkout, args.master_seed)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
