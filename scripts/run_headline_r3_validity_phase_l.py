from __future__ import annotations

import argparse
import json
from pathlib import Path

from eco_genetic_warning_extensions.headline_r3_validity_phase_l import phase_l_audit


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(phase_l_audit(), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
