from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT = ROOT / "manuscript" / "warning_validity.md"
BUILDER = ROOT / "scripts" / "build_warning_submission_bundle.py"


def test_warning_manuscript_cites_relevant_prior_art_in_body() -> None:
    text = MANUSCRIPT.read_text(encoding="utf-8")
    body, refs = text.split("## References", 1)
    for citation in (
        "Scheffer et al. 2009",
        "Drake & Griffen 2010",
        "Hastings & Wysham 2010",
        "Boettiger & Hastings 2012",
        "Boettiger & Hastings 2013",
        "Gsell et al. 2016",
        "Schwartz et al. 2007",
        "Hughes et al. 2008",
        "Stange et al. 2021",
    ):
        assert citation in body, citation
    for surname in (
        "Boettiger",
        "Drake",
        "Gsell",
        "Hastings",
        "Hughes",
        "Scheffer",
        "Schwartz",
        "Stange",
    ):
        assert surname in refs, surname


def test_warning_bundle_is_lane_specific_and_checksummed(tmp_path: Path) -> None:
    out = tmp_path / "warning_bundle"
    subprocess.run(
        [sys.executable, str(BUILDER), "--repo-root", str(ROOT), "--output", str(out)],
        check=True,
        cwd=ROOT,
    )
    expected = {
        "README.md",
        "manifest.json",
        "manuscript/manuscript.md",
        "tables/warning_validity_audit.csv",
        "data/trajectory_endpoint_records.csv",
        "provenance/warning_validity_audit.json",
        "provenance/source_manifest.json",
        "provenance/precedence_discrimination_theorem.md",
    }
    observed = {str(path.relative_to(out)) for path in out.rglob("*") if path.is_file()}
    assert observed == expected

    manuscript = (out / "manuscript" / "manuscript.md").read_text(encoding="utf-8")
    for token in ("0.2543", "+5.33", "+5.20", "alignment_propagation", "natural_data_four_gate_program"):
        assert token not in manuscript
    for token in ("35/35", "48/48", "33/33", "49/49", "specificity was 0", "binary-marker AUC was 0.5"):
        assert token in manuscript

    manifest = json.loads((out / "manifest.json").read_text(encoding="utf-8"))
    assert manifest["lane"] == "warning_validity"
    assert manifest["schema_version"] == 1
    assert set(manifest["files"]) == expected - {"manifest.json"}
    for relative, digest in manifest["files"].items():
        actual = hashlib.sha256((out / relative).read_bytes()).hexdigest()
        assert actual == digest


def test_warning_bundle_excludes_state_and_integrated_manuscripts(tmp_path: Path) -> None:
    out = tmp_path / "warning_bundle"
    subprocess.run(
        [sys.executable, str(BUILDER), "--repo-root", str(ROOT), "--output", str(out)],
        check=True,
        cwd=ROOT,
    )
    names = {path.name for path in out.rglob("*") if path.is_file()}
    assert "state_validity_and_empirical_measurement_gates.md" not in names
    assert "main_text.md" not in names
    assert "publication_lanes.json" not in names
