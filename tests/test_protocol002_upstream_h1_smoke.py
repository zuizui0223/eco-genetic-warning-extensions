from pathlib import Path

import pytest

from eco_genetic_warning_extensions.protocol002_stage0 import UPSTREAM_COMMIT, UPSTREAM_REPOSITORY
from eco_genetic_warning_extensions.protocol002_upstream_h1_smoke import (
    UPSTREAM_H1_MODULE,
    UPSTREAM_MUTATION_MODULE,
    run_upstream_h1_sym_smoke,
)


def test_upstream_h1_smoke_contract_is_pinned() -> None:
    assert UPSTREAM_REPOSITORY == "zuizui0223/eco-genetic-criticality"
    assert UPSTREAM_COMMIT == "dd8ee379d0d3518194c767d16402042525bc00dc"
    assert UPSTREAM_H1_MODULE == "causal_model.finite_h1_boundary_resolution_audit"
    assert UPSTREAM_MUTATION_MODULE == "causal_model.symmetric_allele_mutation_closure"


def test_upstream_h1_smoke_rejects_missing_checkout(tmp_path: Path) -> None:
    missing = tmp_path / "missing-upstream"
    with pytest.raises(FileNotFoundError, match="upstream checkout"):
        run_upstream_h1_sym_smoke(missing)


def test_upstream_h1_smoke_validates_symmetric_mutation_rate(tmp_path: Path) -> None:
    checkout = tmp_path / "upstream"
    checkout.mkdir()
    with pytest.raises(ValueError, match=r"\[0, 0.5\)"):
        run_upstream_h1_sym_smoke(checkout, symmetric_mutation_rate=0.5)
