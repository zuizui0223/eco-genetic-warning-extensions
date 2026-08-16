from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "src/eco_genetic_warning_extensions/publication_figures.py"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one match, found {count}")
    return text.replace(old, new, 1)


def main() -> int:
    text = PATH.read_text(encoding="utf-8")
    text = replace_once(
        text,
        '''    panel_specs = (\n        ("A", "median_positive_lead_time", "generations", 0.0, 185.0, 85),\n        ("B", "median_positive_lead_fraction_of_horizon", "fraction of calibrated horizon", 0.0, 0.82, 690),\n    )''',
        '''    panel_specs = (\n        ("A", "median_positive_lead_time", "generations", 0.0, 180.0, 85),\n        ("B", "median_positive_lead_fraction_of_horizon", "fraction of calibrated horizon", 0.0, 0.82, 690),\n    )''',
        "Figure 6 panel scale",
    )
    text = replace_once(
        text,
        '''        for tick in range(6):\n            frac = tick / 5\n            y = top + plot_h - frac * plot_h\n            value = ymin + frac * (ymax-ymin)\n            label = f"{value:.1f}" if metric.endswith("horizon") else f"{value:.0f}"\n            parts.append(f'<line x1="{left-6}" y1="{y}" x2="{left}" y2="{y}" stroke="#333"/><text x="{left-10}" y="{y+4}" text-anchor="end" font-family="sans-serif" font-size="11">{label}</text>')''',
        '''        tick_values = (0.0, 50.0, 100.0, 150.0) if metric == "median_positive_lead_time" else (0.0, 0.2, 0.4, 0.6, 0.8)\n        for value in tick_values:\n            frac = (value-ymin)/(ymax-ymin)\n            y = top + plot_h - frac * plot_h\n            label = f"{value:.1f}" if metric.endswith("horizon") else f"{value:.0f}"\n            parts.append(f'<line x1="{left-6}" y1="{y}" x2="{left}" y2="{y}" stroke="#333"/><text x="{left-10}" y="{y+4}" text-anchor="end" font-family="sans-serif" font-size="11">{label}</text>')''',
        "Figure 6 ticks",
    )
    text = replace_once(
        text,
        '''    parts.append('<text x="640" y="785" text-anchor="middle" font-family="sans-serif" font-size="11">95% intervals resample whole trajectories; the absolute timing contrast is not a single-factor transition-direction effect.</text>')''',
        '''    parts.append('<text x="640" y="785" text-anchor="middle" font-family="sans-serif" font-size="11">Direct D−S bootstrap: all six horizon-normalized 95% intervals include 0; absolute intervals exclude 0 only for Hα 5% and 10%.</text>')''',
        "Figure 6 uncertainty note",
    )
    PATH.write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
