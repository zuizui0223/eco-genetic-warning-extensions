"""Post-Phase-J deterministic SVG builders for the distributional manuscript spine.

These builders render only committed warning-blind summaries. They do not run
simulations, inspect genetic-warning outcomes, or recalibrate any condition.
"""
from __future__ import annotations

import html
from typing import Any, Mapping


def _header(width: int, height: int, title: str, desc: str, identifier: str) -> list[str]:
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="{identifier}-title {identifier}-desc">',
        f'<title id="{identifier}-title">{html.escape(title)}</title>',
        f'<desc id="{identifier}-desc">{html.escape(desc)}</desc>',
        '<rect width="100%" height="100%" fill="white"/>',
        f'<text x="{width/2}" y="34" text-anchor="middle" font-family="sans-serif" font-size="21" font-weight="bold">{html.escape(title)}</text>',
    ]


def _axis(parts: list[str], left: float, top: float, width: float, height: float, *, ylabel: str) -> None:
    parts.append(f'<rect x="{left}" y="{top}" width="{width}" height="{height}" fill="white" stroke="#333"/>')
    for value in (0.0, 0.25, 0.5, 0.75, 1.0):
        y = top + height * (1.0 - value)
        parts.append(f'<line x1="{left-5}" y1="{y}" x2="{left}" y2="{y}" stroke="#333"/>')
        parts.append(f'<text x="{left-9}" y="{y+4}" text-anchor="end" font-family="sans-serif" font-size="9">{value:g}</text>')
    parts.append(
        f'<text x="{left-48}" y="{top+height/2}" text-anchor="middle" font-family="sans-serif" font-size="10" '
        f'transform="rotate(-90 {left-48} {top+height/2})">{html.escape(ylabel)}</text>'
    )


def _band(parts: list[str], left: float, top: float, width: float, height: float) -> None:
    y = top + height * (1.0 - 0.70)
    h = height * 0.40
    parts.append(f'<rect x="{left}" y="{y}" width="{width}" height="{h}" fill="#e5e7eb" opacity="0.72"/>')
    parts.append(f'<text x="{left+8}" y="{y+15}" font-family="sans-serif" font-size="9">operational incidence zone .30–.70</text>')


def _seed_rates(row: Mapping[str, Any]) -> list[float]:
    if "seed_rates" in row:
        return [float(value) for value in row["seed_rates"]]
    return [float(block["trait_loss_rate"]) for block in row["seed_blocks"]]


