"""Semantic relabelling for historical-source figures retained in the final spine.

Figure 3 still renders historical Protocol-002 screen evidence, and Figure 6 still
renders the same Stage-III records. This helper changes only titles/descriptions
whose old wording implied stronger biological interpretation than the current
high-precision evidence permits.
"""
from __future__ import annotations

from pathlib import Path


def relabel_condition_figure_semantics(output_dir: str | Path) -> None:
    out = Path(output_dir)
    figure3 = out / "figure3_source_loss_regimes.svg"
    if figure3.exists():
        text = figure3.read_text(encoding="utf-8")
        text = text.replace(
            "Recurrent state turnover reorganises source feasibility and functional-loss regime",
            "Recurrent state turnover reorganises source feasibility and historical loss-screen placement",
        )
        text = text.replace(
            "Panel B shows the dominant warning-blind functional-loss regime and closest pooled loss rate for the same coordinates.",
            "Panel B shows the dominant historical warning-blind screen label and closest pooled loss rate for the same coordinates.",
        )
        text = text.replace("H heterogeneous=", "H mixed-screen=")
        figure3.write_text(text, encoding="utf-8")

    figure6 = out / "figure6_portability.svg"
    if figure6.exists():
        text = figure6.read_text(encoding="utf-8")
        text = text.replace(
            "Portability after evaluability is separately recovered",
            "Portability after downstream loss conditions are separately recovered",
        )
        figure6.write_text(text, encoding="utf-8")
