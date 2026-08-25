from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = (ROOT / 'manuscript' / 'empirical_campanula_colonization_visitation_preregistration.md').read_text(encoding='utf-8')
SCRIPT = (ROOT / 'scripts' / 'fetch_campanula_colonization_visitation_schema.py').read_text(encoding='utf-8')
WORKFLOW = (ROOT / '.github' / 'workflows' / 'campanula-colonization-visitation-discovery.yml').read_text(encoding='utf-8')


def test_zenodo_files_and_hashes_are_locked() -> None:
    assert '10.5281/zenodo.10814705' in DOC
    for name, md5 in (
        ('PLdataindividual.csv', 'b84fa5c83513dbe75c0bf7840d1c74aa'),
        ('pollinator.csv', '81e0deaa78a6a97e1211484cb9d0d3b3'),
    ):
        assert name in DOC and name in SCRIPT
        assert md5 in DOC and md5 in SCRIPT


def test_schema_only_boundary_precedes_outcomes() -> None:
    assert 'Schema-only boundary' in DOC
    assert 'must not read data rows' in DOC
    assert 'No data row' in SCRIPT
    assert 'Upload schema manifest only' in WORKFLOW


def test_realised_visitation_and_context_roles_are_fixed() -> None:
    assert 'visits.per.flower' in DOC
    assert 'I_realised' in DOC
    assert '`autonomy`' in DOC
    assert '`R` candidate' in DOC
    assert 'site -> experimental population -> individual -> treatment' in DOC


def test_identifiability_outcomes_are_fixed() -> None:
    for token in (
        'realised_visitation_function_state_identifiable',
        'partial_realised_visitation_function_state_identifiable',
        'not_identifiable_from_archive',
    ):
        assert token in DOC
    assert 'second preregistration' in DOC
    assert 'whole experimental populations as the held-out unit' in DOC


def test_claim_ceiling_preserves_effective_service_boundary() -> None:
    assert 'does not measure stigma pollen receipt or donor identity' in DOC
    assert 'would not prove a universally sufficient interaction state' in DOC