def figure4_certificate_sampling_svg(
    phase_c: Mapping[str, Any],
    phase_d: Mapping[str, Any],
    phase_j: Mapping[str, Any],
) -> str:
    """Historical finite certificate recovery plus Phase-J sampling boundary."""
    width, height = 1320, 720
    parts = _header(
        width,
        height,
        "Finite calibration certificates and their sampling boundary",
        "Panel A retains the prospectively recovered finite R4 frontier panels. Panel B shows 20 fresh fixed-condition Phase-J block loss rates grouped into four prospectively fixed panels. Panel C shows the exact 75 versus 25 percent split of all possible five-block panels from those 20 rates.",
        "figure4",
    )

    # Panel A: historical finite certificate recovery.
    left_a, top, pw_a, ph = 90, 115, 360, 400
    parts.append('<text x="45" y="78" font-family="sans-serif" font-size="13" font-weight="bold">A. Historical finite certificate recovery</text>')
    _axis(parts, left_a, top, pw_a, ph, ylabel="seed-block loss rate")
    _band(parts, left_a, top, pw_a, ph)
    c_lookup = {float(row["p_star"]): row for row in phase_c["cells"]}
    d_lookup = {float(row["p_star"]): row for row in phase_d["cells"]}
    display = [
        (".325 D", d_lookup[0.325]),
        (".350 C", c_lookup[0.35]),
        (".350 D", d_lookup[0.35]),
        (".375 D", d_lookup[0.375]),
        (".400 C", c_lookup[0.40]),
    ]
    for i, (label, row) in enumerate(display):
        x = left_a + 36 + i * 68
        for j, rate in enumerate(_seed_rates(row)):
            y = top + ph * (1.0 - rate)
            parts.append(f'<circle cx="{x+(j-2)*4}" cy="{y}" r="3.5" fill="#6b7280" stroke="#111"/>')
        pooled = float(row["pooled_trait_loss_rate"])
        yp = top + ph * (1.0 - pooled)
        parts.append(f'<rect x="{x-5}" y="{yp-5}" width="10" height="10" fill="#111"/>')
        label_regime = str(row["regime"]).replace("_highrep", "")
        parts.append(f'<text x="{x}" y="{top+ph+20}" text-anchor="middle" font-family="sans-serif" font-size="8.5">{label}</text>')
        parts.append(f'<text x="{x}" y="{top+ph+35}" text-anchor="middle" font-family="sans-serif" font-size="8.5" font-weight="bold">{label_regime}</text>')
    parts.append(f'<text x="{left_a+pw_a/2}" y="{top+ph+62}" text-anchor="middle" font-family="sans-serif" font-size="9">circles = seed blocks; squares = pooled incidence</text>')
    parts.append(f'<text x="{left_a}" y="{top+ph+88}" font-family="sans-serif" font-size="9">Historical R4 = finite all-block certificate, not warning success.</text>')

    # Panel B: Phase-J 20 fresh blocks in fixed panels.
    left_b, pw_b = 520, 500
    parts.append(f'<text x="{left_b-25}" y="78" font-family="sans-serif" font-size="13" font-weight="bold">B. Fixed-condition Phase-J panels</text>')
    _axis(parts, left_b, top, pw_b, ph, ylabel="seed-block loss rate")
    _band(parts, left_b, top, pw_b, ph)
    blocks = {int(row["master_seed"]): row for row in phase_j["seed_blocks"]}
    panel_width = pw_b / 4.0
    for pindex, panel in enumerate(phase_j["panels"]):
        x0 = left_b + pindex * panel_width
        regime = str(panel["regime"]).replace("_highrep", "")
        parts.append(f'<rect x="{x0+2}" y="{top+2}" width="{panel_width-4}" height="{ph-4}" fill="none" stroke="#9ca3af" stroke-dasharray="3,3"/>')
        for j, seed in enumerate(panel["master_seeds"]):
            rate = float(blocks[int(seed)]["trait_loss_rate"])
            x = x0 + 15 + j * ((panel_width - 30) / 4.0)
            y = top + ph * (1.0 - rate)
            fill = "#dc2626" if rate > 0.70 or rate < 0.30 else "#2563eb"
            parts.append(f'<circle cx="{x}" cy="{y}" r="5" fill="{fill}" stroke="#111"/>')
            if rate > 0.70 or rate < 0.30:
                parts.append(f'<text x="{x}" y="{y-10}" text-anchor="middle" font-family="sans-serif" font-size="8">{rate:.3f}</text>')
        parts.append(f'<text x="{x0+panel_width/2}" y="{top+ph+20}" text-anchor="middle" font-family="sans-serif" font-size="9">Panel {pindex+1}</text>')
        parts.append(f'<text x="{x0+panel_width/2}" y="{top+ph+35}" text-anchor="middle" font-family="sans-serif" font-size="9" font-weight="bold">{regime}</text>')
    diag = phase_j["twenty_seed_diagnostics"]
    parts.append(f'<text x="{left_b}" y="{top+ph+62}" font-family="sans-serif" font-size="9">19/20 blocks inside zone; mean={float(diag["mean_trait_loss_rate"]):.3f}; median={float(diag["median_trait_loss_rate"]):.3f}</text>')
    parts.append(f'<text x="{left_b}" y="{top+ph+80}" font-family="sans-serif" font-size="9">One block at .750 determines whether a five-block panel receives R3.</text>')

    # Panel C: exact all-combinations certificate frequency.
    left_c, top_c, bar_w = 1080, 150, 170
    parts.append(f'<text x="{left_c-25}" y="78" font-family="sans-serif" font-size="13" font-weight="bold">C. All five-block panels</text>')
    parts.append(f'<rect x="{left_c}" y="{top_c}" width="{bar_w}" height="46" fill="#e5e7eb" stroke="#333"/>')
    r4_w = bar_w * 0.75
    parts.append(f'<rect x="{left_c}" y="{top_c}" width="{r4_w}" height="46" fill="#2563eb" stroke="#333"/>')
    parts.append(f'<text x="{left_c+r4_w/2}" y="{top_c+29}" text-anchor="middle" font-family="sans-serif" font-size="11" fill="white" font-weight="bold">R4 75%</text>')
    parts.append(f'<text x="{left_c+r4_w+(bar_w-r4_w)/2}" y="{top_c+29}" text-anchor="middle" font-family="sans-serif" font-size="10" font-weight="bold">R3 25%</text>')
    parts.append(f'<text x="{left_c}" y="{top_c+78}" font-family="sans-serif" font-size="9">15,504 possible five-block panels</text>')
    parts.append(f'<text x="{left_c}" y="{top_c+96}" font-family="sans-serif" font-size="9">11,628 R4; 3,876 R3</text>')
    parts.append(f'<text x="{left_c}" y="{top_c+132}" font-family="sans-serif" font-size="9">All-pass design identity:</text>')
    parts.append(f'<text x="{left_c}" y="{top_c+150}" font-family="sans-serif" font-size="12" font-weight="bold">P(certificate)=q^B</text>')
    parts.append(f'<text x="{left_c}" y="{top_c+176}" font-family="sans-serif" font-size="9">q = single-block pass probability</text>')
    parts.append(f'<text x="{left_c}" y="{top_c+193}" font-family="sans-serif" font-size="9">B = panel size</text>')
    parts.append(f'<text x="{left_c}" y="{top_c+235}" font-family="sans-serif" font-size="9">Finite certificate ≠</text>')
    parts.append(f'<text x="{left_c}" y="{top_c+252}" font-family="sans-serif" font-size="9">sample-size-invariant regime</text>')
    parts.append('</svg>')
    return "\n".join(parts) + "\n"


