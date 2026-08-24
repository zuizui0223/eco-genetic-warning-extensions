from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREREG = (ROOT / 'manuscript' / 'empirical_e3_norway_preregistration.md').read_text(encoding='utf-8')
FETCH = (ROOT / 'scripts' / 'fetch_e3_norway_dryad.py').read_text(encoding='utf-8')
WORKFLOW = (ROOT / '.github' / 'workflows' / 'e3-norway-dryad-discovery.yml').read_text(encoding='utf-8')


def test_source_is_locked_before_schema_inspection() -> None:
    for text in (PREREG, FETCH, WORKFLOW):
        assert '10.5061/dryad.d51c59zzj' in text
    assert 'before inspecting the downloaded Dryad workbook' in PREREG


def test_four_species_and_fragment_holdout_are_fixed() -> None:
    assert 'All four focal plant species' in PREREG
    assert 'leave-one-fragment-out' in PREREG
    assert 'Random row splits are prohibited' in PREREG


def test_process_state_precedes_landscape_context() -> None:
    assert 'E3-S1 — proximal process state' in PREREG
    assert 'E3-S2 — residual landscape-context model' in PREREG
    for phrase in ('patch size', 'patch isolation', 'patch complexity', 'percentage forest'):
        assert phrase in PREREG


def test_falsification_outcomes_are_all_allowed() -> None:
    for label in (
        'residual_context_detected',
        'no_detected_residual_context',
        'mixed_predictive_evidence',
        'not_identifiable_for_species',
    ):
        assert label in PREREG
    assert 'alpha = 0.0125' in PREREG


def test_raw_third_party_data_are_not_committed_by_workflow() -> None:
    assert '_external/e3_norway_dryad' in WORKFLOW
    assert 'upload-artifact' in WORKFLOW
    assert 'public_dryad_archive_discovered' in WORKFLOW
