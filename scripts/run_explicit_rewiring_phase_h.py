from __future__ import annotations

import argparse

from eco_genetic_warning_extensions.explicit_rewiring_phase_h_runner import write_phase_h


def main() -> None:
    parser = argparse.ArgumentParser(description="Run warning-blind explicit rewiring Phase H")
    parser.add_argument("--upstream-checkout", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    print(write_phase_h(args.upstream_checkout, args.output))


if __name__ == "__main__":
    main()
