from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _load_validator():
    path = ROOT / "scripts" / "validate_publication_lanes.py"
    spec = importlib.util.spec_from_file_location("publication_lanes", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_publication_lanes_are_disjoint_and_fail_closed() -> None:
    assert _load_validator().main() == 0
