from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
from pathlib import Path

from eco_genetic_warning_extensions.state_validity_submission_figures import (
    write_propagation_figure,
    write_state_counterexample_figure,
)


STATE_TITLE = "Matching eco-genetic summaries can hide different ecological futures"
FORBIDDEN_PATH_TOKENS = (
    "warning_validity",
    "natural_data",
    "empirical_",
    "stage3_",
    "fragmentation_gradient",
)


def _copy(root: Path, out: Path, relative: str, destination: str | None = None) -> None:
    source = root / relative
    if not source.is_file():
        raise FileNotFoundError(source)
    target = out / (destination or relative)
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)


def _write_propagation_grid(root: Path, out: Path) -> None:
    payload = json.loads((root / "artifacts/alignment_propagation/locked_summary.json").read_text(encoding="utf-8"))
    rows = payload["result"]["cells"]
    expected = {(h, n) for h in (5, 10, 20, 40) for n in (500, 1000, 1500)}
    observed = {(int(row["horizon"]), int(row["n_pairs"])) for row in rows}
    if observed != expected:
        raise RuntimeError("propagation grid no longer contains exactly the 12 predeclared cells")
    path = out / "tables/propagation_complete_grid.csv"
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = (
        "horizon",
        "n_pairs",
        "aligned_loss_count",
        "anti_aligned_loss_count",
        "risk_difference_anti_minus_aligned",
        "ci95_lower",
        "ci95_upper",
        "discordance_rate",
        "mcnemar_exact_p",
    )
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in sorted(rows, key=lambda item: (item["horizon"], item["n_pairs"])):
            writer.writerow({field: row[field] for field in fields})


def _write_manifest(out: Path) -> None:
    entries: list[str] = []
    for path in sorted(p for p in out.rglob("*") if p.is_file() and p.name != "MANIFEST.sha256"):
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        entries.append(f"{digest}  {path.relative_to(out).as_posix()}")
    (out / "MANIFEST.sha256").write_text("\n".join(entries) + "\n", encoding="utf-8")


def _validate_bundle(out: Path) -> None:
    manuscript = (out / "manuscript/main_text.md").read_text(encoding="utf-8")
    cover = (out / "manuscript/cover_letter.md").read_text(encoding="utf-8")
    if not manuscript.startswith(f"# {STATE_TITLE}\n"):
        raise RuntimeError("state-validity manuscript title drifted")
    if STATE_TITLE not in cover:
        raise RuntimeError("state-validity cover letter title is not synchronized")
    for path in out.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(out).as_posix().casefold()
        if any(token in relative for token in FORBIDDEN_PATH_TOKENS):
            raise RuntimeError(f"non-state evidence leaked into state submission bundle: {relative}")
    propagation = json.loads((out / "provenance/alignment_propagation_locked_summary.json").read_text(encoding="utf-8"))
    primary = propagation["result"]["primary_horizon_cells"]
    expected = {
        5: (0.0, 0.0, 0.0),
        10: (0.0033333333333333335, -0.004395170139262505, 0.01106183680592917),
        20: (0.05333333333333334, 0.020439227320699846, 0.08622743934596683),
        40: (0.052, 0.019623552659379068, 0.08437644734062093),
    }
    for row in primary:
        horizon = int(row["horizon"])
        got = (
            float(row["risk_difference_anti_minus_aligned"]),
            float(row["ci95_lower"]),
            float(row["ci95_upper"]),
        )
        if got != expected[horizon]:
            raise RuntimeError(f"locked propagation headline drifted at horizon {horizon}: {got}")


def build_bundle(root: Path, out: Path) -> None:
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)

    manuscript_files = {
        "manuscript/state_validity_and_empirical_measurement_gates.md": "manuscript/main_text.md",
        "manuscript/state_validity_references.md": "manuscript/references.md",
        "manuscript/cover_letter.md": "manuscript/cover_letter.md",
        "manuscript/submission_metadata.md": "manuscript/submission_metadata.md",
        "manuscript/state_validity_display_allocation.md": "manuscript/display_allocation.md",
        "manuscript/PUBLICATION_LANES.md": "provenance/PUBLICATION_LANES.md",
        "manuscript/EG_SERIES_PUBLICATION_ROADMAP_2026-09-04.md": "provenance/EG_SERIES_PUBLICATION_ROADMAP_2026-09-04.md",
    }
    for source, destination in manuscript_files.items():
        _copy(root, out, source, destination)

    evidence_files = {
        "artifacts/cross_layer_alignment/phase_v_locked_summary.json": "provenance/phase_v_locked_summary.json",
        "experiments/alignment_propagation_protocol.json": "provenance/alignment_propagation_protocol.json",
        "artifacts/alignment_propagation/locked_summary.json": "provenance/alignment_propagation_locked_summary.json",
        "docs/ALIGNMENT_PROPAGATION_RESULT_2026-09-04.md": "provenance/ALIGNMENT_PROPAGATION_RESULT_2026-09-04.md",
        "artifacts/fresh_connectivity_replication/phase_u_locked_summary.json": "supplement/phase_u_fresh_connectivity.json",
        "artifacts/process_resolved_movement/phase_r_locked_summary.json": "supplement/phase_r_whole_individual_movement.json",
        "artifacts/process_resolved_pollen/phase_s_locked_summary.json": "supplement/phase_s_pollen_only_movement.json",
        "artifacts/dynamic_partner_architecture/phase_t_locked_summary.json": "supplement/phase_t_partner_architecture.json",
    }
    for source, destination in evidence_files.items():
        _copy(root, out, source, destination)

    write_state_counterexample_figure(
        root / "artifacts/cross_layer_alignment/phase_v_locked_summary.json",
        out / "figures/figure1_state_counterexample.svg",
    )
    write_propagation_figure(
        root / "artifacts/alignment_propagation/locked_summary.json",
        out / "figures/figure2_horizon_propagation.svg",
    )
    _write_propagation_grid(root, out)
    _validate_bundle(out)
    _write_manifest(out)


def main() -> int:
    parser = argparse.ArgumentParser(description="Build the standalone state-validity submission bundle")
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    build_bundle(Path(args.repo_root), Path(args.output))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
