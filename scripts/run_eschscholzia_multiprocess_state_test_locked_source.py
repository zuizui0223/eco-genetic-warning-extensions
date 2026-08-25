from __future__ import annotations

import argparse
import hashlib
import importlib.util
import io
import json
import sys
import zipfile
from pathlib import Path
from urllib.request import Request, urlopen

BASE_PATH = Path(__file__).with_name("run_eschscholzia_multiprocess_state_test.py")
spec = importlib.util.spec_from_file_location("esch_base", BASE_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError("could not load locked Eschscholzia analysis module")
base = importlib.util.module_from_spec(spec)
# dataclasses resolves annotation/module metadata through sys.modules while the
# module body executes. Register the module before exec_module; this is a pure
# loader fix and does not modify any preregistered scientific logic.
sys.modules[spec.name] = base
spec.loader.exec_module(base)


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _download_source_member_locked(source: dict[str, str]):
    """Correct only the unstable transport-wrapper lock.

    The EIDC ZIP can be regenerated. Source identity is DOI/UUID + exact member
    path + locked CSV SHA-256. No model, endpoint, key, seed, validation unit or
    decision logic is changed here.
    """
    url = f"{base.DATA_ROOT}/{source['uuid']}.zip"
    req = Request(url, headers={"User-Agent": base.USER_AGENT, "Accept": "application/zip,*/*"})
    with urlopen(req, timeout=180) as response:
        package = response.read()
    package_sha = _sha256(package)
    with zipfile.ZipFile(io.BytesIO(package)) as archive:
        try:
            raw = archive.read(source["member"])
        except KeyError as exc:
            raise RuntimeError(f"locked CSV member absent: {source['member']}") from exc
    observed_csv = _sha256(raw)
    if observed_csv != source["csv_sha256"]:
        raise RuntimeError(
            f"CSV SHA mismatch for {source['doi']}: expected={source['csv_sha256']} observed={observed_csv}; "
            f"transport_package_sha={package_sha}"
        )
    return package, raw, url


# Monkeypatch only the access/source-identity function. All scientific logic is
# executed from the preregistered base module unchanged.
base._download_source = _download_source_member_locked


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="artifacts/empirical/eschscholzia_multiprocess_state_result.json")
    args = parser.parse_args()
    result = base.run()
    result["source_lock_correction"] = {
        "outer_zip_sha_policy": "record_only_not_identity",
        "identity": "EIDC DOI/UUID + exact CSV member path + locked CSV-member SHA-256",
        "correction_note": "manuscript/empirical_eschscholzia_source_lock_correction.md",
    }
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "decision": result.get("decision"),
                "primary_endpoint_decisions": result.get("primary_endpoint_decisions"),
                "F_process": result.get("F_seed", {}).get("comparisons", {}).get("S0_to_S1"),
                "F_habitat": result.get("F_seed", {}).get("comparisons", {}).get("S1_to_S2"),
                "G_process": result.get("G_mating", {}).get("comparisons", {}).get("S0_to_S1"),
                "G_habitat": result.get("G_mating", {}).get("comparisons", {}).get("S1_to_S2"),
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
