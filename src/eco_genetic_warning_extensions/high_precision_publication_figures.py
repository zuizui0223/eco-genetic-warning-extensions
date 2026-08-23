"""Deterministic Figure 4/5 builders from the consolidated high-precision C2 map.

These builders render already locked summaries only. They do not run simulations,
select conditions, or inspect genetic-warning fields.
"""
from __future__ import annotations

import html
import json
from pathlib import Path
from typing import Any, Mapping


def _header(width: int, height: int, title: str, desc: str, identifier: str) -> list[str]:
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="{identifier}-title {identifier}-desc">',
        f'<title id="{identifier}-title">{html.escape(title)}</title>',
        f'<desc id="{identifier}-desc">{html.escape(desc)}</desc>',
        '<rect width="100%" height="100%" fill="white"/>',
        f'<text x="{width/2}" y="36" text-anchor="middle" font-family="sans-serif" font-size="22" font-weight="bold">{html.escape(title)}</text>',
    ]


def _json(path: str | Path) -> dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _loss_y(value: float, top: float, height: float) -> float:
    return top + height * (1.0 - value)


def _p_y(value: float, top: float, height: float) -> float:
    return top + height * (1.0 - value)


def _axes(parts: list[str], left: float, top: float, width: float, height: float, *, ylabel: str) -> None:
    parts.append(f'<rect x="{left}" y="{top}" width="{width}" height="{height}" fill="white" stroke="#333"/>')
    for frac in (0.0, 0.25, 0.5, 0.75, 1.0):
        y = top + height * (1 - frac)
        parts.append(f'<line x1="{left-5}" y1="{y}" x2="{left}" y2="{y}" stroke="#333"/>')
        parts.append(f'<text x="{left-9}" y="{y+4}" text-anchor="end" font-family="sans-serif" font-size="10">{frac:.2g}</text>')
    parts.append(f'<text x="{left-52}" y="{top+height/2}" text-anchor="middle" font-family="sans-serif" font-size="11" transform="rotate(-90 {left-52} {top+height/2})">{html.escape(ylabel)}</text>')


def _frontier_values(row: Mapping[str, Any]) -> tuple[list[float], list[float]]:
    if float(row["p_star"]) == 0.35:
        return (
            [float(row["pooled_loss_phase_d_family"]), float(row["pooled_loss_phase_c_family"])],
            [float(row["equal_rate_p_phase_d"]), float(row["equal_rate_p_phase_c"])],
        )
    return [float(row["pooled_loss"])], [float(row["equal_rate_p"])]


