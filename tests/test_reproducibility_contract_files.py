from __future__ import annotations

import json
import tomllib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_upstream_lock_matches_protocol_and_locked_stage3_summary() -> None:
    lock = json.loads(
        (ROOT / "reproducibility/upstream-lock.json").read_text(encoding="utf-8")
    )
    assert lock["schema_version"] == 1
    assert lock["role"] == "independent_extension_and_submission_orchestrator"
    assert lock["upstream"]["scientific_commit"] == (
        "dd8ee379d0d3518194c767d16402042525bc00dc"
    )

    summary = json.loads(
        (ROOT / "artifacts/protocol003/stage3_validation_summary.json").read_text(
            encoding="utf-8"
        )
    )
    domains = {domain["domain"]["label"]: domain for domain in summary["domains"]}
    assert domains["symmetric_bridge"]["aggregate_ordering_across_six_endpoints"] == (
        lock["locked_publication_inputs"]["stage3"]["symmetric_ordering"]
    )
    assert domains["transition"]["aggregate_ordering_across_six_endpoints"] == (
        lock["locked_publication_inputs"]["stage3"]["directional_ordering"]
    )


def test_package_metadata_exposes_submission_roles() -> None:
    pyproject = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    project = pyproject["project"]
    assert project["readme"] == "README.md"
    assert "dev" in project["optional-dependencies"]
    assert "reproducibility" in project["optional-dependencies"]
    assert project["urls"]["Mechanistic parent"].endswith("eco-genetic-criticality")


def test_readme_is_submission_facing_not_pre_simulation() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "The directional-transition campaigns are complete" in readme
    assert "No new simulation result exists yet" not in readme
    assert "submission bundle" in readme
    assert "2,269 of 3,375" in readme
    assert "323 leads" in readme
    assert "184 leads" in readme


def test_submission_bundle_adds_both_software_packages() -> None:
    assembler = (ROOT / "scripts/assemble_software_bundle.py").read_text(
        encoding="utf-8"
    )
    workflow = (ROOT / ".github/workflows/paper-completion-sprint.yml").read_text(
        encoding="utf-8"
    )
    assert 'for role in ("parent", "extension")' in assembler
    assert 'software / "parent"' not in assembler  # roles are handled uniformly
    assert "provenance / \"parent\"" in assembler
    assert "--upstream upstream" in workflow
    assert "software_dist/parent" in workflow
    assert "software_dist/extension" in workflow
    assert "assemble_software_bundle.py" in workflow


def test_reproducibility_guide_retains_protocol_boundaries() -> None:
    guide = (ROOT / "REPRODUCIBILITY.md").read_text(encoding="utf-8")
    for statement in (
        "parent and extension trajectories are separate evidence",
        "Protocol 002 remains closed with 15/15 `no_domain_selected`",
        "Protocol 003 is a separately declared calibration and validation campaign",
        "finite Type S evidence",
    ):
        assert statement in guide
