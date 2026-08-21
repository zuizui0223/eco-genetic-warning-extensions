from __future__ import annotations

import argparse

from eco_genetic_warning_extensions.pollen_movement_phase_i_runner import write_phase_i


def main() -> None:
    parser = argparse.ArgumentParser(description="Run warning-blind pollen-movement Phase I")
    parser.add_argument("--upstream-checkout", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    print(write_phase_i(args.upstream_checkout, args.output))


if __name__ == "__main__":
    main()
