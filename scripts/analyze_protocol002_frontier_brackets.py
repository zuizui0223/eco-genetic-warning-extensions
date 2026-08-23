from __future__ import annotations

import argparse

from eco_genetic_warning_extensions.protocol002_frontier_brackets import write_frontier_brackets


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract warning-blind matched p_star frontier brackets.")
    parser.add_argument("--batch-root", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    print(write_frontier_brackets(args.batch_root, args.output))


if __name__ == "__main__":
    main()
