from __future__ import annotations

import argparse
import base64
import csv
import gzip
import hashlib
import json
import shutil
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "artifacts/locked_publication_inputs"


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _verify_file(path: Path, expected: str) -> bytes:
    data = path.read_bytes()
    actual = _sha256_bytes(data)
    if actual != expected:
        raise RuntimeError(f"checksum drift for {path}: {actual} != {expected}")
    return data


def _validate_stage3(csv_bytes: bytes, manifest: dict[str, object]) -> None:
    spec = manifest["files"]["stage3_trajectory_endpoint_records.csv.gz.b64"]
    if len(csv_bytes) != spec["decoded_csv_bytes"]:
        raise RuntimeError("Stage III decoded byte count drifted")
    if _sha256_bytes(csv_bytes) != spec["decoded_csv_sha256"]:
        raise RuntimeError("Stage III decoded CSV checksum drifted")

    text = csv_bytes.decode("utf-8")
    rows = list(csv.DictReader(text.splitlines()))
    if len(rows) != spec["decoded_data_rows"]:
        raise RuntimeError("Stage III trajectory-endpoint row count drifted")
    domains = Counter(row["domain"] for row in rows)
    if domains != {"recalibrated_symmetric_domain": 600, "directional_calibrated_domain": 600}:
        raise RuntimeError(f"Stage III domain counts drifted: {domains}")

    valid = Counter(row["domain"] for row in rows if row["valid_pair"].lower() == "true")
    if valid != {"recalibrated_symmetric_domain": 324, "directional_calibrated_domain": 201}:
        raise RuntimeError(f"Stage III valid-pair counts drifted: {valid}")

    categories = {
        domain: Counter(row["category"] for row in rows if row["domain"] == domain)
        for domain in domains
    }
    if categories["recalibrated_symmetric_domain"]["lead"] != 323:
        raise RuntimeError("symmetric Stage III lead count drifted")
    if categories["recalibrated_symmetric_domain"]["tie"] != 1:
        raise RuntimeError("symmetric Stage III tie count drifted")
    if categories["directional_calibrated_domain"]["lead"] != 184:
        raise RuntimeError("directional Stage III lead count drifted")
    if categories["directional_calibrated_domain"]["tie"] != 5:
        raise RuntimeError("directional Stage III tie count drifted")
    if categories["directional_calibrated_domain"]["lag"] != 12:
        raise RuntimeError("directional Stage III lag count drifted")


def materialize(destination: str | Path) -> Path:
    destination = Path(destination)
    manifest = json.loads((SOURCE / "manifest.json").read_text(encoding="utf-8"))
    files = manifest["files"]

    for name in (
        "stage1_publication_summary.json",
        "stage1_coordinate_summary.csv",
        "stage2_coordinate_regimes.csv",
    ):
        _verify_file(SOURCE / name, files[name]["sha256"])

    encoded = _verify_file(
        SOURCE / "stage3_trajectory_endpoint_records.csv.gz.b64",
        files["stage3_trajectory_endpoint_records.csv.gz.b64"]["sha256"],
    )
    compressed = base64.b64decode(encoded, validate=True)
    compressed_spec = files["stage3_trajectory_endpoint_records.csv.gz.b64"]
    if _sha256_bytes(compressed) != compressed_spec["compressed_sha256"]:
        raise RuntimeError("Stage III compressed checksum drifted")
    csv_bytes = gzip.decompress(compressed)
    _validate_stage3(csv_bytes, manifest)

    if destination.exists():
        shutil.rmtree(destination)
    (destination / "stage1").mkdir(parents=True)
    (destination / "stage2").mkdir(parents=True)
    (destination / "stage3").mkdir(parents=True)

    shutil.copy2(SOURCE / "stage1_publication_summary.json", destination / "stage1")
    shutil.copy2(SOURCE / "stage1_coordinate_summary.csv", destination / "stage1")
    shutil.copy2(SOURCE / "stage2_coordinate_regimes.csv", destination / "stage2")
    (destination / "stage3/stage3_trajectory_endpoint_records.csv").write_bytes(csv_bytes)
    shutil.copy2(SOURCE / "manifest.json", destination / "manifest.json")

    summary = json.loads((destination / "stage1/stage1_publication_summary.json").read_text(encoding="utf-8"))
    if summary["attempt_count"] != 3375 or summary["totals"]["projection_supported"] != 2269:
        raise RuntimeError("Stage I locked headline totals drifted")

    stage2_rows = list(csv.DictReader((destination / "stage2/stage2_coordinate_regimes.csv").open(encoding="utf-8")))
    if len(stage2_rows) != 15 or any(row["domain_selected"] != "False" for row in stage2_rows):
        raise RuntimeError("Stage II locked no-domain result drifted")

    print(
        "Materialized locked publication inputs: "
        "Stage I 3375/2269; Stage II 15/15 no-domain; Stage III 1200 endpoint rows"
    )
    return destination


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    materialize(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
