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


def write_stage3_figures(audit_path: str | Path, output_dir: str | Path) -> None:
    audit = json.loads(Path(audit_path).read_text(encoding="utf-8"))
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    (out / "figure4_stage3_cumulative_incidence.svg").write_text(
        _stage3_cumulative_incidence_svg(audit["domains"]), encoding="utf-8"
    )
    (out / "figure5_stage3_availability_ordering.svg").write_text(
        _stage3_availability_ordering_svg(audit["domains"]), encoding="utf-8"
    )
    (out / "figure6_stage3_lead_time_normalized.svg").write_text(
        _stage3_lead_time_svg(audit["domains"]), encoding="utf-8"
    )


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
            fill = f'rgb({shade},{shade},255)'
            x, y = x0 + j*cell_w, y0 + i*cell_h
            parts.append(f'<rect x="{x}" y="{y}" width="100" height="74" fill="{fill}" stroke="#222" stroke-width="1.5"/>')
            parts.append(f'<text x="{x+50}" y="{y+31}" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="bold">{rate:.2f}</text>')
            parts.append(f'<text x="{x+50}" y="{y+54}" text-anchor="middle" font-family="sans-serif" font-size="12">{row["projection_supported"]}/{row["attempted"]}</text>')
    parts.append('<text x="410" y="392" text-anchor="middle" font-family="sans-serif" font-size="13">Printed values give projection-supported fraction and supported/planned attempts.</text>')
    parts.append('</svg>')
    return "\n".join(parts) + "\n"


_DOMAIN_LABELS = {
    "recalibrated_symmetric_domain": "Recalibrated symmetric domain",
    "directional_calibrated_domain": "Directional calibrated domain",
}


def _endpoint_label(endpoint: str) -> str:
    return html.escape(endpoint.replace("H_alpha", "Hα").replace("H_gamma", "Hγ").replace("_", " "))


def _polyline(points: list[tuple[float, float]]) -> str:
    return " ".join(f"{x:.2f},{y:.2f}" for x, y in points)


