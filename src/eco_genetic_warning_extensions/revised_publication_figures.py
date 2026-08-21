"""Publication SVG builders for the condition-recovered manuscript spine.

All figures in this module are deterministic renderings of already locked or
committed summaries. They do not run simulations or inspect new warning fields.
"""
from __future__ import annotations

import csv
import html
import json
from pathlib import Path
from typing import Any, Iterable, Mapping


DOMAIN_ORDER = ("recalibrated_symmetric_domain", "directional_calibrated_domain")
DOMAIN_LABELS = {
    "recalibrated_symmetric_domain": "Recalibrated symmetric",
    "directional_calibrated_domain": "Directional calibrated",
}


def _header(width: int, height: int, title: str, desc: str, identifier: str) -> list[str]:
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="{identifier}-title {identifier}-desc">',
        f'<title id="{identifier}-title">{html.escape(title)}</title>',
        f'<desc id="{identifier}-desc">{html.escape(desc)}</desc>',
        '<rect width="100%" height="100%" fill="white"/>',
        f'<text x="{width/2}" y="36" text-anchor="middle" font-family="sans-serif" font-size="22" font-weight="bold">{html.escape(title)}</text>',
    ]


def _csv_rows(path: str | Path) -> list[dict[str, str]]:
    with Path(path).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _json(path: str | Path) -> dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def figure2_parent_bridge_svg(h3_rows: Iterable[Mapping[str, Any]], h2_rows: Iterable[Mapping[str, Any]]) -> str:
    h3_rows = list(h3_rows)
    h2_rows = list(h2_rows)
    width, height = 1240, 650
    parts = _header(
        width,
        height,
        "Fragmentation creates vulnerability and genetic warning is conditionally possible",
        "Panel A shows paired median reductions under equal isolation for interaction, local effective size, and realised high-trait mass across 1,055 H1-qualified sources. Panel B shows lead and lag counts for relative and absolute genetic-warning definitions in the inherited symmetric benchmark.",
        "figure2",
    )
    parts.append('<text x="55" y="75" font-family="sans-serif" font-size="14" font-weight="bold">A. Paired fragmentation effect</text>')
    labels = {
        "final_interaction": "Interaction",
        "final_local_effective_size": "Local effective size",
        "realised_high_trait_mass": "Realised high-trait mass",
    }
    left, max_w = 210, 390
    for i, row in enumerate(h3_rows):
        y = 125 + i * 120
        metric = str(row["metric"])
        reduction = float(row["median_paired_fractional_reduction"])
        q25 = float(row["paired_fractional_reduction_q25"])
        q75 = float(row["paired_fractional_reduction_q75"])
        parts.append(f'<text x="{left-15}" y="{y+25}" text-anchor="end" font-family="sans-serif" font-size="13">{html.escape(labels[metric])}</text>')
        parts.append(f'<rect x="{left}" y="{y}" width="{max_w}" height="40" rx="5" fill="#e5e7eb"/>')
        parts.append(f'<rect x="{left}" y="{y}" width="{max_w*reduction:.2f}" height="40" rx="5" fill="#4b5563"/>')
        parts.append(f'<text x="{left+8}" y="{y+26}" font-family="sans-serif" font-size="13" fill="white" font-weight="bold">{100*reduction:.2f}% median reduction</text>')
        parts.append(f'<text x="{left}" y="{y+62}" font-family="sans-serif" font-size="11">paired IQR {100*q25:.1f}–{100*q75:.1f}%; n={int(row["h1_qualified_replicates"])}</text>')
    parts.append(f'<text x="{left}" y="520" font-family="sans-serif" font-size="11">Bars encode median paired fractional reduction; printed values are the primary reading channel.</text>')

    panel_x = 690
    parts.append(f'<text x="{panel_x}" y="75" font-family="sans-serif" font-size="14" font-weight="bold">B. Genetic-warning ordering</text>')
    relative = {(r["diversity"]): r for r in h2_rows if r["endpoint_type"] == "relative" and r["threshold"] == "0.20"}
    absolute = {(r["diversity"]): r for r in h2_rows if r["endpoint_type"] == "absolute"}
    display = [
        ("Relative Hα 5/10/20%", relative["H_alpha"]),
        ("Relative Hγ 5/10/20%", relative["H_gamma"]),
        ("Absolute Hα ≤ 0.20", absolute["H_alpha"]),
        ("Absolute Hγ ≤ 0.20", absolute["H_gamma"]),
    ]
    bar_left, bar_w = panel_x + 170, 300
    for i, (label, row) in enumerate(display):
        y = 120 + i * 105
        valid = int(row["valid_pairs"])
        lead, tie, lag = int(row["lead"]), int(row["tie"]), int(row["lag"])
        parts.append(f'<text x="{bar_left-12}" y="{y+25}" text-anchor="end" font-family="sans-serif" font-size="12">{html.escape(label)}</text>')
        x = bar_left
        for value, fill, code in ((lead, "#2563eb", "Lead"), (tie, "#facc15", "Tie"), (lag, "#dc2626", "Lag")):
            w = 0 if valid == 0 else bar_w * value / valid
            if w > 0:
                parts.append(f'<rect x="{x:.2f}" y="{y}" width="{w:.2f}" height="38" fill="{fill}" stroke="white"/>')
                if w > 30:
                    text_fill = "#111" if code == "Tie" else "white"
                    parts.append(f'<text x="{x+w/2:.2f}" y="{y+24}" text-anchor="middle" font-family="sans-serif" font-size="11" fill="{text_fill}">{code} {value}</text>')
            x += w
        parts.append(f'<text x="{bar_left+bar_w+10}" y="{y+24}" font-family="sans-serif" font-size="11">valid n={valid}</text>')
        if row["endpoint_type"] == "relative":
            parts.append(f'<text x="{bar_left}" y="{y+58}" font-family="sans-serif" font-size="10">same 35/0/0 lead/tie/lag at 5%, 10% and 20%</text>')
    parts.append(f'<text x="{panel_x}" y="570" font-family="sans-serif" font-size="11">Relative endpoints: 83 available trajectories, 35 observed functional losses, 48 loss-censored.</text>')
    parts.append('</svg>')
    return "\n".join(parts) + "\n"


