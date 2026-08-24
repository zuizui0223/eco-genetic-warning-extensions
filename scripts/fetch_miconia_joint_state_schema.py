from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from urllib.request import Request, urlopen

import openpyxl

DOI = "10.5061/dryad.1cm80"
DRYAD_ROOT = "https://datadryad.org"
FILES = (
    (30526, "correlation_dbh_number of inflorescences.xlsx"),
    (30527, "genotypes_Miconia affinis.xlsx"),
    (30528, "pollen_dispersal_analysis_data.xlsx"),
    (30529, "seed_viability_analysis_data.xlsx"),
)


def _download(file_id: int) -> tuple[str, bytes]:
    url = f"{DRYAD_ROOT}/downloads/file_stream/{file_id}"
    request = Request(url, headers={"User-Agent": "eco-genetic-warning-extensions/1.0"})
    with urlopen(request, timeout=120) as response:
        payload = response.read()
    return url, payload


def _schema(path: Path) -> list[dict[str, object]]:
    workbook = openpyxl.load_workbook(path, read_only=False, data_only=False)
    sheets: list[dict[str, object]] = []
    for ws in workbook.worksheets:
        columns: list[str] = []
        if ws.max_row >= 1:
            for cell in ws[1]:
                value = cell.value
                columns.append("" if value is None else str(value))
        sheets.append(
            {
                "sheet": ws.title,
                "rows_including_header": int(ws.max_row),
                "data_rows": max(int(ws.max_row) - 1, 0),
                "columns_count": int(ws.max_column),
                "columns": columns,
            }
        )
    workbook.close()
    return sheets


def discover(output_dir: Path, manifest_path: Path) -> dict[str, object]:
    output_dir.mkdir(parents=True, exist_ok=True)
    inventory: list[dict[str, object]] = []
    for file_id, filename in FILES:
        url, payload = _download(file_id)
        target = output_dir / filename
        target.write_bytes(payload)
        inventory.append(
            {
                "file_stream_id": file_id,
                "filename": filename,
                "download_url": url,
                "bytes": len(payload),
                "sha256": hashlib.sha256(payload).hexdigest(),
                "workbook_schema": _schema(target),
            }
        )

    result: dict[str, object] = {
        "status": "schema_only_discovery_complete",
        "dataset_doi": DOI,
        "files": inventory,
        "inspection_boundary": (
            "Only workbook names, hashes, dimensions and first-row column labels were inspected. "
            "No data-cell values, outcome summaries, fitted models or effect directions were used."
        ),
        "next_gate": (
            "Map keys and source-defined process variables from schema only, classify joint_state_identifiable / "
            "partial_joint_state_identifiable / not_identifiable_from_archive, then preregister exact models before "
            "any outcome analysis."
        ),
    }
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default="_external/miconia_joint_state")
    parser.add_argument("--manifest", default="artifacts/empirical/miconia_joint_state_schema.json")
    args = parser.parse_args()
    result = discover(Path(args.output_dir), Path(args.manifest))
    print(json.dumps({"status": result["status"], "files": [f["filename"] for f in result["files"]]}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
