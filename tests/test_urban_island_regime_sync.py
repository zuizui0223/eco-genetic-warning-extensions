from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEXT = (ROOT / "manuscript" / "urban_island_regime_tests.md").read_text(encoding="utf-8")


def test_connectivity_story_is_phase_u_rst_current():
    assert "did not reproduce" in TEXT
    assert "Phase U" in TEXT
    assert "Phase R" in TEXT
    assert "Phase S" in TEXT
    assert "Phase T" in TEXT
    assert "no robust portable connectivity heterogeneity effect" in TEXT
    assert "m=0–0.05` retained R4-highrep" not in TEXT
    assert "m=0.10–0.20` produced R3-highrep" not in TEXT


def test_cross_system_claim_is_prospective_and_state_conditional():
    assert "contrasting causal routes" in TEXT
    assert "future-relevant joint functional state" in TEXT
    assert "origin and fragmentation history no longer add predictive information" in TEXT
    assert "does not" in TEXT.lower()


def test_regime_definition_retains_joint_spatial_alignment():
    assert "joint spatial alignment" in TEXT
    assert "coarse-state insufficiency" in TEXT.lower()
    assert "H_alpha" in TEXT
    assert "H_gamma" in TEXT
    assert "F_ST" in TEXT
