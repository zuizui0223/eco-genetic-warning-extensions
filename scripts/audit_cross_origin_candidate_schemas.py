from __future__ import annotations

import argparse
import http.cookiejar
import json
import re
import shutil
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from pathlib import Path
from typing import Any

import pandas as pd

CANDIDATES = (
    {
        "id": "U1_commelina",
        "origin": "urban",
        "doi": "10.5061/dryad.pd775",
        "source": "Ushimaru et al. 2014",
    },
    {
        "id": "U2_chicago",
        "origin": "urban",
        "doi": "10.5061/dryad.44j0zpcm6",
        "source": "Zink et al. 2024",
    },
    {
        "id": "I1_hiraiwa2017",
        "origin": "island",
        "doi": "10.5061/dryad.pm29d",
        "source": "Hiraiwa & Ushimaru 2017",
    },
    {
        "id": "I2_hawaii2019",
        "origin": "island",
        "doi": "10.5061/dryad.tm575v4",
        "source": "Aslan et al. 2019",
    },
)

VISIT_RE = re.compile(r"visit|visitor|pollinat|bee|hover|syrph|hymen|flower.?obs|interaction", re.I)
REPRO_RE = re.compile(r"fruit|seed|pollen|ovule|repro|fertili|set$|success|offspring", re.I)
EFFORT_RE = re.compile(r"effort|minute|hour|duration|time|census|observation|flowers?.?(observed|count|number)|n.?flower", re.I)
CONTEXT_RE = re.compile(r"urban|impervious|develop|distance|island|site|garden|population|locality|location|habitat", re.I)
PREFERRED_KEYS = {
    "site",
    "siteid",
    "garden",
    "id",
    "individual",
    "plant",
    "plantid",
    "population",
    "pop",
    "plot",
    "locality",
    "location",
    "species",
    "date",
    "block",
}

BROWSER_UA = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)


def _norm(value: object) -> str:
    text = str(value).strip().lower()
    return re.sub(r"[^a-z0-9]+", "", text)


def _request(url: str, *, referer: str | None = None, json_only: bool = False) -> urllib.request.Request:
    headers = {
        "User-Agent": BROWSER_UA,
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control": "no-cache",
    }
    if json_only:
        headers["Accept"] = "application/json"
    else:
        headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    if referer:
        headers["Referer"] = referer
    return urllib.request.Request(url, headers=headers)


def _get_json(url: str) -> dict[str, Any]:
    with urllib.request.urlopen(_request(url, json_only=True), timeout=120) as response:
        return json.loads(response.read().decode("utf-8"))


def _dryad_file_manifest(doi: str) -> list[dict[str, Any]]:
    encoded = urllib.parse.quote(f"doi:{doi}", safe="")
    versions_url = f"https://datadryad.org/api/v2/datasets/{encoded}/versions"
    versions = _get_json(versions_url).get("_embedded", {}).get("stash:versions", [])
    if not versions:
        raise RuntimeError(f"no Dryad versions returned for {doi}")
    latest = versions[-1]
    files_href = latest.get("_links", {}).get("stash:files", {}).get("href")
    if not files_href:
        raise RuntimeError(f"latest Dryad version lacks stash:files link for {doi}")
    if str(files_href).startswith("/"):
        files_url = "https://datadryad.org" + str(files_href)
    else:
        files_url = str(files_href)
    files = _get_json(files_url).get("_embedded", {}).get("stash:files", [])
    manifest: list[dict[str, Any]] = []
    for item in files:
        self_href = item.get("_links", {}).get("self", {}).get("href", "")
        match = re.search(r"/files/(\d+)$", str(self_href))
        if not match:
            continue
        manifest.append(
            {
                "file_id": int(match.group(1)),
                "path": str(item.get("path") or f"file_{match.group(1)}"),
                "size": item.get("size"),
                "mime_type": item.get("mimeType"),
                "digest": item.get("digest"),
                "digest_type": item.get("digestType"),
                "download_attempts": [],
            }
        )
    if not manifest:
        raise RuntimeError(f"no Dryad file ids returned for {doi}")
    return manifest