def figure5_condition_synthesis_svg(
    phase_e: Mapping[str, Any],
    phase_f: Mapping[str, Any],
    phase_g: Mapping[str, Any],
    phase_h: Mapping[str, Any],
    phase_i: Mapping[str, Any],
) -> str:
    """Synthesis of connectivity, interaction and movement layers."""
    width, height = 1380, 790
    parts = _header(
        width,
        height,
        "Connectivity and interaction processes reshape different layers of functional loss",
        "Four panels show allele-frequency connectivity, aggregate interaction support, partner loss and explicit rewiring, and process-resolved pollen movement. The figure separates mean incidence, trajectory switching, network state and finite calibration labels.",
        "figure5",
    )

    # A. Phase E connectivity.
    left, top, pw, ph = 80, 105, 570, 270
    parts.append('<text x="40" y="72" font-family="sans-serif" font-size="13" font-weight="bold">A. Genetic-state connectivity</text>')
    _axis(parts, left, top, pw, ph, ylabel="functional-loss rate")
    _band(parts, left, top, pw, ph)
    rows_e = phase_e["migration_condition_summaries"]
    for i, row in enumerate(rows_e):
        x = left + 55 + i * 110
        for j, rate in enumerate(_seed_rates(row)):
            y = top + ph * (1.0 - rate)
            parts.append(f'<circle cx="{x+(j-2)*5}" cy="{y}" r="3.4" fill="#6b7280" stroke="#111"/>')
        pooled = float(row["pooled_trait_loss_rate"])
        yp = top + ph * (1.0 - pooled)
        parts.append(f'<rect x="{x-5}" y="{yp-5}" width="10" height="10" fill="#111"/>')
        parts.append(f'<text x="{x}" y="{top+ph+18}" text-anchor="middle" font-family="sans-serif" font-size="9">m={float(row["migration_rate"]):g}</text>')
        parts.append(f'<text x="{x}" y="{top+ph+33}" text-anchor="middle" font-family="sans-serif" font-size="8">{str(row["regime"]).replace("_highrep","")}</text>')
    switches = phase_e["paired_loss_status_vs_isolation"]
    text = ", ".join(f'm={float(r["migration_rate"]):g}: {int(r["loss_to_no_loss"])+int(r["no_loss_to_loss"])}/91' for r in switches)
    parts.append(f'<text x="{left}" y="{top+ph+54}" font-family="sans-serif" font-size="8.5">paired status switches vs m=0 — {html.escape(text)}</text>')
    parts.append(f'<text x="{left}" y="{top+ph+70}" font-family="sans-serif" font-size="8.5">Phase-I/J show the exact m=.10 R3 label is not portable across seed ensembles.</text>')

    # B. Phase F scalar support.
    left_b = 760
    parts.append(f'<text x="{left_b-30}" y="72" font-family="sans-serif" font-size="13" font-weight="bold">B. Aggregate interaction support</text>')
    rows_f = phase_f["interaction_support_summaries"]
    base_y = 330
    for i, row in enumerate(rows_f):
        x = left_b + i * 180
        eligible = int(row["status_counts"]["baseline_eligible"])
        pooled = float(row["pooled_trait_loss_rate"])
        parts.append(f'<rect x="{x}" y="{base_y-2.1*eligible}" width="48" height="{2.1*eligible}" fill="#6b7280" stroke="#111"/>')
        parts.append(f'<text x="{x+24}" y="{base_y-2.1*eligible-7}" text-anchor="middle" font-family="sans-serif" font-size="9">eligible {eligible}/100</text>')
        parts.append(f'<text x="{x+24}" y="{base_y+18}" text-anchor="middle" font-family="sans-serif" font-size="9">κ={float(row["interaction_kappa"]):g}</text>')
        parts.append(f'<text x="{x+24}" y="{base_y+34}" text-anchor="middle" font-family="sans-serif" font-size="9">loss {pooled:.3f}</text>')
    parts.append(f'<text x="{left_b}" y="{base_y+58}" font-family="sans-serif" font-size="8.5">All 15 tested seed-block rates were in the operational incidence zone.</text>')

    # C. Partner loss + rewiring.
    top_c = 470
    parts.append(f'<text x="40" y="{top_c-25}" font-family="sans-serif" font-size="13" font-weight="bold">C. Partner loss and explicit rewiring</text>')
    g_rows = {row["partner_architecture"]: row for row in phase_g["partner_architecture_summaries"]}
    h_rows = {row["network_condition"]: row for row in phase_h["network_condition_summaries"]}
    labels = [
        ("G intact", float(g_rows["intact_control"]["pooled_trait_loss_rate"]), "R4"),
        ("G even loss", float(g_rows["even_redundant"]["pooled_trait_loss_rate"]), "R3"),
        ("G graded loss", float(g_rows["graded_contributions"]["pooled_trait_loss_rate"]), "R3"),
        ("G dominant loss", float(g_rows["dominant_partner"]["pooled_trait_loss_rate"]), "R3"),
        ("H no rewire", float(h_rows["partner_loss_no_rewiring"]["pooled_trait_loss_rate"]), "R3"),
        ("H rewire", float(h_rows["partner_loss_trait_capacity_rewiring"]["pooled_trait_loss_rate"]), "R3"),
    ]
    bar_left, bar_top, bar_w, bar_h = 85, top_c, 520, 175
    parts.append(f'<rect x="{bar_left}" y="{bar_top}" width="{bar_w}" height="{bar_h}" fill="white" stroke="#333"/>')
    for i, (label, pooled, cert) in enumerate(labels):
        x = bar_left + 25 + i * 82
        h = pooled * 150
        parts.append(f'<rect x="{x}" y="{bar_top+155-h}" width="35" height="{h}" fill="#6b7280" stroke="#111"/>')
        parts.append(f'<text x="{x+17.5}" y="{bar_top+155-h-6}" text-anchor="middle" font-family="sans-serif" font-size="8">{pooled:.3f}</text>')
        parts.append(f'<text x="{x+17.5}" y="{bar_top+170}" text-anchor="middle" font-family="sans-serif" font-size="7.5">{html.escape(label)}</text>')
        parts.append(f'<text x="{x+17.5}" y="{bar_top+184}" text-anchor="middle" font-family="sans-serif" font-size="7.5" font-weight="bold">{cert}</text>')
    h_rewire = h_rows["partner_loss_trait_capacity_rewiring"]["network_diagnostics"]
    h_no = h_rows["partner_loss_no_rewiring"]["network_diagnostics"]
    parts.append(f'<text x="{bar_left}" y="{bar_top+215}" font-family="sans-serif" font-size="8.5">H rewiring: active edges {float(h_no["mean_final_active_edge_count"]):.0f}→{float(h_rewire["mean_final_active_edge_count"]):.0f}; connectance {float(h_no["mean_final_realised_connectance"]):.3f}→{float(h_rewire["mean_final_realised_connectance"]):.3f}; support {float(h_no["mean_final_support_multiplier"]):.3f}→{float(h_rewire["mean_final_support_multiplier"]):.3f}</text>')
    parts.append(f'<text x="{bar_left}" y="{bar_top+232}" font-family="sans-serif" font-size="8.5">Network recovery occurred without comparable recovery of the functional-loss distribution.</text>')

    # D. Phase I pollen movement.
    left_d = 760
    parts.append(f'<text x="{left_d-30}" y="{top_c-25}" font-family="sans-serif" font-size="13" font-weight="bold">D. Process-resolved pollen movement</text>')
    i_rows = phase_i["movement_condition_summaries"]
    x0, y0 = left_d, top_c + 5
    short = {
        "no_pollen_control": "no pollen",
        "regional_pollen_pool_g020": "regional g=.20",
        "legacy_allele_mixing_m010": "legacy m=.10",
        "ring_pollen_pool_g020": "ring g=.20",
    }
    for idx, row in enumerate(i_rows):
        y = y0 + idx * 45
        pooled = float(row["pooled_trait_loss_rate"])
        parts.append(f'<text x="{x0}" y="{y+16}" font-family="sans-serif" font-size="9">{html.escape(short[str(row["movement_condition"])])}</text>')
        parts.append(f'<rect x="{x0+125}" y="{y}" width="{pooled*300:.1f}" height="24" fill="#6b7280" stroke="#111"/>')
        parts.append(f'<text x="{x0+435}" y="{y+16}" font-family="sans-serif" font-size="9">loss={pooled:.3f} · {str(row["regime"]).replace("_highrep","")}</text>')
    eq = phase_i["regional_legacy_equivalence"]
    parts.append(f'<text x="{x0}" y="{y0+205}" font-family="sans-serif" font-size="8.5">regional g=.20 = legacy m=.10 snapshot-exact: {int(eq["pair_count"])-int(eq["mismatch_count"])}/{int(eq["pair_count"])}</text>')
    pair = next(row for row in phase_i["paired_loss_status"] if row["comparison"] == "ring_pollen_pool_g020")
    parts.append(f'<text x="{x0}" y="{y0+222}" font-family="sans-serif" font-size="8.5">regional→ring switches: {int(pair["loss_to_no_loss"])} loss→no-loss; {int(pair["no_loss_to_loss"])} no-loss→loss.</text>')
    parts.append(f'<text x="{x0}" y="{y0+250}" font-family="sans-serif" font-size="9" font-weight="bold">State/network, movement process, mean incidence and heterogeneity are distinct layers.</text>')

    parts.append('</svg>')
    return "\n".join(parts) + "\n"
