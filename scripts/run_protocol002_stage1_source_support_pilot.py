#!/usr/bin/env python3
from __future__ import annotations

import argparse

from eco_genetic_warning_extensions.protocol002_stage1_pilot import (
    DEFAULT_STAGE1_PILOT_PATH,
    write_stage1_source_support_pilot,
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--upstream-checkout", required=True)
    parser.add_argument("--output", default=str(DEFAULT_STAGE1_PILOT_PATH))
    args = parser.parse_args()
    output = write_stage1_source_support_pilot(args.upstream_checkout, args.output)
    print(f"wrote Protocol 002 Stage I source-support pilot artifact: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
