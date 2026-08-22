from __future__ import annotations

import argparse
import json
from pathlib import Path

from eco_genetic_warning_extensions.r4_gate_validity_phase_j import phase_j_audit


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(phase_j_audit(), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