def _stage3_cumulative_incidence_svg(domains: dict[str, Any]) -> str:
    width, height = 1180, 760
    parts = _svg_header(
        width,
        height,
        "Cumulative warning and functional-loss incidence",
        "Four panels retain all baseline-eligible completed trajectories. Rows show H-alpha and H-gamma warning families; columns show the recalibrated symmetric and directional calibrated domains. Curves give cumulative observed incidence across the calibrated horizon for 5, 10, and 20 percent relative warnings and realised functional-trait loss.",
        "figure4",
    )
    domain_order = ("recalibrated_symmetric_domain", "directional_calibrated_domain")
    diversity_order = ("H_alpha", "H_gamma")
    colors = {0.05: "#3b82f6", 0.10: "#8b5cf6", 0.20: "#ea580c"}
    dashes = {0.05: "", 0.10: "8,5", 0.20: "3,4"}
    lefts = (90, 640)
    tops = (105, 395)
    plot_w, plot_h = 450, 225

    for col, domain in enumerate(domain_order):
        domain_data = domains[domain]
        horizon = int(domain_data["schedule"]["horizon"])
        for row, diversity in enumerate(diversity_order):
            left, top = lefts[col], tops[row]
            parts.append(f'<rect x="{left}" y="{top}" width="{plot_w}" height="{plot_h}" fill="white" stroke="#444" stroke-width="1"/>')
            if row == 0:
                label = html.escape(_DOMAIN_LABELS[domain])
                parts.append(f'<text x="{left+plot_w/2}" y="{top-34}" text-anchor="middle" font-family="sans-serif" font-size="15" font-weight="bold">{label}</text>')
                parts.append(f'<text x="{left+plot_w/2}" y="{top-14}" text-anchor="middle" font-family="sans-serif" font-size="12">calibrated horizon = {horizon} generations</text>')
            parts.append(f'<text x="{left-55}" y="{top+plot_h/2}" text-anchor="middle" font-family="sans-serif" font-size="15" font-weight="bold" transform="rotate(-90 {left-55} {top+plot_h/2})'>{"Hα" if diversity=="H_alpha" else "Hγ"}</text>')

            for tick in range(5):
                frac = tick / 4
                x = left + frac * plot_w
                y = top + plot_h - frac * plot_h
                parts.append(f'<line x1="{x}" y1="{top+plot_h}" x2="{x}" y2="{top+plot_h+6}" stroke="#333"/>')
                parts.append(f'<text x="{x}" y="{top+plot_h+22}" text-anchor="middle" font-family="sans-serif" font-size="10">{round(horizon*frac)}</text>')
                parts.append(f'<line x1="{left-6}" y1="{y}" x2="{left}" y2="{y}" stroke="#333"/>')
                parts.append(f'<text x="{left-10}" y="{y+4}" text-anchor="end" font-family="sans-serif" font-size="10">{frac:.2f}</text>')
            parts.append(f'<text x="{left+plot_w/2}" y="{top+plot_h+43}" text-anchor="middle" font-family="sans-serif" font-size="11">generation</text>')
            parts.append(f'<text x="{left-43}" y="{top+plot_h/2}" text-anchor="middle" font-family="sans-serif" font-size="11" transform="rotate(-90 {left-43} {top+plot_h/2})">cumulative observed incidence</text>')

            loss_endpoint = f"{diversity}_0.05"
            loss_series = domain_data["cumulative_event_incidence"][loss_endpoint]["series"]
            loss_points = [(left + plot_w * item["generation"] / horizon, top + plot_h * (1-item["trait_loss_incidence"])) for item in loss_series]
            parts.append(f'<polyline points="{_polyline(loss_points)}" fill="none" stroke="#111" stroke-width="3"/>')
            for fraction in (0.05, 0.10, 0.20):
                endpoint = f"{diversity}_{fraction:.2f}"
                series = domain_data["cumulative_event_incidence"][endpoint]["series"]
                points = [(left + plot_w * item["generation"] / horizon, top + plot_h * (1-item["warning_incidence"])) for item in series]
                dash = f' stroke-dasharray="{dashes[fraction]}"' if dashes[fraction] else ""
                parts.append(f'<polyline points="{_polyline(points)}" fill="none" stroke="{colors[fraction]}" stroke-width="2.2"{dash}/>')
            n_value = domain_data["cumulative_event_incidence"][loss_endpoint]["baseline_eligible_completed"]
            parts.append(f'<text x="{left+plot_w-5}" y="{top+18}" text-anchor="end" font-family="sans-serif" font-size="10">baseline-eligible completed n={n_value}</text>')

    legend_y = 705
    parts.append(f'<line x1="160" y1="{legend_y}" x2="205" y2="{legend_y}" stroke="#111" stroke-width="3"/><text x="215" y="{legend_y+4}" font-family="sans-serif" font-size="12">functional-trait loss</text>')
    for i, fraction in enumerate((0.05, 0.10, 0.20)):
        x = 390 + i*215
        dash = f' stroke-dasharray="{dashes[fraction]}"' if dashes[fraction] else ""
        parts.append(f'<line x1="{x}" y1="{legend_y}" x2="{x+45}" y2="{legend_y}" stroke="{colors[fraction]}" stroke-width="2.2"{dash}/><text x="{x+55}" y="{legend_y+4}" font-family="sans-serif" font-size="12">{int(fraction*100)}% relative warning</text>')
    parts.append("</svg>")
    return "\n".join(parts) + "\n"


def _stage3_availability_ordering_svg(domains: dict[str, Any]) -> str:
    width, height = 1280, 760
    parts = _svg_header(
        width,
        height,
        "Warning availability, censoring and ordering",
        "Each horizontal bar represents 100 attempted trajectories for one warning endpoint. Segment counts show source-preparation failure, baseline ineligibility, both events censored, warning censoring, trait-loss censoring, lead, tie, and lag. The full attempted denominator is retained so differences in valid-pair availability remain visible.",
        "figure5",
    )
    domain_order = ("recalibrated_symmetric_domain", "directional_calibrated_domain")
    endpoints = ("H_alpha_0.05", "H_alpha_0.10", "H_alpha_0.20", "H_gamma_0.05", "H_gamma_0.10", "H_gamma_0.20")
    categories = (
        ("source_preparation_failed", "SF", "#d1d5db"),
        ("baseline_ineligible", "BI", "#9ca3af"),
        ("both_censored", "BC", "#c4b5fd"),
        ("warning_censored", "WC", "#f9a8d4"),
        ("trait_loss_censored", "TC", "#a7f3d0"),
        ("lead", "Lead", "#2563eb"),
        ("tie", "Tie", "#facc15"),
        ("lag", "Lag", "#dc2626"),
    )
    panel_lefts = (110, 690)
    plot_w = 480
    top = 105
    bar_h = 42
    gap = 78

    for di, domain in enumerate(domain_order):
        left = panel_lefts[di]
        label = html.escape(_DOMAIN_LABELS[domain])
        parts.append(f'<text x="{left+plot_w/2}" y="78" text-anchor="middle" font-family="sans-serif" font-size="16" font-weight="bold">{label}</text>')
        for ei, endpoint in enumerate(endpoints):
            y = top + ei*gap
            parts.append(f'<text x="{left-15}" y="{y+26}" text-anchor="end" font-family="sans-serif" font-size="12">{_endpoint_label(endpoint)}</text>')
            counts = domains[domain]["endpoints"][endpoint]["counts"]
            cursor = left
            for key, code, fill in categories:
                value = int(counts[key])
                seg_w = plot_w * value / 100.0
                if value:
                    parts.append(f'<rect x="{cursor:.2f}" y="{y}" width="{seg_w:.2f}" height="{bar_h}" fill="{fill}" stroke="white" stroke-width="0.8"/>')
                    if seg_w >= 30:
                        text_fill = "white" if key in ("lead", "lag") else "#111"
                        parts.append(f'<text x="{cursor+seg_w/2:.2f}" y="{y+26}" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="{text_fill}">{code} {value}</text>')
                cursor += seg_w
            valid = int(domains[domain]["endpoints"][endpoint]["valid_pairs"])
            parts.append(f'<text x="{left+plot_w}" y="{y+58}" text-anchor="end" font-family="sans-serif" font-size="10">valid pairs={valid}/100</text>')
        for tick in (0, 20, 40, 60, 80, 100):
            x = left + plot_w * tick / 100
            parts.append(f'<text x="{x}" y="610" text-anchor="middle" font-family="sans-serif" font-size="11">{tick}</text>')
        parts.append(f'<text x="{left+plot_w/2}" y="635" text-anchor="middle" font-family="sans-serif" font-size="12">attempted trajectories per endpoint</text>')

    legend_y = 675
    x = 70
    for key, code, fill in categories:
        parts.append(f'<rect x="{x}" y="{legend_y}" width="18" height="18" fill="{fill}" stroke="#555"/>')
        label = {"source_preparation_failed":"source failure","baseline_ineligible":"baseline ineligible","both_censored":"both censored","warning_censored":"warning censored","trait_loss_censored":"trait-loss censored","lead":"lead","tie":"tie","lag":"lag"}[key]
        parts.append(f'<text x="{x+24}" y="{legend_y+14}" font-family="sans-serif" font-size="11">{code}: {html.escape(label)}</text>')
        x += 145 if key not in ("source_preparation_failed", "baseline_ineligible", "trait_loss_censored") else 170
    parts.append('<text x="640" y="735" text-anchor="middle" font-family="sans-serif" font-size="11">Bars retain source failures and censored outcomes; valid-pair ordering is not normalized to equal bar length.</text>')
    parts.append("</svg>")
    return "\n".join(parts) + "\n"


def _stage3_lead_time_svg(domains: dict[str, Any]) -> str:
    width, height = 1280, 820
    parts = _svg_header(
        width,
        height,
        "Positive warning lead time before functional-trait loss",
        "Two panels show conventional median positive lead time with trajectory-bootstrap 95 percent intervals. Panel A uses generations; Panel B divides each lead time by that domain's calibrated deterioration horizon. Point labels give the number of leading trajectories contributing to the median.",
        "figure6",
    )
    domain_order = ("recalibrated_symmetric_domain", "directional_calibrated_domain")
    endpoints = ("H_alpha_0.05", "H_alpha_0.10", "H_alpha_0.20", "H_gamma_0.05", "H_gamma_0.10", "H_gamma_0.20")
    colors = {"recalibrated_symmetric_domain": "#2563eb", "directional_calibrated_domain": "#ea580c"}
    shapes = {"recalibrated_symmetric_domain": "circle", "directional_calibrated_domain": "square"}
    panel_specs = (
        ("A", "median_positive_lead_time", "generations", 0.0, 185.0, 85, 100, 500, 500),
        ("B", "median_positive_lead_fraction_of_horizon", "fraction of calibrated horizon", 0.0, 0.82, 690, 100, 500, 500),
    )

    for panel, metric, ylabel, ymin, ymax, left, top, plot_w, plot_h in panel_specs:
        parts.append(f'<text x="{left-48}" y="{top-28}" font-family="sans-serif" font-size="16" font-weight="bold">{panel}</text>')
        parts.append(f'<rect x="{left}" y="{top}" width="{plot_w}" height="{plot_h}" fill="white" stroke="#444"/>')
        ticks = 5
        for t in range(ticks + 1):
            frac = t / ticks
            y = top + plot_h - frac*plot_h
            value = ymin + frac*(ymax-ymin)
            label = f"{value:.1f}" if metric.endswith("horizon") else f"{value:.0f}"
            parts.append(f'<line x1="{left-6}" y1="{y}" x2="{left}" y2="{y}" stroke="#333"/>')
            parts.append(f'<text x="{left-10}" y="{y+4}" text-anchor="end" font-family="sans-serif" font-size="11">{label}</text>')
            parts.append(f'<line x1="{left}" y1="{y}" x2="{left+plot_w}" y2="{y}" stroke="#eee"/>')
        parts.append(f'<text x="{left-60}" y="{top+plot_h/2}" text-anchor="middle" font-family="sans-serif" font-size="12" transform="rotate(-90 {left-60} {top+plot_h/2})">{html.escape(ylabel)}</text>')

        group_w = plot_w / len(endpoints)
        for ei, endpoint in enumerate(endpoints):
            center = left + group_w*(ei+0.5)
            parts.append(f'<text x="{center}" y="{top+plot_h+35}" text-anchor="end" font-family="sans-serif" font-size="11" transform="rotate(-28 {center} {top+plot_h+35})">{_endpoint_label(endpoint)}</text>')
            offsets = (-12, 12)
            for di, domain in enumerate(domain_order):
                point = domains[domain]["endpoints"][endpoint][metric]
                ci = domains[domain]["endpoint_bootstrap_95_ci"][endpoint][metric]
                lo, hi = ci["lower"], ci["upper"]
                x = center + offsets[di]
                def yy(value: float) -> float:
                    return top + plot_h - (float(value)-ymin)/(ymax-ymin)*plot_h
                y = yy(point)
                ylo, yhi = yy(lo), yy(hi)
                parts.append(f'<line x1="{x}" y1="{yhi}" x2="{x}" y2="{ylo}" stroke="{colors[domain]}" stroke-width="2"/>')
                parts.append(f'<line x1="{x-5}" y1="{yhi}" x2="{x+5}" y2="{yhi}" stroke="{colors[domain]}" stroke-width="2"/>')
                parts.append(f'<line x1="{x-5}" y1="{ylo}" x2="{x+5}" y2="{ylo}" stroke="{colors[domain]}" stroke-width="2"/>')
                if shapes[domain] == "circle":
                    parts.append(f'<circle cx="{x}" cy="{y}" r="5.5" fill="{colors[domain]}" stroke="#111"/>')
                else:
                    parts.append(f'<rect x="{x-5.5}" y="{y-5.5}" width="11" height="11" fill="{colors[domain]}" stroke="#111"/>')
                n = domains[domain]["endpoints"][endpoint]["positive_leads"]
                parts.append(f'<text x="{x}" y="{max(top+12, y-12)}" text-anchor="middle" font-family="sans-serif" font-size="9">n={n}</text>')

    legend_y = 700
    parts.append(f'<circle cx="230" cy="{legend_y}" r="6" fill="{colors["recalibrated_symmetric_domain"]}" stroke="#111"/>')
    parts.append(f'<text x="245" y="{legend_y+4}" font-family="sans-serif" font-size="12">Recalibrated symmetric domain: horizon 240 (ramp 30 + hold 210)</text>')
    parts.append(f'<rect x="224" y="{legend_y+24}" width="12" height="12" fill="{colors["directional_calibrated_domain"]}" stroke="#111"/>')
    parts.append(f'<text x="245" y="{legend_y+34}" font-family="sans-serif" font-size="12">Directional calibrated domain: horizon 120 (ramp 30 + hold 90)</text>')
    parts.append('<text x="640" y="785" text-anchor="middle" font-family="sans-serif" font-size="11">Intervals are percentile 95% bootstrap intervals resampling whole trajectories; absolute timing is not a single-factor transition-direction contrast.</text>')
    parts.append("</svg>")
    return "\n".join(parts) + "\n"
