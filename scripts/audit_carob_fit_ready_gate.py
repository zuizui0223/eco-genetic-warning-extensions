from __future__ import annotations

import argparse
import hashlib
import io
import json
import math
import re
import urllib.request
import zipfile
from collections import defaultdict
from pathlib import Path, PurePosixPath
from xml.etree import ElementTree as ET

RECORD_ID = 13939480
RECORD_URL = f"https://zenodo.org/api/records/{RECORD_ID}"
TARGET_FILE = "Dataset_CarobTree.xlsx"
MAIN_NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"
OFFICE_REL_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
REQUIRED_PREDICTORS = ("PolinAbun", "Pnatur1k", "FarmSys", "ratMF")
REQUIRED_RESPONSE_FIELDS = ("TotalFlowers", "TotalFruits")


def _request(url: str, *, json_only: bool = False) -> urllib.request.Request:
    return urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36",
            "Accept": "application/json" if json_only else "application/octet-stream,*/*;q=0.8",
        },
    )


def _json(url: str) -> dict:
    with urllib.request.urlopen(_request(url, json_only=True), timeout=120) as response:
        return json.loads(response.read().decode("utf-8"))


def _download(url: str) -> bytes:
    with urllib.request.urlopen(_request(url), timeout=120) as response:
        return response.read()


def _column_index(ref: str) -> int:
    m = re.match(r"([A-Z]+)", ref.upper())
    if not m:
        return 0
    n = 0
    for ch in m.group(1):
        n = n * 26 + ord(ch) - 64
    return n


def _shared_strings(zf: zipfile.ZipFile) -> list[str]:
    if "xl/sharedStrings.xml" not in zf.namelist():
        return []
    root = ET.fromstring(zf.read("xl/sharedStrings.xml"))
    return [
        "".join(node.text or "" for node in si.findall(f".//{{{MAIN_NS}}}t"))
        for si in root.findall(f"{{{MAIN_NS}}}si")
    ]


def _cell_value(cell: ET.Element, shared: list[str]):
    cell_type = cell.attrib.get("t")
    if cell_type == "s":
        v = cell.find(f"{{{MAIN_NS}}}v")
        if v is None or v.text is None:
            return None
        idx = int(v.text)
        return shared[idx] if 0 <= idx < len(shared) else None
    if cell_type == "inlineStr":
        return "".join(node.text or "" for node in cell.findall(f".//{{{MAIN_NS}}}t"))
    v = cell.find(f"{{{MAIN_NS}}}v")
    if v is None or v.text is None:
        return None
    if cell_type == "str":
        return v.text
    text = v.text.strip()
    try:
        value = float(text)
        if value.is_integer():
            return int(value)
        return value
    except ValueError:
        return text


def _sheet_rows(data: bytes) -> dict[str, list[dict[str, object]]]:
    with zipfile.ZipFile(io.BytesIO(data)) as zf:
        shared = _shared_strings(zf)
        workbook = ET.fromstring(zf.read("xl/workbook.xml"))
        rel_root = ET.fromstring(zf.read("xl/_rels/workbook.xml.rels"))
        rels = {rel.attrib["Id"]: rel.attrib["Target"] for rel in rel_root.findall(f"{{{REL_NS}}}Relationship")}
        refs = []
        for sheet in workbook.findall(f".//{{{MAIN_NS}}}sheet"):
            rid = sheet.attrib.get(f"{{{OFFICE_REL_NS}}}id")
            target = rels.get(rid, "")
            path = target.lstrip("/") if target.startswith("/") else str(PurePosixPath("xl") / target)
            refs.append((sheet.attrib.get("name", ""), str(PurePosixPath(path))))

        output: dict[str, list[dict[str, object]]] = {}
        for name, path in refs:
            root = ET.fromstring(zf.read(path))
            matrix: list[dict[int, object]] = []
            for row in root.findall(f".//{{{MAIN_NS}}}row"):
                values: dict[int, object] = {}
                for cell in row.findall(f"{{{MAIN_NS}}}c"):
                    col = _column_index(cell.attrib.get("r", ""))
                    value = _cell_value(cell, shared)
                    if col and value is not None:
                        values[col] = value
                matrix.append(values)
            if not matrix:
                output[name] = []
                continue
            header_row = matrix[0]
            headers = {col: str(value).strip() for col, value in header_row.items() if str(value).strip()}
            rows: list[dict[str, object]] = []
            for raw in matrix[1:]:
                record = {headers[col]: raw.get(col) for col in headers}
                if any(value not in (None, "") for value in record.values()):
                    rows.append(record)
            output[name] = rows
        return output


