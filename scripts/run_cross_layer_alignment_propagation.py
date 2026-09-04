"""Run the preregistered cross-layer alignment propagation audit."""
from __future__ import annotations

import argparse

from eco_genetic_warning_extensions.cross_layer_alignment_propagation import (
    LOCKED_SUMMARY_DEFAULT,
    write_propagation_audit,
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default="artifacts/cross_layer_alignment/propagation_audit.json",
    )
    parser.add_argument(
        "--locked-summary",
        default=str(LOCKED_SUMMARY_DEFAULT),
    )
    args = parser.parse_args()
    destination = write_propagation_audit(
        args.output,
        locked_summary_path=args.locked_summary,
    )
    print(destination)


if __name__ == "__main__":
    main()
