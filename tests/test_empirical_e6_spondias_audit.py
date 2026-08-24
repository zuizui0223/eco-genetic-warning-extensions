from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = (ROOT / "manuscript" / "empirical_e6_spondias_audit.md").read_text(encoding="utf-8")
CROSSWALK = (ROOT / "manuscript" / "empirical_measurement_crosswalk.md").read_text(encoding="utf-8")


def test_spondias_links_interaction_connectivity_function_and_genetics() -> None:
    for phrase in (
        "pollinator assemblage and visitation (`I`)",
        "realized pollen flow by paternity assignment (`C_pollen`)",
        "adult, seed and juvenile genetic diversity",
        "joint interaction–connectivity limitation with cohort-emergent genetic deterioration",
    ):
        assert phrase in DOC


def test_spondias_quantitative_pollen_flow_anchor_is_retained() -> None:
    for phrase in (
        "209.15 ± 19.28 m",
        "44.91 ± 1.98 m",
        "7.7–828.2 m",
        "2.98–134 m",
        "N_ep ≈ 2.58",
        "N_ep ≈ 1.58",
    ):
        assert phrase in DOC


def test_spondias_genetic_effect_is_cohort_specific() -> None:
    assert "continuous juveniles observed heterozygosity `H_o ≈ 0.465`" in DOC
    assert "fragmented juveniles `H_o ≈ 0.272`" in DOC
    assert "fragmented seeds `H_o ≈ 0.311`" in DOC
    assert "cohort identity belongs in the state" in DOC
    assert "Adult neutral genetics alone is insufficient" in CROSSWALK


def test_spondias_is_not_a_universal_fragmentation_threshold() -> None:
    assert "does not claim that the numerical distances or heterozygosity values are universal thresholds" in DOC
    assert "Near-complete synchronized joint-state anchor" in CROSSWALK
    assert "habitat class/history adds predictive information after the measured joint state" in CROSSWALK
