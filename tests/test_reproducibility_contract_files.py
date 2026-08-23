from __future__ import annotations

import json
import tomllib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_upstream_lock_matches_protocol_and_locked_stage3_summary() -> None:
    lock = json.loads((ROOT / "reproducibility/upstream-lock.json").read_text(encoding="utf-8"))
    assert lock["schema_version"] == 1
    assert lock["role"] == "independent_extension_and_submission_orchestrator"
    assert lock["upstream"]["scientific_commit"] == "dd8ee379d0d3518194c767d16402042525bc00dc"
    summary = json.loads((ROOT / "artifacts/protocol003/stage3_validation_summary.json").read_text(encoding="utf-8"))
    domains = {domain["domain"]["label"]: domain for domain in summary["domains"]}
    assert domains["symmetric_bridge"]["aggregate_ordering_across_six_endpoints"] == lock["locked_publication_inputs"]["stage3"]["symmetric_ordering"]
    assert domains["transition"]["aggregate_ordering_across_six_endpoints"] == lock["locked_publication_inputs"]["stage3"]["directional_ordering"]


def test_package_metadata_exposes_submission_roles() -> None:
    project = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))["project"]
    assert project["readme"] == "README.md"
    assert "dev" in project["optional-dependencies"]
    assert "reproducibility" in project["optional-dependencies"]
    assert project["urls"]["Mechanistic parent"].endswith("eco-genetic-criticality")


def test_readme_reports_closed_condition_first_state() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    lower = readme.lower().replace("**", "")
    assert "warning is a downstream conditional outcome" in lower
    assert "2,269/3,375" in readme
    assert "phase f is closed" in lower
    assert "historical r3 is not automatically" in lower
    assert "pooled loss is `.499/.573/.598`" in readme
    assert "all predeclared kappa 3.0/4.5/6.0 remain r4" in lower
    assert "partner loss is a negative population-level result" in lower
    assert "warning remains conditional and portability bounded" in lower
    assert "active missing condition" not in lower


def test_submission_bundle_adds_both_packages_and_condition_evidence() -> None:
    assembler = (ROOT / "scripts/assemble_software_bundle.py").read_text(encoding="utf-8")
    replacer = (ROOT / "scripts/replace_submission_figures.py").read_text(encoding="utf-8")
    workflow = (ROOT / ".github/workflows/paper-completion-sprint.yml").read_text(encoding="utf-8")
    assert 'for role in ("parent", "extension")' in assembler
    assert "provenance / \"parent\"" in assembler
    assert "no wheel found" in assembler
    assert "no source archive found" in assembler
    assert "artifacts/interaction_support/phase_f_summary.json" in assembler
    assert "interaction_support_phase_f_summary.json" in replacer
    assert "high_precision_condition_map.json" in replacer
    assert "partner_phase_g_summary.json" in replacer
    assert "--upstream upstream" in workflow
    assert "software_dist/parent" in workflow
    assert "software_dist/extension" in workflow
    assert "assemble_software_bundle.py" in workflow
    assert "git -C upstream archive" in workflow
    assert "git archive" in workflow
    assert "scientific-dd8ee379.tar.gz" in workflow
    assert "repository-$(git rev-parse --short=8 HEAD).tar.gz" in workflow


def test_secondary_audit_lock_preserves_source_artifact_provenance() -> None:
    lock = json.loads((ROOT / "reproducibility/upstream-lock.json").read_text(encoding="utf-8"))
    review = lock["secondary_review_audit"]
    assert review["bootstrap"] == {
        "interval": "percentile 95%",
        "replicates": 20000,
        "seed": 20260814,
        "unit": "whole attempted trajectory",
    }
    assert review["source_workflow_run"] == 29417632137
    assert [row["artifact_id"] for row in review["source_artifacts"]] == [8343958766, 8343922879]

    vendored = json.loads(
        (ROOT / "artifacts/locked_publication_inputs/manifest.json").read_text(encoding="utf-8")
    )
    stage3 = vendored["files"]["stage3_trajectory_endpoint_records.csv.gz.b64"]
    assert stage3["source_workflow_run"] == review["source_workflow_run"]
    assert [row["artifact_id"] for row in stage3["source_artifacts"]] == [
        row["artifact_id"] for row in review["source_artifacts"]
    ]

    workflow = (ROOT / ".github/workflows/paper-completion-sprint.yml").read_text(encoding="utf-8")
    attributes = (ROOT / ".gitattributes").read_text(encoding="utf-8")
    assert "scripts/materialize_locked_publication_inputs.py --output locked" in workflow
    assert "--stage3-records locked/stage3/stage3_trajectory_endpoint_records.csv" in workflow
    assert "artifacts/locked_publication_inputs/**" in workflow
    assert '".gitattributes"' in workflow
    assert "artifacts/locked_publication_inputs/** -text -diff" in attributes
    assert "manuscript/tables/stage3_review_summary.csv -text" in attributes
    assert "manuscript/tables/stage3_between_domain_differences.csv -text" in attributes
    assert "--stage3-domain0" not in workflow
    assert "--stage3-domain1" not in workflow


def test_locked_publication_inputs_materialize_from_committed_bytes(tmp_path: Path) -> None:
    from scripts.materialize_locked_publication_inputs import materialize

    locked = materialize(tmp_path / "locked")
    assert (locked / "stage1/stage1_publication_summary.json").is_file()
    assert (locked / "stage2/stage2_coordinate_regimes.csv").is_file()
    assert (locked / "stage3/stage3_trajectory_endpoint_records.csv").is_file()


def test_reproducibility_guide_retains_current_boundaries() -> None:
    guide = (ROOT / "REPRODUCIBILITY.md").read_text(encoding="utf-8")
    lower = guide.lower()
    for statement in (
        "parent trajectories and extension trajectories are separate evidence",
        "15/15 `no_domain_selected`",
        "historical r1–r4 screen is a calibration device, not a latent biological classification",
        "recurrent turnover: pooled loss declines",
        "only `m=.10` shows detectable high-precision between-block heterogeneity",
        "all three predeclared `kappa=3.0/4.5/6.0` remain intermediate",
        "reduced-form partner loss",
        "protocol 003 tests bounded portability across non-matched calibrated domains",
        "finite type s results",
    ):
        assert statement in lower


def test_committed_phase_f_summary_matches_reproducibility_claim() -> None:
    phase_f = json.loads((ROOT / "artifacts/interaction_support/phase_f_summary.json").read_text(encoding="utf-8"))
    rows = phase_f["interaction_support_summaries"]
    assert [row["interaction_kappa"] for row in rows] == [3.0, 4.5, 6.0]
    assert [row["status_counts"]["baseline_eligible"] for row in rows] == [77, 94, 87]
    assert [row["regime"] for row in rows] == ["R4_highrep"] * 3
    assert phase_f["run_provenance"]["workflow_run_id"] == 32441549848
    assert phase_f["run_provenance"]["artifact_id"] == 9432854668
