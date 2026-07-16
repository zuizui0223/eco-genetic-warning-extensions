from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
from pathlib import Path
from xml.sax.saxutils import escape


def _figure1(path: Path) -> None:
    rows = []
    for kappa in (0.05, 0.20, 0.35):
        for pstar in (0.10, 0.25, 0.50, 0.75, 0.90):
            rows.append((kappa, pstar, kappa * pstar, kappa * (1.0 - pstar)))
    lines = ['<svg xmlns="http://www.w3.org/2000/svg" width="820" height="440" viewBox="0 0 820 440">',
             '<rect width="100%" height="100%" fill="white"/>',
             '<text x="30" y="34" font-family="sans-serif" font-size="20" font-weight="bold">Directional recurrent-mutation coordinates</text>',
             '<text x="30" y="62" font-family="sans-serif" font-size="13">u(L→H)=κμp*, u(H→L)=κμ(1−p*)</text>']
    x0, y0, cw, ch = 155, 90, 120, 90
    for ci, pstar in enumerate((0.10, 0.25, 0.50, 0.75, 0.90)):
        lines.append(f'<text x="{x0+ci*cw+50}" y="82" text-anchor="middle" font-family="sans-serif" font-size="13">p*={pstar:.2f}</text>')
    for ri, kappa in enumerate((0.05, 0.20, 0.35)):
        lines.append(f'<text x="120" y="{y0+ri*ch+38}" text-anchor="end" font-family="sans-serif" font-size="13">κμ={kappa:.2f}</text>')
        for ci, pstar in enumerate((0.10, 0.25, 0.50, 0.75, 0.90)):
            lohi, hilo = kappa*pstar, kappa*(1-pstar)
            x, y = x0+ci*cw, y0+ri*ch
            shade = int(245 - 120*pstar)
            lines += [f'<rect x="{x}" y="{y}" width="100" height="66" fill="rgb({shade},{shade},245)" stroke="black"/>',
                      f'<text x="{x+50}" y="{y+27}" text-anchor="middle" font-family="sans-serif" font-size="12">L→H {lohi:.3f}</text>',
                      f'<text x="{x+50}" y="{y+47}" text-anchor="middle" font-family="sans-serif" font-size="12">H→L {hilo:.3f}</text>']
    lines.append('<text x="30" y="415" font-family="sans-serif" font-size="12">Mechanism diagram; no finite ecological outcome is inferred from this panel alone.</text></svg>')
    path.write_text('\n'.join(lines) + '\n', encoding='utf-8')


def _figure4(stage2_csv: Path, path: Path) -> None:
    rows = list(csv.DictReader(stage2_csv.open(encoding='utf-8')))
    lines = ['<svg xmlns="http://www.w3.org/2000/svg" width="900" height="540" viewBox="0 0 900 540">',
             '<rect width="100%" height="100%" fill="white"/>',
             '<text x="30" y="34" font-family="sans-serif" font-size="20" font-weight="bold">Stage II candidate-regime composition</text>']
    x0, y0, barw, gap = 210, 60, 600, 30
    for i, row in enumerate(rows):
        rapid = int(row['rapid_loss_candidate_count'])
        mixed = int(row['seed_heterogeneous_candidate_count'])
        persist = int(row['persistence_candidate_count'])
        total = max(1, rapid + mixed + persist)
        y = y0 + i*gap
        label = f"κ={float(row['kappa_mu']):.2f}, p*={float(row['p_star']):.2f}"
        lines.append(f'<text x="195" y="{y+13}" text-anchor="end" font-family="sans-serif" font-size="11">{escape(label)}</text>')
        cursor = x0
        for value, fill in ((rapid, '#d95f02'), (mixed, '#7570b3'), (persist, '#1b9e77')):
            width = barw * value / total
            lines.append(f'<rect x="{cursor:.2f}" y="{y}" width="{width:.2f}" height="18" fill="{fill}"/>')
            cursor += width
    lines += ['<rect x="260" y="515" width="16" height="12" fill="#d95f02"/><text x="282" y="526" font-family="sans-serif" font-size="12">rapid loss</text>',
              '<rect x="390" y="515" width="16" height="12" fill="#7570b3"/><text x="412" y="526" font-family="sans-serif" font-size="12">seed heterogeneous</text>',
              '<rect x="565" y="515" width="16" height="12" fill="#1b9e77"/><text x="587" y="526" font-family="sans-serif" font-size="12">persistence</text>',
              '</svg>']
    path.write_text('\n'.join(lines) + '\n', encoding='utf-8')


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--stage1-dir', required=True)
    parser.add_argument('--stage2-dir', required=True)
    parser.add_argument('--repo-root', default='.')
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    root = Path(args.repo_root)
    stage1 = Path(args.stage1_dir)
    stage2 = Path(args.stage2_dir)
    out = Path(args.output)
    if out.exists():
        shutil.rmtree(out)
    (out / 'figures').mkdir(parents=True)
    (out / 'tables').mkdir(parents=True)
    (out / 'manuscript').mkdir(parents=True)

    required_stage1 = ['stage1_publication_summary.json', 'stage1_coordinate_summary.csv', 'figure2_stage1_source_feasibility.svg', 'figure5_stage3_ordering.svg', 'figure6_stage3_lead_time.svg']
    required_stage2 = ['stage2_coordinate_regimes.csv', 'figure_stage2_coordinate_regimes.svg']
    for name in required_stage1:
        if not (stage1 / name).exists():
            raise FileNotFoundError(stage1 / name)
    for name in required_stage2:
        if not (stage2 / name).exists():
            raise FileNotFoundError(stage2 / name)

    shutil.copy2(stage1 / 'stage1_publication_summary.json', out / 'tables')
    shutil.copy2(stage1 / 'stage1_coordinate_summary.csv', out / 'tables')
    shutil.copy2(stage2 / 'stage2_coordinate_regimes.csv', out / 'tables')
    shutil.copy2(root / 'manuscript/tables/stage3_endpoint_summary.csv', out / 'tables')
    shutil.copy2(stage1 / 'figure2_stage1_source_feasibility.svg', out / 'figures/figure2_stage1_source_feasibility.svg')
    shutil.copy2(stage2 / 'figure_stage2_coordinate_regimes.svg', out / 'figures/figure3_stage2_coordinate_regimes.svg')
    shutil.copy2(stage1 / 'figure5_stage3_ordering.svg', out / 'figures')
    shutil.copy2(stage1 / 'figure6_stage3_lead_time.svg', out / 'figures')
    _figure1(out / 'figures/figure1_mutation_coordinates.svg')
    _figure4(stage2 / 'stage2_coordinate_regimes.csv', out / 'figures/figure4_stage2_regime_composition.svg')

    for name in ('main_text.md', 'supplementary_methods.md', 'claim_evidence_map.md', 'artifact_index.md', 'submission_checklist.md'):
        shutil.copy2(root / 'manuscript' / name, out / 'manuscript')

    manifest = {'files': {}}
    for file in sorted(p for p in out.rglob('*') if p.is_file()):
        manifest['files'][str(file.relative_to(out))] = hashlib.sha256(file.read_bytes()).hexdigest()
    (out / 'manifest.json').write_text(json.dumps(manifest, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
