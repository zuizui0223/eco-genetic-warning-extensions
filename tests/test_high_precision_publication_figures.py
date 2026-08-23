from pathlib import Path
import json

from eco_genetic_warning_extensions.high_precision_publication_figures import (
    figure4_high_precision_incidence_svg,
    figure5_high_precision_connectivity_svg,
    write_high_precision_condition_figures,
)
from eco_genetic_warning_extensions.publication_figure_semantics import relabel_condition_figure_semantics

ROOT = Path(__file__).resolve().parents[1]


def _payload():
    return json.loads((ROOT / "artifacts/high_precision_condition_map.json").read_text())


def test_figure4_uses_precision_frontier_not_old_narrow_r4_story() -> None:
    svg = figure4_high_precision_incidence_svg(_payload())
    assert "High-precision recurrent-turnover incidence frontier" in svg
    assert "0.682" in svg and "0.407" in svg and "0.273" in svg
    assert "0.295" in svg and "0.151" in svg
    assert "narrow reproducible event regime" not in svg.lower()


def test_figure5_shows_historical_observation_and_fresh_nonreplication() -> None:
    svg = figure5_high_precision_connectivity_svg(_payload())
    assert "Historical m=.10 heterogeneity failed fresh-seed replication" in svg
    assert "historical m=.10 block-heterogeneity observation (p=.0205)" in svg
    assert "fresh m=.10 equal-rate p=.745" in svg
    assert "paired McNemar p=0.694" in svg
    assert "historical heterogeneity did not replicate" in svg
    assert "migration_rate remains allele-frequency mixing only" in svg


def test_writer_overwrites_legacy_figure4_5_filenames(tmp_path: Path) -> None:
    write_high_precision_condition_figures(ROOT / "artifacts/high_precision_condition_map.json", tmp_path)
    figure4 = (tmp_path / "figure4_r4_recovery.svg").read_text()
    figure5 = (tmp_path / "figure5_connectivity_estimability.svg").read_text()
    assert "High-precision recurrent-turnover incidence frontier" in figure4
    assert "failed fresh-seed replication" in figure5


def test_semantic_relabel_removes_old_regime_and_evaluability_titles(tmp_path: Path) -> None:
    (tmp_path / "figure3_source_loss_regimes.svg").write_text(
        "Recurrent state turnover reorganises source feasibility and functional-loss regime H heterogeneous=84",
        encoding="utf-8",
    )
    (tmp_path / "figure6_portability.svg").write_text(
        "Portability after evaluability is separately recovered",
        encoding="utf-8",
    )
    relabel_condition_figure_semantics(tmp_path)
    f3 = (tmp_path / "figure3_source_loss_regimes.svg").read_text()
    f6 = (tmp_path / "figure6_portability.svg").read_text()
    assert "historical loss-screen placement" in f3
    assert "H mixed-screen=84" in f3
    assert "downstream loss conditions" in f6
