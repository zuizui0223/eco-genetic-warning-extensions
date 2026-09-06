from __future__ import annotations

import argparse
from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one match, found {count}")
    return text.replace(old, new, 1)


def finalize_figure3(path: Path) -> None:
    text = path.read_text(encoding="utf-8")

    # Legacy mechanistic Figure 3 needs a layout-only subtitle split and horizon legend.
    # The newer sorting-buffering Figure 3 already carries its own labels and must not
    # be rewritten by this compatibility finalizer.
    legacy_phrase = "matching-dependent recruitment is opposed by feedback-mediated compensation"
    if legacy_phrase not in text:
        return

    old = (
        '<text x="1240.0" y="670" text-anchor="middle" '
        'font-family="Arial,Helvetica,sans-serif" font-size="12" font-weight="normal">'
        'matching-dependent recruitment is opposed by feedback-mediated compensation</text>'
    )
    if old not in text:
        old = old.replace('x="1240.0"', 'x="1240"')
    new = (
        '<text x="1240" y="666" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" '
        'font-size="12" font-weight="normal">matching-dependent recruitment</text>'
        '<text x="1240" y="688" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" '
        'font-size="12" font-weight="normal">opposed by feedback-mediated compensation</text>'
    )
    text = replace_once(text, old, new, "figure3 synthesis subtitle")

    legend = (
        '<line x1="820" y1="126" x2="855" y2="126" stroke="#111" stroke-width="2"/>'
        '<text x="865" y="130" text-anchor="start" font-family="Arial,Helvetica,sans-serif" '
        'font-size="11" font-weight="normal">g20</text>'
        '<line x1="900" y1="126" x2="935" y2="126" stroke="#111" stroke-width="2" stroke-dasharray="7 5"/>'
        '<text x="945" y="130" text-anchor="start" font-family="Arial,Helvetica,sans-serif" '
        'font-size="11" font-weight="normal">g40</text>'
    )
    text = replace_once(text, '</svg>', legend + '</svg>', "figure3 horizon legend")
    path.write_text(text, encoding="utf-8")


def validate_svg(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    if 'role="img"' not in text or '<title ' not in text or '<desc ' not in text:
        raise RuntimeError(f"missing accessibility metadata: {path}")
    for forbidden in ("Crepis", "Miyake", "Zosterops", "Conospermum", "Spondias"):
        if forbidden in text:
            raise RuntimeError(f"natural projection leaked into main figure {path.name}: {forbidden}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--figures", required=True)
    args = parser.parse_args()
    root = Path(args.figures)
    expected = [
        root / "figure1_mathematical_boundaries.svg",
        root / "figure2_state_separation.svg",
        root / "figure3_relational_state.svg",
        root / "figure4_warning_discrimination.svg",
    ]
    for path in expected:
        if not path.is_file():
            raise RuntimeError(f"missing main figure: {path}")
    finalize_figure3(root / "figure3_relational_state.svg")
    for path in expected:
        validate_svg(path)
    print("NEE figure QA: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
