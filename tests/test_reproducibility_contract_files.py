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


def test_readme_is_submission_facing_not_pre_simulation() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "campaigns are complete" in readme
    assert "No new simulation result exists yet" not in readme
    assert "submission bundle" in readme
    assert "2,269 of 3,375" in readme
    assert "323 leads" in readme
    assert "184 leads" in readme
    assert "not a single-factor causal effect" in readme


def test_submission_bundle_adds_both_packages_and_source_archives() -> None:
    assembler = (ROOT / "scripts/assemble_software_bundle.py").read_text(encoding="utf-8")
    workflow = (ROOT / ".github/workflows/paper-completion-sprint.yml").read_text(encoding="utf-8")
    assert 'for role in ("parent", "extension")' in assembler
    assert "provenance / \"parent\"" in assembler
    assert "no wheel found" in assembler
    assert "no source archive found" in assembler
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
    workflow = (ROOT / ".github/workflows/paper-completion-sprint.yml").read_text(encoding="utf-8")
    assert "protocol003-stage3-validation-domain-0" in workflow
    assert "protocol003-stage3-validation-domain-1" in workflow
    assert "--stage3-domain0" in workflow and "--stage3-domain1" in workflow


def test_reproducibility_guide_retains_protocol_boundaries() -> None:
    guide = (ROOT / "REPRODUCIBILITY.md").read_text(encoding="utf-8")
    for statement in (
        "parent trajectories and extension trajectories are separate evidence",
        "15/15 `no_domain_selected`",
        "Protocol 003 is separately declared",
        "Amendment 001 expanded its candidate family",
        "Stage III therefore tests warning portability across calibrated eco-genetic domains",
        "finite Type S results",
    ):
        assert statement in guide
