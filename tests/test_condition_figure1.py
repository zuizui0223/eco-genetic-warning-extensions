from eco_genetic_warning_extensions.condition_figure1 import figure1_estimability_svg


def test_figure1_has_condition_first_causal_order() -> None:
    svg = figure1_estimability_svg()
    assert 'role="img"' in svg
    assert 'aria-labelledby="figure1-title figure1-desc"' in svg
    assert "Eco-genetic causal architecture and four-question hierarchy" in svg
    order = [
        svg.index("Functional fragmentation"),
        svg.index("Loss-regime conditions"),
        svg.index("Conditional warning"),
        svg.index("Warning portability"),
    ]
    assert order == sorted(order)
    assert "turnover · connectivity" in svg
    assert "interaction support" in svg
    assert "Only after an evaluable loss regime is fixed" in svg


def test_figure1_keeps_biological_states_distinct() -> None:
    svg = figure1_estimability_svg()
    for label in (
        "Population persistence",
        "Interaction state",
        "Realised function",
        "Genetic connectivity",
        "Genetic diversity",
        "Warning timing",
    ):
        assert label in svg
    assert "R4 is an operational reproducible intermediate-risk event regime" in svg
    assert "not evidence of warning success" in svg
