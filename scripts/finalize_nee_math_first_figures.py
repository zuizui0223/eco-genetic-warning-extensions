from __future__ import annotations

import argparse
from pathlib import Path


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
        validate_svg(path)
    print("NEE figure QA: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
