from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build_warning_bundle(root: Path, output: Path) -> Path:
    manuscript = root / "manuscript" / "warning_validity.md"
    audit_csv = root / "manuscript" / "tables" / "warning_validity_audit.csv"
    audit_json = root / "artifacts" / "prepublication_review" / "warning_validity_audit.json"
    records = root / "artifacts" / "warning_validity" / "trajectory_endpoint_records.csv"
    source_manifest = root / "artifacts" / "warning_validity" / "source_manifest.json"
    theorem = root / "docs" / "PRECEDENCE_DISCRIMINATION_THEOREM_2026-09-03.md"

    required = (manuscript, audit_csv, audit_json, records, source_manifest, theorem)
    missing = [str(path.relative_to(root)) for path in required if not path.is_file()]
    if missing:
        raise FileNotFoundError("missing warning-lane files: " + ", ".join(missing))

    source = json.loads(source_manifest.read_text(encoding="utf-8"))
    expected_record_sha = source["record_table"]["sha256"]
    observed_record_sha = sha256(records)
    if observed_record_sha != expected_record_sha:
        raise RuntimeError("warning trajectory record checksum differs from source manifest")

    manuscript_text = manuscript.read_text(encoding="utf-8")
    required_tokens = (
        "35/35",
        "48/48",
        "33/33",
        "49/49",
        "specificity was 0",
        "binary-marker AUC was 0.5",
        "No endpoint rerun or post-result threshold search is",
        "## References",
    )
    for token in required_tokens:
        if token not in manuscript_text:
            raise RuntimeError(f"warning manuscript missing required token: {token}")

    forbidden_tokens = (
        "0.2543",
        "alignment_propagation",
        "natural_data_four_gate_program",
        "state_validity_and_empirical_measurement_gates",
        "+5.33",
        "+5.20",
    )
    for token in forbidden_tokens:
        if token in manuscript_text:
            raise RuntimeError(f"non-warning result leaked into warning manuscript: {token}")

    if output.exists():
        shutil.rmtree(output)
    (output / "manuscript").mkdir(parents=True)
    (output / "tables").mkdir(parents=True)
    (output / "data").mkdir(parents=True)
    (output / "provenance").mkdir(parents=True)

    shutil.copy2(manuscript, output / "manuscript" / "manuscript.md")
    shutil.copy2(audit_csv, output / "tables" / "warning_validity_audit.csv")
    shutil.copy2(records, output / "data" / "trajectory_endpoint_records.csv")
    shutil.copy2(audit_json, output / "provenance" / "warning_validity_audit.json")
    shutil.copy2(source_manifest, output / "provenance" / "source_manifest.json")
    shutil.copy2(theorem, output / "provenance" / "precedence_discrimination_theorem.md")

    readme = """# Warning-validity submission lane\n\nThis bundle contains only the active warning-validity manuscript and the evidence needed to audit its full-denominator result. It intentionally excludes the state-validity manuscript, propagation experiment, integrated source archive, and natural-data four-gate programme.\n\n## Frozen evidence\n\n- inherited event/non-event trajectories: 35 / 48\n- fresh event/non-event trajectories: 33 / 49\n- six frozen thresholds per trajectory\n- all event trajectories: threshold preceded loss\n- all non-event trajectories: threshold fired by horizon\n- resulting binary horizon-marker specificity: 0\n- resulting binary horizon-marker AUC: 0.5\n\nHuman-supplied author/title-page metadata, journal-form fields, archive DOI, and final venue formatting are intentionally outside this anonymous lane bundle.\n"""
    (output / "README.md").write_text(readme, encoding="utf-8")

    manifest: dict[str, object] = {
        "schema_version": 1,
        "lane": "warning_validity",
        "source_record_sha256": observed_record_sha,
        "files": {},
    }
    files = manifest["files"]
    assert isinstance(files, dict)
    for path in sorted(p for p in output.rglob("*") if p.is_file() and p.name != "manifest.json"):
        files[str(path.relative_to(output))] = sha256(path)
    (output / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return output


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=str(ROOT))
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    build_warning_bundle(Path(args.repo_root), Path(args.output))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
