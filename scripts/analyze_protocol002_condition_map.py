from __future__ import annotations

import argparse

from eco_genetic_warning_extensions.protocol002_condition_map import write_condition_map


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build a warning-blind condition map from the locked Protocol 002 Stage II batches."
    )
    parser.add_argument("--batch-root", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    path = write_condition_map(args.batch_root, args.output)
    print(path)


if __name__ == "__main__":
    main()
