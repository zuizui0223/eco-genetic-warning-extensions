from __future__ import annotations

import argparse
import shutil
from pathlib import Path

from eco_genetic_warning_extensions.condition_figure1 import figure1_estimability_svg
from eco_genetic_warning_extensions.revised_publication_figures import write_revised_main_figures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bundle", required=True)
    parser.add_argument("--repo-root", default=".")
    args = parser.parse_args()

    bundle = Path(args.bundle)
    root = Path(args.repo_root)
    figures = bundle / "figures"
    supplement = bundle / "supplement"
    tables = bundle / "tables"
    if not figures.is_dir() or not tables.is_dir():
        raise FileNotFoundError("submission bundle must already contain figures/ and tables/")
    supplement.mkdir(parents=True, exist_ok=True)

    # Preserve the historical conditional lead-time diagnostic as Supplementary S3
    # before replacing the old main-figure spine.
    old_lead = figures / "figure6_stage3_lead_time_normalized.svg"
    if not old_lead.exists():
        raise FileNotFoundError(old_lead)
    shutil.copy2(old_lead, supplement / "figure_s3_stage3_lead_time_normalized.svg")

    for path in figures.glob("*.svg"):
        path.unlink()

    (figures / "figure1_eco_genetic_estimability.svg").write_text(
        figure1_estimability_svg(), encoding="utf-8"
    )
    write_revised_main_figures(
        stage1_csv=tables / "stage1_coordinate_summary.csv",
        stage2_csv=tables / "stage2_coordinate_regimes.csv",
        h3_csv=root / "manuscript/tables/inherited_h3_effect_summary.csv",
        h2_csv=root / "manuscript/tables/inherited_h2_warning_summary.csv",
        phase_b_json=root / "artifacts/frontier_refinement/phase_b_summary.json",
        phase_c_json=root / "artifacts/frontier_refinement/phase_c_summary.json",
        phase_d_json=root / "artifacts/frontier_refinement/phase_d_summary.json",
        phase_e_json=root / "artifacts/migration_condition/phase_e_summary.json",
        stage3_summary_csv=tables / "stage3_review_summary.csv",
        stage3_audit_json=tables / "stage3_review_audit.json",
        output_dir=figures,
    )

    # Add every machine-readable condition result used by the current manuscript.
    # Phase F is text-supported rather than a seventh main figure, but its evidence
    # belongs in the same checksummed bundle as Phases B-E.
    shutil.copy2(root / "manuscript/tables/inherited_h2_warning_summary.csv", tables / "inherited_h2_warning_summary.csv")
    shutil.copy2(root / "artifacts/frontier_refinement/phase_b_summary.json", tables / "frontier_phase_b_summary.json")
    shutil.copy2(root / "artifacts/frontier_refinement/phase_c_summary.json", tables / "frontier_phase_c_summary.json")
    shutil.copy2(root / "artifacts/frontier_refinement/phase_d_summary.json", tables / "frontier_phase_d_summary.json")
    shutil.copy2(root / "artifacts/migration_condition/phase_e_summary.json", tables / "migration_phase_e_summary.json")
    shutil.copy2(root / "artifacts/interaction_support/phase_f_summary.json", tables / "interaction_support_phase_f_summary.json")

    expected = {
        "figure1_eco_genetic_estimability.svg",
        "figure2_fragmentation_warning_bridge.svg",
        "figure3_source_loss_regimes.svg",
        "figure4_r4_recovery.svg",
        "figure5_connectivity_estimability.svg",
        "figure6_portability.svg",
    }
    actual = {path.name for path in figures.glob("*.svg")}
    if actual != expected:
        raise RuntimeError(f"main figure set mismatch: {sorted(actual)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
