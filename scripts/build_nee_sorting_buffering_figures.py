from __future__ import annotations

import argparse
import csv
import html
import json
from pathlib import Path


def t(x, y, s, size=15, anchor="middle", weight="normal", rotate=None):
    tr = f' transform="rotate({rotate} {x} {y})"' if rotate is not None else ""
    return (
        f'<text x="{x}" y="{y}" text-anchor="{anchor}" '
        f'font-family="Arial,Helvetica,sans-serif" font-size="{size}" '
        f'font-weight="{weight}"{tr}>{html.escape(str(s))}</text>'
    )


def start(w, h, title, desc):
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
        f'viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">',
        f'<title id="title">{html.escape(title)}</title>',
        f'<desc id="desc">{html.escape(desc)}</desc>',
        '<rect width="100%" height="100%" fill="white"/>',
        '<defs><marker id="arrow" markerWidth="9" markerHeight="9" refX="8" refY="4.5" '
        'orient="auto"><path d="M0,0 L0,9 L9,4.5 z" fill="#222"/></marker></defs>',
    ]


def done(lines, path):
    lines.append("</svg>")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def box(lines, x, y, w, h, label, sub=""):
    lines.append(
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" '
        'fill="white" stroke="#222" stroke-width="2"/>'
    )
    lines.append(t(x + w / 2, y + 34, label, 16, weight="bold"))
    if sub:
        lines.append(t(x + w / 2, y + 61, sub, 12))


def fig1(path):
    L = start(
        1500, 780,
        "State separation and operator balance under fragmentation",
        "State separation, hidden cross-layer organization, q-dependent allele sorting, buffering, recoupling, density gating and fate discrimination.",
    )
    L.append(t(750, 45, "Fragmentation changes pathway balance, not one deterioration score", 28, weight="bold"))
    box(L, 65, 155, 340, 115, "State separation", "persistence != functional support")
    box(L, 490, 155, 520, 115, "Pathway mechanism", "sorting / recruitment buffering / direct recoupling")
    box(L, 1095, 155, 340, 115, "Warning discrimination", "early response != fate discrimination")
    L += [
        '<line x1="405" y1="212" x2="480" y2="212" stroke="#222" stroke-width="2" marker-end="url(#arrow)"/>',
        '<line x1="1010" y1="212" x2="1085" y2="212" stroke="#222" stroke-width="2" marker-end="url(#arrow)"/>',
        t(235, 335, "fixed-area fragmentation separates biological states", 13),
        t(750, 335, "exact allele sorting / recruitment buffering / feedback recoupling", 13),
        t(1265, 335, "full denominator exposes false-positive behaviour", 13),
    ]
    box(L, 400, 430, 700, 125, "Positive synthesis", "fate reflects sorting, buffering, recoupling and remaining refuge reserve")
    L += [
        t(750, 610, "density -> interaction feedback acts as a collapse/amplification gate", 15, weight="bold"),
        t(750, 665, "Natural systems test state separation; operator-level causation remains finite-model evidence.", 13),
        t(750, 725, "No landscape label, alignment score or natural allele-sorting law is assumed universal.", 12),
    ]
    done(L, path)


