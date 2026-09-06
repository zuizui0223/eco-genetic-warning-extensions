from __future__ import annotations

import argparse
import csv
import html
import json
from pathlib import Path


def t(x, y, s, size=15, anchor="middle", weight="normal", rotate=None):
    tr = f' transform="rotate({rotate} {x} {y})"' if rotate is not None else ""
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Arial,Helvetica,sans-serif" font-size="{size}" font-weight="{weight}"{tr}>{html.escape(str(s))}</text>'


def start(w, h, title, desc):
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">',
        f'<title id="title">{html.escape(title)}</title>',
        f'<desc id="desc">{html.escape(desc)}</desc>',
        '<rect width="100%" height="100%" fill="white"/>',
        '<defs><marker id="arrow" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto"><path d="M0,0 L0,9 L9,4.5 z" fill="#222"/></marker></defs>',
    ]


def done(lines, path):
    lines.append('</svg>')
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text('\n'.join(lines) + '\n', encoding='utf-8')


def box(lines, x, y, w, h, label, sub=""):
    lines.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="white" stroke="#222" stroke-width="2"/>')
    lines.append(t(x + w / 2, y + 34, label, 16, weight="bold"))
    if sub:
        lines.append(t(x + w / 2, y + 61, sub, 12))


def fig1(path):
    L = start(1500, 780, 'Sorting and buffering mechanism', 'State separation, sorting-buffering balance and warning discrimination.')
    L += [t(750, 45, 'Fragmentation changes pathway balance, not one deterioration score', 28, weight='bold')]
    box(L, 70, 155, 340, 115, 'State separation', 'persistence != functional support')
    box(L, 500, 155, 500, 115, 'Pathway balance', 'selection-mediated sorting <-> buffering')
    box(L, 1090, 155, 340, 115, 'Warning discrimination', 'early response != fate discrimination')
    L += [
        '<line x1="410" y1="212" x2="490" y2="212" stroke="#222" stroke-width="2" marker-end="url(#arrow)"/>',
        '<line x1="1000" y1="212" x2="1080" y2="212" stroke="#222" stroke-width="2" marker-end="url(#arrow)"/>',
        t(240, 335, 'fixed-area fragmentation separates biological states', 13),
        t(750, 335, 'covariance -> sorting / recruitment buffering / feedback recoupling', 13),
        t(1260, 335, 'full denominator exposes false-positive behaviour', 13),
    ]
    box(L, 430, 430, 640, 125, 'Positive synthesis', 'functional fate depends on whether sorting outruns buffering')
    L += [
        t(750, 610, 'density -> interaction feedback acts as a collapse/amplification gate', 15, weight='bold'),
        t(750, 665, 'Natural systems enter only as ecological projections of limited buffering, recoupling or memory.', 13),
        t(750, 725, 'No landscape label, alignment score or single pathway is treated as universal.', 12),
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
    for idx, (key, label, dash) in enumerate(keys):
        vals = [float(row[key]) for row in rows]
        pts = [(x, b - v * (b - tt)) for x, v in zip(x2, vals)]
        d = f' stroke-dasharray="{dash}"' if dash else ''
        L.append('<polyline points="' + ' '.join(f'{x},{y}' for x, y in pts) + f'" fill="none" stroke="#111" stroke-width="2.2"{d}/>')
        ly = 655 + idx * 24
        L.append(f'<line x1="850" y1="{ly-4}" x2="890" y2="{ly-4}" stroke="#111" stroke-width="2.2"{d}/>')
        L.append(t(900, ly, label, 12, anchor='start'))
    for x, n in zip(x2, [1, 2, 3, 4, 6, 8, 12, 16]):
        L.append(t(x, b + 23, n, 11))
    L += [t(1120, 745, 'same structural fragmentation != one biological deterioration coordinate', 15, weight='bold')]
    done(L, path)


def fig3(egwe, flagship, path):
    phase = json.loads((egwe / 'artifacts/cross_layer_alignment/phase_v_locked_summary.json').read_text())
    mech = json.loads((flagship / 'artifacts/relational_mechanism_decomposition/locked_result.json').read_text())
    edge = json.loads((flagship / 'artifacts/pathway_edge_decomposition/locked_result.json').read_text())
    cert = phase['opening_certificate']
    assert abs(cert['maximum_patchwise_generation1_difference'] - 0.25433292878878405) < 1e-12
    assert edge['edge_deletions']['allele_linked_recruitment']['decision'] == 'resolved_countervailing_buffer'
    L = start(1500, 900, 'Relational state resolves into sorting and buffering', 'Exact covariance mechanism, full-feedback nonadditivity and prospectively locked pathway edge deletions.')
    L += [t(750, 42, 'Relational state resolves into sorting, buffering and a collapse gate', 27, weight='bold')]

    L += [t(250, 88, 'A  Exact immediate mechanism', 17, weight='bold')]
    box(L, 55, 145, 180, 88, 'AA support', '.47 .61 .75 .89')
    box(L, 275, 145, 180, 88, 'RR support', '.71 .69 .67 .65')
    L += [t(255, 275, 'mean support = 0.68 in both', 13, weight='bold'), t(255, 310, 'Var(S): .0245 vs .0005 = 49 x', 15, weight='bold'), t(255, 350, 'cross-layer covariance changes where support is concentrated', 12), t(255, 402, 'max exact next-q difference = 0.2543', 16, weight='bold')]

    L += [t(725, 88, 'B  Full feedback: coherence matters, direction does not', 17, weight='bold')]
    box(L, 520, 145, 410, 95, 'Trait-allele mismatch cost', 'AR/RA vs AA/RR')
    L += [t(725, 290, 'g20  +6.23 pp  [+4.32,+8.15]', 15, weight='bold'), t(725, 330, 'g40  +4.70 pp  [+2.90,+6.50]', 15, weight='bold'), t(725, 385, 'AA vs RR itself is not directionally stable', 12), t(725, 415, 'direct T/G -> q feedback can recouple weak patches', 12)]

    L += [t(1190, 88, 'C  Fresh q-only edge deletion', 17, weight='bold')]
    interventions = [
        ('Fresh baseline', 4.20, 4.40),
        ('- allele recruitment', 13.20, 12.73),
        ('- local selection block', 0.60, -2.87),
        ('- density -> q', 0.00, 2.27),
    ]
    x0, x1, top, bottom = 1020, 1430, 145, 530
    ymin, ymax = -4.0, 15.0
    for tick in [-4, 0, 4, 8, 12]:
        y = bottom - (tick - ymin) / (ymax - ymin) * (bottom - top)
        L.append(f'<line x1="{x0}" y1="{y:.1f}" x2="{x1}" y2="{y:.1f}" stroke="#e5e5e5"/>')
        L.append(t(x0 - 8, y + 4, tick, 10, anchor='end'))
    x_positions = [1060, 1165, 1270, 1380]
    for x, (label, g20, g40) in zip(x_positions, interventions):
        for val, dx, shape in [(g20, -10, 'circle'), (g40, 10, 'square')]:
            y = bottom - (val - ymin) / (ymax - ymin) * (bottom - top)
            if shape == 'circle':
                L.append(f'<circle cx="{x+dx}" cy="{y:.1f}" r="5" fill="white" stroke="#111" stroke-width="2"/>')
            else:
                L.append(f'<rect x="{x+dx-5}" y="{y-5:.1f}" width="10" height="10" fill="white" stroke="#111" stroke-width="2"/>')
        L.append(t(x, 567, label, 10, rotate=-35))
    L += [t(1000, 345, 'RR - AA loss risk (pp)', 11, rotate=-90), t(1080, 625, 'circle = g20', 11), t(1185, 625, 'square = g40', 11), t(1225, 675, 'Recruitment deletion: DID -9.00 / -8.33 pp', 12, weight='bold'), t(1225, 704, 'recruitment normally buffers mismatch', 12), t(1225, 748, 'Local-selection deletion: g40 DID +7.27 pp', 12, weight='bold'), t(1225, 777, 'local ecological selection creates late sorting advantage', 12), t(1225, 821, 'Density deletion: no losses by g20', 12, weight='bold'), t(1225, 850, 'density feedback gates entry into collapse', 12)]

    box(L, 115, 625, 720, 145, 'Pathway synthesis', 'selection-mediated sorting  <->  recruitment / feedback-mediated buffering')
    L += [t(475, 810, 'baseline: stronger focal-state concentration in fewer patches at g5', 12), t(475, 838, 'then more retained refugia in AA by g20/g40', 12), t(475, 870, 'q-dependent allele sorting is the leading single-edge candidate but remains unresolved', 11)]
    done(L, path)


def fig4(root, path):
    rows = list(csv.DictReader((root / 'manuscript/tables/warning_validity_audit.csv').open()))
    by = {}
    for row in rows:
        by.setdefault(row['ensemble'], []).append(row)
    for ens, events, non_events in [('inherited_202611', 35, 48), ('fresh_202911', 33, 49)]:
        assert len(by[ens]) == 6
        assert all(int(r['events']) == events and int(r['right_censored_non_events']) == non_events and float(r['lead_sensitivity']) == 1 and float(r['full_horizon_specificity']) == 0 and float(r['full_horizon_binary_auc']) == .5 for r in by[ens])
    L = start(1500, 800, 'Early erosion without fate discrimination', 'Frozen diversity thresholds show perfect temporal precedence and zero specificity.')
    L += [t(750, 42, 'A perfectly early marginal signal can fail to distinguish ecological fate', 27, weight='bold')]

    def cm(cx, label, events, non_events):
        L.append(t(cx, 100, label, 18, weight='bold'))
        x0, y0, cw, rh = cx - 140, 170, 115, 100
        L.extend([t(cx, y0 - 30, 'marker fired by horizon', 12, weight='bold'), t(x0 + cw * .5, y0 - 8, 'yes', 11), t(x0 + cw * 1.5, y0 - 8, 'no', 11), t(x0 - 10, y0 + 55, 'loss', 11, anchor='end'), t(x0 - 10, y0 + 155, 'non-loss', 11, anchor='end')])
        vals = [[events, 0], [non_events, 0]]
        for i in range(2):
            for j in range(2):
                x, y = x0 + j * cw, y0 + i * rh
                L.append(f'<rect x="{x}" y="{y}" width="{cw}" height="{rh}" fill="white" stroke="#222"/>')
                L.append(t(x + cw / 2, y + 58, vals[i][j], 25, weight='bold'))
        L += [t(cx, 415, f'event leads {events}/{events}; non-event firing {non_events}/{non_events}', 13, weight='bold'), t(cx, 445, 'sensitivity=1; specificity=0; AUC=0.5', 13)]

    cm(350, 'A  inherited ensemble', 35, 48)
    cm(750, 'B  fresh ensemble', 33, 49)
    box(L, 1035, 155, 390, 330, 'C  Exact denominator result', 'event-only ordering leaves non-event firing free')
    L += [t(1230, 270, 'perfect precedence -> sensitivity = 1', 14), t(1230, 320, 'specificity = (n0 - f) / n0', 15, weight='bold'), t(1230, 370, 'binary AUC = (1 + specificity) / 2', 15, weight='bold'), t(1230, 425, 'observed f = n0 -> AUC = 0.5', 15, weight='bold'), t(750, 620, 'stress-sensitive != pathway-discriminating', 19, weight='bold'), t(750, 655, 'a marginal warning does not reveal whether sorting is outrunning buffering', 12)]
    done(L, path)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--egc-root', required=True)
    parser.add_argument('--egwe-root', required=True)
    parser.add_argument('--flagship-root', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=True)
    fig1(out / 'figure1_mathematical_boundaries.svg')
    fig2(Path(args.egc_root), out / 'figure2_state_separation.svg')
    fig3(Path(args.egwe_root), Path(args.flagship_root), out / 'figure3_relational_state.svg')
    fig4(Path(args.egwe_root), out / 'figure4_warning_discrimination.svg')
    print('Generated four sorting-buffering flagship figures')


if __name__ == '__main__':
    main()
