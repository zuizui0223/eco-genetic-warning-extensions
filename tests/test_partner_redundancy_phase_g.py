from types import SimpleNamespace

import pytest

from eco_genetic_warning_extensions.partner_redundancy_phase_g import (
    PHASE_G_MASTER_SEEDS,
    PHASE_G_REPLICATES_PER_SEED,
    lost_partner_index,
    mean_retained_support_per_seed,
    phase_g_conditions,
    phase_g_manifest,
    retained_support,
)
from eco_genetic_warning_extensions.partner_redundancy_phase_g_runner import patched_interaction_support_multiplier


def test_phase_g_manifest_is_balanced_and_warning_blind() -> None:
    manifest = phase_g_manifest()
    assert manifest["calibration_scope"] == "source_and_trait_loss_only"
    assert manifest["blinding_scope"] == "source_and_trait_loss_only"
    assert manifest["partner_count_before_loss"] == 4
    assert manifest["partner_count_after_loss"] == 3
    assert manifest["paired_across_partner_architectures"] is True
    assert manifest["prepared_source_count"] == len(PHASE_G_MASTER_SEEDS) * PHASE_G_REPLICATES_PER_SEED
    assert manifest["trajectory_count"] == 4 * len(PHASE_G_MASTER_SEEDS) * PHASE_G_REPLICATES_PER_SEED


def test_loss_architectures_match_mean_support_but_not_variance() -> None:
    conditions = phase_g_conditions()
    assert [condition.name for condition in conditions] == [
        "intact_control",
        "even_redundant",
        "graded_contributions",
        "dominant_partner",
    ]
    assert mean_retained_support_per_seed(conditions[0]) == pytest.approx(1.0)
    for condition in conditions[1:]:
        assert mean_retained_support_per_seed(condition) == pytest.approx(0.75)
    cvs = [condition.contribution_cv for condition in conditions[1:]]
    assert cvs[0] < cvs[1] < cvs[2]


def test_partner_loss_identity_is_exactly_balanced_per_seed_block() -> None:
    counts = {index: 0 for index in range(4)}
    for replicate in range(PHASE_G_REPLICATES_PER_SEED):
        counts[lost_partner_index(replicate)] += 1
    assert counts == {0: 5, 1: 5, 2: 5, 3: 5}


def test_dominant_architecture_retained_support_has_declared_levels() -> None:
    dominant = phase_g_conditions()[-1]
    values = [retained_support(dominant, replicate) for replicate in range(PHASE_G_REPLICATES_PER_SEED)]
    assert values.count(pytest.approx(0.3)) == 5
    assert values.count(pytest.approx(0.9)) == 15


def test_support_patch_is_scoped_and_restored() -> None:
    module = SimpleNamespace()
    module.interaction_support_signal = lambda q, trait, allele, parameters: q + trait + allele
    original = module.interaction_support_signal
    with patched_interaction_support_multiplier(module, 0.5):
        assert module.interaction_support_signal(0.2, 0.3, 0.1, None) == pytest.approx(0.3)
    assert module.interaction_support_signal is original
