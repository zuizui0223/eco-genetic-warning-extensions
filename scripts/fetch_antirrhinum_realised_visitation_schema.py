from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import zipfile
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen

import openpyxl
import xlrd

RECORDS = (
    {
        "role": "wild_visitation",
        "record_id": 5552,
        "doi": "10.15479/AT:ISTA:36",
        "filename": "IST-2016-36-v1+1_tag_assay_archive.zip",
        "md5": "cbc61b523d4d475a04a737d50dc470ef",
    },
    {
        "role": "wild_paternity_2012",
        "record_id": 5553,
        "doi": "10.15479/AT:ISTA:37",
        "filename": "IST-2016-37-v1+1_paternity_archive.zip",
        "md5": "4ae751b1fa4897fa216241f975a57313",
    },
)
ROOT = "https://research-explorer.ista.ac.at"
UA = "eco-genetic-warning-extensions/1.0"


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "a":
            return
        for key, value in attrs:
            if key.lower() == "href" and value:
                self.links.append(value)


def _request(url: str, *, accept: str) -> bytes:
    req = Request(url, headers={"User-Agent": UA, "Accept": accept})
    with urlopen(req, timeout=180) as response:
        return response.read()


def _resolve_archive(record: dict[str, object]) -> tuple[str, bytes]:
    landing = f"{ROOT}/record/{record['record_id']}"
    html = _request(landing, accept="text/html,*/*")
    parser = LinkParser()
    parser.feed(html.decode("utf-8", errors="replace"))
    exact = str(record["filename"])
    candidates: list[str] = []
    for href in parser.links:
        url = urljoin(landing, href)
        parsed = urlparse(url)
        if parsed.scheme != "https" or not parsed.netloc.endswith("ista.ac.at"):
            continue
        if exact in url or Path(parsed.path).name == exact:
            candidates.append(url)
    candidates = sorted(set(candidates))
    if not candidates:
        raise RuntimeError(f"landing page exposed no exact archive link for {exact}")

    failures: list[str] = []
    for url in candidates:
        try:
            payload = _request(url, accept="application/zip,application/octet-stream,*/*")
        except Exception as exc:
            failures.append(f"{url}:{type(exc).__name__}")
            continue
        observed = hashlib.md5(payload).hexdigest()
        if observed != record["md5"]:
            failures.append(f"{url}:md5={observed}")
            continue
        if not zipfile.is_zipfile(io.BytesIO(payload)):
            failures.append(f"{url}:not_zip")
            continue
        return url, payload
    raise RuntimeError(f"no exact MD5-locked archive resolved for {exact}: {failures!r}")


def _decode_text(raw: bytes) -> str:
    for encoding in ("utf-8-sig", "utf-8", "latin-1"):
        try:
            return raw.decode(encoding)
        except UnicodeDecodeError:
            continue
    raise RuntimeError("could not decode text header")


def _delimited_header(raw: bytes, suffix: str) -> list[str]:
    text = _decode_text(raw)
    first_line = text.splitlines()[0] if text.splitlines() else ""
    delimiter = "\t" if suffix in {".tsv", ".tab"} else ","
    if suffix == ".txt":
        delimiter = "\t" if "\t" in first_line else ","
    row = next(csv.reader([first_line], delimiter=delimiter), [])
    return [str(v) for v in row]


def _xlsx_schema(raw: bytes) -> list[dict[str, object]]:
    wb = openpyxl.load_workbook(io.BytesIO(raw), read_only=True, data_only=False)
    out: list[dict[str, object]] = []
    for ws in wb.worksheets:
        first = next(ws.iter_rows(min_row=1, max_row=1, values_only=True), tuple())
        out.append({
            "sheet": ws.title,
            "rows_including_header": int(ws.max_row or 0),
            "columns_count": int(ws.max_column or 0),
            "columns": ["" if x is None else str(x) for x in first],
        })
    wb.close()
    return out


def _xls_schema(raw: bytes) -> list[dict[str, object]]:
    wb = xlrd.open_workbook(file_contents=raw, on_demand=True)
    out: list[dict[str, object]] = []
    for name in wb.sheet_names():
        ws = wb.sheet_by_name(name)
        out.append({
            "sheet": name,
            "rows_including_header": int(ws.nrows),
            "columns_count": int(ws.ncols),
            "columns": [str(v) for v in (ws.row_values(0) if ws.nrows else [])],
        })
    wb.release_resources()
    return out


def _member_schema(name: str, raw: bytes) -> dict[str, object]:
    suffix = Path(name).suffix.lower()
    result: dict[str, object] = {
        "member_name": name,
        "member_bytes": len(raw),
        "sha256": hashlib.sha256(raw).hexdigest(),
    }
    if suffix in {".csv", ".tsv", ".tab", ".txt"}:
        result["columns"] = _delimited_header(raw, suffix)
    elif suffix == ".xlsx":
        result["workbook_schema"] = _xlsx_schema(raw)
    elif suffix == ".xls":
        result["workbook_schema"] = _xls_schema(raw)
    return result


def discover(manifest_path: Path) -> dict[str, object]:
    records: list[dict[str, object]] = []
    for record in RECORDS:
        url, payload = _resolve_archive(record)
        members: list[dict[str, object]] = []
        with zipfile.ZipFile(io.BytesIO(payload)) as archive:
            for info in archive.infolist():
                if info.is_dir():
                    continue
                raw = archive.read(info)
                members.append(_member_schema(info.filename, raw))
        records.append({
            **record,
            "resolved_archive_url": url,
            "archive_bytes": len(payload),
            "observed_md5": hashlib.md5(payload).hexdigest(),
            "sha256": hashlib.sha256(payload).hexdigest(),
            "members": members,
        })

    result: dict[str, object] = {
        "status": "schema_only_discovery_complete",
        "records": records,
        "inspection_boundary": (
            "Only ISTA landing links, MD5-locked archive bytes, archive member names/sizes/hashes, and first header rows or workbook header rows were inspected. "
            "No data-row value, visitation outcome, reproductive value, paternity assignment, genotype value, effect direction, coefficient, p-value or descriptive outcome statistic was read or computed."
        ),
        "next_gate": (
            "Use schema/header names only to map 2012 year/time, wild plant identity, spatial/phenotypic state, I_realised_proxy, any explicit F_reproduction endpoint, and G_mating/C_pollen. "
            "Classify wild_IFG_joint_state_identifiable, wild_IG_partial_state_identifiable, or wild_state_not_identifiable."
        ),
    }
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", default="artifacts/empirical/antirrhinum_realised_visitation_schema.json")
    args = parser.parse_args()
    result = discover(Path(args.manifest))
    print(json.dumps({
        "status": result["status"],
        "records": {
            row["role"]: [member["member_name"] for member in row["members"]]
            for row in result["records"]
        },
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
