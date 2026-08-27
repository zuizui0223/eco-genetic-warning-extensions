from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import urllib.request
import zipfile
from pathlib import Path, PurePosixPath
from xml.etree import ElementTree as ET

RECORD_ID = 13939480
RECORD_URL = f"https://zenodo.org/api/records/{RECORD_ID}"
MAIN_NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"
OFFICE_REL_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"


def _request(url: str, *, json_only: bool = False) -> urllib.request.Request:
    return urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36",
            "Accept": "application/json" if json_only else "application/octet-stream,*/*;q=0.8",
        },
    )


def _get_json(url: str) -> dict:
    with urllib.request.urlopen(_request(url, json_only=True), timeout=120) as response:
        return json.loads(response.read().decode("utf-8"))


def _download(url: str) -> tuple[bytes, dict]:
    with urllib.request.urlopen(_request(url), timeout=120) as response:
        payload = response.read()
        return payload, {"status": int(response.status), "bytes": len(payload), "final_url": response.geturl()}


def _column_number(cell_ref: str) -> int:
    letters = re.match(r"([A-Z]+)", cell_ref.upper())
    if not letters:
        return 0
    n = 0
    for ch in letters.group(1):
        n = n * 26 + ord(ch) - 64
    return n


def _shared_strings(zf: zipfile.ZipFile) -> list[str]:
    if "xl/sharedStrings.xml" not in zf.namelist():
        return []
    root = ET.fromstring(zf.read("xl/sharedStrings.xml"))
    out = []
    for si in root.findall(f"{{{MAIN_NS}}}si"):
        out.append("".join(node.text or "" for node in si.findall(f".//{{{MAIN_NS}}}t")))
    return out


def _xlsx_schema(data: bytes, limit_rows: int = 10) -> dict:
    with zipfile.ZipFile(io.BytesIO(data)) as zf:
        shared = _shared_strings(zf)
        workbook_root = ET.fromstring(zf.read("xl/workbook.xml"))
        rel_root = ET.fromstring(zf.read("xl/_rels/workbook.xml.rels"))
        rels = {rel.attrib["Id"]: rel.attrib["Target"] for rel in rel_root.findall(f"{{{REL_NS}}}Relationship")}
        sheet_refs = []
        for sheet in workbook_root.findall(f".//{{{MAIN_NS}}}sheet"):
            rid = sheet.attrib.get(f"{{{OFFICE_REL_NS}}}id")
            target = rels.get(rid, "")
            path = target.lstrip("/") if target.startswith("/") else str(PurePosixPath("xl") / target)
            sheet_refs.append((sheet.attrib.get("name", ""), str(PurePosixPath(path))))
        output = {"sheetnames": [name for name, _ in sheet_refs], "sheets": {}}
        for name, path in sheet_refs:
            root = ET.fromstring(zf.read(path))
            max_row = 0
            max_col = 0
            string_rows = []
            for row in root.findall(f".//{{{MAIN_NS}}}row"):
                row_num = int(row.attrib.get("r", "0") or 0)
                max_row = max(max_row, row_num)
                strings = []
                for cell in row.findall(f"{{{MAIN_NS}}}c"):
                    ref = cell.attrib.get("r", "")
                    col_num = _column_number(ref)
                    max_col = max(max_col, col_num)
                    if row_num > limit_rows:
                        continue
                    cell_type = cell.attrib.get("t")
                    text = None
                    if cell_type == "s":
                        v = cell.find(f"{{{MAIN_NS}}}v")
                        if v is not None and v.text is not None:
                            idx = int(v.text)
                            if 0 <= idx < len(shared):
                                text = shared[idx]
                    elif cell_type == "inlineStr":
                        text = "".join(node.text or "" for node in cell.findall(f".//{{{MAIN_NS}}}t"))
                    elif cell_type == "str":
                        v = cell.find(f"{{{MAIN_NS}}}v")
                        text = None if v is None else v.text
                    if isinstance(text, str) and text.strip():
                        strings.append({"column": col_num, "cell": ref, "text": text.strip()})
                if strings and row_num <= limit_rows:
                    string_rows.append({"row": row_num, "string_cells": strings})
            output["sheets"][name] = {"max_row": max_row, "max_column": max_col, "first_rows_string_cells_only": string_rows}
        return output


