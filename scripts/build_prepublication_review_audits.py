"""Rebuild the locked prepublication warning and precision audits."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from eco_genetic_warning_extensions.precision_bounded_null import (
    audit as precision_audit,
    write_output as write_precision_output,
)
from eco_genetic_warning_extensions.warning_validity_audit import (
    audit as warning_audit,
    load_records,
    write_audit_outputs,
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--warning-records",
        default="artifacts/warning_validity/trajectory_endpoint_records.csv",
    )
    parser.add_argument(
        "--precision-counts",
        default="artifacts/precision_bounded_null/source_counts.json",
    )
    parser.add_argument("--artifact-dir", default="artifacts/prepublication_review")
    parser.add_argument("--table-dir", default="manuscript/tables")
    args = parser.parse_args()
    artifact_dir = Path(args.artifact_dir)
    table_dir = Path(args.table_dir)
    warning = warning_audit(load_records(args.warning_records))
    write_audit_outputs(
        warning,
        artifact_dir / "warning_validity_audit.json",
        table_dir / "warning_validity_audit.csv",
    )
    precision_source = json.loads(Path(args.precision_counts).read_text(encoding="utf-8"))
    precision = precision_audit(precision_source)
    write_precision_output(precision, artifact_dir / "precision_bounded_null_audit.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
