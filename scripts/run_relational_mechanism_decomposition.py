from __future__ import annotations

import argparse
from pathlib import Path

from eco_genetic_warning_extensions.relational_mechanism_decomposition import write


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--summary", required=True)
    parser.add_argument("--records", required=True)
    parser.add_argument("--protocol", default="experiments/relational_mechanism_decomposition_protocol.json")
    args = parser.parse_args()
    write(Path(args.summary), Path(args.records), Path(args.protocol))


if __name__ == "__main__":
    main()
