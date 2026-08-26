from __future__ import annotations

import argparse
import http.cookiejar
import json
import re
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

CANDIDATES = (
    ("U1_commelina", "10.5061/dryad.pd775"),
    ("U2_chicago", "10.5061/dryad.44j0zpcm6"),
    ("I1_hiraiwa2017", "10.5061/dryad.pm29d"),
    ("I2_hawaii2019", "10.5061/dryad.tm575v4"),
)

UA = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)


def request(url: str, *, referer: str | None = None, json_only: bool = False, range_only: bool = False):
    headers = {
        "User-Agent": UA,
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control": "no-cache",
    }
    headers["Accept"] = "application/json" if json_only else "*/*"
    if referer:
        headers["Referer"] = referer
    if range_only:
        headers["Range"] = "bytes=0-4095"
    return urllib.request.Request(url, headers=headers)


def get_json(url: str) -> dict[str, Any]:
    with urllib.request.urlopen(request(url, json_only=True), timeout=60) as response:
        return json.loads(response.read().decode("utf-8"))


def abs_url(href: str) -> str:
    if href.startswith("http://") or href.startswith("https://"):
        return href
    if href.startswith("/"):
        return "https://datadryad.org" + href
    return "https://datadryad.org/" + href


def flatten_links(links: dict[str, Any] | None) -> dict[str, str]:
    out: dict[str, str] = {}
    for key, value in (links or {}).items():
        if isinstance(value, dict) and value.get("href"):
            out[str(key)] = abs_url(str(value["href"]))
    return out


def candidate_urls(file_id: int, list_links: dict[str, str], detail_links: dict[str, str]) -> list[tuple[str, str]]:
    ordered: list[tuple[str, str]] = []
    for source_name, links in (("list_link", list_links), ("detail_link", detail_links)):
        for rel, href in links.items():
            if "download" in rel.lower() or "download" in href.lower() or "stream" in href.lower():
                ordered.append((f"{source_name}:{rel}", href))
    ordered.extend(
        [
            ("api_file_download", f"https://datadryad.org/api/v2/files/{file_id}/download"),
            ("stash_file_stream", f"https://datadryad.org/stash/downloads/file_stream/{file_id}"),
            ("legacy_file_stream", f"https://datadryad.org/downloads/file_stream/{file_id}"),
        ]
    )
    seen: set[str] = set()
    unique: list[tuple[str, str]] = []
    for label, url in ordered:
        if url not in seen:
            seen.add(url)
            unique.append((label, url))
    return unique


def inspect_response(
    opener: urllib.request.OpenerDirector,
    url: str,
    referer: str,
    expected_size: int | None,
    expected_mime: str | None,
) -> dict[str, Any]:
    result: dict[str, Any] = {"url": url, "status": None, "error": None}
    try:
        with opener.open(request(url, referer=referer, range_only=True), timeout=60) as response:
            body = response.read(4096)
            result.update(
                {
                    "status": int(response.status),
                    "final_url": response.geturl(),
                    "content_type": response.headers.get("Content-Type"),
                    "content_length": response.headers.get("Content-Length"),
                    "content_range": response.headers.get("Content-Range"),
                    "body_prefix_hex": body[:16].hex(),
                    "body_prefix_text": body[:120].decode("utf-8", errors="replace"),
                }
            )
            content_type = (response.headers.get("Content-Type") or "").lower()
            result["looks_like_challenge_html"] = (
                "text/html" in content_type
                and (b"Validating" in body or b"within.website" in body or b"<!doctype html" in body.lower())
            )
            if expected_size is not None:
                total: int | None = None
                cr = response.headers.get("Content-Range")
                if cr and "/" in cr:
                    try:
                        total = int(cr.rsplit("/", 1)[1])
                    except ValueError:
                        total = None
                cl = response.headers.get("Content-Length")
                if total is None and cl and response.status == 200:
                    try:
                        total = int(cl)
                    except ValueError:
                        total = None
                result["reported_total_size"] = total
                result["expected_size"] = int(expected_size)
                result["size_matches"] = total == int(expected_size) if total is not None else None
            if expected_mime:
                result["expected_mime"] = expected_mime
    except urllib.error.HTTPError as exc:
        result["status"] = int(exc.code)
        result["error"] = f"HTTPError: {exc.code} {exc.reason}"
        try:
            body = exc.read(1024)
            result["error_body_prefix"] = body.decode("utf-8", errors="replace")[:200]
        except Exception:
            pass
    except Exception as exc:  # pragma: no cover - network dependent
        result["error"] = f"{type(exc).__name__}: {exc}"
    return result


