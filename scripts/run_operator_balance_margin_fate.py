from __future__ import annotations

import argparse

from eco_genetic_warning_extensions.operator_balance_margin_fate import write


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--summary", required=True)
    parser.add_argument("--records", required=True)
    parser.add_argument("--protocol", default=None)
    args = parser.parse_args()
    if args.protocol is None:
        write(args.summary, args.records)
    else:
        write(args.summary, args.records, args.protocol)


if __name__ == "__main__":
    main()
