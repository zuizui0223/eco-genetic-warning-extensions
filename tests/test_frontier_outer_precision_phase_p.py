from eco_genetic_warning_extensions.frontier_outer_precision_phase_p import (
    PHASE_P_MIN_BASELINE_ELIGIBLE_PER_SEED, PHASE_P_REPLICATES_PER_SEED,
    expected_prefix, phase_p_manifest,
)
from eco_genetic_warning_extensions.frontier_refinement_manifest import PHASE_C_MASTER_SEEDS, PHASE_C_P_STAR


def test_phase_p_reuses_locked_phase_c_design():
    m=phase_p_manifest(); assert tuple(m['master_seeds'])==PHASE_C_MASTER_SEEDS; assert tuple(m['p_star_values'])==PHASE_C_P_STAR
    assert PHASE_P_REPLICATES_PER_SEED==100; assert PHASE_P_MIN_BASELINE_ELIGIBLE_PER_SEED==70
    assert 'no replacement seeds' in m['seed_selection']; assert m['source_reconstruction'].startswith('independent for each p_star')


def test_phase_p_prefix_counts_lock_phase_c():
    assert expected_prefix(20290320,.35)==(19,11); assert expected_prefix(20290320,.40)==(20,6)
    assert expected_prefix(20290321,.40)==(15,6); assert expected_prefix(20290324,.35)==(19,7); assert expected_prefix(20290324,.40)==(19,5)


def test_phase_p_preserves_gate_and_scope():
    m=phase_p_manifest(); assert m['historical_r4_rule_unchanged']=='all five observed block loss rates inside [0.30,0.70]'
    assert m['prepared_source_attempts']==1000; assert m['blinding_scope']=='source_and_trait_loss_only'
    assert 'no replacement seeds' in m['stop_rule']; assert 'new p_star values' in m['stop_rule']