def figure3_source_regime_svg(stage1_rows: Iterable[Mapping[str, Any]], stage2_rows: Iterable[Mapping[str, Any]]) -> str:
    stage1_rows = list(stage1_rows)
    stage2_rows = list(stage2_rows)
    width, height = 1280, 610
    parts = _header(
        width,
        height,
        "Recurrent state turnover reorganises source feasibility and functional-loss regime",
        "Panel A maps projection-supported source fractions across 15 recurrent-transition coordinates. Panel B shows the dominant warning-blind functional-loss regime and closest pooled loss rate for the same coordinates. Every cell prints its value or regime code so interpretation does not depend on colour.",
        "figure3",
    )
    p_values = sorted({float(r["p_star"]) for r in stage1_rows})
    k_values = sorted({float(r["kappa_mu"]) for r in stage1_rows})
    s1 = {(float(r["kappa_mu"]), float(r["p_star"])): r for r in stage1_rows}
    s2 = {(float(r["kappa_mu"]), float(r["p_star"])): r for r in stage2_rows}
    cell_w, cell_h = 92, 105
    left_a, left_b, top = 125, 760, 105
    parts.append('<text x="50" y="75" font-family="sans-serif" font-size="14" font-weight="bold">A. Source feasibility</text>')
    parts.append('<text x="685" y="75" font-family="sans-serif" font-size="14" font-weight="bold">B. Functional-loss regime</text>')
    for panel_left in (left_a, left_b):
        for j, p in enumerate(p_values):
            parts.append(f'<text x="{panel_left+j*cell_w+cell_w/2}" y="96" text-anchor="middle" font-family="sans-serif" font-size="11">p*={p:.2f}</text>')
    palette = {"rapid-loss": "#b2182b", "seed-heterogeneous": "#fdae61", "persistence": "#2166ac"}
    codes = {"rapid-loss": "R", "seed-heterogeneous": "H", "persistence": "P"}
    for i, k in enumerate(k_values):
        y = top + i * cell_h
        parts.append(f'<text x="{left_a-12}" y="{y+45}" text-anchor="end" font-family="sans-serif" font-size="11">κμ={k:.2f}</text>')
        parts.append(f'<text x="{left_b-12}" y="{y+45}" text-anchor="end" font-family="sans-serif" font-size="11">κμ={k:.2f}</text>')
        for j, p in enumerate(p_values):
            a = s1[(k, p)]
            rate = float(a["projection_supported_rate"])
            shade = int(245 - 155 * rate)
            x = left_a + j * cell_w
            parts.append(f'<rect x="{x+3}" y="{y+3}" width="{cell_w-6}" height="{cell_h-10}" fill="rgb({shade},{shade},255)" stroke="#222"/>')
            parts.append(f'<text x="{x+cell_w/2}" y="{y+39}" text-anchor="middle" font-family="sans-serif" font-size="15" font-weight="bold">{rate:.2f}</text>')
            parts.append(f'<text x="{x+cell_w/2}" y="{y+62}" text-anchor="middle" font-family="sans-serif" font-size="9">{int(a["projection_supported"])}/{int(a["attempted"])}</text>')

            b = s2[(k, p)]
            regime = str(b["dominant_regime"])
            x2 = left_b + j * cell_w
            text_fill = "#111" if regime == "seed-heterogeneous" else "white"
            parts.append(f'<rect x="{x2+3}" y="{y+3}" width="{cell_w-6}" height="{cell_h-10}" fill="{palette[regime]}" stroke="#222"/>')
            parts.append(f'<text x="{x2+cell_w/2}" y="{y+34}" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="bold" fill="{text_fill}">{codes[regime]}</text>')
            parts.append(f'<text x="{x2+cell_w/2}" y="{y+57}" text-anchor="middle" font-family="sans-serif" font-size="9" fill="{text_fill}">closest P={float(b["closest_pooled_trait_loss_rate"]):.3f}</text>')
            parts.append(f'<text x="{x2+cell_w/2}" y="{y+76}" text-anchor="middle" font-family="sans-serif" font-size="9" fill="{text_fill}">complete n={int(b["complete_candidate_count"])}</text>')
    total_rapid = sum(int(r["rapid_loss_candidate_count"]) for r in stage2_rows)
    total_het = sum(int(r["seed_heterogeneous_candidate_count"]) for r in stage2_rows)
    total_persist = sum(int(r["persistence_candidate_count"]) for r in stage2_rows)
    parts.append(f'<text x="{left_a}" y="520" font-family="sans-serif" font-size="11">Source support: 2,269/3,375 overall; coordinate range 44.89–86.67%.</text>')
    parts.append(f'<text x="{left_b}" y="510" font-family="sans-serif" font-size="11">R rapid={total_rapid}; H heterogeneous={total_het}; P persistence={total_persist}</text>')
    parts.append(f'<text x="{left_b}" y="532" font-family="sans-serif" font-size="11">Original strict R4 candidates = 0; all 15 retained as no_domain_selected.</text>')
    parts.append('</svg>')
    return "\n".join(parts) + "\n"


