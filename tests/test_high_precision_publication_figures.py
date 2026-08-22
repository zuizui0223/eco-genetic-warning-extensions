from pathlib import Path
import json

from eco_genetic_warning_extensions.high_precision_publication_figures import (
    figure4_high_precision_incidence_svg,
    figure5_high_precision_connectivity_svg,
    write_high_precision_condition_figures,
)

ROOT = Path(__file__).resolve().parents[1]


def _payload():
    return json.loads((ROOT / "artifacts/high_precision_condition_map.json").read_text())


def test_figure4_uses_precision_frontier_not_old_narrow_r4_story() -> None:
    svg = figure4_high_precision_incidence_svg(_payload())
    assert "High-precision recurrent-turnover incidence frontier" in svg
    assert "0.682" in svg and "0.407" in svg and "0.273" in svg
    assert "0.295" in svg and "0.151" in svg
    assert "narrow reproducible event regime" not in svg.lower()


def test_figure5_separates_heterogeneity_from_paired_marginal_risk() -> None:
    svg = figure5_high_precision_connectivity_svg(_payload())
    assert "Allele-frequency connectivity separates marginal risk from block heterogeneity" in svg
    assert "p=0.0205" in svg
    assert ">71<" in svg and ">63<" in svg
    assert "McNemar p=1.000" in svg
    assert "migration_rate is allele-frequency mixing only" in svg


def test_writer_overwrites_legacy_figure4_5_filenames(tmp_path: Path) -> None:
    write_high_precision_condition_figures(ROOT / "artifacts/high_precision_condition_map.json", tmp_path)
    figure4 = (tmp_path / "figure4_r4_recovery.svg").read_text()
    figure5 = (tmp_path / "figure5_connectivity_estimability.svg").read_text()
    assert "High-precision recurrent-turnover incidence frontier" in figure4
    assert "separates marginal risk from block heterogeneity" in figure5
