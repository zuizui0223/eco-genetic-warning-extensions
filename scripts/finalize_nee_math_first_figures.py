from __future__ import annotations

import argparse
from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if text.count(old) != 1:
        raise RuntimeError(f"{label}: expected one match, found {text.count(old)}")
    return text.replace(old, new, 1)


def finalize_figure2(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    specs = [
        (655, "interaction", ""),
        (679, "local effective size", ' stroke-dasharray="8 5"'),
        (703, "realised high-trait mass", ' stroke-dasharray="3 4"'),
    ]
    for y, label, dash in specs:
        old = (
            f'<text x="900" y="{y}" text-anchor="start" '
            f'font-family="Arial,Helvetica,sans-serif" font-size="12" font-weight="normal">{label}</text>'
        )
        new = (
            f'<line x1="842" y1="{y-4}" x2="887" y2="{y-4}" stroke="#111" stroke-width="2.2"{dash}/>'
            + old
        )
        text = replace_once(text, old, new, f"figure2 legend {label}")
    path.write_text(text, encoding="utf-8")


def finalize_figure3(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    for y, label in ((254, "aligned"), (369, "anti-aligned")):
        old = (
            f'<text x="55" y="{y}" text-anchor="start" '
            f'font-family="Arial,Helvetica,sans-serif" font-size="13" font-weight="bold">{label}</text>'
        )
        new = (
            f'<text x="78" y="{y}" text-anchor="end" '
            f'font-family="Arial,Helvetica,sans-serif" font-size="13" font-weight="bold">{label}</text>'
        )
        text = replace_once(text, old, new, f"figure3 row label {label}")

    old_axis = (
        '<text x="785" y="380" text-anchor="middle" '
        'font-family="Arial,Helvetica,sans-serif" font-size="12" font-weight="normal" '
        'transform="rotate(-90 785 380)">anti-aligned - aligned loss risk (pp)</text>'
    )
    new_axis = (
        '<text x="758" y="380" text-anchor="middle" '
        'font-family="Arial,Helvetica,sans-serif" font-size="12" font-weight="normal" '
        'transform="rotate(-90 758 380)">anti-aligned - aligned loss risk (pp)</text>'
    )
    text = replace_once(text, old_axis, new_axis, "figure3 y-axis label")

    l, top, bottom = 825, 150, 610
    ymin, ymax = -0.02, 0.10
    ticks = []
    for pp in (-2, 0, 2, 4, 6, 8, 10):
        value = pp / 100.0
        y = bottom - (value - ymin) / (ymax - ymin) * (bottom - top)
        ticks.append(
            f'<line x1="820" y1="{y:.1f}" x2="825" y2="{y:.1f}" stroke="#777" stroke-width="1"/>'
        )
        ticks.append(
            f'<text x="813" y="{y+4:.1f}" text-anchor="end" font-family="Arial,Helvetica,sans-serif" '
            f'font-size="11" font-weight="normal">{pp}</text>'
        )
    ticks.append(f'<line x1="{l}" y1="{top}" x2="{l}" y2="{bottom}" stroke="#777" stroke-width="1"/>')
    text = replace_once(text, '</svg>', ''.join(ticks) + '</svg>', "figure3 y ticks")
    path.write_text(text, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--figures", required=True)
    args = parser.parse_args()
    root = Path(args.figures)
    finalize_figure2(root / "figure2_state_separation.svg")
    finalize_figure3(root / "figure3_relational_state.svg")
    print("Applied layout-only NEE figure QA fixes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
