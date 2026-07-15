from __future__ import annotations

import argparse

from eco_genetic_warning_extensions.protocol003_stage3_validation import write_protocol003_validation_domain


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("upstream_checkout")
    parser.add_argument("domain_index", type=int)
    parser.add_argument("output")
    args = parser.parse_args()
    write_protocol003_validation_domain(args.upstream_checkout, args.domain_index, args.output)


if __name__ == "__main__":
    main()