def figure4_high_precision_incidence_svg(payload: Mapping[str, Any]) -> str:
    rows = sorted(payload["recurrent_turnover"]["conditions"], key=lambda item: float(item["p_star"]))
    width, height = 1280, 690
    parts = _header(
        width,
        height,
        "High-precision recurrent-turnover incidence frontier",
        "Panel A shows pooled realised functional-loss incidence for the exact historical Phase-C and Phase-D seed families after 100-attempt precision expansion. Panel B shows separate equal-rate diagnostics across high-precision seed blocks. The historical R4 band is an operational incidence screen, not a biological heterogeneity class.",
        "figure4",
    )
    left, top, pw, ph = 100, 120, 500, 410
    parts.append('<text x="55" y="80" font-family="sans-serif" font-size="14" font-weight="bold">A. Functional-loss incidence</text>')
    _axes(parts, left, top, pw, ph, ylabel="pooled functional-loss incidence")
    band_y = _loss_y(0.70, top, ph)
    band_h = ph * 0.40
    parts.append(f'<rect x="{left}" y="{band_y}" width="{pw}" height="{band_h}" fill="#e5e7eb" opacity="0.72"/>')
    xmin, xmax = 0.325, 0.400
    for row in rows:
        pstar = float(row["p_star"])
        x = left + (pstar - xmin) / (xmax - xmin) * pw
        losses, _ = _frontier_values(row)
        offsets = [0.0] if len(losses) == 1 else [-7.0, 7.0]
        for index, (loss, dx) in enumerate(zip(losses, offsets, strict=True)):
            y = _loss_y(loss, top, ph)
            parts.append(f'<circle cx="{x+dx:.1f}" cy="{y:.1f}" r="6" fill="#2563eb" stroke="#111"/>')
            label = f"{loss:.3f}" if len(losses) == 1 else ("D " if index == 0 else "C ") + f"{loss:.3f}"
            parts.append(f'<text x="{x+dx:.1f}" y="{max(top+12,y-12):.1f}" text-anchor="middle" font-family="sans-serif" font-size="9">{html.escape(label)}</text>')
        screen = str(row["screen"]).replace("_highrep", "")
        parts.append(f'<text x="{x:.1f}" y="{top+ph+23}" text-anchor="middle" font-family="sans-serif" font-size="10">p*={pstar:.3f}</text>')
        parts.append(f'<text x="{x:.1f}" y="{top+ph+41}" text-anchor="middle" font-family="sans-serif" font-size="10" font-weight="bold">{html.escape(screen)}</text>')
    parts.append(f'<text x="{left+12}" y="{band_y+18}" font-family="sans-serif" font-size="10">historical intermediate-incidence screen 0.30–0.70</text>')
    parts.append(f'<text x="{left+pw/2}" y="{top+ph+66}" text-anchor="middle" font-family="sans-serif" font-size="10">two points at p*=.350 are independent historical Phase-D and Phase-C seed families</text>')

    left2, pw2 = 730, 450
    parts.append('<text x="690" y="80" font-family="sans-serif" font-size="14" font-weight="bold">B. Between-block equal-rate diagnostics</text>')
    _axes(parts, left2, top, pw2, ph, ylabel="equal-rate p value")
    threshold_y = _p_y(0.05, top, ph)
    parts.append(f'<line x1="{left2}" y1="{threshold_y:.1f}" x2="{left2+pw2}" y2="{threshold_y:.1f}" stroke="#dc2626" stroke-width="2" stroke-dasharray="6,5"/>')
    parts.append(f'<text x="{left2+8}" y="{threshold_y-7:.1f}" font-family="sans-serif" font-size="9">0.05 diagnostic line</text>')
    for row in rows:
        pstar = float(row["p_star"])
        x = left2 + (pstar - xmin) / (xmax - xmin) * pw2
        _, pvals = _frontier_values(row)
        offsets = [0.0] if len(pvals) == 1 else [-7.0, 7.0]
        for index, (pval, dx) in enumerate(zip(pvals, offsets, strict=True)):
            y = _p_y(pval, top, ph)
            parts.append(f'<circle cx="{x+dx:.1f}" cy="{y:.1f}" r="6" fill="#6b7280" stroke="#111"/>')
            label = f"{pval:.3f}" if len(pvals) == 1 else ("D " if index == 0 else "C ") + f"{pval:.3f}"
            parts.append(f'<text x="{x+dx:.1f}" y="{max(top+12,y-11):.1f}" text-anchor="middle" font-family="sans-serif" font-size="9">{html.escape(label)}</text>')
        parts.append(f'<text x="{x:.1f}" y="{top+ph+23}" text-anchor="middle" font-family="sans-serif" font-size="10">{pstar:.3f}</text>')
    parts.append(f'<text x="{left2+pw2/2}" y="{top+ph+52}" text-anchor="middle" font-family="sans-serif" font-size="10">no tested frontier condition shows detected excess block heterogeneity</text>')
    parts.append('</svg>')
    return "\n".join(parts) + "\n"


