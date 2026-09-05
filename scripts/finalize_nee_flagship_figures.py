from __future__ import annotations

import argparse
from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if text.count(old) != 1:
        raise RuntimeError(f"{label}: expected one occurrence, found {text.count(old)}")
    return text.replace(old, new, 1)


def fix_figure2(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    old = '<text x="35.0" y="390.0" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="13" font-weight="normal">% supported outcomes</text>'
    new = '<text x="28.0" y="390.0" text-anchor="middle" transform="rotate(-90 28 390)" font-family="Arial,Helvetica,sans-serif" font-size="13" font-weight="normal">% supported outcomes</text>'
    text = replace_once(text, old, new, "figure2 y-axis label")

    replacements = [
        (
            '<text x="875.0" y="655.0" text-anchor="start" font-family="Arial,Helvetica,sans-serif" font-size="13" font-weight="normal">interaction</text>',
            '<line x1="830" y1="650" x2="865" y2="650" stroke="#111" stroke-width="2.2"/><circle cx="847.5" cy="650" r="4" fill="white" stroke="#111"/><text x="875.0" y="655.0" text-anchor="start" font-family="Arial,Helvetica,sans-serif" font-size="13" font-weight="normal">interaction</text>',
            "figure2 interaction key",
        ),
        (
            '<text x="875.0" y="680.0" text-anchor="start" font-family="Arial,Helvetica,sans-serif" font-size="13" font-weight="normal">local effective size</text>',
            '<line x1="830" y1="675" x2="865" y2="675" stroke="#111" stroke-width="2.2" stroke-dasharray="8 5"/><rect x="843.5" y="671" width="8" height="8" fill="white" stroke="#111"/><text x="875.0" y="680.0" text-anchor="start" font-family="Arial,Helvetica,sans-serif" font-size="13" font-weight="normal">local effective size</text>',
            "figure2 Ne key",
        ),
        (
            '<text x="875.0" y="705.0" text-anchor="start" font-family="Arial,Helvetica,sans-serif" font-size="13" font-weight="normal">realised high-trait mass</text>',
            '<line x1="830" y1="700" x2="865" y2="700" stroke="#111" stroke-width="2.2" stroke-dasharray="3 4"/><path d="M847.5,695 L842.5,704 L852.5,704 Z" fill="white" stroke="#111"/><text x="875.0" y="705.0" text-anchor="start" font-family="Arial,Helvetica,sans-serif" font-size="13" font-weight="normal">realised high-trait mass</text>',
            "figure2 trait-mass key",
        ),
    ]
    for old, new, label in replacements:
        text = replace_once(text, old, new, label)
    path.write_text(text, encoding="utf-8")


def fix_figure3(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    text = replace_once(
        text,
        '<text x="45.0" y="244.0" text-anchor="start" font-family="Arial,Helvetica,sans-serif" font-size="14" font-weight="bold">aligned</text>',
        '<text x="5.0" y="244.0" text-anchor="start" font-family="Arial,Helvetica,sans-serif" font-size="12" font-weight="bold">aligned</text>',
        "figure3 aligned label",
    )
    text = replace_once(
        text,
        '<text x="45.0" y="364.0" text-anchor="start" font-family="Arial,Helvetica,sans-serif" font-size="14" font-weight="bold">anti-aligned</text>',
        '<text x="5.0" y="364.0" text-anchor="start" font-family="Arial,Helvetica,sans-serif" font-size="12" font-weight="bold">anti-aligned</text>',
        "figure3 anti-aligned label",
    )
    text = replace_once(
        text,
        '<text x="800.0" y="400.0" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="12" font-weight="normal">anti-aligned − aligned risk (pp)</text>',
        '<text x="780.0" y="400.0" text-anchor="middle" transform="rotate(-90 780 400)" font-family="Arial,Helvetica,sans-serif" font-size="12" font-weight="normal">anti-aligned - aligned risk (pp)</text>',
        "figure3 risk-axis label",
    )
    path.write_text(text, encoding="utf-8")


def fix_figure4(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    replacements = [
        ("specificity = (n₀ − f) / n₀", "specificity = (n0 - f) / n0", "figure4 specificity formula"),
        ("specificity ∈ [0,1] ⇒ AUC ∈ [0.5,1]", "specificity in [0,1] -> AUC in [0.5,1]", "figure4 range formula"),
        ("observed f = n₀ ⇒ AUC = 0.5", "observed f = n0 -> AUC = 0.5", "figure4 observed endpoint"),
    ]
    for old, new, label in replacements:
        text = replace_once(text, old, new, label)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--figures", required=True)
    args = parser.parse_args()
    root = Path(args.figures)
    fix_figure2(root / "figure2_state_separation.svg")
    fix_figure3(root / "figure3_hidden_state_futures.svg")
    fix_figure4(root / "figure4_precedence_discrimination.svg")
    print("NEE flagship final figure layout QA fixes applied")


if __name__ == "__main__":
    main()
