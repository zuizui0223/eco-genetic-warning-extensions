from __future__ import annotations

import argparse

from eco_genetic_warning_extensions.protocol003_bracket_pilot import write_protocol003_bracket_cell


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--upstream-checkout", required=True)
    parser.add_argument("--cell-index", required=True, type=int)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    path = write_protocol003_bracket_cell(
        args.upstream_checkout,
        args.cell_index,
        args.output,
    )
    print(path)


if __name__ == "__main__":
    main()
