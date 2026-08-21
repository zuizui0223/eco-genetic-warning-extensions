from __future__ import annotations

import argparse

from eco_genetic_warning_extensions.partner_redundancy_phase_g_runner import write_phase_g


def main() -> None:
    parser = argparse.ArgumentParser(description="Run warning-blind partner-redundancy Phase G")
    parser.add_argument("--upstream-checkout", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    print(write_phase_g(args.upstream_checkout, args.output))


if __name__ == "__main__":
    main()
