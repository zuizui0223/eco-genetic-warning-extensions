from __future__ import annotations

import argparse
import json
import traceback
from pathlib import Path

from eco_genetic_warning_extensions.protocol002_stage1_projection_pilot import (
    write_stage1_source_projection_pilot,
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--upstream-checkout", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    try:
        write_stage1_source_projection_pilot(args.upstream_checkout, args.output)
    except Exception as exc:
        target = Path(args.output)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(
            json.dumps(
                {
                    "stage": "Protocol 002 Stage I projection pilot failure",
                    "error_type": type(exc).__name__,
                    "error": str(exc),
                    "traceback": traceback.format_exc(),
                },
                indent=2,
                sort_keys=True,
            )
            + "\n",
            encoding="utf-8",
        )
        raise
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
