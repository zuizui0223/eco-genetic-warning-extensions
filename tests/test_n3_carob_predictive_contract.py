import json
from pathlib import Path


def test_n3_carob_predictive_contract_is_frozen_before_fit():
    contract = json.loads(Path('configs/n3_carob_predictive_contract.json').read_text())
    assert contract['data']['doi'] == '10.5281/zenodo.13939480'
    assert contract['data']['expected_md5'] == '9cf7668ae8d825c72edda3346ebf36a6'
    assert contract['unit']['holdout_unit'] == 'StudyOrchard'
    assert contract['endpoint'] == 'fruit_count'
    assert contract['model_family'] == 'NB2_log'
    assert contract['validation']['method'] == 'leave_one_orchard_out'
    assert contract['validation']['bootstrap_seed'] == 20260827
    assert contract['validation']['bootstrap_n'] == 10000
    assert contract['B1']['require_both_interaction_representations'] is True
    assert contract['B2']['opens_only_if_B1_both_pass'] is True
    assert contract['B2']['require_representation_agreement_for_claim'] is True
    forbidden = ' '.join(contract['forbidden_repairs']).lower()
    assert 'alternate endpoint' in forbidden
    assert 'favorable polinabun' in forbidden


def test_carob_preregistration_states_representation_gate_and_claim_ceiling():
    text = Path('manuscript/N3_CAROB_PREDICTIVE_PREREGISTRATION.md').read_text()
    required = [
        'I_embedded',
        'I_joined',
        'process_representation_sensitive',
        'B2 may open only if **both**',
        'Seed production and seed weight are **not** fallback endpoints',
        'leave-one-orchard-out',
        'context_predictively_redundant_given_partial_process_state',
        'one island system and one urban system',
    ]
    for phrase in required:
        assert phrase in text
