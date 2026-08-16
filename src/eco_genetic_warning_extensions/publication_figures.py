"""Publication-facing source aggregation and Stage III figure generation."""
from __future__ import annotations

import csv
import html
import json
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable

STAGE1_RUN_IDS = (
    29177214259, 29186610167, 29188592519,
    29188748077, 29190149319, 29190149344,
)
DOMAIN_ORDER = ("recalibrated_symmetric_domain", "directional_calibrated_domain")
DOMAIN_LABELS = {
    "recalibrated_symmetric_domain": "Recalibrated symmetric domain",
    "directional_calibrated_domain": "Directional calibrated domain",
}
ENDPOINTS = (
    "H_alpha_0.05", "H_alpha_0.10", "H_alpha_0.20",
    "H_gamma_0.05", "H_gamma_0.10", "H_gamma_0.20",
)


def _load_stage1_jsons(root: str | Path) -> list[dict[str, Any]]:
    records = []
    for path in sorted(Path(root).rglob("*.json")):
        try:
            value = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue
        if isinstance(value, dict) and value.get("stage") == "Protocol 002 Stage I source reconstruction batch":
            records.append(value)
    return records


def aggregate_stage1(root: str | Path) -> dict[str, Any]:
    records = _load_stage1_jsons(root)
    by_index = {int(row["campaign"]["batch_index"]): row for row in records}
    expected = set(range(135))
    if set(by_index) != expected:
        raise ValueError(
            "Stage I artifact coverage mismatch; "
            f"missing={sorted(expected-set(by_index))}, extra={sorted(set(by_index)-expected)}"
        )

    grouped: dict[tuple[float, float], dict[str, Any]] = defaultdict(
        lambda: {
            "attempted": 0, "source_supported": 0, "source_prepared": 0,
            "projection_supported": 0, "projection_failed": 0,
            "projection_not_run": 0,
        }
    )
    for index in range(135):
        row = by_index[index]
        cell = row["cell"]
        key = (float(cell["kappa_mu"]), float(cell["p_star"]))
        target = grouped[key]
        target["kappa_mu"], target["p_star"] = key
        target["attempted"] += int(row["campaign"]["attempts_per_batch"])
        for name in (
            "source_supported", "source_prepared", "projection_supported",
            "projection_failed", "projection_not_run",
        ):
            target[name] += int(row["status_counts"][name])

    rows = []
    for key in sorted(grouped):
        row = grouped[key]
        for name in ("source_supported", "source_prepared", "projection_supported"):
            row[f"{name}_rate"] = row[name] / row["attempted"]
        rows.append(row)
    totals = {
        name: sum(int(row[name]) for row in rows)
        for name in (
            "attempted", "source_supported", "source_prepared",
            "projection_supported", "projection_failed", "projection_not_run",
        )
    }
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
    (out / "stage1_publication_summary.json").write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    fields = [
        "kappa_mu", "p_star", "attempted", "source_supported", "source_supported_rate",
        "source_prepared", "source_prepared_rate", "projection_supported",
        "projection_supported_rate", "projection_failed", "projection_not_run",
    ]
    with (out / "stage1_coordinate_summary.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows({field: row[field] for field in fields} for row in result["coordinates"])
    (out / "figure2_stage1_source_feasibility.svg").write_text(
        _stage1_svg(result["coordinates"]), encoding="utf-8"
    )
    return result


def _header(width: int, height: int, title: str, desc: str, identifier: str) -> list[str]:
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="{identifier}-title {identifier}-desc">',
        f'<title id="{identifier}-title">{html.escape(title)}</title>',
        f'<desc id="{identifier}-desc">{html.escape(desc)}</desc>',
        '<rect width="100%" height="100%" fill="white"/>',
        f'<text x="30" y="36" font-family="sans-serif" font-size="20" font-weight="bold">{html.escape(title)}</text>',
    ]