def audit_one(candidate_id: str, doi: str) -> dict[str, Any]:
    encoded = urllib.parse.quote(f"doi:{doi}", safe="")
    landing = f"https://datadryad.org/stash/dataset/{encoded}"
    versions_url = f"https://datadryad.org/api/v2/datasets/{encoded}/versions"
    versions = get_json(versions_url).get("_embedded", {}).get("stash:versions", [])
    if not versions:
        raise RuntimeError("no versions")
    latest = versions[-1]
    files_href = latest.get("_links", {}).get("stash:files", {}).get("href")
    if not files_href:
        raise RuntimeError("no files link")
    files_url = abs_url(str(files_href))
    file_items = get_json(files_url).get("_embedded", {}).get("stash:files", [])

    jar = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))
    landing_probe: dict[str, Any] = {"url": landing}
    try:
        with opener.open(request(landing), timeout=60) as response:
            response.read(4096)
            landing_probe["status"] = int(response.status)
    except Exception as exc:
        landing_probe["error"] = f"{type(exc).__name__}: {exc}"

    files: list[dict[str, Any]] = []
    for item in file_items:
        list_links = flatten_links(item.get("_links"))
        self_href = list_links.get("self", "")
        match = re.search(r"/files/(\d+)$", self_href)
        if not match:
            continue
        file_id = int(match.group(1))
        detail: dict[str, Any] = {}
        detail_error: str | None = None
        try:
            detail = get_json(self_href)
        except Exception as exc:
            detail_error = f"{type(exc).__name__}: {exc}"
        detail_links = flatten_links(detail.get("_links") if detail else {})
        expected_size = item.get("size") or detail.get("size")
        expected_mime = item.get("mimeType") or detail.get("mimeType")
        probes: list[dict[str, Any]] = []
        for label, url in candidate_urls(file_id, list_links, detail_links):
            probe = inspect_response(opener, url, landing, int(expected_size) if expected_size else None, expected_mime)
            probe["label"] = label
            probes.append(probe)
        files.append(
            {
                "file_id": file_id,
                "path": item.get("path") or detail.get("path"),
                "expected_size": expected_size,
                "expected_mime": expected_mime,
                "digest": item.get("digest") or detail.get("digest"),
                "digest_type": item.get("digestType") or detail.get("digestType"),
                "list_links": list_links,
                "detail_links": detail_links,
                "detail_error": detail_error,
                "probes": probes,
            }
        )

    usable_probe_count = 0
    for file_record in files:
        for probe in file_record["probes"]:
            if probe.get("status") in (200, 206) and not probe.get("looks_like_challenge_html", False):
                if probe.get("size_matches") is not False:
                    usable_probe_count += 1
                    break
    return {
        "candidate_id": candidate_id,
        "doi": doi,
        "landing_probe": landing_probe,
        "files_url": files_url,
        "files": files,
        "usable_probe_count": usable_probe_count,
        "file_count": len(files),
        "all_files_have_usable_public_probe": bool(files) and usable_probe_count == len(files),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="artifacts/empirical/dryad_public_download_diagnostic.json")
    args = parser.parse_args()
    result: dict[str, Any] = {
        "analysis": "dryad_public_download_diagnostic",
        "boundary": "Transport-only diagnostic; no dataset outcome values are parsed.",
        "candidates": {},
    }
    for candidate_id, doi in CANDIDATES:
        try:
            result["candidates"][candidate_id] = audit_one(candidate_id, doi)
        except Exception as exc:
            result["candidates"][candidate_id] = {
                "candidate_id": candidate_id,
                "doi": doi,
                "error": f"{type(exc).__name__}: {exc}",
                "files": [],
                "file_count": 0,
                "usable_probe_count": 0,
                "all_files_have_usable_public_probe": False,
            }
    result["summary"] = {
        "candidate_count": len(CANDIDATES),
        "candidate_with_full_public_file_probe_count": sum(
            bool(value.get("all_files_have_usable_public_probe")) for value in result["candidates"].values()
        ),
    }
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
