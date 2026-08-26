"""Run the prospectively fixed exploratory continuous warning audit."""
from __future__ import annotations

import argparse
import json

from eco_genetic_warning_extensions.continuous_warning_landmark import (
    exploratory_audit,
    extract_trajectory_series,
    write_outputs,
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--inherited-json", required=True)
    parser.add_argument("--fresh-json", required=True)
    parser.add_argument("--protocol-commit", required=True)
    parser.add_argument(
        "--json-output",
        default="artifacts/prepublication_review/continuous_warning_landmark_auc.json",
    )
    parser.add_argument(
        "--csv-output",
        default="manuscript/tables/continuous_warning_landmark_auc.csv",
    )
    args = parser.parse_args()
    trajectories, source_manifest = extract_trajectory_series(
        {
            "inherited_202611": args.inherited_json,
            "fresh_202911": args.fresh_json,
        }
    )
    result = exploratory_audit(
        trajectories,
        source_manifest,
        protocol_commit=args.protocol_commit,
    )
    write_outputs(result, args.json_output, args.csv_output)
    print(
        json.dumps(
            {
                ensemble: values["auc_range"]
                for ensemble, values in result["ensembles"].items()
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