def _stage1_svg(rows: Iterable[dict[str, Any]]) -> str:
    rows = list(rows)
    parts = _header(
        820, 420, "Source feasibility across transition coordinates",
        "A fifteen-cell map of projection-supported source fractions. Every cell prints the fraction and supported/planned attempts, so values do not depend on colour.",
        "figure2",
    )
    p_values = sorted({float(row["p_star"]) for row in rows})
    k_values = sorted({float(row["kappa_mu"]) for row in rows})
    lookup = {(float(row["kappa_mu"]), float(row["p_star"])): row for row in rows}
    x0, y0, cell_w, cell_h = 170, 82, 112, 88
    for j, p_star in enumerate(p_values):
        parts.append(f'<text x="{x0+j*cell_w+48}" y="68" text-anchor="middle" font-family="sans-serif" font-size="14">p*={p_star:.2f}</text>')
    for i, kappa_mu in enumerate(k_values):
        y = y0 + i * cell_h
        parts.append(f'<text x="152" y="{y+38}" text-anchor="end" font-family="sans-serif" font-size="14">κμ={kappa_mu:.2f}</text>')
        for j, p_star in enumerate(p_values):
            row = lookup[(kappa_mu, p_star)]
            rate = float(row["projection_supported_rate"])
            shade = int(245 - 170 * rate)
            x = x0 + j * cell_w
            parts.append(f'<rect x="{x}" y="{y}" width="100" height="74" fill="rgb({shade},{shade},255)" stroke="#222" stroke-width="1.5"/>')
            parts.append(f'<text x="{x+50}" y="{y+31}" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="bold">{rate:.2f}</text>')
            parts.append(f'<text x="{x+50}" y="{y+54}" text-anchor="middle" font-family="sans-serif" font-size="12">{row["projection_supported"]}/{row["attempted"]}</text>')
    parts.append('<text x="410" y="392" text-anchor="middle" font-family="sans-serif" font-size="13">Printed values give projection-supported fraction and supported/planned attempts.</text>')
    parts.append('</svg>')
    return "\n".join(parts) + "\n"


def _endpoint_label(endpoint: str) -> str:
    return html.escape(endpoint.replace("H_alpha", "Hα").replace("H_gamma", "Hγ").replace("_", " "))


def _polyline(points: list[tuple[float, float]]) -> str:
    return " ".join(f"{x:.2f},{y:.2f}" for x, y in points)


