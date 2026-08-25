from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = (ROOT / 'manuscript' / 'empirical_campanula_colonization_visitation_test_preregistration.md').read_text(encoding='utf-8')
SCRIPT = (ROOT / 'scripts' / 'run_campanula_colonization_visitation_state_test.py').read_text(encoding='utf-8')
WORKFLOW = (ROOT / '.github' / 'workflows' / 'campanula-colonization-visitation-state.yml').read_text(encoding='utf-8')


def test_second_preregistration_precedes_row_analysis() -> None:
    assert 'second exact-model preregistration' in DOC
    assert 'No row-level seed number or realised visitation value' in DOC
    assert '16eced5334c10d9b7745b45424d0eed705c29346' not in DOC  # provenance is supplied by git history, not self-referential text


def test_source_and_primary_measurement_are_locked() -> None:
    assert '10.5281/zenodo.10814705' in DOC
    assert 'b84fa5c83513dbe75c0bf7840d1c74aa' in DOC and 'b84fa5c83513dbe75c0bf7840d1c74aa' in SCRIPT
    assert '81e0deaa78a6a97e1211484cb9d0d3b3' in DOC and '81e0deaa78a6a97e1211484cb9d0d3b3' in SCRIPT
    assert 'visits.per.flower' in DOC and 'visits.per.flower' in SCRIPT
    assert 'total.poll.visits' in DOC
    assert 'not opened as alternatives' in DOC


def test_primary_pollen_limitation_endpoint_is_fixed() -> None:
    assert 'PL_{abs}' in DOC
    assert 'supplemented' in DOC and 'control' in DOC
    assert 'No ratio or relative transformation' in DOC
    assert 'PL_abs' in SCRIPT
    assert 'F_control' in SCRIPT


def test_whole_population_validation_and_state_sequence_are_fixed() -> None:
    assert 'leave-one-experimental-population-out (LOPO)' in DOC
    assert 'Row-wise or individual-wise cross-validation is prohibited' in DOC
    for state in ('### S0', '### S1', '### S2', '### S3'):
        assert state in DOC
    assert 'held_out_unit\": \"experimental.population' in SCRIPT


def test_model_and_uncertainty_are_fixed() -> None:
    assert 'Ridge(alpha=1.0)' in DOC and 'Ridge(alpha=1.0)' in SCRIPT
    assert '10,000' in DOC
    assert '20260825' in DOC
    assert 'N_BOOT = 10_000' in SCRIPT
    assert 'RNG_SEED = 20260825' in SCRIPT
    assert 'OneHotEncoder(handle_unknown="ignore"' in SCRIPT


def test_decision_set_and_stop_rule_are_fixed() -> None:
    for token in (
        'realised_visitation_informative_context_redundant',
        'residual_colonization_size_after_visitation',
        'residual_compensation_after_context',
        'realised_visitation_not_predictively_supported',
        'not_identifiable_for_primary_endpoint',
    ):
        assert token in DOC and token in SCRIPT
    assert 'Do not switch to `total.poll.visits`' in DOC
    assert 'No category spelling is repaired after outcome inspection' in DOC


def test_workflow_uploads_only_derived_result() -> None:
    assert 'Run preregistered realised-visitation analysis' in WORKFLOW
    assert 'Upload derived result only' in WORKFLOW
    assert 'campanula_colonization_visitation_result.json' in WORKFLOW
