from __future__ import annotations

import argparse

from eco_genetic_warning_extensions.protocol002_stage2_selection import write_stage2_selection


def main() -> int:
    parser = argparse.ArgumentParser(description="Aggregate Stage II batches and select calibration domains")
    parser.add_argument("--batch-root", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    output = write_stage2_selection(args.batch_root, args.output)
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