def _stage3_cumulative_incidence_svg(domains: dict[str, Any]) -> str:
    width, height = 1180, 760
    parts = _header(
        width, height, "Cumulative warning and functional-loss incidence",
        "Four panels retain all baseline-eligible completed trajectories. Rows show H-alpha and H-gamma; columns show the recalibrated symmetric and directional calibrated domains. Curves give cumulative observed warning and functional-loss incidence across each calibrated horizon.",
        "figure4",
    )
    colors = {0.05: "#2563eb", 0.10: "#7c3aed", 0.20: "#ea580c"}
    dashes = {0.05: "", 0.10: "8,5", 0.20: "3,4"}
    lefts, tops = (90, 640), (105, 395)
    plot_w, plot_h = 450, 225

    for col, domain in enumerate(DOMAIN_ORDER):
        data = domains[domain]
        horizon = int(data["schedule"]["horizon"])
        for row_index, diversity in enumerate(("H_alpha", "H_gamma")):
            left, top = lefts[col], tops[row_index]
            parts.append(f'<rect x="{left}" y="{top}" width="{plot_w}" height="{plot_h}" fill="white" stroke="#444"/>')
            if row_index == 0:
                parts.append(f'<text x="{left+plot_w/2}" y="{top-34}" text-anchor="middle" font-family="sans-serif" font-size="15" font-weight="bold">{html.escape(DOMAIN_LABELS[domain])}</text>')
                parts.append(f'<text x="{left+plot_w/2}" y="{top-14}" text-anchor="middle" font-family="sans-serif" font-size="12">calibrated horizon = {horizon} generations</text>')
            row_label = "Hα" if diversity == "H_alpha" else "Hγ"
            parts.append(f'<text x="{left-55}" y="{top+plot_h/2}" text-anchor="middle" font-family="sans-serif" font-size="15" font-weight="bold" transform="rotate(-90 {left-55} {top+plot_h/2})">{row_label}</text>')

            for tick in range(5):
                frac = tick / 4
                x = left + frac * plot_w
                y = top + plot_h - frac * plot_h
                parts.append(f'<line x1="{x}" y1="{top+plot_h}" x2="{x}" y2="{top+plot_h+6}" stroke="#333"/>')
                parts.append(f'<text x="{x}" y="{top+plot_h+23}" text-anchor="middle" font-family="sans-serif" font-size="11">{frac:.2g}</text>')
                parts.append(f'<line x1="{left-6}" y1="{y}" x2="{left}" y2="{y}" stroke="#333"/>')
                parts.append(f'<text x="{left-10}" y="{y+4}" text-anchor="end" font-family="sans-serif" font-size="11">{frac:.2g}</text>')
            if row_index == 1:
                parts.append(f'<text x="{left+plot_w/2}" y="{top+plot_h+48}" text-anchor="middle" font-family="sans-serif" font-size="12">fraction of calibrated horizon</text>')
            if col == 0:
                parts.append(f'<text x="{left-74}" y="{top+plot_h/2}" text-anchor="middle" font-family="sans-serif" font-size="11" transform="rotate(-90 {left-74} {top+plot_h/2})">cumulative observed incidence</text>')

            loss_key = f"{diversity}_0.05"
            series = data["cumulative_event_incidence"][loss_key]["series"]
            loss_points = [
                (left + plot_w * item["generation"] / horizon,
                 top + plot_h * (1 - item["trait_loss_incidence"]))
                for item in series
            ]
            parts.append(f'<polyline points="{_polyline(loss_points)}" fill="none" stroke="#111" stroke-width="3"/>')
            for fraction in (0.05, 0.10, 0.20):
                endpoint = f"{diversity}_{fraction:.2f}"
                series = data["cumulative_event_incidence"][endpoint]["series"]
                points = [
                    (left + plot_w * item["generation"] / horizon,
                     top + plot_h * (1 - item["warning_incidence"]))
                    for item in series
                ]
                dash = f' stroke-dasharray="{dashes[fraction]}"' if dashes[fraction] else ""
                parts.append(f'<polyline points="{_polyline(points)}" fill="none" stroke="{colors[fraction]}" stroke-width="2.2"{dash}/>')
            n_value = data["cumulative_event_incidence"][loss_key]["baseline_eligible_completed"]
            parts.append(f'<text x="{left+plot_w-5}" y="{top+18}" text-anchor="end" font-family="sans-serif" font-size="10">baseline-eligible completed n={n_value}</text>')

    legend_y = 705
    parts.append(f'<line x1="120" y1="{legend_y}" x2="165" y2="{legend_y}" stroke="#111" stroke-width="3"/><text x="175" y="{legend_y+4}" font-family="sans-serif" font-size="12">functional-trait loss</text>')
    for i, fraction in enumerate((0.05, 0.10, 0.20)):
        x = 370 + i * 220
        dash = f' stroke-dasharray="{dashes[fraction]}"' if dashes[fraction] else ""
        parts.append(f'<line x1="{x}" y1="{legend_y}" x2="{x+45}" y2="{legend_y}" stroke="{colors[fraction]}" stroke-width="2.2"{dash}/><text x="{x+55}" y="{legend_y+4}" font-family="sans-serif" font-size="12">{int(fraction*100)}% relative warning</text>')
    parts.append('</svg>')
    return "\n".join(parts) + "\n"


