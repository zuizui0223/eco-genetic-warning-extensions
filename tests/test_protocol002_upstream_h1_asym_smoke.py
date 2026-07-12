from pathlib import Path
from types import SimpleNamespace

import pytest

from eco_genetic_warning_extensions.mutation_coordinates import MutationCoordinates
from eco_genetic_warning_extensions.protocol002_upstream_h1_asym_smoke import (
    patched_protocol002_mutation_runner,
    run_upstream_h1_asym_smoke,
)


class DummyPatch:
    def __init__(self) -> None:
        self.apply_symmetric_allele_mutation = lambda frequency, rate: rate + (1.0 - 2.0 * rate) * frequency
        self.entered_rate = None

    def patched_h1_mutation_runner(self, rate):
        self.entered_rate = rate
        module = self

        class Context:
            def __enter__(self):
                return None

            def __exit__(self, exc_type, exc, tb):
                return False

        return Context()


def test_protocol002_patch_replaces_only_mutation_transform_and_restores_it() -> None:
    module = DummyPatch()
    original = module.apply_symmetric_allele_mutation
    coordinate = MutationCoordinates(kappa_mu=0.20, p_star=0.75)
    with patched_protocol002_mutation_runner(module, coordinate):
        assert module.entered_rate == pytest.approx(0.10)
        assert module.apply_symmetric_allele_mutation(0.40, 0.10) == pytest.approx(coordinate.apply(0.40))
    assert module.apply_symmetric_allele_mutation is original


def test_protocol002_patch_rejects_zero_relaxation() -> None:
    module = DummyPatch()
    with pytest.raises(ValueError, match="0 < kappa_mu < 1"):
        with patched_protocol002_mutation_runner(module, MutationCoordinates(kappa_mu=0.0, p_star=0.75)):
            pass


def test_asymmetric_h1_smoke_rejects_symmetric_coordinate(tmp_path: Path) -> None:
    checkout = tmp_path / "upstream"
    checkout.mkdir()
    with pytest.raises(ValueError, match="p_star != 0.5"):
        run_upstream_h1_asym_smoke(
            checkout,
            coordinate=MutationCoordinates(kappa_mu=0.20, p_star=0.50),
        )


def test_asymmetric_h1_smoke_rejects_missing_checkout(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError, match="upstream checkout"):
        run_upstream_h1_asym_smoke(
            tmp_path / "missing",
            coordinate=MutationCoordinates(kappa_mu=0.20, p_star=0.75),
        )
