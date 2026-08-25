from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import zipfile
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen

DATASETS = (
    (
        "pollinator_availability",
        "10.5285/01906784-6742-44bf-b244-a4b63bed8d82",
        "01906784-6742-44bf-b244-a4b63bed8d82",
    ),
    (
        "seed_function_supplemented_exposed",
        "10.5285/8caf2d8a-564d-4f2e-a797-174165a83796",
        "8caf2d8a-564d-4f2e-a797-174165a83796",
    ),
    (
        "seed_function_exposed_excluded",
        "10.5285/5b400b69-b828-45e8-b04e-7ccbfdb0987f",
        "5b400b69-b828-45e8-b04e-7ccbfdb0987f",
    ),
    (
        "paternity",
        "10.5285/7b721c07-bc38-4815-8669-4675867663d0",
        "7b721c07-bc38-4815-8669-4675867663d0",
    ),
)
DATA_ROOT = "https://data-package.ceh.ac.uk/data"
USER_AGENT = "eco-genetic-warning-extensions/1.0"


class _LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.targets: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for key, value in attrs:
            if key.lower() in {"href", "action"} and value:
                self.targets.append(value)


def _request(url: str) -> tuple[str, bytes]:
    request = Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "application/zip,text/csv,application/octet-stream,text/html,*/*",
        },
    )
    with urlopen(request, timeout=180) as response:
        content_type = str(response.headers.get("Content-Type", ""))
        payload = response.read()
    return content_type, payload


def _looks_like_csv(content_type: str, payload: bytes) -> bool:
    if "csv" in content_type.lower():
        return True
    lines = payload.splitlines()
    if not lines:
        return False
    first = lines[0]
    return b"," in first or b"\t" in first


def _candidate_links(landing_url: str, html_payload: bytes, uuid: str) -> list[str]:
    parser = _LinkParser()
    parser.feed(html_payload.decode("utf-8", errors="replace"))

    # NERC-CEH catalogue's own download-service tests use the canonical
    # downloadable-package form `https://data-package.ceh.ac.uk/data/<id>.zip`.
    # Add this metadata-defined route prospectively alongside every relevant
    # href/action exposed by the landing HTML.
    out: set[str] = {f"{DATA_ROOT}/{uuid}.zip"}

    for target in parser.targets:
        url = urljoin(landing_url, target)
        parsed = urlparse(url)
        host = parsed.netloc.lower()
        path_lower = parsed.path.lower()
        if parsed.scheme != "https" or not host.endswith("ceh.ac.uk"):
            continue
        if url.rstrip("/") == landing_url.rstrip("/"):
            continue
        # Access-route selection is based only on URL/link structure. Every
        # same-EIDC candidate that looks like a data/download route is fetched;
        # no candidate is selected from file contents or outcome values.
        if (
            uuid.lower() in url.lower()
            or path_lower.endswith((".csv", ".zip"))
            or "/download" in path_lower
            or "/data/" in path_lower
        ):
            out.add(url)
    return sorted(out)


def _csv_header(payload: bytes) -> list[str]:
    text = payload.decode("utf-8-sig")
    reader = csv.reader(io.StringIO(text))
    try:
        header = next(reader)
    except StopIteration as exc:
        raise RuntimeError("CSV payload has no header row") from exc
    return [str(value) for value in header]


def _archive_schema(payload: bytes) -> list[dict[str, object]]:
    buffer = io.BytesIO(payload)
    if not zipfile.is_zipfile(buffer):
        raise RuntimeError("payload is not a ZIP archive")
    members: list[dict[str, object]] = []
    with zipfile.ZipFile(buffer) as archive:
        for info in archive.infolist():
            if info.is_dir():
                continue
            row: dict[str, object] = {
                "member_name": info.filename,
                "member_bytes": int(info.file_size),
                "member_compressed_bytes": int(info.compress_size),
            }
            if info.filename.lower().endswith(".csv"):
                raw = archive.read(info)
                row["sha256"] = hashlib.sha256(raw).hexdigest()
                row["columns"] = _csv_header(raw)
            members.append(row)
    return members


