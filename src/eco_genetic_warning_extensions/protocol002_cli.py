"""Command-line entry points for Protocol 002.

The CLI is intentionally limited to pre-simulation certification and skeleton
artifact writing. It must not run ecological simulations, calibration, or warning
validation.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Sequence

from .protocol002_source_example import (
    DEFAULT_SOURCE_EXAMPLE_PATH,
    example_source_skeleton_artifact,
    write_source_skeleton_example,
)
from .protocol002_source_grid import (
    DEFAULT_SOURCE_GRID_LOCK_PATH,
    DEFAULT_SOURCE_GRID_PATH,
    planned_source_grid_artifact,
    planned_source_grid_lock_artifact,
    write_planned_source_grid,
    write_planned_source_grid_lock,
)
from .protocol002_stage0 import stage0_certificate, write_stage0_certificate

DEFAULT_STAGE0_PATH = Path("artifacts/protocol002/stage0_operator_certificate.json")


def _add_output_arguments(parser: argparse.ArgumentParser, *, default: Path, stdout_help: str) -> None:
    parser.add_argument(
        "--output",
        type=Path,
        default=default,
        help=f"output JSON path; default: {default}",
    )
    parser.add_argument(
        "--stdout",
        action="store_true",
        help=stdout_help,
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="overwrite an existing output file",
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="protocol002",
        description="Protocol 002 utility commands for mutation-direction phase-diagram work.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    write_stage0 = subparsers.add_parser(
        "write-stage0",
        help="write the deterministic Stage 0 operator certificate JSON",
    )
    _add_output_arguments(
        write_stage0,
        default=DEFAULT_STAGE0_PATH,
        stdout_help="print the certificate JSON to stdout instead of writing a file",
    )

    write_source_example = subparsers.add_parser(
        "write-source-skeleton-example",
        help="write the deterministic no-simulation source-skeleton example manifest",
    )
    _add_output_arguments(
        write_source_example,
        default=DEFAULT_SOURCE_EXAMPLE_PATH,
        stdout_help="print the source-skeleton example manifest JSON to stdout instead of writing a file",
    )

    write_source_grid = subparsers.add_parser(
        "write-source-grid-plan",
        help="write the deterministic no-simulation planned source-grid manifest",
    )
    _add_output_arguments(
        write_source_grid,
        default=DEFAULT_SOURCE_GRID_PATH,
        stdout_help="print the planned source-grid manifest JSON to stdout instead of writing a file",
    )

    write_source_grid_lock = subparsers.add_parser(
        "write-source-grid-lock",
        help="write the deterministic lightweight lock for the planned source-grid manifest",
    )
    _add_output_arguments(
        write_source_grid_lock,
        default=DEFAULT_SOURCE_GRID_LOCK_PATH,
        stdout_help="print the planned source-grid lock JSON to stdout instead of writing a file",
    )
    return parser


def _refuse_overwrite_without_force(output: Path, *, force: bool) -> None:
    if output.exists() and not force:
        raise SystemExit(f"refusing to overwrite existing file without --force: {output}")


def _write_stage0(args: argparse.Namespace) -> int:
    if args.stdout:
        sys.stdout.write(json.dumps(stage0_certificate(), indent=2, sort_keys=True) + "\n")
        return 0

    output: Path = args.output
    _refuse_overwrite_without_force(output, force=args.force)
    write_stage0_certificate(output)
    print(f"wrote Protocol 002 Stage 0 certificate: {output}")
    return 0


def _write_source_skeleton_example(args: argparse.Namespace) -> int:
    if args.stdout:
        sys.stdout.write(json.dumps(example_source_skeleton_artifact(), indent=2, sort_keys=True) + "\n")
        return 0

    output: Path = args.output
    _refuse_overwrite_without_force(output, force=args.force)
    write_source_skeleton_example(output)
    print(f"wrote Protocol 002 source-skeleton example manifest: {output}")
    return 0


def _write_source_grid_plan(args: argparse.Namespace) -> int:
    if args.stdout:
        sys.stdout.write(json.dumps(planned_source_grid_artifact(), indent=2, sort_keys=True) + "\n")
        return 0

    output: Path = args.output
    _refuse_overwrite_without_force(output, force=args.force)
    write_planned_source_grid(output)
    print(f"wrote Protocol 002 planned source-grid manifest: {output}")
    return 0


def _write_source_grid_lock(args: argparse.Namespace) -> int:
    if args.stdout:
        sys.stdout.write(json.dumps(planned_source_grid_lock_artifact(), indent=2, sort_keys=True) + "\n")
        return 0

    output: Path = args.output
    _refuse_overwrite_without_force(output, force=args.force)
    write_planned_source_grid_lock(output)
    print(f"wrote Protocol 002 planned source-grid lock: {output}")
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command == "write-stage0":
        return _write_stage0(args)
    if args.command == "write-source-skeleton-example":
        return _write_source_skeleton_example(args)
    if args.command == "write-source-grid-plan":
        return _write_source_grid_plan(args)
    if args.command == "write-source-grid-lock":
        return _write_source_grid_lock(args)
    parser.error(f"unknown command: {args.command}")
    return 2


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