def _key(row: dict[str, object]) -> tuple[str, str] | None:
    orchard = row.get("StudyOrchard")
    year = row.get("Year")
    if orchard in (None, "") or year in (None, ""):
        return None
    return str(orchard).strip(), str(year).strip()


def _missing(rows: list[dict[str, object]], columns: tuple[str, ...]) -> dict[str, int]:
    return {column: sum(row.get(column) in (None, "") for row in rows) for column in columns}


def _canon(value: object):
    if isinstance(value, float):
        if math.isnan(value):
            return None
        return round(value, 12)
    if isinstance(value, str):
        return value.strip().casefold()
    return value


def _constant_by_key(rows: list[dict[str, object]], columns: tuple[str, ...]) -> dict[str, dict]:
    out = {}
    for column in columns:
        grouped: dict[tuple[str, str], set] = defaultdict(set)
        for row in rows:
            key = _key(row)
            value = row.get(column)
            if key is not None and value not in (None, ""):
                grouped[key].add(_canon(value))
        nonconstant = sorted([list(key) for key, values in grouped.items() if len(values) > 1])
        out[column] = {
            "keys_with_observed_value": len(grouped),
            "nonconstant_key_count": len(nonconstant),
            "nonconstant_keys": nonconstant,
        }
    return out


def audit() -> dict:
    record = _json(RECORD_URL)
    files = {str(item.get("key")): item for item in record.get("files", [])}
    if TARGET_FILE not in files:
        return {"decision": "target_workbook_missing", "record_id": RECORD_ID}
    item = files[TARGET_FILE]
    url = item.get("links", {}).get("content") or item.get("links", {}).get("self")
    payload = _download(str(url))
    checksum = str(item.get("checksum", ""))
    md5 = hashlib.md5(payload).hexdigest()
    expected = checksum.split(":", 1)[1] if checksum.startswith("md5:") else None
    if expected is not None and md5 != expected:
        raise RuntimeError("Zenodo workbook checksum mismatch")

    sheets = _sheet_rows(payload)
    required_sheets = {"PollinatorAbundance", "FruitProduction"}
    if not required_sheets.issubset(sheets):
        return {"decision": "required_sheets_missing", "missing_sheets": sorted(required_sheets - set(sheets))}

    poll = sheets["PollinatorAbundance"]
    fruit = sheets["FruitProduction"]
    poll_keys = [_key(row) for row in poll]
    fruit_keys = [_key(row) for row in fruit]
    poll_key_set = {key for key in poll_keys if key is not None}
    fruit_key_set = {key for key in fruit_keys if key is not None}
    poll_key_counts = defaultdict(int)
    for key in poll_keys:
        if key is not None:
            poll_key_counts[key] += 1
    duplicate_poll_keys = sorted([list(key) for key, count in poll_key_counts.items() if count > 1])

    production_orchards = sorted({key[0] for key in fruit_key_set})
    production_years = sorted({key[1] for key in fruit_key_set})
    missing_predictors = _missing(fruit, REQUIRED_PREDICTORS)
    missing_response = _missing(fruit, REQUIRED_RESPONSE_FIELDS)
    constancy = _constant_by_key(fruit, REQUIRED_PREDICTORS)

    cross_sheet_mismatch = {}
    poll_by_key = {key: row for key, row in zip(poll_keys, poll) if key is not None and poll_key_counts[key] == 1}
    for column in REQUIRED_PREDICTORS:
        mismatched_keys = set()
        for row in fruit:
            key = _key(row)
            if key is None or key not in poll_by_key:
                continue
            a = row.get(column)
            b = poll_by_key[key].get(column)
            if a not in (None, "") and b not in (None, "") and _canon(a) != _canon(b):
                mismatched_keys.add(key)
        cross_sheet_mismatch[column] = {
            "mismatch_key_count": len(mismatched_keys),
            "mismatch_keys": sorted([list(key) for key in mismatched_keys]),
        }

    invalid_exposure = 0
    invalid_fruits = 0
    for row in fruit:
        flowers = row.get("TotalFlowers")
        fruits = row.get("TotalFruits")
        if flowers not in (None, ""):
            try:
                if float(flowers) <= 0:
                    invalid_exposure += 1
            except (TypeError, ValueError):
                invalid_exposure += 1
        if fruits not in (None, ""):
            try:
                if float(fruits) < 0:
                    invalid_fruits += 1
            except (TypeError, ValueError):
                invalid_fruits += 1

    gate_conditions = {
        "at_least_10_independent_orchards": len(production_orchards) >= 10,
        "all_production_keys_have_pollinator_row": fruit_key_set.issubset(poll_key_set),
        "pollinator_keys_unique": not duplicate_poll_keys,
        "required_predictors_complete": all(value == 0 for value in missing_predictors.values()),
        "fruit_response_fields_complete": all(value == 0 for value in missing_response.values()),
        "predictors_constant_within_orchard_year": all(item["nonconstant_key_count"] == 0 for item in constancy.values()),
        "predictors_agree_across_pollinator_and_fruit_sheets": all(item["mismatch_key_count"] == 0 for item in cross_sheet_mismatch.values()),
        "positive_flower_exposure": invalid_exposure == 0,
        "nonnegative_fruit_counts": invalid_fruits == 0,
    }
    fit_ready = all(gate_conditions.values())

    rows_per_key = defaultdict(int)
    for key in fruit_keys:
        if key is not None:
            rows_per_key[key] += 1
    return {
        "analysis": "N3_carob_fit_ready_stage_A_gate",
        "record_id": RECORD_ID,
        "doi": record.get("doi"),
        "workbook": {
            "file": TARGET_FILE,
            "bytes": len(payload),
            "md5": md5,
            "checksum_verified": expected is None or md5 == expected,
        },
        "pollinator_sheet": {
            "row_count": len(poll),
            "orchard_year_key_count": len(poll_key_set),
            "duplicate_key_count": len(duplicate_poll_keys),
            "duplicate_keys": duplicate_poll_keys,
        },
        "fruit_sheet": {
            "row_count": len(fruit),
            "orchard_count": len(production_orchards),
            "orchards": production_orchards,
            "years": production_years,
            "orchard_year_key_count": len(fruit_key_set),
            "rows_per_orchard_year": {f"{key[0]}|{key[1]}": count for key, count in sorted(rows_per_key.items())},
            "keys_missing_from_pollinator_sheet": sorted([list(key) for key in fruit_key_set - poll_key_set]),
            "missing_predictors": missing_predictors,
            "missing_response_fields": missing_response,
            "invalid_totalflowers_count": invalid_exposure,
            "invalid_totalfruits_count": invalid_fruits,
        },
        "predictor_constancy_within_orchard_year": constancy,
        "predictor_cross_sheet_agreement": cross_sheet_mismatch,
        "gate_conditions": gate_conditions,
        "decision": "fit_ready_stage_a" if fit_ready else "not_fit_ready_stage_a",
        "response_firewall": "Stage A inspected only archive identity, StudyOrchard/Year/Tree keys, missingness, within-key constancy, cross-sheet equality, and basic count/exposure validity. No reproductive outcome magnitude, predictor magnitude, association, coefficient, effect direction, or model score was surfaced or computed.",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="artifacts/empirical/n3_carob_fit_ready_stage_a.json")
    args = parser.parse_args()
    try:
        result = audit()
    except Exception as exc:
        result = {
            "analysis": "N3_carob_fit_ready_stage_A_gate",
            "record_id": RECORD_ID,
            "decision": "stage_a_audit_error",
            "error": f"{type(exc).__name__}: {exc}",
            "response_firewall": "No reproductive outcome association or model score was computed.",
        }
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"decision": result["decision"], "gate_conditions": result.get("gate_conditions")}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
