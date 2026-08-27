from pathlib import Path


def test_carob_predictive_implementation_matches_frozen_contract_surface():
    text = Path('scripts/run_n3_carob_predictive.py').read_text()
    required = [
        'NegativeBinomial',
        'BOOTSTRAP_SEED = 20260827',
        'BOOTSTRAP_N = 10000',
        '"embedded": "I_embedded"',
        '"joined": "I_joined"',
        'restricted_kind="baseline"',
        'full_kind="process"',
        'restricted_kind="process"',
        'full_kind="context"',
        'process_adequacy_supported_across_representations',
        'context_predictively_redundant_given_partial_process_state',
        'residual_context_representation_sensitive',
        'fruit_count=("TotalFruits", "sum")',
        'flower_exposure=("TotalFlowers", "sum")',
    ]
    for phrase in required:
        assert phrase in text
    forbidden = ['Poisson(', 'Gaussian', 'Seeds1000', 'SeedWeight']
    for phrase in forbidden:
        assert phrase not in text
