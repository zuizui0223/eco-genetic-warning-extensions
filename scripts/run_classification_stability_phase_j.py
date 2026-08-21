from __future__ import annotations

import argparse

from eco_genetic_warning_extensions.classification_stability_phase_j_runner import write_phase_j


def main() -> None:
    parser = argparse.ArgumentParser(description="Run warning-blind R4 classification-stability Phase J")
    parser.add_argument("--upstream-checkout", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    print(write_phase_j(args.upstream_checkout, args.output))


if __name__ == "__main__":
    main()
