from __future__ import annotations

import argparse
import json
from pathlib import Path

from eco_genetic_warning_extensions.protocol003_calibration import run_protocol003_calibration_cell


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("upstream_checkout")
    parser.add_argument("cell_index", type=int)
    parser.add_argument("output")
    args = parser.parse_args()
    payload = run_protocol003_calibration_cell(args.upstream_checkout, args.cell_index)
    target = Path(args.output)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(target)


if __name__ == "__main__":
    main()
