from __future__ import annotations

import html
import json
from pathlib import Path


def _text(x: float, y: float, value: str, *, size: int = 18, anchor: str = "middle", weight: str = "normal") -> str:
    return (
        f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" '
        f'font-family="sans-serif" font-size="{size}" font-weight="{weight}">{html.escape(value)}</text>'
    )


def write_state_counterexample_figure(summary_path: Path, output_path: Path) -> None:
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    cert = summary["opening_certificate"]
    aligned = cert["aligned_generation1_interaction"]
    anti = cert["anti_aligned_generation1_interaction"]
    aligned_support = cert["aligned_support_signal"]
    anti_support = cert["anti_aligned_support_signal"]
    max_diff = cert["maximum_patchwise_generation1_difference"]

    if not cert["coarse_marginal_signatures_identical"]:
        raise RuntimeError("locked state counterexample no longer has identical coarse marginals")
    if cert["coarse_marginals_are_transition_sufficient"]:
        raise RuntimeError("locked transition-sufficiency decision drifted")
    if len(aligned) != 4 or len(anti) != 4:
        raise RuntimeError("expected four patchwise generation-1 interaction values")

    width, height = 1200, 720
    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        '<title id="title">Matching eco-genetic marginals can hide different next transitions</title>',
        '<desc id="desc">Aligned and anti-aligned four-patch states retain identical declared coarse marginals but reverse cross-layer covariance. Their exact generation-one interaction transitions differ patchwise, with a maximum difference of 0.2543.</desc>',
        '<rect width="100%" height="100%" fill="white"/>',
        _text(600, 45, "Matching marginals can hide different next transitions", size=28, weight="bold"),
        _text(300, 88, "A  State construction", size=21, weight="bold"),
        _text(900, 88, "B  Exact generation-1 interaction", size=21, weight="bold"),
        _text(300, 125, f"aligned covariance = {cert['aligned_cross_layer_covariance']:+.3f}"),
        _text(300, 153, f"anti-aligned covariance = {cert['anti_aligned_cross_layer_covariance']:+.3f}"),
        _text(300, 190, "same census, layer-wise marginals, Hα, Hγ and FST", size=15),
    ]

    # Panel A: paired patch rows. A plain structural diagram avoids implying a metric scale.
    x_positions = [95, 230, 365, 500]
    y_aligned, y_anti = 275, 430
    lines.extend([
        _text(40, y_aligned + 5, "aligned", size=16, anchor="start", weight="bold"),
        _text(40, y_anti + 5, "anti", size=16, anchor="start", weight="bold"),
    ])
    for i, x in enumerate(x_positions):
        for y, label, support in (
            (y_aligned, f"q{i+1}", aligned_support[i]),
            (y_anti, f"q{i+1}", anti_support[i]),
        ):
            lines.append(f'<rect x="{x-48}" y="{y-38}" width="96" height="76" rx="8" fill="white" stroke="#111" stroke-width="2"/>')
            lines.append(_text(x, y-5, label, size=15, weight="bold"))
            lines.append(_text(x, y+20, f"support {support:.2f}", size=13))
    lines.append(_text(300, 520, "cross-layer assignment changes; declared marginals do not", size=15))

    # Panel B: simple dot/line plot with a common y scale.
    plot_left, plot_right = 680, 1130
    plot_top, plot_bottom = 165, 555
    ymin, ymax = 0.40, 0.90
    lines.append(f'<line x1="{plot_left}" y1="{plot_bottom}" x2="{plot_right}" y2="{plot_bottom}" stroke="#111" stroke-width="2"/>')
    lines.append(f'<line x1="{plot_left}" y1="{plot_top}" x2="{plot_left}" y2="{plot_bottom}" stroke="#111" stroke-width="2"/>')
    for tick in (0.4, 0.5, 0.6, 0.7, 0.8, 0.9):
        y = plot_bottom - (tick - ymin) / (ymax - ymin) * (plot_bottom - plot_top)
        lines.append(f'<line x1="{plot_left-6}" y1="{y:.1f}" x2="{plot_right}" y2="{y:.1f}" stroke="#ddd" stroke-width="1"/>')
        lines.append(_text(plot_left-12, y+5, f"{tick:.1f}", size=13, anchor="end"))
    lines.append(_text(plot_left-54, 360, "interaction", size=15))

    px = [730, 850, 970, 1090]
    aligned_points: list[tuple[float, float]] = []
    anti_points: list[tuple[float, float]] = []
    for i, x in enumerate(px):
        ya = plot_bottom - (aligned[i] - ymin) / (ymax - ymin) * (plot_bottom - plot_top)
        yn = plot_bottom - (anti[i] - ymin) / (ymax - ymin) * (plot_bottom - plot_top)
        aligned_points.append((x, ya))
        anti_points.append((x, yn))
        lines.append(_text(x, plot_bottom + 28, f"patch {i+1}", size=13))
    lines.append('<polyline points="' + ' '.join(f"{x:.1f},{y:.1f}" for x, y in aligned_points) + '" fill="none" stroke="#111" stroke-width="2"/>')
    lines.append('<polyline points="' + ' '.join(f"{x:.1f},{y:.1f}" for x, y in anti_points) + '" fill="none" stroke="#777" stroke-width="2" stroke-dasharray="8 5"/>')
    for x, y in aligned_points:
        lines.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6" fill="white" stroke="#111" stroke-width="2"/>')
    for x, y in anti_points:
        lines.append(f'<rect x="{x-5:.1f}" y="{y-5:.1f}" width="10" height="10" fill="white" stroke="#777" stroke-width="2"/>')
    lines.extend([
        f'<line x1="720" y1="600" x2="765" y2="600" stroke="#111" stroke-width="2"/>',
        _text(775, 605, "aligned", size=14, anchor="start"),
        f'<line x1="880" y1="600" x2="925" y2="600" stroke="#777" stroke-width="2" stroke-dasharray="8 5"/>',
        _text(935, 605, "anti-aligned", size=14, anchor="start"),
        _text(900, 650, f"maximum patchwise difference = {max_diff:.4f}", size=17, weight="bold"),
        '</svg>',
    ])
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

    width, height = 1200, 720
    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        '<title id="title">Horizon-dependent propagation of hidden eco-genetic state</title>',
        '<desc id="desc">Anti-aligned minus aligned functional-loss risk is near zero at generations five and ten, about five percentage points at generations twenty and forty, and uncertainty contracts across nested paired samples of five hundred, one thousand and fifteen hundred pairs.</desc>',
        '<rect width="100%" height="100%" fill="white"/>',
        _text(600, 45, "Hidden state structure propagates to functional-loss risk", size=28, weight="bold"),
        _text(315, 88, "A  Primary 1,500-pair horizon curve", size=20, weight="bold"),
        _text(905, 88, "B  Precision audit at generations 20 and 40", size=20, weight="bold"),
    ]

    # Panel A.
    left, right, top, bottom = 80, 570, 145, 570
    y_min, y_max = -0.02, 0.10
    lines.extend([
        f'<line x1="{left}" y1="{bottom}" x2="{right}" y2="{bottom}" stroke="#111" stroke-width="2"/>',
        f'<line x1="{left}" y1="{top}" x2="{left}" y2="{bottom}" stroke="#111" stroke-width="2"/>',
    ])
    for tick in (-0.02, 0.00, 0.02, 0.04, 0.06, 0.08, 0.10):
        y = bottom - (tick-y_min)/(y_max-y_min)*(bottom-top)
        lines.append(f'<line x1="{left}" y1="{y:.1f}" x2="{right}" y2="{y:.1f}" stroke="{"#888" if tick == 0 else "#ddd"}" stroke-width="{2 if tick == 0 else 1}"/>')
        lines.append(_text(left-10, y+5, f"{tick*100:.0f}", size=13, anchor="end"))
    lines.append(_text(32, 360, "risk difference (pp)", size=14))
    xmap = {5: 135, 10: 235, 20: 365, 40: 525}
    pts = []
    for row in primary:
        x = xmap[row["horizon"]]
        est, lo, hi = row["risk_difference_anti_minus_aligned"], row["ci95_lower"], row["ci95_upper"]
        y = bottom - (est-y_min)/(y_max-y_min)*(bottom-top)
        ylo = bottom - (lo-y_min)/(y_max-y_min)*(bottom-top)
        yhi = bottom - (hi-y_min)/(y_max-y_min)*(bottom-top)
        pts.append((x, y))
        lines.append(f'<line x1="{x}" y1="{yhi:.1f}" x2="{x}" y2="{ylo:.1f}" stroke="#111" stroke-width="2"/>')
        lines.append(f'<line x1="{x-7}" y1="{yhi:.1f}" x2="{x+7}" y2="{yhi:.1f}" stroke="#111" stroke-width="2"/>')
        lines.append(f'<line x1="{x-7}" y1="{ylo:.1f}" x2="{x+7}" y2="{ylo:.1f}" stroke="#111" stroke-width="2"/>')
        lines.append(f'<circle cx="{x}" cy="{y:.1f}" r="6" fill="white" stroke="#111" stroke-width="2"/>')
        lines.append(_text(x, bottom+28, str(row["horizon"]), size=13))
        lines.append(_text(x, y-14, f"{est*100:+.2f}", size=12))
    lines.append('<polyline points="' + ' '.join(f"{x},{y:.1f}" for x, y in pts) + '" fill="none" stroke="#111" stroke-width="2"/>')
    lines.append(_text(325, 615, "generation", size=14))

    # Panel B: nested precision diagnostics, same y scale.
    left2, right2, top2, bottom2 = 670, 1145, 145, 570
    lines.extend([
        f'<line x1="{left2}" y1="{bottom2}" x2="{right2}" y2="{bottom2}" stroke="#111" stroke-width="2"/>',
        f'<line x1="{left2}" y1="{top2}" x2="{left2}" y2="{bottom2}" stroke="#111" stroke-width="2"/>',
    ])
    for tick in (-0.02, 0.00, 0.02, 0.04, 0.06, 0.08, 0.10, 0.12):
        # panel B allows up to 12 pp because the 500-pair upper bound exceeds 11 pp
        yy_min, yy_max = -0.02, 0.12
        y = bottom2 - (tick-yy_min)/(yy_max-yy_min)*(bottom2-top2)
        lines.append(f'<line x1="{left2}" y1="{y:.1f}" x2="{right2}" y2="{y:.1f}" stroke="{"#888" if tick == 0 else "#ddd"}" stroke-width="{2 if tick == 0 else 1}"/>')
        lines.append(_text(left2-10, y+5, f"{tick*100:.0f}", size=13, anchor="end"))
    group_x = {20: [760, 820, 880], 40: [970, 1030, 1090]}
    pairs = [500, 1000, 1500]
    for horizon in (20, 40):
        for idx, n_pairs in enumerate(pairs):
            row = next(r for r in cells if r["horizon"] == horizon and r["n_pairs"] == n_pairs)
            x = group_x[horizon][idx]
            yy_min, yy_max = -0.02, 0.12
            est, lo, hi = row["risk_difference_anti_minus_aligned"], row["ci95_lower"], row["ci95_upper"]
            y = bottom2 - (est-yy_min)/(yy_max-yy_min)*(bottom2-top2)
            ylo = bottom2 - (lo-yy_min)/(yy_max-yy_min)*(bottom2-top2)
            yhi = bottom2 - (hi-yy_min)/(yy_max-yy_min)*(bottom2-top2)
            lines.append(f'<line x1="{x}" y1="{yhi:.1f}" x2="{x}" y2="{ylo:.1f}" stroke="#111" stroke-width="2"/>')
            lines.append(f'<circle cx="{x}" cy="{y:.1f}" r="5" fill="white" stroke="#111" stroke-width="2"/>')
            lines.append(_text(x, bottom2+25, f"{n_pairs//1000 if n_pairs==1000 else n_pairs/1000:g}k", size=12))
        lines.append(_text(sum(group_x[horizon])/3, bottom2+52, f"generation {horizon}", size=14, weight="bold"))
    lines.extend([
        _text(905, 640, "nested prefixes are precision diagnostics, not independent experiments", size=13),
        _text(905, 670, "error bars: paired 95% confidence intervals", size=13),
        '</svg>',
    ])
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
