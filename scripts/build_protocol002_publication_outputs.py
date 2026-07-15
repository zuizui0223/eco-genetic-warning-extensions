#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from eco_genetic_warning_extensions.protocol002_publication_outputs import (
    write_publication_csv,
    write_regime_svg,
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--audit", type=Path, required=True)
    parser.add_argument("--csv", type=Path, required=True)
    parser.add_argument("--svg", type=Path, required=True)
    args = parser.parse_args()
    rows = write_publication_csv(args.audit, args.csv)
    write_regime_svg(rows, args.svg)
    print(f"wrote {len(rows)} coordinate rows")


if __name__ == "__main__":
    main()
