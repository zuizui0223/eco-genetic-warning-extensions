from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import subprocess
import sys
import urllib.request
import zipfile
from pathlib import Path

VERSION_URL = "https://datadryad.org/api/v2/versions/393871/download"
EXPECTED_SIZE = 5543
EXPECTED_SHA256 = "0739cd11bf2afea3a8da7db953e7940fcde5570d5f7cb88e15f08a02140b3127"
EXPECTED_CODES = {"DECA", "LOSI", "PEHI", "SYNO"}


def _request(url: str) -> urllib.request.Request:
    return urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36",
            "Accept": "application/zip,application/octet-stream,*/*;q=0.8",
        },
    )


def acquire_exact_csv(destination: Path) -> dict:
    with urllib.request.urlopen(_request(VERSION_URL), timeout=120) as response:
        payload = response.read()
        download = {
            "status": int(response.status),
            "content_type": response.headers.get("Content-Type"),
            "bundle_bytes": len(payload),
            "final_url": response.geturl(),
        }
    with zipfile.ZipFile(io.BytesIO(payload)) as zf:
        matches = [name for name in zf.namelist() if Path(name).name == "data.csv"]
        if len(matches) != 1:
            raise RuntimeError(f"expected exactly one data.csv, found {matches}")
        data = zf.read(matches[0])
    digest = hashlib.sha256(data).hexdigest()
    if len(data) != EXPECTED_SIZE:
        raise RuntimeError(f"data.csv size mismatch: {len(data)} != {EXPECTED_SIZE}")
    if digest != EXPECTED_SHA256:
        raise RuntimeError(f"data.csv SHA256 mismatch: {digest} != {EXPECTED_SHA256}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(data)
    return {
        **download,
        "member": matches[0],
        "data_bytes": len(data),
        "data_sha256": digest,
        "accepted": True,
    }


def canonicalize_codes(source: Path, destination: Path) -> dict:
    with source.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None or "species_phytometer" not in reader.fieldnames:
            raise RuntimeError("species_phytometer column missing")
        rows = list(reader)
        fieldnames = list(reader.fieldnames)

    observed_raw = sorted({str(row["species_phytometer"]).strip() for row in rows})
    observed_canonical = {value.upper() for value in observed_raw}
    if observed_canonical != EXPECTED_CODES:
        raise RuntimeError(
            f"case-insensitive phytometer-code set differs from preregistration: {sorted(observed_canonical)}"
        )

    for row in rows:
        row["species_phytometer"] = str(row["species_phytometer"]).strip().upper()

    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    return {
        "repair": "species_phytometer_case_only",
        "observed_raw_codes": observed_raw,
        "canonical_codes": sorted(observed_canonical),
        "row_count": len(rows),
        "outcome_columns_inspected_for_repair": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="artifacts/empirical/toronto_residual_context_result_v2.json")
    parser.add_argument("--repair-audit", default="artifacts/empirical/toronto_schema_repair_audit.json")
    args = parser.parse_args()

    raw = Path(".tmp/toronto_v2/data.csv")
    canonical = Path(".tmp/toronto_v2/data_case_normalized.csv")
    acquisition = acquire_exact_csv(raw)
    repair = canonicalize_codes(raw, canonical)
    audit = {
        "analysis": "Toronto_response_firewalled_schema_normalization",
        "acquisition": acquisition,
        "repair": repair,
    }
    audit_path = Path(args.repair_audit)
    audit_path.parent.mkdir(parents=True, exist_ok=True)
    audit_path.write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    command = [
        sys.executable,
        "scripts/run_toronto_residual_context.py",
        "--input",
        str(canonical),
        "--output",
        args.output,
    ]
    completed = subprocess.run(command, check=False)
    return int(completed.returncode)


if __name__ == "__main__":
    raise SystemExit(main())