def _payload_schema(url: str, content_type: str, payload: bytes) -> dict[str, object] | None:
    package_sha = hashlib.sha256(payload).hexdigest()
    buffer = io.BytesIO(payload)
    if zipfile.is_zipfile(buffer):
        return {
            "resolved_url": url,
            "content_type": content_type,
            "response_kind": "zip",
            "package_bytes": len(payload),
            "package_sha256": package_sha,
            "members": _archive_schema(payload),
        }
    if _looks_like_csv(content_type, payload):
        return {
            "resolved_url": url,
            "content_type": content_type,
            "response_kind": "direct_csv",
            "package_bytes": len(payload),
            "package_sha256": package_sha,
            "members": [
                {
                    "member_name": Path(urlparse(url).path).name or "direct_response.csv",
                    "member_bytes": len(payload),
                    "sha256": package_sha,
                    "columns": _csv_header(payload),
                }
            ],
        }
    return None


def _resolve_dataset(uuid: str) -> tuple[str, str, int, str, list[dict[str, object]], list[str]]:
    landing_url = f"{DATA_ROOT}/{uuid}"
    landing_type, landing_payload = _request(landing_url)
    direct = _payload_schema(landing_url, landing_type, landing_payload)
    if direct is not None:
        return (
            landing_url,
            landing_type,
            len(landing_payload),
            hashlib.sha256(landing_payload).hexdigest(),
            [direct],
            [],
        )

    if "html" not in landing_type.lower():
        raise RuntimeError(
            f"unexpected EIDC landing response: content_type={landing_type!r}, bytes={len(landing_payload)}"
        )

    candidates = _candidate_links(landing_url, landing_payload, uuid)
    resolved_payloads: list[dict[str, object]] = []
    attempted: list[str] = []
    for url in candidates:
        attempted.append(url)
        try:
            content_type, payload = _request(url)
        except Exception:
            continue
        schema = _payload_schema(url, content_type, payload)
        if schema is not None:
            resolved_payloads.append(schema)

    if not resolved_payloads:
        raise RuntimeError(
            "EIDC landing/package candidates yielded no verifiable ZIP/CSV payload; "
            f"uuid={uuid}, candidates={attempted!r}"
        )

    return (
        landing_url,
        landing_type,
        len(landing_payload),
        hashlib.sha256(landing_payload).hexdigest(),
        resolved_payloads,
        attempted,
    )


def discover(manifest_path: Path) -> dict[str, object]:
    datasets: list[dict[str, object]] = []
    for role, doi, uuid in DATASETS:
        landing_url, landing_type, landing_bytes, landing_sha, payloads, attempted = _resolve_dataset(uuid)
        datasets.append(
            {
                "role": role,
                "doi": doi,
                "uuid": uuid,
                "landing_url": landing_url,
                "landing_content_type": landing_type,
                "landing_bytes": landing_bytes,
                "landing_sha256": landing_sha,
                "access_candidates_attempted": attempted,
                "payloads": payloads,
            }
        )

    result: dict[str, object] = {
        "status": "schema_only_discovery_complete",
        "datasets": datasets,
        "inspection_boundary": (
            "Only EIDC landing-link attributes, package/file identifiers, byte hashes/sizes, archive member names and CSV header labels were inspected. "
            "No data rows, outcome values, descriptive outcome statistics, correlations, model fits, p-values or effect directions were read or computed."
        ),
        "next_gate": (
            "Using schema/header names only, map block/array/plant/habitat keys and I/T/F_seed/R/G_mating-C roles; "
            "classify joint_state_identifiable, partial_joint_state_identifiable, or not_identifiable_from_archive. "
            "If analysis is identifiable, commit a second exact-model preregistration before reading outcome rows."
        ),
    }
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--manifest",
        default="artifacts/empirical/eschscholzia_joint_state_schema.json",
    )
    args = parser.parse_args()
    result = discover(Path(args.manifest))
    print(
        json.dumps(
            {
                "status": result["status"],
                "datasets": {
                    row["role"]: [
                        {
                            "kind": payload["response_kind"],
                            "url": payload["resolved_url"],
                            "members": [m["member_name"] for m in payload["members"]],
                        }
                        for payload in row["payloads"]
                    ]
                    for row in result["datasets"]
                },
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
