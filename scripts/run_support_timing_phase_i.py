from __future__ import annotations

import argparse
import json
from pathlib import Path

from eco_genetic_warning_extensions.support_timing_phase_i_runner import run_phase_i


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--upstream-checkout", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    artifact = run_phase_i(args.upstream_checkout)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(artifact, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
