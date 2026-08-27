from __future__ import annotations

import argparse
import hashlib
import io
import json
import re
import urllib.parse
import urllib.request
import zipfile
from pathlib import Path, PurePosixPath
from xml.etree import ElementTree as ET

DOI = "10.5061/dryad.hqbzkh1bm"
REQUIRED_FILES = {"Dryad.xlsx", "Dryad_notes.docx"}
MAIN_NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"
DOC_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
OFFICE_REL_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"


def _request(url: str, *, json_only: bool = False) -> urllib.request.Request:
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


def _docx_text(data: bytes) -> str:
    with zipfile.ZipFile(io.BytesIO(data)) as zf:
        xml = zf.read("word/document.xml")
    root = ET.fromstring(xml)
    ns = {"w": DOC_NS}
    paragraphs = []
    for paragraph in root.findall(".//w:p", ns):
        parts = [node.text or "" for node in paragraph.findall(".//w:t", ns)]
        text = "".join(parts).strip()
        if text:
            paragraphs.append(text)
    return "\n".join(paragraphs)


def _column_number(cell_ref: str) -> int:
    letters = re.match(r"([A-Z]+)", cell_ref.upper())
    if not letters:
        return 0
    n = 0
    for ch in letters.group(1):
        n = n * 26 + (ord(ch) - 64)
    return n


def _shared_strings(zf: zipfile.ZipFile) -> list[str]:
    if "xl/sharedStrings.xml" not in zf.namelist():
        return []
    root = ET.fromstring(zf.read("xl/sharedStrings.xml"))
    out = []
    for si in root.findall(f"{{{MAIN_NS}}}si"):
        parts = [node.text or "" for node in si.findall(f".//{{{MAIN_NS}}}t")]
        out.append("".join(parts))
    return out


def _xlsx_schema(data: bytes, limit_rows: int = 12) -> dict:
    with zipfile.ZipFile(io.BytesIO(data)) as zf:
        shared = _shared_strings(zf)
        workbook_root = ET.fromstring(zf.read("xl/workbook.xml"))
        rel_root = ET.fromstring(zf.read("xl/_rels/workbook.xml.rels"))
        rels = {
            rel.attrib["Id"]: rel.attrib["Target"]
            for rel in rel_root.findall(f"{{{REL_NS}}}Relationship")
        }
        sheets = []
        for sheet in workbook_root.findall(f".//{{{MAIN_NS}}}sheet"):
            rid = sheet.attrib.get(f"{{{OFFICE_REL_NS}}}id")
            target = rels.get(rid, "")
            if target.startswith("/"):
                path = target.lstrip("/")
            else:
                path = str(PurePosixPath("xl") / target)
            path = str(PurePosixPath(path))
            sheets.append((sheet.attrib.get("name", ""), path))

        output = {"sheetnames": [name for name, _ in sheets], "sheets": {}}
        for name, path in sheets:
            if path not in zf.namelist():
                output["sheets"][name] = {"error": f"worksheet XML missing: {path}"}
                continue
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
                        parts = [node.text or "" for node in cell.findall(f".//{{{MAIN_NS}}}t")]
                        text = "".join(parts)
                    elif cell_type == "str":
                        v = cell.find(f"{{{MAIN_NS}}}v")
                        if v is not None:
                            text = v.text
                    if isinstance(text, str) and text.strip():
                        strings.append({"column": col_num, "cell": ref, "text": text.strip()})
                if strings and row_num <= limit_rows:
                    string_rows.append({"row": row_num, "string_cells": strings})
            output["sheets"][name] = {
                "max_row": max_row,
                "max_column": max_col,
                "first_rows_string_cells_only": string_rows,
            }
        return output


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
        str(item["path"]): {
            "size": item.get("size"),
            "digest": item.get("digest"),
            "digest_type": item.get("digestType"),
        }
        for item in items
    }
    missing = sorted(REQUIRED_FILES - set(manifest))
    if missing:
        return {"analysis": "Mallorca_original_Dryad_schema_audit", "doi": DOI, "decision": "required_files_missing", "missing": missing}

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

    workbook = _xlsx_schema(payloads["Dryad.xlsx"])
    notes = _docx_text(payloads["Dryad_notes.docx"])
    terms = ["visit", "rate", "pollinator", "species", "year", "seed", "fitness", "flower", "network"]
    relevant_note_lines = [line for line in notes.splitlines() if any(term in line.casefold() for term in terms)]

    combined_text = "\n".join(
        cell["text"]
        for sheet in workbook["sheets"].values()
        for row in sheet.get("first_rows_string_cells_only", [])
        for cell in row["string_cells"]
    ).casefold() + "\n" + notes.casefold()
    direct_visit_terms = any(term in combined_text for term in ["visitation rate", "visits per flower", "number of visits", "pollinator visits"])
    function_terms = any(term in combined_text for term in ["seeds per flower", "seed weight", "fitness"])

    return {
        "analysis": "Mallorca_original_Dryad_schema_audit",
        "doi": DOI,
        "version": latest["_links"]["self"]["href"],
        "download": download,
        "file_verification": verification,
        "workbook": workbook,
        "documentation": {"relevant_note_lines": relevant_note_lines},
        "schema_signals": {
            "direct_visitation_language_present": direct_visit_terms,
            "reproductive_function_language_present": function_terms,
        },
        "decision": "schema_documented_for_manual_gate_review",
        "response_firewall": "Only archive identity, workbook sheet names/dimensions, string-typed cells from the first 12 rows, and documentation text were surfaced. Numeric visitation and reproductive outcome cell values were not surfaced or modeled.",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="artifacts/empirical/n3_mallorca_original_dryad_schema.json")
    args = parser.parse_args()
    try:
        result = audit()
    except Exception as exc:
        result = {
            "analysis": "Mallorca_original_Dryad_schema_audit",
            "doi": DOI,
            "decision": "schema_audit_error",
            "error": f"{type(exc).__name__}: {exc}",
            "response_firewall": "No numeric visitation or reproductive outcome values were modeled.",
        }
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"decision": result["decision"], "schema_signals": result.get("schema_signals")}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
