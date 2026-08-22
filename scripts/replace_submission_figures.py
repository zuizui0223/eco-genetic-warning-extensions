from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

from eco_genetic_warning_extensions.condition_figure1 import figure1_estimability_svg
from eco_genetic_warning_extensions.high_precision_publication_figures import write_high_precision_condition_figures
from eco_genetic_warning_extensions.publication_figure_semantics import relabel_condition_figure_semantics
from eco_genetic_warning_extensions.revised_publication_figures import write_revised_main_figures


def _validate_phase_f(path: Path) -> None:
    """Keep the immutable historical Phase-F artifact as provenance."""
    data = json.loads(path.read_text(encoding="utf-8"))
    rows = data["interaction_support_summaries"]
    if [row["interaction_kappa"] for row in rows] != [3.0, 4.5, 6.0]:
        raise RuntimeError("Phase F kappa contract drifted")
    if [row["status_counts"]["attempted"] for row in rows] != [100, 100, 100]:
        raise RuntimeError("Phase F attempted denominators drifted")
    provenance = data["run_provenance"]
    if provenance["workflow_run_id"] != 32441549848 or provenance["artifact_id"] != 9432854668:
        raise RuntimeError("Phase F run provenance drifted")


def _validate_high_precision_map(path: Path) -> None:
    data = json.loads(path.read_text(encoding="utf-8"))
    frontier = data["recurrent_turnover"]["conditions"]
    if [round(float(row["p_star"]), 3) for row in frontier] != [0.325, 0.35, 0.375, 0.4]:
        raise RuntimeError("high-precision recurrent-turnover map drifted")
    connectivity = {float(row["m"]): row for row in data["connectivity"]["conditions"]}
    if not (float(connectivity[0.10]["equal_rate_p"]) < 0.05 < float(connectivity[0.20]["equal_rate_p"])):
        raise RuntimeError("high-precision connectivity heterogeneity contract drifted")
    if not all(row["screen"] == "R4_highrep" for row in data["reduced_form_partner_loss"]["conditions"]):
        raise RuntimeError("high-precision partner-loss screen contract drifted")
    if not all(row["screen"] == "R4_highrep" for row in data["aggregate_interaction_support"]["conditions"]):
        raise RuntimeError("high-precision interaction-support screen contract drifted")


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
    relabel_condition_figure_semantics(figures)
    high_precision = root / "artifacts/high_precision_condition_map.json"
    _validate_high_precision_map(high_precision)
    write_high_precision_condition_figures(high_precision, figures)

    # Preserve historical condition artifacts and add the current precision layer.
    phase_f = root / "artifacts/interaction_support/phase_f_summary.json"
    _validate_phase_f(phase_f)
    shutil.copy2(root / "manuscript/tables/inherited_h2_warning_summary.csv", tables / "inherited_h2_warning_summary.csv")
    shutil.copy2(root / "artifacts/frontier_refinement/phase_b_summary.json", tables / "frontier_phase_b_summary.json")
    shutil.copy2(root / "artifacts/frontier_refinement/phase_c_summary.json", tables / "frontier_phase_c_summary.json")
    shutil.copy2(root / "artifacts/frontier_refinement/phase_d_summary.json", tables / "frontier_phase_d_summary.json")
    shutil.copy2(root / "artifacts/migration_condition/phase_e_summary.json", tables / "migration_phase_e_summary.json")
    shutil.copy2(phase_f, tables / "interaction_support_phase_f_summary.json")
    shutil.copy2(root / "artifacts/partner_redundancy/phase_g_summary.json", tables / "partner_phase_g_summary.json")
    shutil.copy2(high_precision, tables / "high_precision_condition_map.json")

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
