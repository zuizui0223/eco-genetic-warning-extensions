from __future__ import annotations

import argparse
import csv
import html
import json
from pathlib import Path


def t(x, y, s, size=15, anchor="middle", weight="normal", rotate=None):
    r = f' transform="rotate({rotate} {x} {y})"' if rotate is not None else ""
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Arial,Helvetica,sans-serif" font-size="{size}" font-weight="{weight}"{r}>{html.escape(str(s))}</text>'


def start(w, h, title, desc):
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">',
        f'<title id="title">{html.escape(title)}</title>',
        f'<desc id="desc">{html.escape(desc)}</desc>',
        '<rect width="100%" height="100%" fill="white"/>',
        '<defs><marker id="a" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto"><path d="M0,0 L0,9 L9,4.5 z" fill="#222"/></marker></defs>',
    ]


def done(lines, path):
    lines.append('</svg>')
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text('\n'.join(lines) + '\n', encoding='utf-8')


def box(lines, x, y, w, h, label, sub=""):
    lines.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="white" stroke="#222" stroke-width="2"/>')
    lines.append(t(x + w / 2, y + 34, label, 16, weight="bold"))
    if sub:
        lines.append(t(x + w / 2, y + 60, sub, 12))


def fig1(path):
    L = start(1500, 760, 'Three mechanistic boundaries', 'Conceptual map linking state separation, competing relational pathways and warning discrimination.')
    L += [t(750, 45, 'Three boundaries on functional vulnerability under fragmentation', 28, weight='bold')]
    items = [
        (80, 'State separation', 'persistence != functional support'),
        (525, 'Relational mechanism', 'matching pathway <-> compensation pathway'),
        (970, 'Warning discrimination', 'perfect precedence != specificity'),
    ]
    for x, a, b in items:
        box(L, x, 160, 350, 115, a, b)
    for x1, x2 in [(430, 525), (875, 970)]:
        L.append(f'<line x1="{x1}" y1="218" x2="{x2-10}" y2="218" stroke="#222" stroke-width="2" marker-end="url(#a)"/>')
    L += [
        t(255, 350, 'Exact state geometry + fixed-area fragmentation', 13),
        t(700, 350, 'Covariance, factorial intervention + recruitment closure', 13),
        t(1145, 350, 'Exact denominator identity + full denominator', 13),
    ]
    box(L, 430, 450, 640, 125, 'Positive synthesis', 'functional fate is the net result of competing relational pathways')
    L += [
        t(750, 620, 'Natural systems enter only as ecological projection:', 15, weight='bold'),
        t(750, 650, 'uncompensated mismatch, feedback-mediated recoupling and temporal lag', 14),
        t(750, 710, 'No landscape label or scalar alignment score is treated as a universal mechanism.', 12),
    ]
    done(L, path)


def fig2(egc, path):
    rows = list(csv.DictReader((egc / 'artifacts/h3_fragmentation_gradient/h3_fragmentation_gradient_pooled_summary.csv').open()))
    assert [int(r['patch_count']) for r in rows] == [1, 2, 3, 4, 6, 8, 12, 16]
    assert int(rows[0]['projection_supported']) == 1037
    L = start(1500, 800, 'Fragmentation separates functional support from persistence', 'Fixed-area fragmentation gradient with distinct biological-state responses.')
    L += [t(750, 42, 'Fragmentation separates functional support from persistence', 28, weight='bold'), t(350, 90, 'A  Potential viability and realised occupancy', 18, weight='bold'), t(1110, 90, 'B  Retained state ratios', 18, weight='bold')]
    left, right, top, bottom = 90, 670, 150, 610
    for p in [0, 25, 50, 75, 100]:
        y = bottom - p / 100 * (bottom - top)
        L.append(f'<line x1="{left}" y1="{y}" x2="{right}" y2="{y}" stroke="#ddd"/>')
        L.append(t(left - 8, y + 4, p, 11, anchor='end'))
    xs = [left + i * (right - left) / 7 for i in range(8)]
    pts = []
    for x, p, n in zip(xs, [100] + [0] * 7, [1, 2, 3, 4, 6, 8, 12, 16]):
        y = bottom - p / 100 * (bottom - top)
        pts.append((x, y))
        L.append(f'<circle cx="{x}" cy="{y}" r="5" fill="white" stroke="#111"/>')
        L.append(t(x, bottom + 23, n, 11))
    L.append('<polyline points="' + ' '.join(f'{x},{y}' for x, y in pts) + '" fill="none" stroke="#111" stroke-width="2.3"/>')
    L += [t(380, 132, 'realised occupancy at generation 30 ~99.6-100%', 12), t(30, 390, 'supported outcomes (%)', 12, rotate=-90), t(380, 665, 'number of isolated equal patches', 12), t(380, 710, 'potential viability: 1,037/1,037 -> 0/1,037 after first split', 14, weight='bold')]

    l, r, tt, b = 820, 1430, 150, 610
    keys = [
        ('final_interaction_mean_ratio_to_n1_median', 'interaction', ''),
        ('final_effective_size_mean_ratio_to_n1_median', 'local effective size', '8 5'),
        ('realised_high_trait_mass_mean_ratio_to_n1_median', 'realised high-trait mass', '3 4'),
    ]
    for q in [0, .25, .5, .75, 1]:
        y = b - q * (b - tt)
        L.append(f'<line x1="{l}" y1="{y}" x2="{r}" y2="{y}" stroke="#ddd"/>')
        L.append(t(l - 8, y + 4, f'{q:.2g}', 11, anchor='end'))
    x2 = [l + i * (r - l) / 7 for i in range(8)]
    for idx, (k, lab, dash) in enumerate(keys):
        vals = [float(row[k]) for row in rows]
        pts = [(x, b - v * (b - tt)) for x, v in zip(x2, vals)]
        d = f' stroke-dasharray="{dash}"' if dash else ''
        L.append('<polyline points="' + ' '.join(f'{x},{y}' for x, y in pts) + f'" fill="none" stroke="#111" stroke-width="2.2"{d}/>')
        ly = 655 + idx * 24
        L.append(f'<line x1="850" y1="{ly-4}" x2="890" y2="{ly-4}" stroke="#111" stroke-width="2.2"{d}/>')
        L.append(t(900, ly, lab, 12, anchor='start'))
    for x, n in zip(x2, [1, 2, 3, 4, 6, 8, 12, 16]):
        L.append(t(x, b + 23, n, 11))
    L += [t(1120, 745, 'same structural fragmentation != one biological deterioration coordinate', 15, weight='bold')]
    done(L, path)


