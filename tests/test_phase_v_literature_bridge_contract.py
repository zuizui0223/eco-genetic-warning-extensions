from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_phase_v_bridge_keeps_urban_and_island_as_contrasting_routes() -> None:
    text = (ROOT / "docs/URBAN_ISLAND_PHASE_V_LITERATURE_BRIDGE.md").read_text(encoding="utf-8").lower()
    assert "not ecological equivalents" in text
    assert "different fragmentation mechanisms can converge" in text
    assert "does not simulate cities or islands" in text
    assert "cross-layer spatial alignment" in text
    assert "convergence would then mean different causal routes arrive at a joint state" in text


def test_bridge_does_not_reintroduce_superseded_connectivity_or_partner_claims() -> None:
    text = (ROOT / "docs/URBAN_ISLAND_PHASE_V_LITERATURE_BRIDGE.md").read_text(encoding="utf-8").lower()
    assert "m=.10–.20" not in text
    assert "partner loss raises" not in text
    assert "rewiring can buffer or destabilise" in text
