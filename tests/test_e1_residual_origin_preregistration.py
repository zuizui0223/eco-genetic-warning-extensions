from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEXT = (ROOT / "manuscript" / "empirical_e1_residual_origin_preregistration.md").read_text(encoding="utf-8")


def test_e1_analysis_is_declared_before_archive_inspection() -> None:
    assert "written before inspecting the downloaded Figshare archive schema" in TEXT
    assert "10.6084/m9.figshare.25025000.v1" in TEXT


def test_e1_primary_state_and_origin_test_are_fixed() -> None:
    for phrase in (
        "community-level trait matching",
        "pollinator functional diversity `FD_Q`",
        "pollinator functional evenness `FEve`",
        "E1-C1 — candidate functional-state model",
        "E1-C2 — residual-origin model",
        "distance_from_mainland",
    ):
        assert phrase in TEXT


def test_e1_validation_holds_out_whole_sites() -> None:
    assert "leave-one-site-out" in TEXT
    assert "8 folds" in TEXT
    assert "Every observation from the held-out site is excluded" in TEXT
    assert "mean squared prediction error" in TEXT


def test_e1_decisions_do_not_promote_habitat_label() -> None:
    assert "ecological_partial_state_convergence_supported" in TEXT
    assert "ecological_partial_state_incomplete" in TEXT
    assert "not_identifiable_from_archive" in TEXT
    assert "not** that `island` is itself a biological regime variable" in TEXT
    assert "search additional network metrics until geography becomes negligible" in TEXT
