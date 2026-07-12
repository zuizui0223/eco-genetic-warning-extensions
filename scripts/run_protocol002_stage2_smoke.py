#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from eco_genetic_warning_extensions.protocol002_stage2_smoke import write_stage2_trait_loss_smoke


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the Protocol 002 Stage II trait-loss-only smoke")
    parser.add_argument("--upstream-checkout", type=Path, required=True)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("artifacts/protocol002/stage2_trait_loss_smoke.json"),
    )
    args = parser.parse_args()
    output = write_stage2_trait_loss_smoke(args.upstream_checkout, args.output)
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
