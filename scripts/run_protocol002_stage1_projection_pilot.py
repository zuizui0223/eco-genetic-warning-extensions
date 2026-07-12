from __future__ import annotations

import argparse

from eco_genetic_warning_extensions.protocol002_stage1_projection_pilot import (
    write_stage1_source_projection_pilot,
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--upstream-checkout", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    write_stage1_source_projection_pilot(args.upstream_checkout, args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
