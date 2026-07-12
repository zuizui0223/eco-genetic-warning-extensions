#!/usr/bin/env python3
"""Run the pinned upstream Protocol 002 H1 SYM integration smoke."""
from __future__ import annotations

import argparse

from eco_genetic_warning_extensions.protocol002_upstream_h1_smoke import (
    DEFAULT_UPSTREAM_H1_SMOKE_PATH,
    write_upstream_h1_sym_smoke,
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--upstream-checkout", required=True)
    parser.add_argument("--output", default=str(DEFAULT_UPSTREAM_H1_SMOKE_PATH))
    args = parser.parse_args()
    output = write_upstream_h1_sym_smoke(args.upstream_checkout, args.output)
    print(f"wrote Protocol 002 upstream H1 SYM smoke artifact: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