def _download_urls(file_id: int) -> tuple[str, ...]:
    return (
        f"https://datadryad.org/stash/downloads/file_stream/{file_id}",
        f"https://datadryad.org/downloads/file_stream/{file_id}",
        f"https://datadryad.org/stash/downloads/file_stream/{file_id}?download=1",
        f"https://datadryad.org/downloads/file_stream/{file_id}?download=1",
    )


def _browser_opener(doi: str) -> tuple[urllib.request.OpenerDirector, str, dict[str, Any]]:
    cookie_jar = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar))
    landing_doi = urllib.parse.quote(f"doi:{doi}", safe="")
    landing_url = f"https://datadryad.org/stash/dataset/{landing_doi}"
    landing_status: dict[str, Any] = {"url": landing_url, "status": None, "error": None}
    try:
        with opener.open(_request(landing_url), timeout=120) as response:
            # Read only a small prefix to establish the browser session/cookies. No dataset values live here.
            response.read(4096)
            landing_status["status"] = int(response.status)
    except urllib.error.HTTPError as exc:
        landing_status["status"] = int(exc.code)
        landing_status["error"] = f"HTTPError: {exc.code} {exc.reason}"
    except Exception as exc:  # pragma: no cover - network dependent
        landing_status["error"] = f"{type(exc).__name__}: {exc}"
    return opener, landing_url, landing_status


def _download_one_file(
    opener: urllib.request.OpenerDirector,
    landing_url: str,
    item: dict[str, Any],
    target: Path,
) -> bool:
    for url in _download_urls(int(item["file_id"])):
        attempt: dict[str, Any] = {"url": url, "status": None, "error": None}
        try:
            request = _request(url, referer=landing_url)
            with opener.open(request, timeout=120) as response, target.open("wb") as handle:
                attempt["status"] = int(response.status)
                attempt["content_type"] = response.headers.get("Content-Type")
                attempt["content_length"] = response.headers.get("Content-Length")
                shutil.copyfileobj(response, handle)
            item["download_attempts"].append(attempt)
            item["download_url_used"] = url
            item["download_status"] = "success"
            return True
        except urllib.error.HTTPError as exc:
            attempt["status"] = int(exc.code)
            attempt["error"] = f"HTTPError: {exc.code} {exc.reason}"
            item["download_attempts"].append(attempt)
        except Exception as exc:  # pragma: no cover - network dependent
            attempt["error"] = f"{type(exc).__name__}: {exc}"
            item["download_attempts"].append(attempt)
    item["download_status"] = "failed"
    return False


def _download_dryad_files(doi: str, destination: Path) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    destination.mkdir(parents=True, exist_ok=True)
    manifest = _dryad_file_manifest(doi)
    opener, landing_url, landing_status = _browser_opener(doi)
    all_success = True
    for item in manifest:
        target = destination / item["path"]
        target.parent.mkdir(parents=True, exist_ok=True)
        success = _download_one_file(opener, landing_url, item, target)
        all_success = all_success and success
        if not success and target.exists():
            target.unlink()

    # Expand nested ZIPs only for schema discovery. Raw outcome values are never read by this script.
    if all_success:
        for nested in list(destination.rglob("*.zip")):
            nested_dir = nested.with_suffix("")
            try:
                with zipfile.ZipFile(nested) as archive:
                    nested_dir.mkdir(parents=True, exist_ok=True)
                    archive.extractall(nested_dir)
            except zipfile.BadZipFile:
                continue
    return manifest, {"landing": landing_status, "all_files_downloaded": all_success}


def _csv_columns(path: Path) -> list[str]:
    last: Exception | None = None
    for encoding in ("utf-8-sig", "utf-8", "latin-1"):
        try:
            frame = pd.read_csv(path, nrows=0, sep=None, engine="python", encoding=encoding)
            return [str(column) for column in frame.columns]
        except Exception as exc:  # pragma: no cover - archive dependent
            last = exc
    raise RuntimeError(f"could not read CSV header {path}: {last}")


