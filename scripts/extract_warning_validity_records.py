"""Extract compact review records from the two immutable warning artifacts."""
from __future__ import annotations

import argparse

from eco_genetic_warning_extensions.warning_validity_audit import (
    extract_records,
    write_extracted_records,
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--inherited-json", required=True)
    parser.add_argument("--fresh-json", required=True)
    parser.add_argument(
        "--records-output",
        default="artifacts/warning_validity/trajectory_endpoint_records.csv",
    )
    parser.add_argument(
        "--manifest-output",
        default="artifacts/warning_validity/source_manifest.json",
    )
    args = parser.parse_args()
    rows, manifest = extract_records(
        {
            "inherited_202611": args.inherited_json,
            "fresh_202911": args.fresh_json,
        }
    )
    write_extracted_records(rows, manifest, args.records_output, args.manifest_output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
