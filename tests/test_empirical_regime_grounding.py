from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = (ROOT / "manuscript" / "empirical_regime_candidates.md").read_text(encoding="utf-8")
MAIN = (ROOT / "manuscript" / "main_text.md").read_text(encoding="utf-8")
REFERENCES = (ROOT / "manuscript" / "references.md").read_text(encoding="utf-8")


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


def test_main_discussion_uses_measured_ecosystems_as_mechanistic_examples() -> None:
    assert "Different fragmentation routes can converge only through a common measured state" in MAIN
    for system in ("Crepis sancta", "Camellia japonica", "Honshu–Izu", "Spondias purpurea"):
        assert system in MAIN
    assert "Miyake-jima" in MAIN
    assert "partner and pollen movement" in MAIN
    assert "cross-layer spatial alignment" in MAIN
    assert "A residual origin effect is evidence to search for a missing process" in MAIN
    assert "habitat label itself is the mechanistic state" in MAIN


def test_empirical_main_text_citations_are_in_reference_ledger() -> None:
    for token in (
        "Abe, H.",
        "Cheptou, P.-O.",
        "Dornier, A.",
        "Hiraiwa, M.K.",
        "10.1371/journal.pone.0062696",
        "10.1111/j.1469-8137.2006.01880.x",
        "10.1038/hdy.2013.3",
    ):
        assert token in REFERENCES
