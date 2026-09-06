from __future__ import annotations

import argparse

from eco_genetic_warning_extensions.allele_sorting_single_edge_proof import write


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--summary", required=True)
    parser.add_argument("--records", required=True)
    parser.add_argument("--protocol", default=None)
    args = parser.parse_args()
    if args.protocol is None:
        write(args.summary, args.records)
    else:
        write(args.summary, args.records, args.protocol)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
