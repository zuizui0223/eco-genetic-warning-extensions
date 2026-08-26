from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import urllib.parse
import urllib.request
import zipfile
from pathlib import Path
from typing import Any

DOI = "10.5061/dryad.9cnp5hqjn"
REQUIRED_FILES = {
    "dataset.csv",
    "rate_perflower2016.csv",
    "rate_perflower2017.csv",
}
YEARS = (2016, 2017)


def _request(url: str, *, json_only: bool = False) -> urllib.request.Request:
    return urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36",
            "Accept": "application/json" if json_only else "application/zip,application/octet-stream,*/*;q=0.8",
        },
    )


def _get_json(url: str) -> dict[str, Any]:
    with urllib.request.urlopen(_request(url, json_only=True), timeout=120) as response:
        return json.loads(response.read().decode("utf-8"))


def _norm(value: str) -> str:
    text = value.strip().casefold().replace("_", " ")
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return " ".join(text.split())


def _csv_rows(data: bytes) -> list[list[str]]:
    text = data.decode("utf-8-sig")
    return list(csv.reader(io.StringIO(text)))


def _axis_identifiers(rows: list[list[str]]) -> tuple[list[str], list[str]]:
    if not rows:
        return [], []
    header = rows[0]
    column_ids = [x for x in header[1:] if x.strip()]
    row_ids = [row[0] for row in rows[1:] if row and row[0].strip()]
    return row_ids, column_ids


def _dataset_schema(rows: list[list[str]]) -> dict[str, Any]:
    if not rows:
        raise RuntimeError("dataset.csv is empty")
    header = rows[0]
    body = [row for row in rows[1:] if any(cell.strip() for cell in row)]
    lowered = [h.casefold() for h in header]
    species_cols = [i for i, h in enumerate(lowered) if "species" in h or h in {"plant", "plant_name", "plant name"}]
    year_cols = [i for i, h in enumerate(lowered) if h == "year" or h.endswith("_year") or h.endswith(" year")]
    year_specific_columns = {
        str(year): [header[i] for i, h in enumerate(lowered) if str(year) in h]
        for year in YEARS
    }
    species_values: list[str] = []
    if len(species_cols) == 1:
        idx = species_cols[0]
        species_values = [row[idx] for row in body if len(row) > idx and row[idx].strip()]
    year_values: list[str] = []
    if len(year_cols) == 1:
        idx = year_cols[0]
        year_values = [row[idx] for row in body if len(row) > idx and row[idx].strip()]
    return {
        "header": header,
        "row_count": len(body),
        "species_candidate_columns": [header[i] for i in species_cols],
        "year_candidate_columns": [header[i] for i in year_cols],
        "year_specific_columns": year_specific_columns,
        "species_unique_count": len({_norm(x) for x in species_values if _norm(x)}),
        "year_unique_values": sorted(set(year_values)),
        "_species_values": species_values,
    }


