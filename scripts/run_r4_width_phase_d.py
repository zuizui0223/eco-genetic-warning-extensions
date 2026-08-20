from __future__ import annotations

import argparse

from eco_genetic_warning_extensions.r4_width_phase_d_runner import write_phase_d_cell


def main() -> None:
    parser = argparse.ArgumentParser(description="Run one high-rep warning-blind Phase-D R4-width cell.")
    parser.add_argument("--upstream-checkout", required=True)
    parser.add_argument("--cell-index", required=True, type=int)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    print(write_phase_d_cell(args.upstream_checkout, args.cell_index, args.output))


if __name__ == "__main__":
    main()
