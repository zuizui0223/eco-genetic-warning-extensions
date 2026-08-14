from __future__ import annotations

import argparse
import json
from pathlib import Path

from eco_genetic_warning_extensions.publication_figures import (
    write_stage1_outputs,
    write_stage3_figures,
)
from eco_genetic_warning_extensions.stage3_review_audit import (
    audit as stage3_review_audit,
    write_outputs as write_stage3_review_outputs,
)
from eco_genetic_warning_extensions.stage3_trajectory_records import (
    build_records,
    write_records,
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stage1-root", required=True)
    parser.add_argument("--stage3-domain0", required=True)
    parser.add_argument("--stage3-domain1", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--bootstrap-replicates", type=int, default=20_000)
    args = parser.parse_args()

    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)
    stage1 = write_stage1_outputs(args.stage1_root, out)

    records = build_records([args.stage3_domain0, args.stage3_domain1])
    records_path = out / "stage3_trajectory_endpoint_records.csv"
    write_records(records, records_path)
    audit_result = stage3_review_audit(records, bootstrap_replicates=args.bootstrap_replicates)
    audit_path = out / "stage3_review_audit.json"
    summary_path = out / "stage3_review_summary.csv"
    write_stage3_review_outputs(audit_result, audit_path, summary_path)
    write_stage3_figures(audit_path, out)

    (out / "publication_build_summary.json").write_text(
        json.dumps(
            {
                "stage1_summary": stage1,
                "stage3_secondary_audit": {
                    "records": str(records_path),
                    "audit": str(audit_path),
                    "summary": str(summary_path),
                    "bootstrap_replicates": args.bootstrap_replicates,
                },
            },
            indent=2,
            sort_keys=True,
        ) + "\n",
        encoding="utf-8",
    )
    print(
        f"aggregated {stage1['batch_count']} Stage I batches / "
        f"{stage1['attempt_count']} attempts and rebuilt Stage III audit"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
