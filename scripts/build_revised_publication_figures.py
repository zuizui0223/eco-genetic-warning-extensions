from __future__ import annotations

import argparse
from pathlib import Path

from eco_genetic_warning_extensions.condition_figure1 import figure1_estimability_svg
from eco_genetic_warning_extensions.high_precision_publication_figures import write_high_precision_condition_figures
from eco_genetic_warning_extensions.revised_publication_figures import write_revised_main_figures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stage1-csv", required=True)
    parser.add_argument("--stage2-csv", required=True)
    parser.add_argument("--stage3-audit", required=True)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()

    root = Path(args.repo_root)
    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)
    (out / "figure1_eco_genetic_estimability.svg").write_text(
        figure1_estimability_svg(), encoding="utf-8"
    )
    write_revised_main_figures(
        stage1_csv=args.stage1_csv,
        stage2_csv=args.stage2_csv,
        h3_csv=root / "manuscript/tables/inherited_h3_effect_summary.csv",
        h2_csv=root / "manuscript/tables/inherited_h2_warning_summary.csv",
        phase_b_json=root / "artifacts/frontier_refinement/phase_b_summary.json",
        phase_c_json=root / "artifacts/frontier_refinement/phase_c_summary.json",
        phase_d_json=root / "artifacts/frontier_refinement/phase_d_summary.json",
        phase_e_json=root / "artifacts/migration_condition/phase_e_summary.json",
        stage3_summary_csv=root / "manuscript/tables/stage3_review_summary.csv",
        stage3_audit_json=args.stage3_audit,
        output_dir=out,
    )
    # The legacy writer above still produces the historical Figure 4/5 files for
    # provenance compatibility. Overwrite only those two filenames with the
    # consolidated precision-validated C2 evidence used by the current manuscript.
    write_high_precision_condition_figures(
        root / "artifacts/high_precision_condition_map.json",
        out,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
