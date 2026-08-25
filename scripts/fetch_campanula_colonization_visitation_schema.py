from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
from pathlib import Path
from urllib.request import Request, urlopen

RECORD_ID = 10814705
FILES = (
    ("PLdataindividual.csv", "b84fa5c83513dbe75c0bf7840d1c74aa"),
    ("pollinator.csv", "81e0deaa78a6a97e1211484cb9d0d3b3"),
)
USER_AGENT = "eco-genetic-warning-extensions/1.0"


def _download(filename: str) -> tuple[str, bytes]:
    url = f"https://zenodo.org/records/{RECORD_ID}/files/{filename}?download=1"
    req = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "text/csv,*/*"})
    with urlopen(req, timeout=180) as response:
        payload = response.read()
    return url, payload


def _header(payload: bytes) -> list[str]:
    reader = csv.reader(io.StringIO(payload.decode("utf-8-sig")))
    try:
        return [str(x) for x in next(reader)]
    except StopIteration as exc:
        raise RuntimeError("CSV has no header") from exc


def discover(manifest_path: Path) -> dict:
    files = []
    for filename, expected_md5 in FILES:
        url, payload = _download(filename)
        observed_md5 = hashlib.md5(payload).hexdigest()  # archive publishes MD5
        if observed_md5 != expected_md5:
            raise RuntimeError(
                f"MD5 mismatch for {filename}: expected={expected_md5}, observed={observed_md5}"
            )
        files.append(
            {
                "filename": filename,
                "download_url": url,
                "bytes": len(payload),
                "md5": observed_md5,
                "sha256": hashlib.sha256(payload).hexdigest(),
                "columns": _header(payload),
            }
        )

    result = {
        "status": "schema_only_discovery_complete",
        "zenodo_record": RECORD_ID,
        "doi": "10.5281/zenodo.10814705",
        "files": files,
        "inspection_boundary": (
            "Only fixed-file byte hashes and CSV header labels were inspected. No data row, visitation summary, seed outcome, "
            "pollen-limitation calculation, effect direction, fitted model or p-value was read or computed."
        ),
        "next_gate": (
            "Apply the preregistered header-only identifiability rule. If identifiable or partial, commit a second exact-model "
            "preregistration before any row-level analysis."
        ),
    }
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", default="artifacts/empirical/campanula_colonization_visitation_schema.json")
    args = parser.parse_args()
    result = discover(Path(args.manifest))
    print(json.dumps({f["filename"]: f["columns"] for f in result["files"]}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
