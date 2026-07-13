from __future__ import annotations

import argparse

from eco_genetic_warning_extensions.protocol002_stage2_no_domain_audit import write_stage2_no_domain_audit


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit why Protocol 002 Stage II selected no calibration domains")
    parser.add_argument("--batch-root", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    output = write_stage2_no_domain_audit(args.batch_root, args.output)
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
