from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
from pathlib import Path

from eco_genetic_warning_extensions.protocol002_publication_outputs import write_regime_svg
from eco_genetic_warning_extensions.publication_figures import (
    _stage1_svg,
    write_stage3_figures,
)
from eco_genetic_warning_extensions.stage3_review_audit import (
    audit as stage3_review_audit,
    load_records as load_stage3_records,
    write_outputs as write_stage3_review_outputs,
)
from eco_genetic_warning_extensions.precision_bounded_null import (
    audit as precision_bounded_null_audit,
    write_output as write_precision_bounded_null_output,
)
from eco_genetic_warning_extensions.warning_validity_audit import (
    audit as warning_validity_audit,
    load_records as load_warning_validity_records,
    write_audit_outputs as write_warning_validity_outputs,
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


def _regenerate_publication_figures(stage1: Path, stage2: Path, stage3_audit_path: Path, out: Path) -> None:
    stage1_rows = _read_stage1_rows(stage1 / 'stage1_coordinate_summary.csv')
    stage2_rows = list(csv.DictReader((stage2 / 'stage2_coordinate_regimes.csv').open(encoding='utf-8')))
    (out / 'figures/figure2_stage1_source_feasibility.svg').write_text(_stage1_svg(stage1_rows), encoding='utf-8')
    write_regime_svg(stage2_rows, out / 'figures/figure3_stage2_coordinate_regimes.svg')
    write_stage3_figures(stage3_audit_path, out / 'figures')


def _copy_h3_gradient(gradient: Path, out: Path) -> None:
    required = (
        'h3_fragmentation_gradient_records.csv',
        'h3_fragmentation_gradient_cell_summary.csv',
        'h3_fragmentation_gradient_pooled_summary.csv',
        'h3_fragmentation_gradient_metadata.json',
        'figure_s_fragmentation_gradient.svg',
        'MANIFEST.sha256',
    )
    missing = [name for name in required if not (gradient / name).exists()]
    if missing:
        raise FileNotFoundError('missing H3 gradient files: ' + ', '.join(missing))

    metadata = json.loads((gradient / 'h3_fragmentation_gradient_metadata.json').read_text(encoding='utf-8'))
    if metadata.get('attempted_source_replicates') != 1200:
        raise RuntimeError('H3 gradient attempted-source denominator drifted')
    if metadata.get('patch_counts') != [1, 2, 3, 4, 6, 8, 12, 16]:
        raise RuntimeError('H3 gradient patch-count contract drifted')
    if metadata.get('warning_endpoints_evaluated') is not False:
        raise RuntimeError('H3 gradient must remain warning-free')

    (out / 'supplement').mkdir(parents=True, exist_ok=True)
    (out / 'provenance/h3_fragmentation_gradient').mkdir(parents=True, exist_ok=True)
    shutil.copy2(gradient / 'figure_s_fragmentation_gradient.svg', out / 'supplement/figure_s1_fragmentation_gradient.svg')
    for name in (
        'h3_fragmentation_gradient_records.csv',
        'h3_fragmentation_gradient_cell_summary.csv',
        'h3_fragmentation_gradient_pooled_summary.csv',
    ):
        shutil.copy2(gradient / name, out / 'tables' / name)
    shutil.copy2(gradient / 'h3_fragmentation_gradient_metadata.json', out / 'provenance/h3_fragmentation_gradient/metadata.json')
    shutil.copy2(gradient / 'MANIFEST.sha256', out / 'provenance/h3_fragmentation_gradient/source_MANIFEST.sha256')


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--stage1-dir', required=True)
    parser.add_argument('--stage2-dir', required=True)
    parser.add_argument('--stage3-records', required=True)
    parser.add_argument('--h3-gradient-dir', required=True)
    parser.add_argument('--repo-root', default='.')
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    root = Path(args.repo_root)
    stage1 = Path(args.stage1_dir)
    stage2 = Path(args.stage2_dir)
    stage3_records = Path(args.stage3_records)
    h3_gradient = Path(args.h3_gradient_dir)
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
    if not stage3_records.exists():
        raise FileNotFoundError(stage3_records)

    shutil.copy2(stage1 / 'stage1_publication_summary.json', out / 'tables')
    shutil.copy2(stage1 / 'stage1_coordinate_summary.csv', out / 'tables')
    shutil.copy2(stage2 / 'stage2_coordinate_regimes.csv', out / 'tables')
    shutil.copy2(root / 'manuscript/tables/stage3_endpoint_summary.csv', out / 'tables')
    shutil.copy2(root / 'manuscript/tables/inherited_h3_effect_summary.csv', out / 'tables')

    # Stage III is vendored as a lossless trajectory-endpoint table derived from
    # the two immutable historical artifacts. The materializer verifies its
    # source artifact IDs/digests, decoded checksum, row counts and headline
    # lead/tie/lag totals before this script receives it.
    shutil.copy2(stage3_records, out / 'tables/stage3_trajectory_endpoint_records.csv')
    records = load_stage3_records(stage3_records)
    audit_result = stage3_review_audit(records)
    audit_path = out / 'tables/stage3_review_audit.json'
    review_csv = out / 'tables/stage3_review_summary.csv'
    difference_csv = out / 'tables/stage3_between_domain_differences.csv'
    write_stage3_review_outputs(audit_result, audit_path, review_csv, difference_csv)

    committed_review_csv = root / 'manuscript/tables/stage3_review_summary.csv'
    if review_csv.read_bytes() != committed_review_csv.read_bytes():
        raise RuntimeError('generated Stage III review summary differs from committed publication summary')
    committed_difference_csv = root / 'manuscript/tables/stage3_between_domain_differences.csv'
    if difference_csv.read_bytes() != committed_difference_csv.read_bytes():
        raise RuntimeError('generated Stage III difference bootstrap differs from committed publication summary')

    warning_records = root / 'artifacts/warning_validity/trajectory_endpoint_records.csv'
    warning_manifest_path = root / 'artifacts/warning_validity/source_manifest.json'
    warning_manifest = json.loads(warning_manifest_path.read_text(encoding='utf-8'))
    expected_warning_sha = warning_manifest['record_table']['sha256']
    observed_warning_sha = hashlib.sha256(warning_records.read_bytes()).hexdigest()
    if observed_warning_sha != expected_warning_sha:
        raise RuntimeError('warning-validity record checksum differs from its source manifest')
    warning_result = warning_validity_audit(load_warning_validity_records(warning_records))
    warning_json = out / 'tables/warning_validity_audit.json'
    warning_csv = out / 'tables/warning_validity_audit.csv'
    write_warning_validity_outputs(warning_result, warning_json, warning_csv)
    if warning_json.read_bytes() != (root / 'artifacts/prepublication_review/warning_validity_audit.json').read_bytes():
        raise RuntimeError('generated warning-validity audit differs from committed review artifact')
    if warning_csv.read_bytes() != (root / 'manuscript/tables/warning_validity_audit.csv').read_bytes():
        raise RuntimeError('generated warning-validity table differs from committed publication table')
    shutil.copy2(warning_records, out / 'tables/warning_validity_trajectory_endpoint_records.csv')
    (out / 'provenance').mkdir(parents=True, exist_ok=True)
    shutil.copy2(warning_manifest_path, out / 'provenance/warning_validity_source_manifest.json')

    precision_source = json.loads(
        (root / 'artifacts/precision_bounded_null/source_counts.json').read_text(encoding='utf-8')
    )
    precision_result = precision_bounded_null_audit(precision_source)
    precision_json = out / 'tables/precision_bounded_null_audit.json'
    write_precision_bounded_null_output(precision_result, precision_json)
    if precision_json.read_bytes() != (root / 'artifacts/prepublication_review/precision_bounded_null_audit.json').read_bytes():
        raise RuntimeError('generated precision-bounded-null audit differs from committed review artifact')
    shutil.copy2(
        root / 'artifacts/precision_bounded_null/source_counts.json',
        out / 'provenance/precision_bounded_null_source_counts.json',
    )
    shutil.copy2(
        root / 'docs/PREPUBLICATION_REVIEW_AUDIT.md',
        out / 'provenance/PREPUBLICATION_REVIEW_AUDIT.md',
    )

    _figure1(out / 'figures/figure1_eco_genetic_closure.svg')
    _regenerate_publication_figures(stage1, stage2, audit_path, out)
    _copy_h3_gradient(h3_gradient, out)

    manuscript_files = (
        'warning_validity.md', 'state_validity_and_empirical_measurement_gates.md',
        'PUBLICATION_LANES.md', 'publication_lanes.json',
        'main_text.md', 'references.md', 'figure_captions.md', 'figure_accessibility_review.md',
        'table_captions.md', 'supplementary_methods.md', 'submission_metadata.md',
        'claim_evidence_map.md', 'artifact_index.md', 'submission_checklist.md',
        'main_story_revision.md', 'empirical_eschscholzia_f_typo_sensitivity_preregistration.md',
        'empirical_eschscholzia_f_typo_sensitivity_stop.md',
    )
    for name in manuscript_files:
        shutil.copy2(root / 'manuscript' / name, out / 'manuscript')
    shutil.copy2(
        root / 'artifacts/empirical/eschscholzia_f_typo_sensitivity_stop.json',
        out / 'provenance/eschscholzia_f_typo_sensitivity_stop.json',
    )

    manifest = {'files': {}}
    for file in sorted(p for p in out.rglob('*') if p.is_file()):
        manifest['files'][str(file.relative_to(out))] = hashlib.sha256(file.read_bytes()).hexdigest()
    (out / 'manifest.json').write_text(json.dumps(manifest, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
