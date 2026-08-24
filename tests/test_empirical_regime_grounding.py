from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = (ROOT / "manuscript" / "empirical_regime_candidates.md").read_text(encoding="utf-8")


def test_registry_uses_real_ecosystems_not_habitat_labels_as_regimes() -> None:
    for system in (
        "Crepis sancta",
        "Camellia japonica",
        "Izu coastal",
        "Penstemon hirsutus",
        "Conospermum undulatum",
        "Primula elatior",
    ):
        assert system in REGISTRY
    assert "candidate regimes, not established universal classes" in REGISTRY
    assert "origin/history no longer improves prediction" in REGISTRY


def test_empirical_state_retains_processes_and_joint_alignment() -> None:
    for label in (
        "demographic support",
        "realised interaction support",
        "genetic and mating state",
        "process-specific connectivity",
        "alternative functional routes",
        "realised ecological function",
        "plausible ecological memory",
        "joint spatial alignment",
    ):
        assert label in REGISTRY
    assert "A_IG = cor_w(I_i, G_i)" in REGISTRY
    assert "not assumed sufficient statistics" in REGISTRY


def test_registry_distinguishes_existing_data_from_missing_measurements() -> None:
    assert "Immediate analyses possible with existing open data" in REGISTRY
    for analysis in ("E1", "E2", "E3", "E4"):
        assert analysis in REGISTRY
    assert "Best next addition" in REGISTRY
    assert "without matched genetics" in REGISTRY
    assert "Do **not** pool incompatible populations or years" in REGISTRY


def test_convergence_is_future_predictive_not_city_vs_island() -> None:
    assert "The goal is not to label habitats as `urban`, `island` or `fragmented`" in REGISTRY
    assert "future-relevant ecological state" in REGISTRY
    assert "smallest measured joint state" in REGISTRY
