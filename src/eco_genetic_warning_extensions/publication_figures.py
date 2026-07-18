"""Publication-facing source aggregation and validation figure generation."""
from __future__ import annotations

import csv
import html
import json
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable

STAGE1_RUN_IDS = (29177214259, 29186610167, 29188592519, 29188748077, 29190149319, 29190149344)


def _load_jsons(root: str | Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for path in sorted(Path(root).rglob("*.json")):
        try:
            value = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue
        if isinstance(value, dict) and value.get("stage") == "Protocol 002 Stage I source reconstruction batch":
            records.append(value)
    return records


def aggregate_stage1(root: str | Path) -> dict[str, Any]:
    records = _load_jsons(root)
    by_index = {int(row["campaign"]["batch_index"]): row for row in records}
    expected = set(range(135))
    if set(by_index) != expected:
        missing = sorted(expected - set(by_index))
        extra = sorted(set(by_index) - expected)
        raise ValueError(f"Stage I artifact coverage mismatch; missing={missing}, extra={extra}")

    coordinate: dict[tuple[float, float], dict[str, Any]] = defaultdict(
        lambda: {
            "attempted": 0,
            "source_supported": 0,
            "source_prepared": 0,
            "projection_supported": 0,
            "projection_failed": 0,
            "projection_not_run": 0,
        }
    )
    totals = {key: 0 for key in ("attempted", "source_supported", "source_prepared", "projection_supported", "projection_failed", "projection_not_run")}
    for index in range(135):
        row = by_index[index]
        cell = row["cell"]
        counts = row["status_counts"]
        key = (float(cell["kappa_mu"]), float(cell["p_star"]))
        target = coordinate[key]
        target["kappa_mu"], target["p_star"] = key
        target["attempted"] += int(row["campaign"]["attempts_per_batch"])
        for name in ("source_supported", "source_prepared", "projection_supported", "projection_failed", "projection_not_run"):
            target[name] += int(counts[name])

    rows = []
    for key in sorted(coordinate):
        row = coordinate[key]
        for name in ("source_supported", "source_prepared", "projection_supported"):
            row[f"{name}_rate"] = row[name] / row["attempted"]
        rows.append(row)
        for name in totals:
            totals[name] += int(row[name])

    return {
        "stage": "Protocol 002 Stage I publication aggregation",
        "source_workflow_run_ids": list(STAGE1_RUN_IDS),
        "batch_count": 135,
        "attempt_count": totals["attempted"],
        "coordinate_count": len(rows),
        "totals": totals,
        "coordinates": rows,
        "evidence_label": "finite Type S evidence for the declared closure",
    }


def write_stage1_outputs(root: str | Path, output_dir: str | Path) -> dict[str, Any]:
    result = aggregate_stage1(root)
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    (out / "stage1_publication_summary.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    fields = [
        "kappa_mu", "p_star", "attempted", "source_supported", "source_supported_rate",
        "source_prepared", "source_prepared_rate", "projection_supported", "projection_supported_rate",
        "projection_failed", "projection_not_run",
    ]
    with (out / "stage1_coordinate_summary.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows({field: row[field] for field in fields} for row in result["coordinates"])
    (out / "figure2_stage1_source_feasibility.svg").write_text(_stage1_svg(result["coordinates"]), encoding="utf-8")
    return result


def write_stage3_figures(summary_path: str | Path, output_dir: str | Path) -> None:
    summary = json.loads(Path(summary_path).read_text(encoding="utf-8"))
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    (out / "figure5_stage3_ordering.svg").write_text(_stage3_ordering_svg(summary["domains"]), encoding="utf-8")
    (out / "figure6_stage3_lead_time.svg").write_text(_stage3_lead_time_svg(summary["domains"]), encoding="utf-8")


def _svg_header(width: int, height: int, title: str, description: str, identifier: str) -> list[str]:
    safe_title = html.escape(title)
    safe_description = html.escape(description)
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="{identifier}-title {identifier}-desc">',
        f'<title id="{identifier}-title">{safe_title}</title>',
        f'<desc id="{identifier}-desc">{safe_description}</desc>',
        '<rect width="100%" height="100%" fill="white"/>',
        f'<text x="30" y="36" font-family="sans-serif" font-size="20" font-weight="bold">{safe_title}</text>',
    ]


def _stage1_svg(rows: Iterable[dict[str, Any]]) -> str:
    rows = list(rows)
    width, height = 820, 420
    parts = _svg_header(
        width,
        height,
        "Source feasibility across transition coordinates",
        "A fifteen-cell map of projection-supported source fractions. Every cell prints both the fraction and supported-attempt count, so values do not depend on colour.",
        "figure2",
    )
    p_values = sorted({row["p_star"] for row in rows})
    k_values = sorted({row["kappa_mu"] for row in rows})
    lookup = {(row["kappa_mu"], row["p_star"]): row for row in rows}
    cell_w, cell_h = 112, 88
    x0, y0 = 170, 82
    for j, p in enumerate(p_values):
        parts.append(f'<text x="{x0 + j*cell_w + 48}" y="68" text-anchor="middle" font-family="sans-serif" font-size="14">p*={p:.2f}</text>')
    for i, k in enumerate(k_values):
        parts.append(f'<text x="152" y="{y0 + i*cell_h + 38}" text-anchor="end" font-family="sans-serif" font-size="14">κμ={k:.2f}</text>')
        for j, p in enumerate(p_values):
            row = lookup[(k, p)]
            rate = float(row["projection_supported_rate"])
            shade = int(245 - 170 * rate)
            fill = f'rgb({shade},{shade},{255})'
            x, y = x0 + j*cell_w, y0 + i*cell_h
            parts.append(f'<rect x="{x}" y="{y}" width="100" height="74" fill="{fill}" stroke="#222" stroke-width="1.5"/>')
            parts.append(f'<text x="{x+50}" y="{y+31}" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="bold">{rate:.2f}</text>')
            parts.append(f'<text x="{x+50}" y="{y+54}" text-anchor="middle" font-family="sans-serif" font-size="12">{row["projection_supported"]}/{row["attempted"]}</text>')
    parts.append('<text x="410" y="392" text-anchor="middle" font-family="sans-serif" font-size="13">Printed values give projection-supported fraction and supported/planned attempts.</text>')
    parts.append('</svg>')
    return "\n".join(parts) + "\n"


def _stage3_ordering_svg(domains: list[dict[str, Any]]) -> str:
    width, height = 860, 410
    parts = _svg_header(
        width,
        height,
        "Warning ordering in calibrated domains",
        "Stacked bars compare lead, tie, and lag counts in the symmetric bridge and directional transition. Every segment is directly labelled with its category and count.",
        "figure5",
    )
    colors = {"lead": "#4c78a8", "tie": "#f2cf5b", "lag": "#e45756"}
    for i, domain in enumerate(domains):
        agg = domain["aggregate_ordering_across_six_endpoints"]
        total = agg["valid_pairs"]
        x, y, bar_w = 250, 105 + i*130, 520
        label = html.escape(str(domain["domain"]["label"]))
        parts.append(f'<text x="230" y="{y+25}" text-anchor="end" font-family="sans-serif" font-size="15">{label}</text>')
        cursor = x
        for name in ("lead", "tie", "lag"):
            value = agg[name]
            w = bar_w * value / total if total else 0
            parts.append(f'<rect x="{cursor}" y="{y}" width="{w}" height="40" fill="{colors[name]}" stroke="#222" stroke-width="0.8"/>')
            if value:
                text_fill = "#111" if name == "tie" else "white"
                parts.append(f'<text x="{cursor+w/2}" y="{y+26}" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="{text_fill}">{name} {value}</text>')
            cursor += w
        parts.append(f'<text x="{x}" y="{y+63}" font-family="sans-serif" font-size="13">valid endpoint comparisons = {total}</text>')
    parts.append('<text x="430" y="380" text-anchor="middle" font-family="sans-serif" font-size="13">Endpoint comparisons are correlated within trajectories; bars are descriptive Type S evidence.</text>')
    parts.append('</svg>')
    return "\n".join(parts) + "\n"


def _stage3_lead_time_svg(domains: list[dict[str, Any]]) -> str:
    width, height = 980, 500
    parts = _svg_header(
        width,
        height,
        "Median positive warning lead time",
        "Paired bars compare median positive lead time across six diversity endpoints. Each bar is directly marked S for symmetric bridge or D for directional transition and labelled with its value.",
        "figure6",
    )
    endpoints = ["H_alpha_0.05", "H_alpha_0.10", "H_alpha_0.20", "H_gamma_0.05", "H_gamma_0.10", "H_gamma_0.20"]
    max_value = max(domain["endpoint_summary"][endpoint]["median_positive_lead_time"] for domain in domains for endpoint in endpoints)
    colors = ["#4c78a8", "#f58518"]
    codes = ["S", "D"]
    x0, y0, group_w, plot_h = 105, 110, 135, 285
    for j, endpoint in enumerate(endpoints):
        x = x0 + j*group_w
        endpoint_label = html.escape(endpoint.replace("H_alpha", "Hα").replace("H_gamma", "Hγ"))
        parts.append(f'<text x="{x+42}" y="438" text-anchor="middle" font-family="sans-serif" font-size="12" transform="rotate(25 {x+42} 438)">{endpoint_label}</text>')
        for i, domain in enumerate(domains):
            value = domain["endpoint_summary"][endpoint]["median_positive_lead_time"]
            h = plot_h * value / max_value
            bx = x + i*42
            by = y0 + plot_h - h
            parts.append(f'<rect x="{bx}" y="{by}" width="36" height="{h}" fill="{colors[i]}" stroke="#222" stroke-width="0.8"/>')
            parts.append(f'<text x="{bx+18}" y="{by-7}" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold">{value}</text>')
            parts.append(f'<text x="{bx+18}" y="{y0+plot_h-8}" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="white">{codes[i]}</text>')
    legend_y = 66
    for i, domain in enumerate(domains):
        label = html.escape(str(domain["domain"]["label"]))
        parts.append(f'<rect x="650" y="{legend_y+i*24}" width="18" height="18" fill="{colors[i]}" stroke="#222"/><text x="676" y="{legend_y+14+i*24}" font-family="sans-serif" font-size="13">{codes[i]} — {label}</text>')
    parts.append('</svg>')
    return "\n".join(parts) + "\n"