def _plot_axes(parts: list[str], left: float, top: float, width: float, height: float, *, y_label: str) -> None:
    parts.append(f'<rect x="{left}" y="{top}" width="{width}" height="{height}" fill="white" stroke="#333"/>')
    for frac in (0.0, 0.25, 0.5, 0.75, 1.0):
        y = top + height * (1 - frac)
        parts.append(f'<line x1="{left-5}" y1="{y}" x2="{left}" y2="{y}" stroke="#333"/>')
        parts.append(f'<text x="{left-9}" y="{y+4}" text-anchor="end" font-family="sans-serif" font-size="10">{frac:.2g}</text>')
    parts.append(f'<text x="{left-52}" y="{top+height/2}" text-anchor="middle" font-family="sans-serif" font-size="11" transform="rotate(-90 {left-52} {top+height/2})">{html.escape(y_label)}</text>')


def figure4_r4_recovery_svg(phase_b: Mapping[str, Any], phase_c: Mapping[str, Any], phase_d: Mapping[str, Any]) -> str:
    width, height = 1280, 690
    parts = _header(
        width,
        height,
        "Warning-blind recovery of a narrow reproducible event regime",
        "Panel A shows the fixed B1 rapid-to-persistence frontier in pooled functional-loss rate. Panel B shows independent high-rep seed-block rates; p-star 0.35 satisfies the R4 band in two fresh campaigns while neighbouring coordinates remain seed heterogeneous.",
        "figure4",
    )
    left, top, pw, ph = 95, 115, 500, 420
    parts.append('<text x="55" y="78" font-family="sans-serif" font-size="14" font-weight="bold">A. Pooled rapid-to-persistence frontier</text>')
    _plot_axes(parts, left, top, pw, ph, y_label="pooled functional-loss rate")
    band_y = top + ph * (1 - 0.70)
    band_h = ph * 0.40
    parts.append(f'<rect x="{left}" y="{band_y}" width="{pw}" height="{band_h}" fill="#e5e7eb" opacity="0.7"/>')
    points: list[tuple[float, float, str]] = [(0.25, 1.0, "historical R2")]
    points += [(float(r["p_star"]), float(r["pooled_trait_loss_rate"]), str(r["regime"])) for r in phase_b["cells"]]
    points.append((0.50, 0.0, "historical R1"))
    xmin, xmax = 0.25, 0.50
    coords = []
    for p, rate, regime in points:
        x = left + (p-xmin)/(xmax-xmin)*pw
        y = top + ph*(1-rate)
        coords.append((x, y))
    parts.append('<polyline points="' + ' '.join(f'{x:.1f},{y:.1f}' for x,y in coords) + '" fill="none" stroke="#111" stroke-width="2.5"/>')
    for (p, rate, regime), (x, y) in zip(points, coords):
        parts.append(f'<circle cx="{x}" cy="{y}" r="6" fill="#2563eb" stroke="#111"/>')
        parts.append(f'<text x="{x}" y="{max(top+12,y-12)}" text-anchor="middle" font-family="sans-serif" font-size="9">{rate:.3f}</text>')
        parts.append(f'<text x="{x}" y="{top+ph+22}" text-anchor="middle" font-family="sans-serif" font-size="10">{p:.3g}</text>')
    parts.append(f'<text x="{left+pw/2}" y="{top+ph+48}" text-anchor="middle" font-family="sans-serif" font-size="11">p* at κμ=0.35, fixed B1 ecological/deterioration anchor</text>')
    parts.append(f'<text x="{left+12}" y="{band_y+18}" font-family="sans-serif" font-size="10">R4 operational band 0.30–0.70</text>')

    left2 = 725
    parts.append(f'<text x="{left2-40}" y="78" font-family="sans-serif" font-size="14" font-weight="bold">B. Independent high-rep seed blocks</text>')
    _plot_axes(parts, left2, top, 470, ph, y_label="seed-block functional-loss rate")
    parts.append(f'<rect x="{left2}" y="{band_y}" width="470" height="{band_h}" fill="#e5e7eb" opacity="0.7"/>')
    c_lookup = {float(r["p_star"]): r for r in phase_c["cells"]}
    d_lookup = {float(r["p_star"]): r for r in phase_d["cells"]}
    display = [
        ("0.325 D", d_lookup[0.325]),
        ("0.350 C", c_lookup[0.35]),
        ("0.350 D", d_lookup[0.35]),
        ("0.375 D", d_lookup[0.375]),
        ("0.400 C", c_lookup[0.40]),
    ]
    for i, (label, row) in enumerate(display):
        x = left2 + 48 + i*92
        for j, rate in enumerate(row["seed_rates"]):
            dx = (j-2)*6
            y = top + ph*(1-float(rate))
            parts.append(f'<circle cx="{x+dx}" cy="{y}" r="4" fill="#6b7280" stroke="#111"/>')
        pooled = float(row["pooled_trait_loss_rate"])
        ypool = top + ph*(1-pooled)
        parts.append(f'<rect x="{x-6}" y="{ypool-6}" width="12" height="12" fill="#111"/>')
        regime = str(row["regime"]).replace("_highrep", "")
        parts.append(f'<text x="{x}" y="{top+ph+22}" text-anchor="middle" font-family="sans-serif" font-size="9">{label}</text>')
        parts.append(f'<text x="{x}" y="{top+ph+39}" text-anchor="middle" font-family="sans-serif" font-size="10" font-weight="bold">{regime}</text>')
        parts.append(f'<text x="{x}" y="{max(top+12,ypool-12)}" text-anchor="middle" font-family="sans-serif" font-size="9">P={pooled:.3f}</text>')
    parts.append(f'<text x="{left2+235}" y="{top+ph+62}" text-anchor="middle" font-family="sans-serif" font-size="10">circles = five independent seed blocks; squares = pooled rate</text>')
    parts.append('</svg>')
    return "\n".join(parts) + "\n"