def fig3(egwe, mechanism_root, path):
    phase = json.loads((egwe / 'artifacts/cross_layer_alignment/phase_v_locked_summary.json').read_text())
    mech = json.loads((mechanism_root / 'artifacts/relational_mechanism_decomposition/locked_result.json').read_text())
    c = phase['opening_certificate']
    assert abs(c['maximum_patchwise_generation1_difference'] - 0.25433292878878405) < 1e-12
    assert abs(mech['analytic_headline']['AA_RR_support_variance_ratio'] - 49.0) < 1e-12

    L = start(1500, 860, 'Competing relational pathways', 'Exact covariance mechanism, full-feedback factorial, and q-only intervention.')
    L += [t(750, 42, 'Relational covariance opens competing pathways to functional fate', 28, weight='bold')]

    # Panel A: exact immediate mechanism.
    L += [t(270, 88, 'A  Same mean support, different spatial variance', 17, weight='bold')]
    box(L, 70, 145, 180, 95, 'AA support', '.47 .61 .75 .89')
    box(L, 300, 145, 180, 95, 'RR support', '.71 .69 .67 .65')
    L += [
        t(275, 285, 'mean = .68 in both states', 13, weight='bold'),
        t(275, 320, 'Var(S): .0245 vs .0005 = 49 x', 15, weight='bold'),
        t(275, 365, 'Cov(q,B) changes support variance', 13),
        t(275, 400, 'while all layer-wise marginals remain fixed', 12),
        t(275, 455, 'max exact next-q difference = 0.2543', 16, weight='bold'),
    ]

    # Panel B: factorial risks.
    L += [t(790, 88, 'B  Full-feedback trait x allele factorial', 17, weight='bold')]
    xcats = {'AA': 615, 'AR': 720, 'RA': 825, 'RR': 930}
    top, bottom = 150, 500
    ymin, ymax = .30, .80
    for tick in [.3, .4, .5, .6, .7, .8]:
        y = bottom - (tick - ymin) / (ymax - ymin) * (bottom - top)
        L.append(f'<line x1="570" y1="{y}" x2="970" y2="{y}" stroke="#eee"/>')
        L.append(t(560, y + 4, f'{tick:.1f}', 10, anchor='end'))
    for h, dash in [('20', ''), ('40', '7 5')]:
        risks = mech['full_feedback_factorial'][f'generation_{h}']['risk'] if f'generation_{h}' in mech['full_feedback_factorial'] else None
        if risks is None:
            risks = {k: v for k, v in mech['full_feedback_factorial'][f'generation_{h}'].items()}
        pts = []
        for code in ['AA', 'AR', 'RA', 'RR']:
            v = mech['full_feedback_factorial'][f'generation_{h}']['risk'][code]
            x = xcats[code]
            y = bottom - (v - ymin) / (ymax - ymin) * (bottom - top)
            pts.append((x, y))
            L.append(f'<circle cx="{x}" cy="{y}" r="5" fill="white" stroke="#111"/>')
        d = f' stroke-dasharray="{dash}"' if dash else ''
        L.append('<polyline points="' + ' '.join(f'{x},{y}' for x, y in pts) + f'" fill="none" stroke="#111" stroke-width="2"{d}/>')
    for code, x in xcats.items():
        L.append(t(x, 525, code, 11, weight='bold'))
    L += [
        t(770, 565, 'mismatched (AR,RA) - matched (AA,RR)', 12),
        t(770, 592, 'g20 +6.23 pp [4.32,8.15]', 13, weight='bold'),
        t(770, 618, 'g40 +4.70 pp [2.90,6.50]', 13, weight='bold'),
        t(770, 650, 'trait x allele interaction is strongly non-additive', 12),
    ]

    # Panel C: q-only intervention.
    L += [t(1240, 88, 'C  Remove direct T/G -> q feedback', 17, weight='bold')]
    box(L, 1060, 145, 360, 90, 'generation 1', 'AA and RR q fields identical')
    L += [
        t(1240, 285, 'later RR - AA functional-loss risk', 13, weight='bold'),
        t(1240, 330, 'g20  +7.13 pp', 18, weight='bold'),
        t(1240, 358, '[+3.91,+10.36]', 12),
        t(1240, 415, 'g40  +6.93 pp', 18, weight='bold'),
        t(1240, 443, '[+3.79,+10.08]', 12),
        t(1240, 505, 'direct q feedback is not necessary', 13, weight='bold'),
        t(1240, 535, 'for relational mismatch to reach loss', 12),
    ]
    box(L, 1035, 610, 410, 110, 'Mechanistic synthesis', 'matching-dependent recruitment is opposed by feedback-mediated compensation')
    L += [t(750, 800, 'Long-horizon fate is not a monotone function of alignment or support variance.', 15, weight='bold')]
    done(L, path)