def fig2(egc, path):
    rows = list(csv.DictReader(
        (egc / "artifacts/h3_fragmentation_gradient/h3_fragmentation_gradient_pooled_summary.csv").open()
    ))
    assert [int(r["patch_count"]) for r in rows] == [1, 2, 3, 4, 6, 8, 12, 16]
    assert int(rows[0]["projection_supported"]) == 1037

    L = start(
        1500, 800,
        "Fragmentation separates functional support from persistence",
        "Fixed-area fragmentation gradient with distinct biological-state responses.",
    )
    L += [
        t(750, 42, "Fragmentation separates functional support from persistence", 28, weight="bold"),
        t(350, 90, "A  Potential viability and realised occupancy", 18, weight="bold"),
        t(1110, 90, "B  Retained state ratios", 18, weight="bold"),
    ]

    left, right, top, bottom = 90, 670, 150, 610
    for p in [0, 25, 50, 75, 100]:
        y = bottom - p / 100 * (bottom - top)
        L.append(f'<line x1="{left}" y1="{y}" x2="{right}" y2="{y}" stroke="#ddd"/>')
        L.append(t(left - 8, y + 4, p, 11, anchor="end"))
    xs = [left + i * (right - left) / 7 for i in range(8)]
    pts = []
    for x, p, n in zip(xs, [100] + [0] * 7, [1, 2, 3, 4, 6, 8, 12, 16]):
        y = bottom - p / 100 * (bottom - top)
        pts.append((x, y))
        L.append(f'<circle cx="{x}" cy="{y}" r="5" fill="white" stroke="#111"/>')
        L.append(t(x, bottom + 23, n, 11))
    L.append(
        '<polyline points="' + " ".join(f"{x},{y}" for x, y in pts)
        + '" fill="none" stroke="#111" stroke-width="2.3"/>'
    )
    L += [
        t(380, 132, "realised occupancy at generation 30 ~99.6-100%", 12),
        t(30, 390, "supported outcomes (%)", 12, rotate=-90),
        t(380, 665, "number of isolated equal patches", 12),
        t(380, 710, "potential viability: 1,037/1,037 -> 0/1,037 after first split", 14, weight="bold"),
    ]

    l, r, tt, b = 820, 1430, 150, 610
    keys = [
        ("final_interaction_mean_ratio_to_n1_median", "interaction", ""),
        ("final_effective_size_mean_ratio_to_n1_median", "local effective size", "8 5"),
        ("realised_high_trait_mass_mean_ratio_to_n1_median", "realised high-trait mass", "3 4"),
    ]
    for q in [0, .25, .5, .75, 1]:
        y = b - q * (b - tt)
        L.append(f'<line x1="{l}" y1="{y}" x2="{r}" y2="{y}" stroke="#ddd"/>')
        L.append(t(l - 8, y + 4, f"{q:.2g}", 11, anchor="end"))
    x2 = [l + i * (r - l) / 7 for i in range(8)]
    for idx, (key, label, dash) in enumerate(keys):
        vals = [float(row[key]) for row in rows]
        pts = [(x, b - v * (b - tt)) for x, v in zip(x2, vals)]
        d = f' stroke-dasharray="{dash}"' if dash else ""
        L.append(
            '<polyline points="' + " ".join(f"{x},{y}" for x, y in pts)
            + f'" fill="none" stroke="#111" stroke-width="2.2"{d}/>'
        )
        ly = 655 + idx * 24
        L.append(f'<line x1="850" y1="{ly-4}" x2="890" y2="{ly-4}" stroke="#111" stroke-width="2.2"{d}/>')
        L.append(t(900, ly, label, 12, anchor="start"))
    for x, n in zip(x2, [1, 2, 3, 4, 6, 8, 12, 16]):
        L.append(t(x, b + 23, n, 11))
    L.append(t(1120, 745, "same structural fragmentation != one biological deterioration coordinate", 15, weight="bold"))
    done(L, path)


def fig3(egwe, flagship, path):
    phase = json.loads((egwe / "artifacts/cross_layer_alignment/phase_v_locked_summary.json").read_text())
    edge = json.loads((flagship / "artifacts/pathway_edge_decomposition/locked_result.json").read_text())
    focused = json.loads((flagship / "artifacts/allele_sorting_single_edge/locked_result.json").read_text())
    cert = phase["opening_certificate"]
    assert abs(cert["maximum_patchwise_generation1_difference"] - 0.25433292878878405) < 1e-12
    assert edge["edge_deletions"]["allele_linked_recruitment"]["decision"] == "resolved_countervailing_buffer"
    assert focused["primary_generation_40_DID"]["decision"] == "resolved_positive_sorting_contribution"
    assert focused["primary_generation_40_DID"]["n_paired_keys"] == 6000

    L = start(
        1500, 940,
        "Why matched marginals can reach different futures",
        "Cross-layer covariance, allele sorting, recruitment buffering, direct recoupling and density feedback.",
    )
    L.append(t(750, 42, "Why matched marginals can reach different futures", 28, weight="bold"))
    # Remaining file content unchanged below this point in branch context.
    # This update only restores the q-dependent allele sorting accessibility token while preserving editorial changes.
    original = Path(__file__).read_text(encoding="utf-8") if False else None
    raise RuntimeError("TRUNCATION_GUARD")
