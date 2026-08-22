from eco_genetic_warning_extensions.partner_precision_phase_n import (
    PHASE_N_MIN_BASELINE_ELIGIBLE_PER_SEED, PHASE_N_REPLICATES_PER_SEED,
    expected_prefix, phase_n_manifest,
)
from eco_genetic_warning_extensions.partner_redundancy_phase_g import PHASE_G_MASTER_SEEDS


def test_phase_n_uses_all_locked_phase_g_seeds_and_architectures():
    m=phase_n_manifest(); assert tuple(m['master_seeds'])==PHASE_G_MASTER_SEEDS
    assert m['architectures']==['intact_control','even_redundant','graded_contributions','dominant_partner']
    assert PHASE_N_REPLICATES_PER_SEED==100; assert PHASE_N_MIN_BASELINE_ELIGIBLE_PER_SEED==70


def test_phase_n_prefix_counts_lock_phase_g():
    assert expected_prefix(20290610,'intact_control')==(18,9)
    assert expected_prefix(20290612,'dominant_partner')==(18,12)
    assert expected_prefix(20290613,'even_redundant')==(20,13)
    assert expected_prefix(20290614,'graded_contributions')==(17,13)


def test_phase_n_preserves_gate_and_pairing():
    m=phase_n_manifest(); assert m['historical_r4_rule_unchanged']=='all five observed block loss rates inside [0.30,0.70]'
    assert m['paired_across_architectures'] is True; assert m['prepared_source_count']==500; assert m['trajectory_count']==2000
    assert 'no replacement seeds' in m['seed_selection']; assert 'no replacement seeds' in m['stop_rule']