def _stage3_availability_ordering_svg(domains: dict[str, Any]) -> str:
    width, height = 1280, 760
    parts = _header(
        width, height, "Warning availability, censoring and ordering",
        "Each horizontal bar represents 100 attempted trajectories for one warning endpoint. Segment counts retain source failure, baseline ineligibility, both-censored, warning-censored, trait-loss-censored, lead, tie and lag outcomes so differences in availability remain visible.",
        "figure5",
    )
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
    panel_lefts, plot_w, top, bar_h, gap = (110, 690), 480, 105, 42, 78
    for domain_index, domain in enumerate(DOMAIN_ORDER):
        left = panel_lefts[domain_index]
        parts.append(f'<text x="{left+plot_w/2}" y="78" text-anchor="middle" font-family="sans-serif" font-size="16" font-weight="bold">{html.escape(DOMAIN_LABELS[domain])}</text>')
        for endpoint_index, endpoint in enumerate(ENDPOINTS):
            y = top + endpoint_index * gap
            parts.append(f'<text x="{left-15}" y="{y+26}" text-anchor="end" font-family="sans-serif" font-size="12">{_endpoint_label(endpoint)}</text>')
            counts = domains[domain]["endpoints"][endpoint]["counts"]
            cursor = left
            for key, code, fill in categories:
                value = int(counts[key])
                seg_w = plot_w * value / 100
                if value:
                    parts.append(f'<rect x="{cursor:.2f}" y="{y}" width="{seg_w:.2f}" height="{bar_h}" fill="{fill}" stroke="white"/>')
                    if seg_w >= 30:
                        text_fill = "white" if key in ("lead", "lag") else "#111"
                        parts.append(f'<text x="{cursor+seg_w/2:.2f}" y="{y+26}" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="{text_fill}">{code} {value}</text>')
                cursor += seg_w
            valid = int(domains[domain]["endpoints"][endpoint]["valid_pairs"])
            parts.append(f'<text x="{left+plot_w}" y="{y+58}" text-anchor="end" font-family="sans-serif" font-size="10">valid pairs={valid}/100</text>')
        for tick in (0, 20, 40, 60, 80, 100):
            x = left + plot_w * tick / 100
            parts.append(f'<text x="{x}" y="610" text-anchor="middle" font-family="sans-serif" font-size="11">{tick}</text>')
        parts.append(f'<text x="{left+plot_w/2}" y="635" text-anchor="middle" font-family="sans-serif" font-size="12">100 attempted trajectories per endpoint</text>')

    legend_y, x = 675, 50
    labels = {
        "source_preparation_failed": "source failure", "baseline_ineligible": "baseline ineligible",
        "both_censored": "both censored", "warning_censored": "warning censored",
        "trait_loss_censored": "trait-loss censored", "lead": "lead", "tie": "tie", "lag": "lag",
    }
    for key, code, fill in categories:
        parts.append(f'<rect x="{x}" y="{legend_y}" width="18" height="18" fill="{fill}" stroke="#555"/>')
        parts.append(f'<text x="{x+24}" y="{legend_y+14}" font-family="sans-serif" font-size="10">{code}: {html.escape(labels[key])}</text>')
        x += 150
    parts.append('<text x="640" y="735" text-anchor="middle" font-family="sans-serif" font-size="11">Bars retain failures and censored outcomes; endpoint rows within trajectories are correlated.</text>')
    parts.append('</svg>')
    return "\n".join(parts) + "\n"