def figure5_high_precision_connectivity_svg(payload: Mapping[str, Any]) -> str:
    rows = sorted(payload["connectivity"]["conditions"], key=lambda item: float(item["m"]))
    width, height = 1280, 690
    parts = _header(
        width,
        height,
        "Allele-frequency connectivity separates marginal risk from block heterogeneity",
        "Panel A shows high-precision pooled functional-loss incidence across allele-frequency mixing levels and marks the only level with detected excess between-block heterogeneity. Panel B shows paired loss-status switches versus isolation in both directions, together with exact McNemar p values.",
        "figure5",
    )
    left, top, pw, ph = 95, 120, 520, 410
    parts.append('<text x="55" y="80" font-family="sans-serif" font-size="14" font-weight="bold">A. Marginal incidence and block heterogeneity</text>')
    _axes(parts, left, top, pw, ph, ylabel="pooled functional-loss incidence")
    band_y = _loss_y(0.70, top, ph); band_h = ph * 0.40
    parts.append(f'<rect x="{left}" y="{band_y}" width="{pw}" height="{band_h}" fill="#e5e7eb" opacity="0.72"/>')
    points = []
    for index, row in enumerate(rows):
        x = left + 50 + index * 105
        loss = float(row["pooled_loss"]); y = _loss_y(loss, top, ph); points.append((x, y))
        hetero_p = float(row["equal_rate_p"])
        fill = "#dc2626" if hetero_p < 0.05 else "#2563eb"
        radius = 8 if hetero_p < 0.05 else 6
        parts.append(f'<circle cx="{x}" cy="{y:.1f}" r="{radius}" fill="{fill}" stroke="#111"/>')
        parts.append(f'<text x="{x}" y="{max(top+12,y-14):.1f}" text-anchor="middle" font-family="sans-serif" font-size="9">loss {loss:.3f}</text>')
        parts.append(f'<text x="{x}" y="{top+ph+22}" text-anchor="middle" font-family="sans-serif" font-size="10">m={float(row["m"]):g}</text>')
        parts.append(f'<text x="{x}" y="{top+ph+40}" text-anchor="middle" font-family="sans-serif" font-size="9">equal-rate p={hetero_p:.3g}</text>')
    parts.append('<polyline points="' + ' '.join(f'{x:.1f},{y:.1f}' for x, y in points) + '" fill="none" stroke="#111" stroke-width="2"/>')
    parts.append(f'<text x="{left+12}" y="{band_y+18}" font-family="sans-serif" font-size="10">historical intermediate-incidence screen</text>')
    parts.append(f'<circle cx="{left+365}" cy="{top+62}" r="8" fill="#dc2626" stroke="#111"/><text x="{left+380}" y="{top+66}" font-family="sans-serif" font-size="10">detected excess block heterogeneity only at m=.10 (p=0.0205)</text>')

    left2, base_y = 735, 520
    parts.append('<text x="680" y="80" font-family="sans-serif" font-size="14" font-weight="bold">B. Paired trajectory-status switching vs isolation</text>')
    parts.append(f'<line x1="{left2}" y1="{base_y}" x2="{left2+450}" y2="{base_y}" stroke="#333"/>')
    paired_rows = [row for row in rows if float(row["m"]) > 0.0]
    max_count = max(max(int(row["loss_to_no_loss"]), int(row["no_loss_to_loss"])) for row in paired_rows)
    max_h = 310.0
    for index, row in enumerate(paired_rows):
        x = left2 + 65 + index * 100
        a = int(row["loss_to_no_loss"]); b = int(row["no_loss_to_loss"])
        ha = max_h * a / max_count; hb = max_h * b / max_count
        parts.append(f'<rect x="{x-25}" y="{base_y-ha:.1f}" width="21" height="{ha:.1f}" fill="#2563eb" stroke="#111"/>')
        parts.append(f'<rect x="{x+4}" y="{base_y-hb:.1f}" width="21" height="{hb:.1f}" fill="#dc2626" stroke="#111"/>')
        parts.append(f'<text x="{x-14}" y="{base_y-ha-7:.1f}" text-anchor="middle" font-family="sans-serif" font-size="10">{a}</text>')
        parts.append(f'<text x="{x+15}" y="{base_y-hb-7:.1f}" text-anchor="middle" font-family="sans-serif" font-size="10">{b}</text>')
        parts.append(f'<text x="{x}" y="{base_y+20}" text-anchor="middle" font-family="sans-serif" font-size="10">m={float(row["m"]):g}</text>')
        parts.append(f'<text x="{x}" y="{base_y+38}" text-anchor="middle" font-family="sans-serif" font-size="9">McNemar p={float(row["mcnemar_p"]):.3f}</text>')
    parts.append(f'<rect x="{left2+25}" y="585" width="14" height="14" fill="#2563eb"/><text x="{left2+45}" y="597" font-family="sans-serif" font-size="10">loss→no loss</text>')
    parts.append(f'<rect x="{left2+170}" y="585" width="14" height="14" fill="#dc2626"/><text x="{left2+190}" y="597" font-family="sans-serif" font-size="10">no loss→loss</text>')
    parts.append(f'<text x="{left2}" y="630" font-family="sans-serif" font-size="10">all paired marginal-risk tests are non-significant; migration_rate is allele-frequency mixing only</text>')
    parts.append('</svg>')
    return "\n".join(parts) + "\n"


def write_high_precision_condition_figures(condition_map_json: str | Path, output_dir: str | Path) -> None:
    payload = _json(condition_map_json)
    out = Path(output_dir); out.mkdir(parents=True, exist_ok=True)
    # Preserve legacy filenames consumed by the submission bundle while replacing
    # their contents with the corrected high-precision Figure 4/5 evidence.
    (out / "figure4_r4_recovery.svg").write_text(figure4_high_precision_incidence_svg(payload), encoding="utf-8")
    (out / "figure5_connectivity_estimability.svg").write_text(figure5_high_precision_connectivity_svg(payload), encoding="utf-8")
