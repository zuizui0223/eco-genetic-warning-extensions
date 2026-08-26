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

DOI = "10.5061/dryad.9cnp5hqjn"
REQUIRED_FILES = {"dataset.csv", "rate_perflower2016.csv", "rate_perflower2017.csv"}


def _request(url: str, json_only: bool = False) -> urllib.request.Request:
    return urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36",
            "Accept": "application/json" if json_only else "application/zip,application/octet-stream,*/*;q=0.8",
        },
    )


def _json(url: str) -> dict:
    with urllib.request.urlopen(_request(url, json_only=True), timeout=120) as response:
        return json.loads(response.read().decode("utf-8"))


def _norm(value: str) -> str:
    value = value.strip().casefold()
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return " ".join(value.split())


def _rows(data: bytes) -> list[list[str]]:
    text = data.decode("utf-8-sig")
    first = text.splitlines()[0] if text.splitlines() else ""
    delimiter = ";" if first.count(";") > first.count(",") else ","
    return list(csv.reader(io.StringIO(text), delimiter=delimiter))


def audit() -> dict:
    encoded = urllib.parse.quote(f"doi:{DOI}", safe="")
    versions = _json(f"https://datadryad.org/api/v2/datasets/{encoded}/versions").get("_embedded", {}).get("stash:versions", [])
    if not versions:
        raise RuntimeError("no Dryad versions")
    latest = versions[-1]
    files_href = latest["_links"]["stash:files"]["href"]
    download_href = latest["_links"]["stash:download"]["href"]
    files_url = "https://datadryad.org" + files_href if files_href.startswith("/") else files_href
    items = _json(files_url).get("_embedded", {}).get("stash:files", [])
    manifest = {
        str(x["path"]): {"size": x.get("size"), "digest": x.get("digest"), "digest_type": x.get("digestType")}
        for x in items
    }
    missing = sorted(REQUIRED_FILES - set(manifest))
    if missing:
        return {"decision": "required_files_missing_from_archive", "missing_files": missing, "doi": DOI}

    download_url = "https://datadryad.org" + download_href if download_href.startswith("/") else download_href
    with urllib.request.urlopen(_request(download_url), timeout=120) as response:
        bundle = response.read()
        download = {"status": int(response.status), "bytes": len(bundle), "final_url": response.geturl()}

    payloads = {}
    verification = {}
    with zipfile.ZipFile(io.BytesIO(bundle)) as zf:
        by_name = {Path(name).name: name for name in zf.namelist()}
        for name in REQUIRED_FILES:
            data = zf.read(by_name[name])
            digest = hashlib.sha256(data).hexdigest()
            accepted = len(data) == int(manifest[name]["size"]) and digest == str(manifest[name]["digest"])
            if not accepted:
                raise RuntimeError(f"identity mismatch for {name}")
            payloads[name] = data
            verification[name] = {"bytes": len(data), "sha256": digest, "accepted": True}

    dataset_rows = _rows(payloads["dataset.csv"])
    header = dataset_rows[0]
    data_rows = [row for row in dataset_rows[1:] if any(cell.strip() for cell in row)]
    if "Year" not in header or "Species" not in header:
        raise RuntimeError(f"expected Year and Species columns, got {header}")
    year_i = header.index("Year")
    species_i = header.index("Species")
    pairs = {
        (str(row[year_i]).strip(), _norm(str(row[species_i])))
        for row in data_rows
        if len(row) > max(year_i, species_i) and str(row[species_i]).strip()
    }
    species_by_year = {
        year: {species for y, species in pairs if y == year}
        for year in ("2016", "2017")
    }

    matrices = {}
    overlap = {}
    for year in ("2016", "2017"):
        name = f"rate_perflower{year}.csv"
        rows = _rows(payloads[name])
        m_header = rows[0]
        if not m_header or m_header[0].strip() != "PlantSpecies":
            raise RuntimeError(f"unexpected first header for {name}: {m_header[:3]}")
        plant_columns = {_norm(x) for x in m_header[1:] if _norm(x)}
        dataset_species = species_by_year[year]
        matched = sorted(dataset_species & plant_columns)
        matrices[year] = {
            "row_count": max(0, len(rows) - 1),
            "plant_column_count": len(plant_columns),
            "first_header": m_header[0],
        }
        overlap[year] = {
            "dataset_species_count": len(dataset_species),
            "matrix_plant_species_count": len(plant_columns),
            "matched_species_count": len(matched),
            "all_dataset_species_present": dataset_species.issubset(plant_columns),
            "matched_species": matched,
        }

    alignment = all(overlap[y]["all_dataset_species_present"] and overlap[y]["dataset_species_count"] > 0 for y in ("2016", "2017"))
    return {
        "analysis": "N3_Mallorca_network_schema_audit_v2",
        "doi": DOI,
        "decision": "species_year_alignment_demonstrated" if alignment else "species_year_alignment_not_yet_demonstrated",
        "version": latest["_links"]["self"]["href"],
        "download": download,
        "file_verification": verification,
        "dataset_schema": {
            "header": header,
            "row_count": len(data_rows),
            "species_year_pair_count": len(pairs),
            "species_counts_by_year": {y: len(species_by_year[y]) for y in ("2016", "2017")},
        },
        "matrix_schemas": matrices,
        "alignment": overlap,
        "response_firewall": "Only delimiter, file identity, headers, dimensions, species identifiers and year alignment were inspected. No visitation or fecundity values were inspected or modeled.",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="artifacts/empirical/n3_mallorca_network_schema_audit_v2.json")
    args = parser.parse_args()
    try:
        result = audit()
    except Exception as exc:
        result = {
            "analysis": "N3_Mallorca_network_schema_audit_v2",
            "doi": DOI,
            "decision": "schema_audit_error",
            "error": f"{type(exc).__name__}: {exc}",
            "response_firewall": "No visitation or fecundity values were inspected or modeled.",
        }
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"decision": result["decision"]}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
