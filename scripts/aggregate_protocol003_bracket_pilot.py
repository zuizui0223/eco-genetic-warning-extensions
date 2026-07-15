from __future__ import annotations

import argparse

from eco_genetic_warning_extensions.protocol003_bracket_aggregate import write_bracket_aggregation


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_root")
    parser.add_argument("output")
    args = parser.parse_args()
    print(write_bracket_aggregation(args.input_root, args.output))


if __name__ == "__main__":
    main()
