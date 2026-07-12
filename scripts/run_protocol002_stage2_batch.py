from __future__ import annotations

import argparse

from eco_genetic_warning_extensions.protocol002_stage2_batch import write_stage2_batch


def main() -> int:
    parser = argparse.ArgumentParser(description="Run one Protocol 002 Stage II calibration batch")
    parser.add_argument("--upstream-checkout", required=True)
    parser.add_argument("--batch-index", required=True, type=int)
    parser.add_argument("--output")
    args = parser.parse_args()
    output = write_stage2_batch(args.upstream_checkout, args.batch_index, args.output)
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
