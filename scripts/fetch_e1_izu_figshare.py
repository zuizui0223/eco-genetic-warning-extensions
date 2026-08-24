#!/usr/bin/env python3
"""Fetch and inventory the public E1 Honshu–Izu Figshare archive.

This script deliberately does not commit third-party raw data. It downloads the
public Figshare item into a temporary/output directory, verifies file metadata,
extracts common archives, and writes a compact machine-readable discovery
manifest containing file names, hashes, tabular headers and R-code I/O/model
hints. The manifest is intended to drive the next preregistered residual-origin
analysis without guessing the archive layout.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import os
import re
import shutil
import tarfile
import urllib.request
import zipfile
from pathlib import Path
from typing import Any

ARTICLE_ID = 25025000
ARTICLE_VERSION = 1
RESOURCE_DOI = "10.6084/m9.figshare.25025000.v1"
API_URL = f"https://api.figshare.com/v2/articles/{ARTICLE_ID}/versions/{ARTICLE_VERSION}"
USER_AGENT = "eco-genetic-warning-extensions/0.1 E1 empirical audit"
TEXT_SUFFIXES = {".csv", ".tsv", ".txt", ".r", ".R", ".md"}
ARCHIVE_SUFFIXES = {".zip", ".tar", ".tgz", ".gz", ".bz2", ".xz"}


def _request_json(url: str) -> dict[str, Any]:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=60) as response:
        return json.loads(response.read().decode("utf-8"))


def _download(url: str, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=120) as response, destination.open("wb") as handle:
        shutil.copyfileobj(response, handle)


def _md5(path: Path) -> str:
    digest = hashlib.md5()  # noqa: S324 - source archive verification only
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _safe_extract_zip(path: Path, destination: Path) -> list[str]:
    extracted: list[str] = []
    with zipfile.ZipFile(path) as archive:
        for member in archive.infolist():
            target = (destination / member.filename).resolve()
            if destination.resolve() not in target.parents and target != destination.resolve():
                raise RuntimeError(f"unsafe zip member: {member.filename}")
        archive.extractall(destination)
        extracted = [member.filename for member in archive.infolist() if not member.is_dir()]
    return extracted


def _safe_extract_tar(path: Path, destination: Path) -> list[str]:
    extracted: list[str] = []
    with tarfile.open(path) as archive:
        for member in archive.getmembers():
            target = (destination / member.name).resolve()
            if destination.resolve() not in target.parents and target != destination.resolve():
                raise RuntimeError(f"unsafe tar member: {member.name}")
        archive.extractall(destination)
        extracted = [member.name for member in archive.getmembers() if member.isfile()]
    return extracted


def _extract_archive(path: Path, destination: Path) -> list[str]:
    destination.mkdir(parents=True, exist_ok=True)
    if zipfile.is_zipfile(path):
        return _safe_extract_zip(path, destination)
    try:
        if tarfile.is_tarfile(path):
            return _safe_extract_tar(path, destination)
    except tarfile.TarError:
        pass
    return []


def _decode_text(path: Path, limit: int = 2_000_000) -> str | None:
    if path.stat().st_size > limit:
        return None
    raw = path.read_bytes()
    for encoding in ("utf-8-sig", "utf-8", "cp932", "latin-1"):
        try:
            return raw.decode(encoding)
        except UnicodeDecodeError:
            continue
    return None


def _tabular_summary(path: Path, text: str) -> dict[str, Any]:
    sample = "\n".join(text.splitlines()[:20])
    suffix = path.suffix.lower()
    delimiter = "\t" if suffix == ".tsv" else ","
    if suffix == ".txt":
        candidates = [",", "\t", ";"]
        counts = {candidate: sample.count(candidate) for candidate in candidates}
        delimiter = max(counts, key=counts.get)
    rows = list(csv.reader(io.StringIO(text), delimiter=delimiter))
    header = rows[0] if rows else []
    return {
        "delimiter": "tab" if delimiter == "\t" else delimiter,
        "header": [value.strip() for value in header[:100]],
        "line_count": len(text.splitlines()),
        "row_count_excluding_header": max(0, len(rows) - 1),
    }


def _r_hints(text: str) -> dict[str, list[str]]:
    lines = text.splitlines()
    io_patterns = (
        r"read\.(?:csv|table|delim)\s*\([^\n]+",
        r"readRDS\s*\([^\n]+",
        r"load\s*\([^\n]+",
        r"write\.(?:csv|table)\s*\([^\n]+",
    )
    model_patterns = (
        r"glmmTMB\s*\([^\n]+",
        r"(?:lmer|glmer|lm|glm)\s*\([^\n]+",
        r"dredge\s*\([^\n]+",
        r"model\.sel\s*\([^\n]+",
    )
    io_hits: list[str] = []
    model_hits: list[str] = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("#"):
            continue
        for pattern in io_patterns:
            if re.search(pattern, stripped):
                io_hits.append(stripped[:500])
                break
        for pattern in model_patterns:
            if re.search(pattern, stripped):
                model_hits.append(stripped[:500])
                break
    return {"io_calls": io_hits[:100], "model_calls": model_hits[:100]}


def _inventory_file(path: Path, base: Path) -> dict[str, Any]:
    rel = path.relative_to(base).as_posix()
    record: dict[str, Any] = {
        "path": rel,
        "size": path.stat().st_size,
        "suffix": path.suffix,
        "sha256": _sha256(path),
    }
    text = _decode_text(path)
    if text is not None and path.suffix.lower() in {".csv", ".tsv", ".txt"}:
        try:
            record["tabular"] = _tabular_summary(path, text)
        except Exception as exc:  # discovery must retain failures, not hide the file
            record["tabular_error"] = f"{type(exc).__name__}: {exc}"
    if text is not None and path.suffix.lower() == ".r":
        record["r_hints"] = _r_hints(text)
    return record


def run(output_root: Path, manifest_path: Path) -> dict[str, Any]:
    metadata = _request_json(API_URL)
    output_root.mkdir(parents=True, exist_ok=True)
    downloads = output_root / "downloads"
    extracted_root = output_root / "extracted"
    downloads.mkdir(exist_ok=True)
    extracted_root.mkdir(exist_ok=True)

    source_files: list[dict[str, Any]] = []
    extraction_records: list[dict[str, Any]] = []
    for item in metadata.get("files", []):
        destination = downloads / item["name"]
        _download(item["download_url"], destination)
        actual_md5 = _md5(destination)
        expected_md5 = item.get("supplied_md5") or item.get("computed_md5")
        size_ok = destination.stat().st_size == int(item.get("size", destination.stat().st_size))
        md5_ok = expected_md5 in (None, "", actual_md5)
        if not size_ok or not md5_ok:
            raise RuntimeError(
                f"download verification failed for {item['name']}: size_ok={size_ok}, md5_ok={md5_ok}"
            )
        source_files.append(
            {
                "id": item.get("id"),
                "name": item["name"],
                "size": destination.stat().st_size,
                "md5": actual_md5,
                "sha256": _sha256(destination),
                "download_url": item.get("download_url"),
            }
        )
        extract_dir = extracted_root / destination.stem
        members = _extract_archive(destination, extract_dir)
        if members:
            extraction_records.append({"source": item["name"], "members": members})

    inventory: list[dict[str, Any]] = []
    for root in (downloads, extracted_root):
        for path in sorted(p for p in root.rglob("*") if p.is_file()):
            inventory.append(_inventory_file(path, output_root))

    structured = [
        record
        for record in inventory
        if "tabular" in record or "r_hints" in record or record["suffix"].lower() in {".rds", ".rdata", ".rda"}
    ]
    manifest = {
        "status": "public_figshare_archive_discovered",
        "article_id": ARTICLE_ID,
        "article_version": ARTICLE_VERSION,
        "resource_doi": RESOURCE_DOI,
        "api_url": API_URL,
        "title": metadata.get("title"),
        "published_date": metadata.get("published_date"),
        "modified_date": metadata.get("modified_date"),
        "source_files": source_files,
        "extractions": extraction_records,
        "inventory": inventory,
        "structured_candidates": structured,
        "analysis_boundary": (
            "Discovery only. No biological claim is made until the archived schema and original analysis code are inspected "
            "and a prospective held-out residual-origin comparison is declared."
        ),
    }
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-root", type=Path, default=Path("_external/e1_izu_figshare"))
    parser.add_argument(
        "--manifest",
        type=Path,
        default=Path("artifacts/empirical/e1_figshare_discovery.json"),
    )
    args = parser.parse_args()
    manifest = run(args.output_root, args.manifest)
    print(json.dumps({
        "status": manifest["status"],
        "title": manifest["title"],
        "source_file_count": len(manifest["source_files"]),
        "inventory_count": len(manifest["inventory"]),
        "structured_candidate_count": len(manifest["structured_candidates"]),
        "manifest": str(args.manifest),
    }, indent=2))


if __name__ == "__main__":
    main()
