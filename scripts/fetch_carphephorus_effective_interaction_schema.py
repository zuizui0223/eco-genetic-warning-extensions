from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
from pathlib import Path
from urllib.parse import quote, urljoin
from urllib.request import Request, urlopen

DOI = "10.5061/dryad.w9ghx3g48"
DRYAD_ROOT = "https://datadryad.org"
API_ROOT = f"{DRYAD_ROOT}/api/v2"
AUTHOR_CODE_REPO = "hultingk/review-SRS-CARBEL"
AUTHOR_CODE_COMMIT = "622e5266db24e99a983bcf89d63a2258ebf93662"
FILES = (
    "CARBEL-arthropods.csv",
    "CARBEL-floral.csv",
    "CARBEL-seeds.csv",
    "Patch_type.csv",
)
USER_AGENT = "eco-genetic-warning-extensions/1.0"


def _request(url: str, accept: str) -> tuple[str, bytes]:
    req = Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": accept,
            "Referer": "https://datadryad.org/",
            "X-API-Version": "2.1.0",
        },
    )
    with urlopen(req, timeout=180) as response:
        return str(response.headers.get("Content-Type", "")), response.read()


def _json(url: str) -> dict:
    _, payload = _request(url, "application/json")
    return json.loads(payload.decode("utf-8"))


def _absolute(href: str) -> str:
    return urljoin(DRYAD_ROOT, href)


def _href(obj: dict, relation: str) -> str | None:
    value = obj.get("_links", {}).get(relation)
    if isinstance(value, dict) and value.get("href"):
        return _absolute(str(value["href"]))
    return None


def _file_id(item: dict) -> int | None:
    if item.get("id") is not None:
        return int(item["id"])
    self_href = _href(item, "self")
    if self_href:
        match = re.search(r"/files/(\d+)$", self_href)
        if match:
            return int(match.group(1))
    return None


def _digest_matches(item: dict, payload: bytes) -> tuple[str, str | None, bool | None]:
    observed_sha = hashlib.sha256(payload).hexdigest()
    expected = item.get("digest")
    digest_type = str(item.get("digestType") or "").lower()
    if not expected:
        return observed_sha, None, None
    expected_text = str(expected).lower().replace("sha256:", "")
    if "sha-256" in digest_type or "sha256" in digest_type or len(expected_text) == 64:
        return observed_sha, expected_text, observed_sha == expected_text
    return observed_sha, str(expected), None


def _resolve_files() -> tuple[str, str, list[dict]]:
    dataset_key = quote(f"doi:{DOI}", safe="")
    dataset_url = f"{API_ROOT}/datasets/{dataset_key}"
    dataset = _json(dataset_url)

    version_url = _href(dataset, "stash:version") or _href(dataset, "version")
    if version_url is None:
        versions = _json(f"{dataset_url}/versions")
        embedded = versions.get("_embedded", {}).get("stash:versions", [])
        if not embedded:
            raise RuntimeError("Dryad dataset exposed no public versions")
        version_url = _href(embedded[0], "self")
        if version_url is None and embedded[0].get("id") is not None:
            version_url = f"{API_ROOT}/versions/{embedded[0]['id']}"
    if version_url is None:
        raise RuntimeError("could not resolve Dryad version")

    version = _json(version_url)
    files_url = _href(version, "stash:files") or _href(version, "files")
    if files_url is None:
        version_id = version.get("id")
        if version_id is None:
            match = re.search(r"/versions/(\d+)$", version_url)
            version_id = int(match.group(1)) if match else None
        if version_id is None:
            raise RuntimeError("could not resolve Dryad version id")
        files_url = f"{API_ROOT}/versions/{version_id}/files"

    page = _json(files_url)
    items = page.get("_embedded", {}).get("stash:files", page.get("files", []))
    if not items:
        raise RuntimeError("Dryad public version returned no files")
    by_name = {str(item.get("path") or item.get("name") or ""): item for item in items}
    resolved = []
    for filename in FILES:
        item = by_name.get(filename)
        if item is None:
            raise RuntimeError(f"locked Carphephorus file absent: {filename}")
        file_id = _file_id(item)
        if file_id is None:
            raise RuntimeError(f"could not resolve file id: {filename}")
        resolved.append({"filename": filename, "file_id": file_id, "metadata": item})
    return dataset_url, files_url, resolved


def _download_verified(record: dict) -> dict:
    filename = record["filename"]
    file_id = int(record["file_id"])
    item = record["metadata"]
    candidates = []
    for relation in ("stash:download", "download"):
        href = _href(item, relation)
        if href:
            candidates.append(href)
    candidates.extend(
        [
            f"{DRYAD_ROOT}/stash/downloads/file_stream/{file_id}",
            f"{DRYAD_ROOT}/downloads/file_stream/{file_id}",
        ]
    )
    candidates = list(dict.fromkeys(candidates))
    errors: list[str] = []
    expected_size = item.get("size")

    for url in candidates:
        try:
            content_type, payload = _request(url, "text/csv,application/octet-stream,*/*")
        except Exception as exc:  # access diagnosis only
            errors.append(f"{url}: {type(exc).__name__}: {exc}")
            continue
        if expected_size is not None and int(expected_size) != len(payload):
            errors.append(f"{url}: size mismatch expected={expected_size} observed={len(payload)}")
            continue
        observed_sha, expected_digest, digest_match = _digest_matches(item, payload)
        if digest_match is False:
            errors.append(f"{url}: SHA-256 mismatch")
            continue
        first_line = payload.splitlines()[0] if payload.splitlines() else b""
        if b"," not in first_line and b"\t" not in first_line:
            errors.append(f"{url}: response is not a recognizable CSV header")
            continue
        reader = csv.reader(io.StringIO(payload.decode("utf-8-sig")))
        try:
            columns = [str(value) for value in next(reader)]
        except StopIteration as exc:
            raise RuntimeError(f"CSV has no header: {filename}") from exc
        return {
            "filename": filename,
            "file_id": file_id,
            "resolved_url": url,
            "content_type": content_type,
            "bytes": len(payload),
            "sha256": observed_sha,
            "metadata_digest": expected_digest,
            "metadata_digest_verified": digest_match,
            "columns": columns,
            "access_candidates_attempted": candidates,
        }

    raise RuntimeError(f"no verified public byte stream for {filename}: {errors!r}")


def discover(manifest_path: Path) -> dict:
    dataset_url, files_url, records = _resolve_files()
    files = [_download_verified(record) for record in records]
    result = {
        "status": "schema_only_discovery_complete",
        "dataset_doi": DOI,
        "author_code_repo": AUTHOR_CODE_REPO,
        "author_code_commit": AUTHOR_CODE_COMMIT,
        "dataset_metadata_url": dataset_url,
        "files_metadata_url": files_url,
        "files": files,
        "inspection_boundary": (
            "Only Dryad metadata/file identifiers, byte size/digest, CSV header labels, and the pinned author-code "
            "variable/join declarations were inspected. No data row, visitation summary, pollination outcome, effect direction, "
            "correlation, model fit, or p-value was read or computed."
        ),
        "next_gate": (
            "Apply the preregistered header-only identifiability rule. If realised_interaction_state_identifiable or partial, "
            "commit a second exact-model preregistration before any row-level analysis."
        ),
    }
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", default="artifacts/empirical/carphephorus_effective_interaction_schema.json")
    args = parser.parse_args()
    result = discover(Path(args.manifest))
    print(json.dumps({"status": result["status"], "files": {f["filename"]: f["columns"] for f in result["files"]}}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