def figure5_connectivity_svg(phase_e: Mapping[str, Any]) -> str:
    width, height = 1280, 690
    parts = _header(
        width,
        height,
        "Effective genetic connectivity changes event-regime estimability",
        "Panel A shows pooled and seed-block functional-loss rates at five allele-frequency migration levels for the same 100 prepared sources. Panel B shows paired loss-status switches relative to isolation among 91 comparable sources, with both switch directions printed separately.",
        "figure5",
    )
    left, top, pw, ph = 95, 115, 520, 420
    parts.append('<text x="55" y="78" font-family="sans-serif" font-size="14" font-weight="bold">A. Event regime across allele-frequency mixing</text>')
    _plot_axes(parts, left, top, pw, ph, y_label="functional-loss rate")
    band_y = top + ph*(1-0.70); band_h = ph*0.40
    parts.append(f'<rect x="{left}" y="{band_y}" width="{pw}" height="{band_h}" fill="#e5e7eb" opacity="0.7"/>')
    rows = phase_e["migration_condition_summaries"]
    xs=[]; pooled_pts=[]
    for i, row in enumerate(rows):
        x = left + 55 + i*105
        xs.append(x)
        for j, rate in enumerate(row["seed_rates"]):
            y = top + ph*(1-float(rate))
            parts.append(f'<circle cx="{x+(j-2)*6}" cy="{y}" r="4" fill="#6b7280" stroke="#111"/>')
        pooled=float(row["pooled_trait_loss_rate"]); ypool=top+ph*(1-pooled); pooled_pts.append((x,ypool))
        regime=str(row["regime"]).replace("_highrep","")
        parts.append(f'<text x="{x}" y="{top+ph+22}" text-anchor="middle" font-family="sans-serif" font-size="10">m={float(row["migration_rate"]):g}</text>')
        parts.append(f'<text x="{x}" y="{top+ph+39}" text-anchor="middle" font-family="sans-serif" font-size="10" font-weight="bold">{regime}</text>')
        parts.append(f'<text x="{x}" y="{max(top+12,ypool-13)}" text-anchor="middle" font-family="sans-serif" font-size="9">P={pooled:.3f}</text>')
    parts.append('<polyline points="'+' '.join(f'{x:.1f},{y:.1f}' for x,y in pooled_pts)+'" fill="none" stroke="#111" stroke-width="2.5"/>')
    for x,y in pooled_pts:
        parts.append(f'<rect x="{x-5}" y="{y-5}" width="10" height="10" fill="#111"/>')
    parts.append(f'<text x="{left+12}" y="{band_y+18}" font-family="sans-serif" font-size="10">R4 operational band 0.30–0.70</text>')

    left2=760
    parts.append(f'<text x="{left2-55}" y="78" font-family="sans-serif" font-size="14" font-weight="bold">B. Paired trajectory-status switching vs isolation</text>')
    base_y=520; max_h=300; max_count=16
    parts.append(f'<line x1="{left2}" y1="{base_y}" x2="{left2+420}" y2="{base_y}" stroke="#333"/>')
    for i,row in enumerate(phase_e["paired_loss_status_vs_isolation"]):
        x=left2+55+i*95
        a=int(row["loss_to_no_loss"]); b=int(row["no_loss_to_loss"])
        ha=max_h*a/max_count; hb=max_h*b/max_count
        parts.append(f'<rect x="{x-24}" y="{base_y-ha}" width="20" height="{ha}" fill="#2563eb" stroke="#111"/>')
        parts.append(f'<rect x="{x+4}" y="{base_y-hb}" width="20" height="{hb}" fill="#dc2626" stroke="#111"/>')
        parts.append(f'<text x="{x-14}" y="{base_y-ha-7}" text-anchor="middle" font-family="sans-serif" font-size="10">{a}</text>')
        parts.append(f'<text x="{x+14}" y="{base_y-hb-7}" text-anchor="middle" font-family="sans-serif" font-size="10">{b}</text>')
        parts.append(f'<text x="{x}" y="{base_y+20}" text-anchor="middle" font-family="sans-serif" font-size="10">m={float(row["migration_rate"]):g}</text>')
        parts.append(f'<text x="{x}" y="{base_y+38}" text-anchor="middle" font-family="sans-serif" font-size="9">switch {a+b}/91</text>')
    parts.append(f'<rect x="{left2+35}" y="580" width="14" height="14" fill="#2563eb"/><text x="{left2+55}" y="592" font-family="sans-serif" font-size="10">loss→no loss</text>')
    parts.append(f'<rect x="{left2+180}" y="580" width="14" height="14" fill="#dc2626"/><text x="{left2+200}" y="592" font-family="sans-serif" font-size="10">no loss→loss</text>')
    parts.append(f'<text x="{left2}" y="625" font-family="sans-serif" font-size="10">migration scope: allele-frequency mixing only; no tested m is a universal threshold</text>')
    parts.append('</svg>')
    return "\n".join(parts) + "\n"


