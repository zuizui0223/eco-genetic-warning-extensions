from __future__ import annotations

import argparse
import hashlib
import json
import platform
import shutil
import subprocess
from pathlib import Path


def _git(repo: Path, *args: str) -> str:
    return subprocess.run(
        ["git", "-C", str(repo), *args],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


def _copy_required(source: Path, destination: Path, relative_paths: tuple[str, ...]) -> None:
    for relative in relative_paths:
        src = source / relative
        if not src.exists():
            raise FileNotFoundError(src)
        dst = destination / relative
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)


def _rewrite_manifest(bundle: Path) -> None:
    manifest_path = bundle / "manifest.json"
    if manifest_path.exists():
        manifest_path.unlink()
    files: dict[str, str] = {}
    for path in sorted(item for item in bundle.rglob("*") if item.is_file()):
        files[str(path.relative_to(bundle))] = hashlib.sha256(path.read_bytes()).hexdigest()
    manifest_path.write_text(
        json.dumps({"algorithm": "sha256", "files": files}, indent=2, sort_keys=True)
        + "\n",
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Add both software packages and provenance records to a submission bundle."
    )
    parser.add_argument("--bundle", required=True)
    parser.add_argument("--extension-root", default=".")
    parser.add_argument("--upstream", required=True)
    parser.add_argument("--dist-root", required=True)
    args = parser.parse_args()

    bundle = Path(args.bundle).resolve()
    extension = Path(args.extension_root).resolve()
    upstream = Path(args.upstream).resolve()
    dist_root = Path(args.dist_root).resolve()

    if not bundle.is_dir():
        raise FileNotFoundError(bundle)

    software = bundle / "software"
    provenance = bundle / "provenance"
    software.mkdir(parents=True, exist_ok=True)
    provenance.mkdir(parents=True, exist_ok=True)

    for role in ("parent", "extension"):
        source = dist_root / role
        if not source.is_dir():
            raise FileNotFoundError(source)
        destination = software / role
        destination.mkdir(parents=True, exist_ok=True)
        distributions = sorted(path for path in source.iterdir() if path.is_file())
        if not distributions:
            raise RuntimeError(f"no distributions found in {source}")
        for distribution in distributions:
            shutil.copy2(distribution, destination / distribution.name)

    _copy_required(
        upstream,
        provenance / "parent",
        (
            "README.md",
            "pyproject.toml",
            "docs/final_evidence_ledger.md",
            "docs/eco_genetic_hypothesis_program.md",
            "manuscript/claim_evidence_map.md",
        ),
    )
    _copy_required(
        extension,
        provenance / "extension",
        (
            "README.md",
            "REPRODUCIBILITY.md",
            "pyproject.toml",
            "reproducibility/upstream-lock.json",
            "manuscript/artifact_index.md",
            "manuscript/claim_evidence_map.md",
        ),
    )

    context = {
        "python": platform.python_version(),
        "extension_commit": _git(extension, "rev-parse", "HEAD"),
        "parent_commit": _git(upstream, "rev-parse", "HEAD"),
        "package_install_order": ["software/parent", "software/extension"],
        "scientific_boundary": (
            "The parent and extension are separate provenance units; "
            "the integrated bundle does not pool trajectories."
        ),
    }
    (provenance / "build_context.json").write_text(
        json.dumps(context, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    (software / "README.md").write_text(
        "# Bundled software\n\n"
        "Install the parent wheel first, followed by the extension wheel. The parent "
        "distribution was built from the exact scientific commit recorded in "
        "`../provenance/extension/reproducibility/upstream-lock.json`.\n\n"
        "```bash\n"
        "python -m venv .venv\n"
        "source .venv/bin/activate  # Windows: .venv\\Scripts\\activate\n"
        "python -m pip install --upgrade pip\n"
        "python -m pip install parent/*.whl\n"
        "python -m pip install extension/*.whl\n"
        "```\n\n"
        "The wheels provide the executable model and protocol code. Manuscript, "
        "evidence, workflow, and artifact provenance remain in the adjacent bundle "
        "directories.\n",
        encoding="utf-8",
    )

    _rewrite_manifest(bundle)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