def _csv_header(data: bytes) -> list[str]:
    text = data.decode("utf-8-sig", errors="replace")
    first = text.splitlines()[0] if text.splitlines() else ""
    delimiter = ";" if first.count(";") > first.count(",") else ","
    rows = csv.reader(io.StringIO(text), delimiter=delimiter)
    return [cell.strip() for cell in next(rows, [])]


def audit() -> dict:
    record = _get_json(RECORD_URL)
    files = record.get("files", [])
    manifest = []
    schemas = {}
    for item in files:
        key = str(item.get("key", ""))
        checksum = str(item.get("checksum", ""))
        size = item.get("size")
        links = item.get("links", {})
        content_url = links.get("content") or links.get("self")
        entry = {"key": key, "size": size, "checksum": checksum, "content_url": content_url}
        manifest.append(entry)
        suffix = Path(key).suffix.casefold()
        if suffix not in {".xlsx", ".csv", ".tsv", ".txt"} or not content_url:
            continue
        payload, transfer = _download(str(content_url))
        digest = hashlib.md5(payload).hexdigest()
        expected_md5 = checksum.split(":", 1)[1] if checksum.startswith("md5:") else None
        verified = expected_md5 is None or digest == expected_md5
        if not verified:
            raise RuntimeError(f"checksum mismatch for {key}")
        if suffix == ".xlsx":
            schema = _xlsx_schema(payload)
        elif suffix in {".csv", ".tsv"}:
            schema = {"header": _csv_header(payload)}
        else:
            text = payload.decode("utf-8-sig", errors="replace")
            schema = {"documentation_lines": [line.strip() for line in text.splitlines() if line.strip()][:100]}
        schemas[key] = {"transfer": transfer, "md5": digest, "schema": schema}

    corpus_parts = []
    for key, item in schemas.items():
        corpus_parts.append(key)
        schema = item["schema"]
        corpus_parts.extend(schema.get("header", []))
        corpus_parts.extend(schema.get("documentation_lines", []))
        for sheet_name, sheet in schema.get("sheets", {}).items():
            corpus_parts.append(sheet_name)
            for row in sheet.get("first_rows_string_cells_only", []):
                corpus_parts.extend(cell["text"] for cell in row["string_cells"])
    corpus = "\n".join(corpus_parts).casefold()
    signals = {
        "orchard_or_site_identifier_language": any(term in corpus for term in ["orchard", "site", "locality", "plot"]),
        "year_language": "year" in corpus,
        "direct_visit_language": any(term in corpus for term in ["visit", "pollinator abundance", "pollinator visits"]),
        "reproductive_function_language": any(term in corpus for term in ["fruit", "seed", "production", "yield"]),
        "context_language": any(term in corpus for term in ["natural habitat", "landscape", "farming system", "male-to-female", "male female ratio"]),
    }
    return {
        "analysis": "N3_Mallorca_carob_Zenodo_schema_audit",
        "record_id": RECORD_ID,
        "conceptdoi": record.get("metadata", {}).get("prereserve_doi", {}).get("doi") or record.get("conceptdoi"),
        "doi": record.get("doi"),
        "manifest": manifest,
        "schemas": schemas,
        "signals": signals,
        "decision": "schema_documented_for_manual_gate_review",
        "response_firewall": "Only Zenodo metadata, file identity/checksums, table headers, workbook sheet names/dimensions, string-typed cells from the first 10 rows, and text documentation were surfaced. Numeric pollinator and production values were not surfaced or modeled.",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="artifacts/empirical/n3_carob_zenodo_schema.json")
    args = parser.parse_args()
    try:
        result = audit()
    except Exception as exc:
        result = {
            "analysis": "N3_Mallorca_carob_Zenodo_schema_audit",
            "record_id": RECORD_ID,
            "decision": "schema_audit_error",
            "error": f"{type(exc).__name__}: {exc}",
            "response_firewall": "No numeric pollinator or production values were modeled.",
        }
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"decision": result["decision"], "signals": result.get("signals"), "files": [x.get("key") for x in result.get("manifest", [])]}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
