from __future__ import annotations

import html
import json
from pathlib import Path


def _text(
    x: float,
    y: float,
    value: str,
    *,
    size: int = 18,
    anchor: str = "middle",
    weight: str = "normal",
) -> str:
    return (
        f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" '
        f'font-family="sans-serif" font-size="{size}" font-weight="{weight}">'
        f"{html.escape(value)}</text>"
    )


def _y(value: float, *, minimum: float, maximum: float, top: float, bottom: float) -> float:
    return bottom - (value - minimum) / (maximum - minimum) * (bottom - top)


def write_state_counterexample_figure(summary_path: Path, output_path: Path) -> None:
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    cert = summary["opening_certificate"]
    aligned = cert["aligned_generation1_interaction"]
    anti = cert["anti_aligned_generation1_interaction"]
    aligned_support = cert["aligned_support_signal"]
    anti_support = cert["anti_aligned_support_signal"]
    max_diff = float(cert["maximum_patchwise_generation1_difference"])

    if not cert["coarse_marginal_signatures_identical"]:
        raise RuntimeError("locked state counterexample no longer has identical coarse marginals")
    if cert["coarse_marginals_are_transition_sufficient"]:
        raise RuntimeError("locked transition-sufficiency decision drifted")
    if len(aligned) != 4 or len(anti) != 4:
        raise RuntimeError("expected four patchwise generation-1 interaction values")
    if abs(max_diff - 0.25433292878878405) > 1e-12:
        raise RuntimeError("locked generation-1 certificate drifted")

    lines = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="720" viewBox="0 0 1200 720" role="img" aria-labelledby="title desc">',
        '<title id="title">Matching eco-genetic marginals can hide different next transitions</title>',
        '<desc id="desc">Aligned and anti-aligned four-patch states retain identical declared coarse marginals but reverse cross-layer covariance. Their exact generation-one interaction transitions differ patchwise, with a maximum difference of 0.2543.</desc>',
        '<rect width="100%" height="100%" fill="white"/>',
        _text(600, 45, "Matching marginals can hide different next transitions", size=28, weight="bold"),
        _text(300, 88, "A  Cross-layer state construction", size=21, weight="bold"),
        _text(900, 88, "B  Exact generation-1 interaction", size=21, weight="bold"),
        _text(300, 125, f"aligned covariance = {cert['aligned_cross_layer_covariance']:+.3f}"),
        _text(300, 153, f"anti-aligned covariance = {cert['anti_aligned_cross_layer_covariance']:+.3f}"),
        _text(300, 190, "same census, layer-wise marginals, Hα, Hγ and FST", size=15),
    ]

    x_positions = [105, 235, 365, 495]
    for row_y, row_name, values in (
        (285, "aligned", aligned_support),
        (430, "anti-aligned", anti_support),
    ):
        lines.append(_text(35, row_y + 5, row_name, size=15, anchor="start", weight="bold"))
        for index, (x, support) in enumerate(zip(x_positions, values, strict=True), start=1):
            lines.append(
                f'<rect x="{x-45}" y="{row_y-35}" width="90" height="70" rx="8" '
                'fill="white" stroke="#111" stroke-width="2"/>'
            )
            lines.append(_text(x, row_y - 5, f"patch {index}", size=13, weight="bold"))
            lines.append(_text(x, row_y + 18, f"joint support {support:.2f}", size=12))
    lines.append(_text(300, 515, "cross-layer assignment changes; declared marginals do not", size=15))

    plot_left, plot_right, plot_top, plot_bottom = 680, 1130, 165, 555
    minimum, maximum = 0.40, 0.90
    lines.append(f'<line x1="{plot_left}" y1="{plot_bottom}" x2="{plot_right}" y2="{plot_bottom}" stroke="#111" stroke-width="2"/>')
    lines.append(f'<line x1="{plot_left}" y1="{plot_top}" x2="{plot_left}" y2="{plot_bottom}" stroke="#111" stroke-width="2"/>')
    for tick in (0.4, 0.5, 0.6, 0.7, 0.8, 0.9):
        yy = _y(tick, minimum=minimum, maximum=maximum, top=plot_top, bottom=plot_bottom)
        lines.append(f'<line x1="{plot_left}" y1="{yy:.1f}" x2="{plot_right}" y2="{yy:.1f}" stroke="#ddd" stroke-width="1"/>')
        lines.append(_text(plot_left - 10, yy + 5, f"{tick:.1f}", size=13, anchor="end"))

    patch_x = [730, 850, 970, 1090]
    aligned_points: list[tuple[float, float]] = []
    anti_points: list[tuple[float, float]] = []
    for index, x in enumerate(patch_x):
        ya = _y(float(aligned[index]), minimum=minimum, maximum=maximum, top=plot_top, bottom=plot_bottom)
        yn = _y(float(anti[index]), minimum=minimum, maximum=maximum, top=plot_top, bottom=plot_bottom)
        aligned_points.append((x, ya))
        anti_points.append((x, yn))
        lines.append(_text(x, plot_bottom + 28, f"patch {index+1}", size=13))
    lines.append('<polyline points="' + ' '.join(f"{x:.1f},{yy:.1f}" for x, yy in aligned_points) + '" fill="none" stroke="#111" stroke-width="2"/>')
    lines.append('<polyline points="' + ' '.join(f"{x:.1f},{yy:.1f}" for x, yy in anti_points) + '" fill="none" stroke="#777" stroke-width="2" stroke-dasharray="8 5"/>')
    for x, yy in aligned_points:
        lines.append(f'<circle cx="{x:.1f}" cy="{yy:.1f}" r="6" fill="white" stroke="#111" stroke-width="2"/>')
    for x, yy in anti_points:
        lines.append(f'<rect x="{x-5:.1f}" y="{yy-5:.1f}" width="10" height="10" fill="white" stroke="#777" stroke-width="2"/>')
    lines.extend(
        [
            '<line x1="720" y1="600" x2="765" y2="600" stroke="#111" stroke-width="2"/>',
            _text(775, 605, "aligned", size=14, anchor="start"),
            '<line x1="880" y1="600" x2="925" y2="600" stroke="#777" stroke-width="2" stroke-dasharray="8 5"/>',
            _text(935, 605, "anti-aligned", size=14, anchor="start"),
            _text(900, 650, f"maximum patchwise difference = {max_diff:.4f}", size=17, weight="bold"),
            '</svg>',
        ]
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_propagation_figure(summary_path: Path, output_path: Path) -> None:
    payload = json.loads(summary_path.read_text(encoding="utf-8"))
    result = payload["result"]
    primary = sorted(result["primary_horizon_cells"], key=lambda row: row["horizon"])
    cells = result["cells"]
    if [row["horizon"] for row in primary] != [5, 10, 20, 40]:
        raise RuntimeError("primary horizon contract drifted")
    if any(row["n_pairs"] != 1500 for row in primary):
        raise RuntimeError("primary pair-count contract drifted")

    lines = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="720" viewBox="0 0 1200 720" role="img" aria-labelledby="title desc">',
        '<title id="title">Horizon-dependent propagation of hidden eco-genetic state</title>',
        '<desc id="desc">Anti-aligned minus aligned functional-loss risk is near zero at generations five and ten, about five percentage points at generations twenty and forty, and uncertainty contracts across nested paired samples of five hundred, one thousand and fifteen hundred pairs.</desc>',
        '<rect width="100%" height="100%" fill="white"/>',
        _text(600, 45, "Hidden state structure propagates to functional-loss risk", size=28, weight="bold"),
        _text(315, 88, "A  Primary 1,500-pair horizon curve", size=20, weight="bold"),
        _text(905, 88, "B  Precision audit at generations 20 and 40", size=20, weight="bold"),
    ]

    left, right, top, bottom = 80, 570, 145, 570
    minimum, maximum = -0.02, 0.10
    lines.append(f'<line x1="{left}" y1="{bottom}" x2="{right}" y2="{bottom}" stroke="#111" stroke-width="2"/>')
    lines.append(f'<line x1="{left}" y1="{top}" x2="{left}" y2="{bottom}" stroke="#111" stroke-width="2"/>')
    for tick in (-0.02, 0.00, 0.02, 0.04, 0.06, 0.08, 0.10):
        yy = _y(tick, minimum=minimum, maximum=maximum, top=top, bottom=bottom)
        grid_color = "#888" if tick == 0 else "#ddd"
        grid_width = 2 if tick == 0 else 1
        lines.append(f'<line x1="{left}" y1="{yy:.1f}" x2="{right}" y2="{yy:.1f}" stroke="{grid_color}" stroke-width="{grid_width}"/>')
        lines.append(_text(left - 10, yy + 5, f"{tick*100:.0f}", size=13, anchor="end"))

    x_positions = {5: 135, 10: 235, 20: 365, 40: 525}
    primary_points: list[tuple[float, float]] = []
    for row in primary:
        x = x_positions[int(row["horizon"])]
        estimate = float(row["risk_difference_anti_minus_aligned"])
        lower = float(row["ci95_lower"])
        upper = float(row["ci95_upper"])
        yy = _y(estimate, minimum=minimum, maximum=maximum, top=top, bottom=bottom)
        y_lower = _y(lower, minimum=minimum, maximum=maximum, top=top, bottom=bottom)
        y_upper = _y(upper, minimum=minimum, maximum=maximum, top=top, bottom=bottom)
        primary_points.append((x, yy))
        lines.extend(
            [
                f'<line x1="{x}" y1="{y_upper:.1f}" x2="{x}" y2="{y_lower:.1f}" stroke="#111" stroke-width="2"/>',
                f'<line x1="{x-7}" y1="{y_upper:.1f}" x2="{x+7}" y2="{y_upper:.1f}" stroke="#111" stroke-width="2"/>',
                f'<line x1="{x-7}" y1="{y_lower:.1f}" x2="{x+7}" y2="{y_lower:.1f}" stroke="#111" stroke-width="2"/>',
                f'<circle cx="{x}" cy="{yy:.1f}" r="6" fill="white" stroke="#111" stroke-width="2"/>',
                _text(x, bottom + 28, str(row["horizon"]), size=13),
                _text(x, yy - 14, f"{estimate*100:+.2f}", size=12),
            ]
        )
    lines.append('<polyline points="' + ' '.join(f"{x:.1f},{yy:.1f}" for x, yy in primary_points) + '" fill="none" stroke="#111" stroke-width="2"/>')
    lines.append(_text(325, 615, "generation", size=14))
    lines.append(_text(28, 355, "anti − aligned risk (pp)", size=13))

    left2, right2, top2, bottom2 = 670, 1145, 145, 570
    minimum2, maximum2 = -0.02, 0.12
    lines.append(f'<line x1="{left2}" y1="{bottom2}" x2="{right2}" y2="{bottom2}" stroke="#111" stroke-width="2"/>')
    lines.append(f'<line x1="{left2}" y1="{top2}" x2="{left2}" y2="{bottom2}" stroke="#111" stroke-width="2"/>')
    for tick in (-0.02, 0.00, 0.02, 0.04, 0.06, 0.08, 0.10, 0.12):
        yy = _y(tick, minimum=minimum2, maximum=maximum2, top=top2, bottom=bottom2)
        grid_color = "#888" if tick == 0 else "#ddd"
        grid_width = 2 if tick == 0 else 1
        lines.append(f'<line x1="{left2}" y1="{yy:.1f}" x2="{right2}" y2="{yy:.1f}" stroke="{grid_color}" stroke-width="{grid_width}"/>')
        lines.append(_text(left2 - 10, yy + 5, f"{tick*100:.0f}", size=13, anchor="end"))

    group_x = {20: [760, 820, 880], 40: [970, 1030, 1090]}
    pair_counts = [500, 1000, 1500]
    for horizon in (20, 40):
        for index, n_pairs in enumerate(pair_counts):
            row = next(r for r in cells if r["horizon"] == horizon and r["n_pairs"] == n_pairs)
            x = group_x[horizon][index]
            estimate = float(row["risk_difference_anti_minus_aligned"])
            lower = float(row["ci95_lower"])
            upper = float(row["ci95_upper"])
            yy = _y(estimate, minimum=minimum2, maximum=maximum2, top=top2, bottom=bottom2)
            y_lower = _y(lower, minimum=minimum2, maximum=maximum2, top=top2, bottom=bottom2)
            y_upper = _y(upper, minimum=minimum2, maximum=maximum2, top=top2, bottom=bottom2)
            label = "0.5k" if n_pairs == 500 else "1k" if n_pairs == 1000 else "1.5k"
            lines.extend(
                [
                    f'<line x1="{x}" y1="{y_upper:.1f}" x2="{x}" y2="{y_lower:.1f}" stroke="#111" stroke-width="2"/>',
                    f'<circle cx="{x}" cy="{yy:.1f}" r="5" fill="white" stroke="#111" stroke-width="2"/>',
                    _text(x, bottom2 + 25, label, size=12),
                ]
            )
        lines.append(_text(sum(group_x[horizon]) / 3, bottom2 + 52, f"generation {horizon}", size=14, weight="bold"))

    lines.extend(
        [
            _text(905, 640, "nested prefixes are precision diagnostics, not independent experiments", size=13),
            _text(905, 670, "error bars: paired 95% confidence intervals", size=13),
            '</svg>',
        ]
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
