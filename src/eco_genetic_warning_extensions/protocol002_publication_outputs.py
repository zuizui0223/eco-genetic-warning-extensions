"""Publication-facing outputs for the completed Protocol 002 event-regime audit."""
from __future__ import annotations

import csv
import html
import json
from pathlib import Path
from typing import Any, Mapping

REGIME_ORDER = ("all_above_band", "mixed_across_band", "all_below_band")
REGIME_LABELS = {
    "all_above_band": "rapid-loss",
    "mixed_across_band": "seed-heterogeneous",
    "all_below_band": "persistence",
}
REGIME_CODES = {
    "rapid-loss": "R",
    "seed-heterogeneous": "H",
    "persistence": "P",
}


def _dominant_pattern(pattern_counts: Mapping[str, int]) -> str:
    if not pattern_counts:
        return "incomplete"
    return max(REGIME_ORDER, key=lambda key: (int(pattern_counts.get(key, 0)), -REGIME_ORDER.index(key)))


def publication_rows(audit: Mapping[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for coordinate in audit["coordinates"]:
        closest = coordinate["closest_candidate_to_predeclared_band"]
        dominant = _dominant_pattern(coordinate.get("pattern_counts", {}))
        rates = list(closest["seed_block_trait_loss_rates"])
        rows.append({
            "kappa_mu": float(coordinate["kappa_mu"]),
            "p_star": float(coordinate["p_star"]),
            "complete_candidate_count": int(coordinate["complete_candidate_count"]),
            "incomplete_candidate_count": int(coordinate["incomplete_candidate_count"]),
            "dominant_regime": REGIME_LABELS.get(dominant, dominant),
            "rapid_loss_candidate_count": int(coordinate.get("pattern_counts", {}).get("all_above_band", 0)),
            "seed_heterogeneous_candidate_count": int(coordinate.get("pattern_counts", {}).get("mixed_across_band", 0)),
            "persistence_candidate_count": int(coordinate.get("pattern_counts", {}).get("all_below_band", 0)),
            "closest_batch_index": int(closest["batch_index"]),
            "closest_area_reference": float(closest["area_reference"]),
            "closest_kappa": float(closest["kappa"]),
            "closest_horizon": int(closest["horizon"]),
            "closest_barrier_increase": float(closest["normalised_barrier_increase"]),
            "closest_pooled_trait_loss_rate": float(closest["pooled_trait_loss_rate"]),
            "closest_inside_band_seed_count": int(closest["inside_band_seed_count"]),
            "closest_maximum_distance_to_band": float(closest["maximum_distance_to_band"]),
            "closest_seed_block_rates": ";".join(f"{float(rate):.6g}" for rate in rates),
            "domain_selected": False,
        })
    return sorted(rows, key=lambda row: (row["kappa_mu"], row["p_star"]))


def write_publication_csv(audit_path: Path, output_path: Path) -> list[dict[str, Any]]:
    audit = json.loads(audit_path.read_text(encoding="utf-8"))
    rows = publication_rows(audit)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    return rows


def write_regime_svg(rows: list[Mapping[str, Any]], output_path: Path) -> None:
    width, height = 980, 570
    left, top, cell_w, cell_h = 170, 95, 145, 112
    p_values = sorted({float(row["p_star"]) for row in rows})
    k_values = sorted({float(row["kappa_mu"]) for row in rows})
    palette = {"rapid-loss": "#b2182b", "seed-heterogeneous": "#fdae61", "persistence": "#2166ac"}
    lookup = {(float(row["kappa_mu"]), float(row["p_star"])): row for row in rows}
    title = "Functional-loss regimes across transition coordinates"
    description = (
        "A fifteen-cell map classifying each transition coordinate as rapid loss, seed heterogeneous, or persistence. "
        "Every cell includes a direct R, H, or P code, regime name, closest pooled loss frequency, and complete-candidate count."
    )
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="figure3-title figure3-desc">',
        f'<title id="figure3-title">{html.escape(title)}</title>',
        f'<desc id="figure3-desc">{html.escape(description)}</desc>',
        '<rect width="100%" height="100%" fill="white"/>',
        f'<text x="{width/2}" y="38" text-anchor="middle" font-family="sans-serif" font-size="22" font-weight="bold">{html.escape(title)}</text>',
    ]
    for ix, p_star in enumerate(p_values):
        x = left + ix * cell_w
        parts.append(f'<text x="{x + cell_w/2}" y="78" text-anchor="middle" font-family="sans-serif" font-size="15">p*={p_star:g}</text>')
    for iy, kappa_mu in enumerate(k_values):
        y = top + iy * cell_h
        parts.append(f'<text x="150" y="{y + cell_h/2}" text-anchor="end" dominant-baseline="middle" font-family="sans-serif" font-size="15">κμ={kappa_mu:g}</text>')
        for ix, p_star in enumerate(p_values):
            row = lookup[(kappa_mu, p_star)]
            x = left + ix * cell_w
            regime = str(row["dominant_regime"])
            fill = palette[regime]
            code = REGIME_CODES[regime]
            pooled = float(row["closest_pooled_trait_loss_rate"])
            complete = int(row["complete_candidate_count"])
            text_fill = "#111" if regime == "seed-heterogeneous" else "white"
            parts.append(f'<rect x="{x+5}" y="{y+5}" width="{cell_w-10}" height="{cell_h-10}" rx="8" fill="{fill}" stroke="#222" stroke-width="1.3"/>')
            parts.append(f'<text x="{x+cell_w/2}" y="{y+30}" text-anchor="middle" font-family="sans-serif" font-size="18" font-weight="bold" fill="{text_fill}">{code}</text>')
            parts.append(f'<text x="{x+cell_w/2}" y="{y+50}" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="{text_fill}">{html.escape(regime)}</text>')
            parts.append(f'<text x="{x+cell_w/2}" y="{y+73}" text-anchor="middle" font-family="sans-serif" font-size="12" fill="{text_fill}">closest P={pooled:.3f}</text>')
            parts.append(f'<text x="{x+cell_w/2}" y="{y+93}" text-anchor="middle" font-family="sans-serif" font-size="12" fill="{text_fill}">complete n={complete}</text>')
    legend_y = top + len(k_values) * cell_h + 30
    for idx, regime in enumerate(("rapid-loss", "seed-heterogeneous", "persistence")):
        x = left + idx * 245
        code = REGIME_CODES[regime]
        parts.append(f'<rect x="{x}" y="{legend_y}" width="24" height="24" fill="{palette[regime]}" stroke="#222"/>')
        parts.append(f'<text x="{x+12}" y="{legend_y+17}" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="{"#111" if regime == "seed-heterogeneous" else "white"}">{code}</text>')
        parts.append(f'<text x="{x+34}" y="{legend_y+17}" font-family="sans-serif" font-size="14">{code} — {regime}</text>')
    parts.append('</svg>')
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(parts) + "\n", encoding="utf-8")