def audit() -> dict[str, Any]:
    encoded = urllib.parse.quote(f"doi:{DOI}", safe="")
    versions_url = f"https://datadryad.org/api/v2/datasets/{encoded}/versions"
    versions = _get_json(versions_url).get("_embedded", {}).get("stash:versions", [])
    if not versions:
        raise RuntimeError("Dryad returned no versions")
    latest = versions[-1]
    version_href = latest.get("_links", {}).get("self", {}).get("href")
    files_href = latest.get("_links", {}).get("stash:files", {}).get("href")
    download_href = latest.get("_links", {}).get("stash:download", {}).get("href")
    if not version_href or not files_href or not download_href:
        raise RuntimeError("Dryad version metadata lacks required links")

    files_url = "https://datadryad.org" + files_href if str(files_href).startswith("/") else str(files_href)
    file_items = _get_json(files_url).get("_embedded", {}).get("stash:files", [])
    manifest = {
        str(item.get("path")): {
            "size": item.get("size"),
            "digest": item.get("digest"),
            "digest_type": item.get("digestType"),
            "mime_type": item.get("mimeType"),
        }
        for item in file_items
    }
    missing = sorted(REQUIRED_FILES - set(manifest))
    if missing:
        return {
            "analysis": "N3_Mallorca_network_schema_audit",
            "doi": DOI,
            "decision": "required_files_missing_from_archive",
            "missing_files": missing,
            "manifest": manifest,
            "response_firewall": "No fecundity or visitation outcome values were inspected or modeled.",
        }

    download_url = "https://datadryad.org" + download_href if str(download_href).startswith("/") else str(download_href)
    try:
        with urllib.request.urlopen(_request(download_url), timeout=120) as response:
            bundle = response.read()
            download_meta = {
                "url": download_url,
                "status": int(response.status),
                "content_type": response.headers.get("Content-Type"),
                "bytes": len(bundle),
                "final_url": response.geturl(),
            }
    except Exception as exc:
        return {
            "analysis": "N3_Mallorca_network_schema_audit",
            "doi": DOI,
            "decision": "locked_archive_bytes_not_acquired",
            "version": version_href,
            "manifest": manifest,
            "download_error": f"{type(exc).__name__}: {exc}",
            "response_firewall": "No fecundity or visitation outcome values were inspected or modeled.",
        }

    try:
        with zipfile.ZipFile(io.BytesIO(bundle)) as zf:
            members = zf.namelist()
            by_name = {Path(name).name: name for name in members}
            payloads: dict[str, bytes] = {}
            file_verification: dict[str, Any] = {}
            for expected in REQUIRED_FILES:
                if expected not in by_name:
                    raise RuntimeError(f"{expected} missing from version bundle")
                data = zf.read(by_name[expected])
                digest = hashlib.sha256(data).hexdigest()
                expected_size = manifest[expected].get("size")
                expected_digest = manifest[expected].get("digest")
                accepted = (expected_size is None or len(data) == int(expected_size)) and (
                    expected_digest is None or digest == str(expected_digest)
                )
                file_verification[expected] = {
                    "member": by_name[expected],
                    "bytes": len(data),
                    "sha256": digest,
                    "expected_size": expected_size,
                    "expected_digest": expected_digest,
                    "accepted": bool(accepted),
                }
                if not accepted:
                    raise RuntimeError(f"identity verification failed for {expected}")
                payloads[expected] = data
    except Exception as exc:
        return {
            "analysis": "N3_Mallorca_network_schema_audit",
            "doi": DOI,
            "decision": "bundle_identity_or_structure_failed",
            "download": download_meta,
            "manifest": manifest,
            "error": f"{type(exc).__name__}: {exc}",
            "response_firewall": "No fecundity or visitation outcome values were inspected or modeled.",
        }

    dataset_rows = _csv_rows(payloads["dataset.csv"])
    dataset = _dataset_schema(dataset_rows)
    species_raw = dataset.pop("_species_values")
    species_norm = {_norm(x) for x in species_raw if _norm(x)}

    matrices: dict[str, Any] = {}
    alignment: dict[str, Any] = {}
    for year in YEARS:
        name = f"rate_perflower{year}.csv"
        rows = _csv_rows(payloads[name])
        row_ids, col_ids = _axis_identifiers(rows)
        row_norm = {_norm(x) for x in row_ids if _norm(x)}
        col_norm = {_norm(x) for x in col_ids if _norm(x)}
        row_overlap = sorted(species_norm & row_norm)
        col_overlap = sorted(species_norm & col_norm)
        matrices[str(year)] = {
            "header": rows[0] if rows else [],
            "row_count": max(0, len(rows) - 1),
            "column_count": len(rows[0]) if rows else 0,
            "first_column_name": rows[0][0] if rows and rows[0] else None,
            "row_identifier_count": len(row_norm),
            "column_identifier_count": len(col_norm),
        }
        alignment[str(year)] = {
            "dataset_species_overlap_with_matrix_rows": len(row_overlap),
            "dataset_species_overlap_with_matrix_columns": len(col_overlap),
            "matching_axis": "rows" if len(row_overlap) > len(col_overlap) else "columns" if len(col_overlap) > len(row_overlap) else "tie",
        }

    has_single_species_key = len(dataset["species_candidate_columns"]) == 1 and dataset["species_unique_count"] > 0
    year_mapping_explicit = (
        len(dataset["year_candidate_columns"]) == 1
        or all(dataset["year_specific_columns"][str(year)] for year in YEARS)
    )
    aligned_each_year = all(
        max(
            alignment[str(year)]["dataset_species_overlap_with_matrix_rows"],
            alignment[str(year)]["dataset_species_overlap_with_matrix_columns"],
        ) > 0
        for year in YEARS
    )
    decision = (
        "species_year_alignment_demonstrated"
        if has_single_species_key and year_mapping_explicit and aligned_each_year
        else "species_year_alignment_not_yet_demonstrated"
    )
    return {
        "analysis": "N3_Mallorca_network_schema_audit",
        "doi": DOI,
        "decision": decision,
        "version": version_href,
        "download": download_meta,
        "manifest": manifest,
        "file_verification": file_verification,
        "dataset_schema": dataset,
        "matrix_schemas": matrices,
        "alignment": alignment,
        "response_firewall": "Only file identity, headers, dimensions and identifier alignment were inspected. No fecundity or visitation outcome values were inspected or modeled.",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="artifacts/empirical/n3_mallorca_network_schema_audit.json")
    args = parser.parse_args()
    output = Path(args.output)
    try:
        result = audit()
    except Exception as exc:
        result = {
            "analysis": "N3_Mallorca_network_schema_audit",
            "doi": DOI,
            "decision": "schema_audit_error",
            "error": f"{type(exc).__name__}: {exc}",
            "response_firewall": "No fecundity or visitation outcome values were inspected or modeled.",
        }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"decision": result["decision"]}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