def fig4(root, path):
    rows = list(csv.DictReader((root / 'manuscript/tables/warning_validity_audit.csv').open()))
    by = {}
    for r in rows:
        by.setdefault(r['ensemble'], []).append(r)
    for ens, ev, ne in [('inherited_202611', 35, 48), ('fresh_202911', 33, 49)]:
        assert len(by[ens]) == 6
        assert all(int(r['events']) == ev and int(r['right_censored_non_events']) == ne and float(r['lead_sensitivity']) == 1 and float(r['full_horizon_specificity']) == 0 and float(r['full_horizon_binary_auc']) == .5 for r in by[ens])
    L = start(1500, 800, 'Early erosion without fate discrimination', 'Frozen diversity thresholds show perfect temporal precedence and zero specificity.')
    L += [t(750, 42, 'A perfectly early marginal signal can fail to distinguish ecological fate', 27, weight='bold')]

    def cm(cx, label, ev, ne):
        L.append(t(cx, 100, label, 18, weight='bold'))
        x0, y0, cw, rh = cx - 140, 170, 115, 100
        L.extend([t(cx, y0 - 30, 'marker fired by horizon', 12, weight='bold'), t(x0 + cw * .5, y0 - 8, 'yes', 11), t(x0 + cw * 1.5, y0 - 8, 'no', 11), t(x0 - 10, y0 + 55, 'loss', 11, anchor='end'), t(x0 - 10, y0 + 155, 'non-loss', 11, anchor='end')])
        vals = [[ev, 0], [ne, 0]]
        for i in range(2):
            for j in range(2):
                x, y = x0 + j * cw, y0 + i * rh
                L.append(f'<rect x="{x}" y="{y}" width="{cw}" height="{rh}" fill="white" stroke="#222"/>')
                L.append(t(x + cw / 2, y + 58, vals[i][j], 25, weight='bold'))
        L.extend([t(cx, 415, f'event leads {ev}/{ev}; non-event firing {ne}/{ne}', 13, weight='bold'), t(cx, 445, 'sensitivity=1; specificity=0; AUC=0.5', 13)])

    cm(350, 'A  inherited ensemble', 35, 48)
    cm(750, 'B  fresh ensemble', 33, 49)
    box(L, 1035, 155, 390, 330, 'C  Exact denominator result', 'event-only ordering leaves non-event firing free')
    L += [t(1230, 270, 'perfect precedence -> sensitivity = 1', 14), t(1230, 320, 'specificity = (n0 - f) / n0', 15, weight='bold'), t(1230, 370, 'binary AUC = (1 + specificity) / 2', 15, weight='bold'), t(1230, 425, 'observed f = n0 -> AUC = 0.5', 15, weight='bold'), t(750, 620, 'stress-sensitive != fate-discriminating', 19, weight='bold'), t(750, 655, 'all six frozen H_alpha/H_gamma rules reach the same horizon classification endpoint', 12)]
    done(L, path)


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--egc-root', required=True)
    p.add_argument('--egwe-root', required=True)
    p.add_argument('--mechanism-root', required=True)
    p.add_argument('--output', required=True)
    a = p.parse_args()
    out = Path(a.output)
    out.mkdir(parents=True, exist_ok=True)
    egc = Path(a.egc_root)
    egwe = Path(a.egwe_root)
    mechanism = Path(a.mechanism_root)
    fig1(out / 'figure1_mathematical_boundaries.svg')
    fig2(egc, out / 'figure2_state_separation.svg')
    fig3(egwe, mechanism, out / 'figure3_relational_state.svg')
    fig4(egwe, out / 'figure4_warning_discrimination.svg')
    print('Generated four mechanistic flagship figures')


if __name__ == '__main__':
    main()