def _stage3_lead_time_svg(domains: dict[str, Any]) -> str:
    width, height = 1280, 820
    parts = _header(
        width, height, "Positive warning lead time before functional-trait loss",
        "Panel A shows conventional median positive lead time in generations; Panel B divides lead time by each domain's calibrated deterioration horizon. Whiskers are percentile 95 percent intervals from whole-trajectory bootstrap resampling and point labels show leading-trajectory counts.",
        "figure6",
    )
    colors = {
        "recalibrated_symmetric_domain": "#2563eb",
        "directional_calibrated_domain": "#ea580c",
    }
    panel_specs = (
        ("A", "median_positive_lead_time", "generations", 0.0, 180.0, 85),
        ("B", "median_positive_lead_fraction_of_horizon", "fraction of calibrated horizon", 0.0, 0.82, 690),
    )
    top, plot_w, plot_h = 100, 500, 500
    for panel, metric, ylabel, ymin, ymax, left in panel_specs:
        parts.append(f'<text x="{left-48}" y="{top-28}" font-family="sans-serif" font-size="16" font-weight="bold">{panel}</text>')
        parts.append(f'<rect x="{left}" y="{top}" width="{plot_w}" height="{plot_h}" fill="white" stroke="#444"/>')
        tick_values = (0.0, 50.0, 100.0, 150.0) if metric == "median_positive_lead_time" else (0.0, 0.2, 0.4, 0.6, 0.8)
        for value in tick_values:
            frac = (value-ymin)/(ymax-ymin)
            y = top + plot_h - frac * plot_h
            label = f"{value:.1f}" if metric.endswith("horizon") else f"{value:.0f}"
            parts.append(f'<line x1="{left-6}" y1="{y}" x2="{left}" y2="{y}" stroke="#333"/><text x="{left-10}" y="{y+4}" text-anchor="end" font-family="sans-serif" font-size="11">{label}</text>')
        parts.append(f'<text x="{left-60}" y="{top+plot_h/2}" text-anchor="middle" font-family="sans-serif" font-size="12" transform="rotate(-90 {left-60} {top+plot_h/2})">{html.escape(ylabel)}</text>')
        group_w = plot_w / len(ENDPOINTS)
        for endpoint_index, endpoint in enumerate(ENDPOINTS):
            center = left + group_w * (endpoint_index + 0.5)
            parts.append(f'<text x="{center}" y="{top+plot_h+35}" text-anchor="end" font-family="sans-serif" font-size="11" transform="rotate(-28 {center} {top+plot_h+35})">{_endpoint_label(endpoint)}</text>')
            for domain_index, domain in enumerate(DOMAIN_ORDER):
                point = float(domains[domain]["endpoints"][endpoint][metric])
                interval = domains[domain]["endpoint_bootstrap_95_ci"][endpoint][metric]
                lo, hi = float(interval["lower"]), float(interval["upper"])
                x = center + (-12 if domain_index == 0 else 12)
                def yy(value: float) -> float:
                    return top + plot_h - (value-ymin)/(ymax-ymin)*plot_h
                y, y_lo, y_hi = yy(point), yy(lo), yy(hi)
                parts.append(f'<line x1="{x}" y1="{y_hi}" x2="{x}" y2="{y_lo}" stroke="{colors[domain]}" stroke-width="2"/>')
                parts.append(f'<line x1="{x-5}" y1="{y_hi}" x2="{x+5}" y2="{y_hi}" stroke="{colors[domain]}" stroke-width="2"/><line x1="{x-5}" y1="{y_lo}" x2="{x+5}" y2="{y_lo}" stroke="{colors[domain]}" stroke-width="2"/>')
                if domain_index == 0:
                    parts.append(f'<circle cx="{x}" cy="{y}" r="5.5" fill="{colors[domain]}" stroke="#111"/>')
                else:
                    parts.append(f'<rect x="{x-5.5}" y="{y-5.5}" width="11" height="11" fill="{colors[domain]}" stroke="#111"/>')
                n = int(domains[domain]["endpoints"][endpoint]["positive_leads"])
                parts.append(f'<text x="{x}" y="{max(top+12,y-12)}" text-anchor="middle" font-family="sans-serif" font-size="9">n={n}</text>')

    parts.append(f'<circle cx="180" cy="700" r="6" fill="{colors[DOMAIN_ORDER[0]]}" stroke="#111"/><text x="195" y="704" font-family="sans-serif" font-size="12">Recalibrated symmetric domain: 240 generations (30 + 210)</text>')
    parts.append(f'<rect x="174" y="724" width="12" height="12" fill="{colors[DOMAIN_ORDER[1]]}" stroke="#111"/><text x="195" y="735" font-family="sans-serif" font-size="12">Directional calibrated domain: 120 generations (30 + 90)</text>')
    parts.append('<text x="640" y="785" text-anchor="middle" font-family="sans-serif" font-size="11">Direct D−S bootstrap: all six horizon-normalized 95% intervals include 0; absolute intervals exclude 0 only for Hα 5% and 10%.</text>')
    parts.append('</svg>')
    return "\n".join(parts) + "\n"


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
