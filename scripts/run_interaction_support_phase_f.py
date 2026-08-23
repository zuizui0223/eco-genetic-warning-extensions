from __future__ import annotations

import argparse

from eco_genetic_warning_extensions.interaction_support_phase_f_runner import write_phase_f


def main() -> None:
    parser = argparse.ArgumentParser(description="Run warning-blind interaction-support Phase F")
    parser.add_argument("--upstream-checkout", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    print(write_phase_f(args.upstream_checkout, args.output))


if __name__ == "__main__":
    main()
