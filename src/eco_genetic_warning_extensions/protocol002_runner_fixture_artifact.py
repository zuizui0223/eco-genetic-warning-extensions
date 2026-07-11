"""Artifact writer for the deterministic Protocol 002 source-runner fixture."""
from __future__ import annotations

import json
from pathlib import Path

from .protocol002_source_runner import deterministic_fixture_source_artifact

DEFAULT_RUNNER_FIXTURE_PATH = Path("artifacts/protocol002/source_runner_fixture.json")


def write_runner_fixture_artifact(path: str | Path = DEFAULT_RUNNER_FIXTURE_PATH) -> Path:
    """Write the deterministic five-status source-runner fixture artifact."""
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(
        json.dumps(deterministic_fixture_source_artifact(), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return destination
