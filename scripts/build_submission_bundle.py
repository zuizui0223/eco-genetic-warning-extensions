from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
from pathlib import Path
from xml.sax.saxutils import escape

from eco_genetic_warning_extensions.protocol002_publication_outputs import write_regime_svg
from eco_genetic_warning_extensions.publication_figures import (
    _stage1_svg,
    _stage3_lead_time_svg,
    _stage3_ordering_svg,
)


def _figure1(path: Path) -> None:
    lines = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="600" viewBox="0 0 1200 600" role="img" aria-labelledby="figure1-title figure1-desc">',
        '<title id="figure1-title">Genetic warning emerges from eco-genetic closure</title>',
        '<desc id="figure1-desc">Conceptual causal chain from fragmentation through interaction state, high-trait state, local effective size, and genetic diversity. Genetic diversity generates a relative warning that can precede realised functional-trait loss. Recurrent transition direction, deterioration, migration, calibration, baseline eligibility, and censoring modify this closure.</desc>',
        '<rect width="100%" height="100%" fill="white"/>',
        '<text x="600" y="58" text-anchor="middle" font-family="sans-serif" font-size="31" font-weight="bold">Eco-genetic closure</text>',
        '<defs><marker id="arrow" markerWidth="9" markerHeight="9" refX="7.5" refY="4.5" orient="auto"><path d="M0,0 L0,9 L8,4.5 z" fill="#111"/></marker></defs>',
        '<rect x="30" y="170" width="160" height="82" rx="10" fill="white" stroke="#111" stroke-width="2"/>',
        '<text x="110" y="218" text-anchor="middle" font-family="sans-serif" font-size="19">Fragmentation</text>',
        '<rect x="245" y="163" width="180" height="96" rx="10" fill="white" stroke="#111" stroke-width="2"/>',
        '<text x="335" y="204" text-anchor="middle" font-family="sans-serif" font-size="19">Interaction</text>',
        '<text x="335" y="228" text-anchor="middle" font-family="sans-serif" font-size="19">state</text>',
        '<rect x="480" y="163" width="180" height="96" rx="10" fill="white" stroke="#111" stroke-width="2"/>',
        '<text x="570" y="204" text-anchor="middle" font-family="sans-serif" font-size="19">High-trait</text>',
        '<text x="570" y="228" text-anchor="middle" font-family="sans-serif" font-size="19">state</text>',
        '<rect x="715" y="163" width="205" height="96" rx="10" fill="white" stroke="#111" stroke-width="2"/>',
        '<text x="817.5" y="204" text-anchor="middle" font-family="sans-serif" font-size="19">Local effective</text>',
        '<text x="817.5" y="228" text-anchor="middle" font-family="sans-serif" font-size="19">size</text>',
        '<rect x="975" y="163" width="180" height="96" rx="10" fill="white" stroke="#111" stroke-width="2"/>',
        '<text x="1065" y="204" text-anchor="middle" font-family="sans-serif" font-size="19">Genetic</text>',
        '<text x="1065" y="228" text-anchor="middle" font-family="sans-serif" font-size="19">diversity</text>',
        '<line x1="190" y1="211" x2="245" y2="211" stroke="#111" stroke-width="2.5" marker-end="url(#arrow)"/>',
        '<line x1="425" y1="211" x2="480" y2="211" stroke="#111" stroke-width="2.5" marker-end="url(#arrow)"/>',
        '<line x1="660" y1="211" x2="715" y2="211" stroke="#111" stroke-width="2.5" marker-end="url(#arrow)"/>',
        '<line x1="920" y1="211" x2="975" y2="211" stroke="#111" stroke-width="2.5" marker-end="url(#arrow)"/>',
        '<rect x="455" y="360" width="250" height="96" rx="10" fill="white" stroke="#111" stroke-width="2"/>',
        '<text x="580" y="401" text-anchor="middle" font-family="sans-serif" font-size="19">Functional-trait</text>',
        '<text x="580" y="425" text-anchor="middle" font-family="sans-serif" font-size="19">loss</text>',
        '<rect x="815" y="360" width="250" height="96" rx="10" fill="white" stroke="#111" stroke-width="2"/>',
        '<text x="940" y="401" text-anchor="middle" font-family="sans-serif" font-size="19">Relative genetic</text>',
        '<text x="940" y="425" text-anchor="middle" font-family="sans-serif" font-size="19">warning</text>',
        '<line x1="570" y1="259" x2="540" y2="360" stroke="#111" stroke-width="2.5" marker-end="url(#arrow)"/>',
        '<line x1="1065" y1="259" x2="985" y2="360" stroke="#111" stroke-width="2.5" marker-end="url(#arrow)"/>',
        '<line x1="815" y1="408" x2="705" y2="408" stroke="#111" stroke-width="2.5" marker-end="url(#arrow)"/>',
        '<text x="600" y="530" text-anchor="middle" font-family="sans-serif" font-size="16">Closure modifiers: recurrent transition direction, deterioration, migration, calibration,</text>',
        '<text x="600" y="555" text-anchor="middle" font-family="sans-serif" font-size="16">baseline eligibility, and censoring</text>',
        '</svg>',
    ]
    path.write_text('\n'.join(lines) + '\n', encoding='utf-8')


