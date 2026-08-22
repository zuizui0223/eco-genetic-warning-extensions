from eco_genetic_warning_extensions.interaction_support_precision_phase_q import PHASE_Q_MIN_BASELINE_ELIGIBLE_PER_SEED,PHASE_Q_REPLICATES_PER_SEED,expected_prefix,phase_q_manifest
from eco_genetic_warning_extensions.interaction_support_phase_f import PHASE_F_INTERACTION_KAPPAS,PHASE_F_MASTER_SEEDS

def test_phase_q_reuses_locked_phase_f_design():
    m=phase_q_manifest();assert tuple(m['master_seeds'])==PHASE_F_MASTER_SEEDS;assert tuple(m['interaction_kappas'])==PHASE_F_INTERACTION_KAPPAS;assert PHASE_Q_REPLICATES_PER_SEED==100;assert PHASE_Q_MIN_BASELINE_ELIGIBLE_PER_SEED==70;assert 'no replacement seeds' in m['seed_selection']

def test_phase_q_prefix_counts_lock_phase_f():
    assert expected_prefix(20290510,3.0)==(14,9);assert expected_prefix(20290510,4.5)==(19,13);assert expected_prefix(20290511,6.0)==(16,11);assert expected_prefix(20290512,3.0)==(12,4);assert expected_prefix(20290514,6.0)==(18,10)

def test_phase_q_preserves_gate_and_scope():
    m=phase_q_manifest();assert m['historical_r4_rule_unchanged']=='all five observed block loss rates inside [0.30,0.70]';assert m['blinding_scope']=='source_and_trait_loss_only';assert 'no replacement seeds' in m['stop_rule']