def _excel_schemas(path: Path) -> list[dict[str, Any]]:
    book = pd.ExcelFile(path)
    records: list[dict[str, Any]] = []
    for sheet in book.sheet_names:
        try:
            frame = pd.read_excel(path, sheet_name=sheet, nrows=0)
            columns = [str(column) for column in frame.columns]
            error = None
        except Exception as exc:  # pragma: no cover - archive dependent
            columns = []
            error = f"{type(exc).__name__}: {exc}"
        records.append({"sheet": str(sheet), "columns": columns, "error": error})
    return records


def _roles(path_label: str, columns: list[str]) -> dict[str, bool]:
    combined = " ".join([path_label, *columns])
    return {
        "visitation": bool(VISIT_RE.search(combined)),
        "reproduction": bool(REPRO_RE.search(combined)),
        "effort": bool(EFFORT_RE.search(combined)),
        "context": bool(CONTEXT_RE.search(combined)),
    }


def _inspect_archive(root: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    supported = {".csv", ".txt", ".tsv", ".xlsx", ".xls"}
    for path in sorted(p for p in root.rglob("*") if p.is_file() and p.suffix.lower() in supported):
        relative = str(path.relative_to(root))
        suffix = path.suffix.lower()
        if suffix in {".xlsx", ".xls"}:
            try:
                sheets = _excel_schemas(path)
            except Exception as exc:  # pragma: no cover - archive dependent
                sheets = [{"sheet": None, "columns": [], "error": f"{type(exc).__name__}: {exc}"}]
            for sheet in sheets:
                columns = sheet["columns"]
                label = f"{relative}::{sheet['sheet']}" if sheet["sheet"] else relative
                records.append(
                    {
                        "container": relative,
                        "sheet": sheet["sheet"],
                        "columns": columns,
                        "normalised_columns": [_norm(column) for column in columns],
                        "roles": _roles(label, columns),
                        "error": sheet["error"],
                    }
                )
        else:
            try:
                columns = _csv_columns(path)
                error = None
            except Exception as exc:  # pragma: no cover - archive dependent
                columns = []
                error = f"{type(exc).__name__}: {exc}"
            records.append(
                {
                    "container": relative,
                    "sheet": None,
                    "columns": columns,
                    "normalised_columns": [_norm(column) for column in columns],
                    "roles": _roles(relative, columns),
                    "error": error,
                }
            )
    return records


def _candidate_decision(records: list[dict[str, Any]]) -> dict[str, Any]:
    visitation = [record for record in records if record["roles"]["visitation"] and record["columns"]]
    reproduction = [record for record in records if record["roles"]["reproduction"] and record["columns"]]
    effort = [record for record in visitation if record["roles"]["effort"]]
    context = [record for record in records if record["roles"]["context"] and record["columns"]]

    join_candidates: list[dict[str, Any]] = []
    for v in visitation:
        vcols = set(v["normalised_columns"])
        for r in reproduction:
            rcols = set(r["normalised_columns"])
            shared = sorted(vcols & rcols)
            preferred = sorted(column for column in shared if column in PREFERRED_KEYS)
            if shared:
                join_candidates.append(
                    {
                        "visitation_table": f"{v['container']}::{v['sheet']}" if v["sheet"] else v["container"],
                        "reproduction_table": f"{r['container']}::{r['sheet']}" if r["sheet"] else r["container"],
                        "shared_columns": shared,
                        "preferred_shared_keys": preferred,
                    }
                )

    preferred_join = any(item["preferred_shared_keys"] for item in join_candidates)
    gates = {
        "visitation_schema_present": bool(visitation),
        "reproduction_schema_present": bool(reproduction),
        "effort_schema_present": bool(effort),
        "join_key_present": bool(preferred_join),
        "context_schema_present": bool(context),
    }
    eligible = all(
        gates[key]
        for key in (
            "visitation_schema_present",
            "reproduction_schema_present",
            "effort_schema_present",
            "join_key_present",
        )
    )
    return {
        "gates": gates,
        "schema_eligible_for_mapping_review": eligible,
        "visitation_tables": [
            f"{record['container']}::{record['sheet']}" if record["sheet"] else record["container"]
            for record in visitation
        ],
        "reproduction_tables": [
            f"{record['container']}::{record['sheet']}" if record["sheet"] else record["container"]
            for record in reproduction
        ],
        "effort_tables": [
            f"{record['container']}::{record['sheet']}" if record["sheet"] else record["container"]
            for record in effort
        ],
        "context_tables": [
            f"{record['container']}::{record['sheet']}" if record["sheet"] else record["container"]
            for record in context
        ],
        "join_candidates": join_candidates,
    }


def run(work_root: Path) -> dict[str, Any]:
    work_root.mkdir(parents=True, exist_ok=True)
    output: dict[str, Any] = {
        "analysis": "response_firewalled_cross_origin_minimal_bridge_schema_audit",
        "candidate_lock": list(CANDIDATES),
        "inspection_boundary": (
            "Only repository metadata, file/sheet names, column names and join-key structure are inspected. "
            "No reproductive outcome values, associations, fitted effects or direction-based inclusion decisions are computed."
        ),
        "download_method": "anonymous Dryad metadata + browser-session public file_stream fallback (new/legacy paths)",
        "candidates": {},
    }

    for candidate in CANDIDATES:
        candidate_dir = work_root / candidate["id"]
        manifest: list[dict[str, Any]] = []
        acquisition: dict[str, Any] = {}
        try:
            manifest, acquisition = _download_dryad_files(candidate["doi"], candidate_dir)
            if not acquisition["all_files_downloaded"]:
                output["candidates"][candidate["id"]] = {
                    "origin": candidate["origin"],
                    "doi": candidate["doi"],
                    "source": candidate["source"],
                    "download_status": "failed",
                    "error": "public file-stream acquisition failed after browser-session new/legacy URL attempts",
                    "acquisition": acquisition,
                    "file_manifest": manifest,
                    "schema_records": [],
                    "decision": {
                        "schema_eligible_for_mapping_review": False,
                        "gates": {},
                    },
                }
                continue
            records = _inspect_archive(candidate_dir)
            decision = _candidate_decision(records)
            output["candidates"][candidate["id"]] = {
                "origin": candidate["origin"],
                "doi": candidate["doi"],
                "source": candidate["source"],
                "download_status": "success",
                "acquisition": acquisition,
                "file_manifest": manifest,
                "schema_records": records,
                "decision": decision,
            }
        except Exception as exc:  # pragma: no cover - network/archive dependent
            output["candidates"][candidate["id"]] = {
                "origin": candidate["origin"],
                "doi": candidate["doi"],
                "source": candidate["source"],
                "download_status": "failed",
                "error": f"{type(exc).__name__}: {exc}",
                "acquisition": acquisition,
                "file_manifest": manifest,
                "schema_records": [],
                "decision": {
                    "schema_eligible_for_mapping_review": False,
                    "gates": {},
                },
            }

    origin_counts: dict[str, int] = {"urban": 0, "island": 0}
    eligible_by_origin: dict[str, int] = {"urban": 0, "island": 0}
    for candidate in output["candidates"].values():
        origin = str(candidate["origin"])
        origin_counts[origin] += 1
        if candidate["decision"]["schema_eligible_for_mapping_review"]:
            eligible_by_origin[origin] += 1
    output["summary"] = {
        "locked_candidates_by_origin": origin_counts,
        "schema_eligible_by_origin": eligible_by_origin,
        "all_four_downloaded": all(c["download_status"] == "success" for c in output["candidates"].values()),
        "metadata_manifest_resolved_for_all": all(bool(c.get("file_manifest")) for c in output["candidates"].values()),
        "next_decision": (
            "freeze_exact_column_mappings_before_outcome_access"
            if eligible_by_origin["urban"] >= 2 and eligible_by_origin["island"] >= 2
            else "minimal_bridge_not_yet_identifiable_from_locked_archives"
        ),
    }
    return output


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--work-root", default=".tmp/cross_origin_schema_audit")
    parser.add_argument("--output", default="artifacts/empirical/cross_origin_minimal_bridge_schema_audit.json")
    args = parser.parse_args()

    result = run(Path(args.work_root))
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
