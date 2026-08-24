from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CREPIS = (ROOT / "manuscript" / "empirical_e3_crepis_audit.md").read_text(encoding="utf-8")
MIYAKE = (ROOT / "manuscript" / "empirical_e4_miyake_audit.md").read_text(encoding="utf-8")
CONOSPERMUM = (ROOT / "manuscript" / "empirical_e5_conospermum_audit.md").read_text(encoding="utf-8")
CROSSWALK = (ROOT / "manuscript" / "empirical_measurement_crosswalk.md").read_text(encoding="utf-8")


def test_crepis_anchor_is_quantitative_and_not_an_urban_label() -> None:
    for phrase in (
        "10% at low flowering-plant density",
        "80% at high density",
        "20% at low density to 80%",
        "12.6 m in JC",
        "1.53 m in HM",
        "interaction-limited local fragmentation",
        "Nonzero movement did not imply maintenance of local pollination function",
    ):
        assert phrase in CREPIS
    assert "not a synchronized refit" in CREPIS
    assert "must **not** be concatenated row-wise" in CREPIS


def test_miyake_anchor_is_compensation_not_island_effect() -> None:
    for phrase in (
        "21 flowers ha⁻¹",
        "2,544 flowers ha⁻¹",
        "83%",
        "26–45%",
        "0.26 ha",
        "1.97 ha",
        "0 to 33.8%",
        "0.62 to 0.96",
        "movement-compensated local fragmentation",
        "This is a **compensation state**, not an island state",
    ):
        assert phrase in MIYAKE
    assert "must not be collapsed into the simulator's allele-frequency `migration_rate`" in MIYAKE


def test_anchor_pair_establishes_opposite_natural_routes() -> None:
    assert "D↓ -> I↓ -> F↓" in MIYAKE
    assert "D↓ -> C_partner/C_pollen↑" in MIYAKE
    assert "local density/resource support cannot be the functional-fragmentation regime by itself" in MIYAKE


def test_conospermum_anchor_preserves_cohort_history_lag() -> None:
    for phrase in (
        "35% to <20%",
        "880 to 5 plants",
        "6% to 3%",
        "strictly self-incompatible",
        "near-complete to complete loss of inter-fragment pollen immigration",
        "cohort/history-lag functional fragmentation",
        "G_adult legacy",
        "C_pollen current ↓",
    ):
        assert phrase in CONOSPERMUM
    assert "adult neutral genetic state is partly a memory variable" in CONOSPERMUM
    assert "cohort identity and habitat history belong in the empirical state" in CONOSPERMUM


def test_crosswalk_preserves_measurement_synchronization() -> None:
    for code in ("`D`", "`I`", "`T`", "`C`", "`R`", "`G`", "`F`", "`M`", "`A`"):
        assert code in CROSSWALK
    assert "Only the second supports a strict empirical state-sufficiency test" in CROSSWALK
    assert "Near-complete programme, not synchronized" in CROSSWALK
    assert "Near-complete compensation system" in CROSSWALK
    assert "smallest sufficient measured state" in CROSSWALK


def test_cross_system_regime_is_predictive_equivalence() -> None:
    assert "future functional trajectory ⟂ fragmentation origin/history" in CROSSWALK
    assert "Low local resource density plus stable function without a measured compensation process is not enough" in CROSSWALK
    assert "Any coordinate can be removed only if predictive sufficiency survives its removal" in CROSSWALK
