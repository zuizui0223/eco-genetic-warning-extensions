from eco_genetic_warning_extensions.frontier_precision_phase_o import (
    PHASE_O_MIN_BASELINE_ELIGIBLE_PER_SEED, PHASE_O_REPLICATES_PER_SEED,
    expected_prefix, phase_o_manifest,
)
from eco_genetic_warning_extensions.frontier_refinement_manifest import PHASE_D_MASTER_SEEDS, PHASE_D_P_STAR


def test_phase_o_reuses_locked_phase_d_design():
    m=phase_o_manifest(); assert tuple(m['master_seeds'])==PHASE_D_MASTER_SEEDS; assert tuple(m['p_star_values'])==PHASE_D_P_STAR
    assert PHASE_O_REPLICATES_PER_SEED==100; assert PHASE_O_MIN_BASELINE_ELIGIBLE_PER_SEED==70
    assert m['seed_selection'].startswith('all five locked Phase-D'); assert m['source_reconstruction'].startswith('independent for each p_star')


def test_phase_o_prefix_counts_lock_phase_d():
    assert expected_prefix(20290310,.325)==(17,9); assert expected_prefix(20290310,.350)==(16,8); assert expected_prefix(20290310,.375)==(17,7)
    assert expected_prefix(20290312,.325)==(20,16); assert expected_prefix(20290314,.375)==(17,4)


def test_phase_o_preserves_gate_and_no_refinement():
    m=phase_o_manifest(); assert m['historical_r4_rule_unchanged']=='all five observed block loss rates inside [0.30,0.70]'
    assert m['prepared_source_attempts']==1500; assert 'no replacement seeds' in m['stop_rule']; assert 'p_star refinement' in m['stop_rule']
    assert m['blinding_scope']=='source_and_trait_loss_only'
