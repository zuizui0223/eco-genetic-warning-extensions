from __future__ import annotations

import argparse

from eco_genetic_warning_extensions.protocol002_stage1_batch import write_stage1_batch


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--upstream-checkout", required=True)
    parser.add_argument("--batch-index", required=True, type=int)
    parser.add_argument("--output")
    args = parser.parse_args()
    write_stage1_batch(args.upstream_checkout, args.batch_index, args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
