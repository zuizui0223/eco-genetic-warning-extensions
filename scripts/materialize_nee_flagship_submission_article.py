from __future__ import annotations

import argparse
from pathlib import Path

INSERT_AFTER = (
    "Indicator science has developed complementary principles for validation, robustness and end use "
    "(Bockstaller & Girardin 2003; Moriarty et al. 2018; Bundy et al. 2019; Carstensen et al. 2024). "
)

NOVELTY = (
    "Recent work has also formalized necessary-condition tests of ecological model validity against empirical time series "
    "(Song & Levine 2025) and demonstrated scalable real-time biodiversity forecasting with independent validation "
    "(Ovaskainen et al. 2026). Our question is logically prior to both: even a well-specified or empirically validated "
    "forecasting model cannot support the intended prediction if the biological state, analytical representation, "
    "candidate signal or empirical measurement supplied to it is invalid for the declared target and horizon. "
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    source = Path(args.source)
    output = Path(args.output)
    text = source.read_text(encoding="utf-8")
    if text.count(INSERT_AFTER) != 1:
        raise RuntimeError("nearest-neighbour insertion anchor drifted")
    if "Song & Levine 2025" in text or "Ovaskainen et al. 2026" in text:
        raise RuntimeError("source manuscript already contains submission-only novelty paragraph")
    text = text.replace(INSERT_AFTER, INSERT_AFTER + NOVELTY, 1)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(text, encoding="utf-8")
    print("Materialized NEE submission article with nearest-neighbour positioning")


if __name__ == "__main__":
    main()
