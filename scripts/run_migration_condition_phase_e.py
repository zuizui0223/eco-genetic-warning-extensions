from __future__ import annotations

import argparse

from eco_genetic_warning_extensions.migration_condition_phase_e_runner import write_phase_e


def main() -> None:
    parser = argparse.ArgumentParser(description="Run warning-blind paired migration-condition Phase E")
    parser.add_argument("--upstream-checkout", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    print(write_phase_e(args.upstream_checkout, args.output))


if __name__ == "__main__":
    main()