def _figure4(stage2_csv: Path, path: Path) -> None:
    rows = list(csv.DictReader(stage2_csv.open(encoding='utf-8')))
    lines = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="900" height="540" viewBox="0 0 900 540" role="img" aria-labelledby="figure4-title figure4-desc">',
        '<title id="figure4-title">Trait-loss regime composition across transition coordinates</title>',
        '<desc id="figure4-desc">Stacked bars show rapid-loss, seed-heterogeneous, and persistence candidate counts for each transition coordinate. Direct labels R, H, and P provide a non-colour encoding.</desc>',
        '<rect width="100%" height="100%" fill="white"/>',
        '<text x="30" y="34" font-family="sans-serif" font-size="20" font-weight="bold">Trait-loss regime composition across transition coordinates</text>',
    ]
    x0, y0, barw, gap = 210, 60, 600, 30
    categories = (
        ('R', 'rapid loss', '#d95f02'),
        ('H', 'seed heterogeneous', '#7570b3'),
        ('P', 'persistence', '#1b9e77'),
    )
    for i, row in enumerate(rows):
        values = (
            int(row['rapid_loss_candidate_count']),
            int(row['seed_heterogeneous_candidate_count']),
            int(row['persistence_candidate_count']),
        )
        total = max(1, sum(values))
        y = y0 + i * gap
        label = f"κ={float(row['kappa_mu']):.2f}, p*={float(row['p_star']):.2f}"
        lines.append(f'<text x="195" y="{y+13}" text-anchor="end" font-family="sans-serif" font-size="11">{escape(label)}</text>')
        cursor = x0
        for value, (code, _name, fill) in zip(values, categories):
            width = barw * value / total
            lines.append(f'<rect x="{cursor:.2f}" y="{y}" width="{width:.2f}" height="18" fill="{fill}" stroke="white" stroke-width="0.5"/>')
            if width >= 22:
                lines.append(f'<text x="{cursor + width/2:.2f}" y="{y+13}" text-anchor="middle" font-family="sans-serif" font-size="10" font-weight="bold" fill="white">{code}</text>')
            cursor += width
    legend_x = (245, 405, 600)
    for x, (code, name, fill) in zip(legend_x, categories):
        lines.append(f'<rect x="{x}" y="510" width="16" height="12" fill="{fill}" stroke="#333" stroke-width="0.5"/>')
        lines.append(f'<text x="{x+22}" y="521" font-family="sans-serif" font-size="12">{code} — {escape(name)}</text>')
    lines.append('</svg>')
    path.write_text('\n'.join(lines) + '\n', encoding='utf-8')


def _read_stage1_rows(path: Path) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    with path.open(encoding='utf-8', newline='') as handle:
        for raw in csv.DictReader(handle):
            row: dict[str, object] = dict(raw)
            for name in ('kappa_mu', 'p_star', 'projection_supported_rate'):
                row[name] = float(raw[name])
            for name in ('projection_supported', 'attempted'):
                row[name] = int(raw[name])
            rows.append(row)
    return rows


def _regenerate_publication_figures(stage1: Path, stage2: Path, root: Path, out: Path) -> None:
    stage1_rows = _read_stage1_rows(stage1 / 'stage1_coordinate_summary.csv')
    stage2_rows = list(csv.DictReader((stage2 / 'stage2_coordinate_regimes.csv').open(encoding='utf-8')))
    stage3_summary_path = root / 'artifacts/protocol003/stage3_validation_summary.json'
    if not stage3_summary_path.exists():
        raise FileNotFoundError(stage3_summary_path)
    stage3 = json.loads(stage3_summary_path.read_text(encoding='utf-8'))

    (out / 'figures/figure2_stage1_source_feasibility.svg').write_text(
        _stage1_svg(stage1_rows), encoding='utf-8'
    )
    write_regime_svg(stage2_rows, out / 'figures/figure3_stage2_coordinate_regimes.svg')
    (out / 'figures/figure5_stage3_ordering.svg').write_text(
        _stage3_ordering_svg(stage3['domains']), encoding='utf-8'
    )
    (out / 'figures/figure6_stage3_lead_time.svg').write_text(
        _stage3_lead_time_svg(stage3['domains']), encoding='utf-8'
    )


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

    required_stage1 = ['stage1_publication_summary.json', 'stage1_coordinate_summary.csv']
    required_stage2 = ['stage2_coordinate_regimes.csv']
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

    _figure1(out / 'figures/figure1_eco_genetic_closure.svg')
    _regenerate_publication_figures(stage1, stage2, root, out)
    _figure4(stage2 / 'stage2_coordinate_regimes.csv', out / 'figures/figure4_trait_loss_regime_composition.svg')

    manuscript_files = (
        'main_text.md',
        'references.md',
        'figure_captions.md',
        'figure_accessibility_review.md',
        'table_captions.md',
        'supplementary_methods.md',
        'submission_metadata.md',
        'claim_evidence_map.md',
        'artifact_index.md',
        'submission_checklist.md',
    )
    for name in manuscript_files:
        shutil.copy2(root / 'manuscript' / name, out / 'manuscript')

    manifest = {'files': {}}
    for file in sorted(p for p in out.rglob('*') if p.is_file()):
        manifest['files'][str(file.relative_to(out))] = hashlib.sha256(file.read_bytes()).hexdigest()
    (out / 'manifest.json').write_text(json.dumps(manifest, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