def figure6_portability_svg(stage3_rows: Iterable[Mapping[str, Any]], audit: Mapping[str, Any]) -> str:
    rows = list(stage3_rows)
    width, height = 1320, 760
    parts = _header(
        width,
        height,
        "Portability after evaluability is separately recovered",
        "Panel A retains the full 100-attempt denominator for six warning endpoints in each independently calibrated domain. Panel B shows cumulative warning and realised functional-loss incidence for H-gamma 20 percent across each domain-specific calibrated horizon.",
        "figure6",
    )
    parts.append('<text x="45" y="76" font-family="sans-serif" font-size="14" font-weight="bold">A. Availability, censoring and ordering</text>')
    categories=(
        ("source_preparation_failed","SF","#d1d5db"),("baseline_ineligible","BI","#9ca3af"),
        ("both_censored","BC","#c4b5fd"),("warning_censored","WC","#f9a8d4"),
        ("trait_loss_censored","TC","#a7f3d0"),("lead","Lead","#2563eb"),
        ("tie","Tie","#facc15"),("lag","Lag","#dc2626"),
    )
    panel_lefts=(105,675); bar_w=500; bar_h=23; top=105; gap=45
    endpoints=("H_alpha_0.05","H_alpha_0.10","H_alpha_0.20","H_gamma_0.05","H_gamma_0.10","H_gamma_0.20")
    row_lookup={(str(r["domain"]),str(r["endpoint"])):r for r in rows}
    for d_idx,domain in enumerate(DOMAIN_ORDER):
        left=panel_lefts[d_idx]
        parts.append(f'<text x="{left+bar_w/2}" y="96" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold">{DOMAIN_LABELS[domain]}</text>')
        for i,endpoint in enumerate(endpoints):
            y=top+i*gap
            parts.append(f'<text x="{left-8}" y="{y+16}" text-anchor="end" font-family="sans-serif" font-size="9">{html.escape(endpoint.replace("H_alpha","Hα").replace("H_gamma","Hγ").replace("_"," "))}</text>')
            row=row_lookup[(domain,endpoint)]; x=left
            for key,code,fill in categories:
                n=int(row[key]); w=bar_w*n/100
                if w>0:
                    parts.append(f'<rect x="{x:.2f}" y="{y}" width="{w:.2f}" height="{bar_h}" fill="{fill}" stroke="white"/>')
                    if w>=25:
                        text_fill="#111" if code in {"BI","BC","WC","TC","Tie"} else "white"
                        parts.append(f'<text x="{x+w/2:.2f}" y="{y+15}" text-anchor="middle" font-family="sans-serif" font-size="8" fill="{text_fill}">{code} {n}</text>')
                x+=w
            valid=int(row["valid_pairs"])
            parts.append(f'<text x="{left+bar_w+6}" y="{y+16}" font-family="sans-serif" font-size="8">valid {valid}/100</text>')
    legend_y=390
    x=105
    for key,code,fill in categories:
        parts.append(f'<rect x="{x}" y="{legend_y}" width="13" height="13" fill="{fill}" stroke="#777"/><text x="{x+18}" y="{legend_y+11}" font-family="sans-serif" font-size="9">{code}</text>')
        x+=115

    parts.append('<text x="45" y="440" font-family="sans-serif" font-size="14" font-weight="bold">B. Cumulative Hγ 20% warning and functional loss</text>')
    for d_idx,domain in enumerate(DOMAIN_ORDER):
        left=105+d_idx*570; top2=465; pw=500; ph=210
        parts.append(f'<rect x="{left}" y="{top2}" width="{pw}" height="{ph}" fill="white" stroke="#333"/>')
        data=audit["domains"][domain]; horizon=int(data["schedule"]["horizon"])
        series=data["cumulative_event_incidence"]["H_gamma_0.20"]["series"]
        warn=[]; loss=[]
        for item in series:
            xpt=left+pw*float(item["generation"])/horizon
            warn.append((xpt,top2+ph*(1-float(item["warning_incidence"]))))
            loss.append((xpt,top2+ph*(1-float(item["trait_loss_incidence"]))))
        parts.append('<polyline points="'+' '.join(f'{x:.1f},{y:.1f}' for x,y in warn)+'" fill="none" stroke="#2563eb" stroke-width="2.5"/>')
        parts.append('<polyline points="'+' '.join(f'{x:.1f},{y:.1f}' for x,y in loss)+'" fill="none" stroke="#111" stroke-width="3"/>')
        parts.append(f'<text x="{left+pw/2}" y="{top2-10}" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold">{DOMAIN_LABELS[domain]} — horizon {horizon}</text>')
        parts.append(f'<text x="{left+pw/2}" y="{top2+ph+24}" text-anchor="middle" font-family="sans-serif" font-size="10">fraction of calibrated horizon</text>')
        for frac in (0,0.5,1):
            xx=left+pw*frac
            parts.append(f'<text x="{xx}" y="{top2+ph+12}" text-anchor="middle" font-family="sans-serif" font-size="8">{frac:g}</text>')
        n=int(data["cumulative_event_incidence"]["H_gamma_0.20"]["baseline_eligible_completed"])
        parts.append(f'<text x="{left+pw-5}" y="{top2+16}" text-anchor="end" font-family="sans-serif" font-size="8">baseline-eligible completed n={n}</text>')
    parts.append('<line x1="480" y1="720" x2="520" y2="720" stroke="#2563eb" stroke-width="2.5"/><text x="530" y="724" font-family="sans-serif" font-size="10">Hγ 20% warning</text>')
    parts.append('<line x1="680" y1="720" x2="720" y2="720" stroke="#111" stroke-width="3"/><text x="730" y="724" font-family="sans-serif" font-size="10">realised functional loss</text>')
    parts.append('</svg>')
    return "\n".join(parts) + "\n"


