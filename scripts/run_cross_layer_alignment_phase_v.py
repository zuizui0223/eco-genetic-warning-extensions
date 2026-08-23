from __future__ import annotations

import argparse

from eco_genetic_warning_extensions.cross_layer_alignment_phase_v_runner import write_phase_v


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="artifacts/cross_layer_alignment/phase_v_summary.json")
    args = parser.parse_args()
    path = write_phase_v(args.output)
    print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
