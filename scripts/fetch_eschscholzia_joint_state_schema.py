from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import zipfile
from pathlib import Path
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


def _download(uuid: str) -> tuple[str, str, bytes]:
    url = f"{DATA_ROOT}/{uuid}"
    request = Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "application/zip,text/csv,application/octet-stream,*/*",
        },
    )
    with urlopen(request, timeout=180) as response:
        content_type = str(response.headers.get("Content-Type", ""))
        payload = response.read()
    return url, content_type, payload


def _csv_header(payload: bytes) -> list[str]:
    text = payload.decode("utf-8-sig")
    stream = io.StringIO(text)
    reader = csv.reader(stream)
    try:
        header = next(reader)
    except StopIteration as exc:
        raise RuntimeError("CSV payload has no header row") from exc
    return [str(value) for value in header]


def _archive_schema(payload: bytes) -> list[dict[str, object]]:
    buffer = io.BytesIO(payload)
    if not zipfile.is_zipfile(buffer):
        raise RuntimeError("payload is neither recognized ZIP nor direct CSV")
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


def _direct_schema(content_type: str, payload: bytes) -> list[dict[str, object]]:
    lowered = content_type.lower()
    if "csv" not in lowered:
        # Some package servers return octet-stream for CSV. Only accept it if
        # the first line parses as a non-trivial CSV header; do not inspect rows.
        first_line = payload.splitlines()[0] if payload.splitlines() else b""
        if b"," not in first_line and b"\t" not in first_line:
            raise RuntimeError(
                f"unexpected non-ZIP package response: content_type={content_type!r}, bytes={len(payload)}"
            )
    return [
        {
            "member_name": "direct_response.csv",
            "member_bytes": len(payload),
            "sha256": hashlib.sha256(payload).hexdigest(),
            "columns": _csv_header(payload),
        }
    ]


def discover(manifest_path: Path) -> dict[str, object]:
    datasets: list[dict[str, object]] = []
    for role, doi, uuid in DATASETS:
        url, content_type, payload = _download(uuid)
        package_sha = hashlib.sha256(payload).hexdigest()
        buffer = io.BytesIO(payload)
        if zipfile.is_zipfile(buffer):
            response_kind = "zip"
            members = _archive_schema(payload)
        else:
            response_kind = "direct_csv"
            members = _direct_schema(content_type, payload)

        datasets.append(
            {
                "role": role,
                "doi": doi,
                "uuid": uuid,
                "package_url": url,
                "content_type": content_type,
                "response_kind": response_kind,
                "package_bytes": len(payload),
                "package_sha256": package_sha,
                "members": members,
            }
        )

    result: dict[str, object] = {
        "status": "schema_only_discovery_complete",
        "datasets": datasets,
        "inspection_boundary": (
            "Only package/file identifiers, byte hashes/sizes, archive member names and CSV header labels were inspected. "
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
                "datasets": [
                    {
                        "role": row["role"],
                        "kind": row["response_kind"],
                        "members": [m["member_name"] for m in row["members"]],
                    }
                    for row in result["datasets"]
                ],
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
