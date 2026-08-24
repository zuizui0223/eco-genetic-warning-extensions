from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urljoin
from urllib.request import Request, urlopen

DOI = "10.5061/dryad.d51c59zzj"
DRYAD_ROOT = "https://datadryad.org"
API_ROOT = f"{DRYAD_ROOT}/api/v2"


def _absolute(url: str) -> str:
    return urljoin(DRYAD_ROOT, url)


def _request(url: str) -> Request:
    return Request(
        _absolute(url),
        headers={
            "User-Agent": "eco-genetic-warning-extensions/1.0",
            "Accept": "*/*",
        },
    )


def _json(url: str) -> dict:
    with urlopen(_request(url), timeout=60) as response:
        return json.load(response)


def _bytes(url: str) -> bytes:
    with urlopen(_request(url), timeout=120) as response:
        return response.read()


def _href(obj: dict, relation: str) -> str | None:
    links = obj.get("_links", {})
    value = links.get(relation)
    if isinstance(value, dict):
        href = value.get("href")
        return _absolute(str(href)) if href else None
    return None


def _public_file_bytes(file_id: int) -> tuple[bytes, str]:
    """Download public bytes from Dryad's landing-page file stream.

    Dryad's REST metadata endpoints are anonymously readable for published data,
    while `/api/v2/files/{id}/download` currently requires bearer auth. The
    public landing page exposes the same published file through file_stream.
    Both observed public route shapes are tried without credentials; this does
    not change the locked DOI, file id, or preregistered analysis.
    """
    candidates = (
        f"{DRYAD_ROOT}/stash/downloads/file_stream/{file_id}",
        f"{DRYAD_ROOT}/downloads/file_stream/{file_id}",
    )
    failures: list[str] = []
    for url in candidates:
        try:
            return _bytes(url), url
        except (HTTPError, URLError) as exc:
            failures.append(f"{url}: {exc!r}")
    raise RuntimeError("public Dryad file stream failed; " + " | ".join(failures))


def discover(output_root: Path, manifest_path: Path) -> dict:
    # Dryad expects the entire `doi:<DOI>` path segment URL-encoded, including `/`.
    dataset_key = quote(f"doi:{DOI}", safe="")
    dataset_url = f"{API_ROOT}/datasets/{dataset_key}"
    dataset = _json(dataset_url)

    version_url = _href(dataset, "stash:version") or _href(dataset, "version")
    if version_url is None:
        version_id = dataset.get("_embedded", {}).get("stash:versions", [{}])[0].get("id")
        if version_id is None:
            version_id = dataset.get("version") or dataset.get("id")
        if version_id is None:
            raise RuntimeError(f"could not resolve Dryad version from {dataset_url}")
        version_url = f"{API_ROOT}/versions/{version_id}"
    version = _json(version_url)

    files_url = _href(version, "stash:files") or _href(version, "files")
    if files_url is None:
        version_id = version.get("id")
        if version_id is None:
            raise RuntimeError("Dryad version did not expose file relation or id")
        files_url = f"{API_ROOT}/versions/{version_id}/files"
    files_page = _json(files_url)
    files = files_page.get("_embedded", {}).get("stash:files", files_page.get("files", []))
    if not files:
        raise RuntimeError("Dryad dataset returned no files")

    downloads = output_root / "downloads"
    downloads.mkdir(parents=True, exist_ok=True)
    source_files = []
    inventory = []

    for item in files:
        file_id = item.get("id")
        if file_id is None:
            raise RuntimeError(f"Dryad file metadata has no id: {item!r}")
        file_id = int(file_id)
        name = str(item.get("path") or item.get("name") or f"dryad_file_{file_id}")
        api_download_url = _href(item, "stash:download") or _href(item, "download")
        if api_download_url is None:
            api_download_url = f"{API_ROOT}/files/{file_id}/download"

        # Do not call the authenticated API download endpoint. Resolve the
        # exact file id from public metadata, then fetch the public file stream.
        payload, public_download_url = _public_file_bytes(file_id)
        target = downloads / Path(name).name
        target.write_bytes(payload)
        digest = hashlib.sha256(payload).hexdigest()
        source_files.append({
            "id": file_id,
            "name": target.name,
            "size": len(payload),
            "sha256": digest,
            "metadata_api_download_url": _absolute(api_download_url),
            "public_download_url": public_download_url,
        })
        inventory.append({"path": str(target.relative_to(output_root)), "size": len(payload), "sha256": digest})

    # Structured inventory is descriptive only and does not alter the preregistered model set.
    try:
        import pandas as pd
        for row in inventory:
            path = output_root / row["path"]
            if path.suffix.lower() in {".xlsx", ".xls"}:
                workbook = pd.ExcelFile(path)
                row["workbook"] = {"sheet_names": list(workbook.sheet_names), "sheets": {}}
                for sheet in workbook.sheet_names:
                    frame = pd.read_excel(path, sheet_name=sheet)
                    row["workbook"]["sheets"][sheet] = {
                        "rows": int(len(frame)),
                        "columns": [str(c) for c in frame.columns],
                    }
    except Exception as exc:  # preserve the locked bytes even if workbook inspection itself fails
        inventory.append({"structured_inventory_error": repr(exc)})

    result = {
        "status": "public_dryad_archive_discovered",
        "resource_doi": DOI,
        "dataset_api_url": dataset_url,
        "version_api_url": _absolute(version_url),
        "title": dataset.get("title") or version.get("title"),
        "source_files": source_files,
        "inventory": inventory,
        "analysis_boundary": (
            "Discovery only. No residual-context result is interpreted until the locked workbook schema is mapped "
            "to the preregistered E3 process/context model sequence."
        ),
    }
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-root", default="_external/e3_norway_dryad")
    parser.add_argument("--manifest", default="artifacts/empirical/e3_norway_dryad_discovery.json")
    args = parser.parse_args()
    result = discover(Path(args.output_root), Path(args.manifest))
    print(json.dumps({"doi": result["resource_doi"], "files": [f["name"] for f in result["source_files"]]}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