def write_revised_main_figures(
    *,
    stage1_csv: str | Path,
    stage2_csv: str | Path,
    h3_csv: str | Path,
    h2_csv: str | Path,
    phase_b_json: str | Path,
    phase_c_json: str | Path,
    phase_d_json: str | Path,
    phase_e_json: str | Path,
    stage3_summary_csv: str | Path,
    stage3_audit_json: str | Path,
    output_dir: str | Path,
) -> None:
    out=Path(output_dir); out.mkdir(parents=True,exist_ok=True)
    (out/"figure2_fragmentation_warning_bridge.svg").write_text(
        figure2_parent_bridge_svg(_csv_rows(h3_csv),_csv_rows(h2_csv)),encoding="utf-8")
    (out/"figure3_source_loss_regimes.svg").write_text(
        figure3_source_regime_svg(_csv_rows(stage1_csv),_csv_rows(stage2_csv)),encoding="utf-8")
    (out/"figure4_r4_recovery.svg").write_text(
        figure4_r4_recovery_svg(_json(phase_b_json),_json(phase_c_json),_json(phase_d_json)),encoding="utf-8")
    (out/"figure5_connectivity_estimability.svg").write_text(
        figure5_connectivity_svg(_json(phase_e_json)),encoding="utf-8")
    (out/"figure6_portability.svg").write_text(
        figure6_portability_svg(_csv_rows(stage3_summary_csv),_json(stage3_audit_json)),encoding="utf-8")
