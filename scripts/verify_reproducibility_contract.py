from __future__ import annotations

import argparse
import csv
import json
import subprocess
import sys
import tomllib
from pathlib import Path
from typing import Any


def _git(repo: Path, *args: str) -> str:
    completed = subprocess.run(
        ["git", "-C", str(repo), *args],
        check=True,
        capture_output=True,
        text=True,
    )
    return completed.stdout.strip()


def _assert_equal(actual: Any, expected: Any, label: str) -> None:
    if actual != expected:
        raise AssertionError(f"{label}: expected {expected!r}, found {actual!r}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify the two-repository submission reproducibility contract.")
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--upstream", required=True)
    parser.add_argument("--lock", default="reproducibility/upstream-lock.json")
    args = parser.parse_args()

    root = Path(args.repo_root).resolve()
    upstream = Path(args.upstream).resolve()
    lock = json.loads((root / args.lock).read_text(encoding="utf-8"))

    upstream_lock = lock["upstream"]
    expected_upstream_commit = upstream_lock["scientific_commit"]
    actual_upstream_commit = _git(upstream, "rev-parse", "HEAD")
    _assert_equal(actual_upstream_commit, expected_upstream_commit, "upstream checkout")

    for relative_path, expected_blob in upstream_lock["required_blobs"].items():
        actual_blob = _git(upstream, "rev-parse", f"HEAD:{relative_path}")
        _assert_equal(actual_blob, expected_blob, f"upstream blob {relative_path}")

    extension_base = lock["extension_base_commit"]
    _git(root, "cat-file", "-e", f"{extension_base}^{{commit}}")
    stage3_lock = lock["locked_publication_inputs"]["stage3"]
    summary_path = stage3_lock["summary_path"]
    base_summary_blob = _git(root, "rev-parse", f"{extension_base}:{summary_path}")
    _assert_equal(base_summary_blob, stage3_lock["summary_blob"], "Stage III summary blob")

    summary = json.loads((root / summary_path).read_text(encoding="utf-8"))
    _assert_equal(summary["source_workflow_run_id"], stage3_lock["workflow_run"], "Stage III workflow")
    _assert_equal(sum(domain["attempted"] for domain in summary["domains"]), stage3_lock["attempted"], "Stage III attempts")

    domains = {domain["domain"]["label"]: domain for domain in summary["domains"]}
    symmetric = domains["symmetric_bridge"]["aggregate_ordering_across_six_endpoints"]
    directional_key = "transition" if "transition" in domains else "directional_transition"
    directional = domains[directional_key]["aggregate_ordering_across_six_endpoints"]
    _assert_equal(symmetric, stage3_lock["symmetric_ordering"], "symmetric ordering")
    _assert_equal(directional, stage3_lock["directional_ordering"], "directional ordering")

    review_lock = lock.get("secondary_review_audit")
    if review_lock:
        _assert_equal(review_lock["bootstrap"]["replicates"], 20000, "secondary bootstrap replicates")
        _assert_equal(review_lock["bootstrap"]["seed"], 20260814, "secondary bootstrap seed")
        review_rows = list(csv.DictReader((root / review_lock["publication_summary_path"]).open(encoding="utf-8")))
        _assert_equal(len(review_rows), 12, "secondary review endpoint rows")
        by_domain: dict[str, list[dict[str, str]]] = {}
        for row in review_rows:
            by_domain.setdefault(row["domain"], []).append(row)
        _assert_equal({row["valid_pairs"] for row in by_domain["recalibrated_symmetric_domain"]}, {"54"}, "secondary symmetric endpoint valid pairs")
        _assert_equal(sum(int(row["valid_pairs"]) for row in by_domain["directional_calibrated_domain"]), 201, "secondary directional aggregate valid pairs")

    pyproject = tomllib.loads((root / "pyproject.toml").read_text(encoding="utf-8"))
    project = pyproject["project"]
    package = lock["package"]
    _assert_equal(project["name"], package["name"], "package name")
    _assert_equal(project["version"], package["version"], "package version")
    _assert_equal(project["requires-python"], package["python"], "Python requirement")

    required_paths = (
        "README.md",
        "REPRODUCIBILITY.md",
        "manuscript/main_text.md",
        "manuscript/claim_evidence_map.md",
        "manuscript/artifact_index.md",
        "reproducibility/upstream-lock.json",
        "manuscript/tables/stage3_review_summary.csv",
        "docs/PROTOCOL_003_SECONDARY_WARNING_AUDIT.md",
    )
    missing = [path for path in required_paths if not (root / path).exists()]
    if missing:
        raise AssertionError("missing submission paths: " + ", ".join(missing))

    manuscript = (root / "manuscript/main_text.md").read_text(encoding="utf-8")
    for token in ("2,269", "20,250", "323", "184", "no_domain_selected"):
        if token not in manuscript:
            raise AssertionError(f"integrated manuscript no longer contains {token}")

    readme = (root / "README.md").read_text(encoding="utf-8")
    if "No new simulation result exists yet" in readme:
        raise AssertionError("README still reports the obsolete pre-simulation status")

    print(json.dumps({
        "status": "verified",
        "extension_base_commit": extension_base,
        "upstream_scientific_commit": expected_upstream_commit,
        "stage3_attempts": stage3_lock["attempted"],
        "package": package,
    }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, FileNotFoundError, KeyError, RuntimeError, subprocess.CalledProcessError) as exc:
        print(f"reproducibility verification failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
