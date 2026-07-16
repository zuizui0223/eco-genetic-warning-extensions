from __future__ import annotations

import argparse

from eco_genetic_warning_extensions.publication_figures import write_stage1_outputs, write_stage3_figures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stage1-root", required=True)
    parser.add_argument("--stage3-summary", required=True)
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()
    result = write_stage1_outputs(args.stage1_root, args.output_dir)
    write_stage3_figures(args.stage3_summary, args.output_dir)
    print(f"aggregated {result['batch_count']} Stage I batches / {result['attempt_count']} attempts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
