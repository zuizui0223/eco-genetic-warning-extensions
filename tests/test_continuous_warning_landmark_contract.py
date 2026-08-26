from eco_genetic_warning_extensions.continuous_warning_landmark import (
    BOOTSTRAP_BASE_SEED,
    DIVERSITY_COORDINATES,
    concordance_auc,
    landmark_cell,
)


def _trajectory(loss_time, alpha, gamma=None):
    return {
        "trait_loss_time": loss_time,
        "series": {
            "H_alpha": alpha,
            "H_gamma": alpha if gamma is None else gamma,
        },
    }


def test_continuous_score_family_is_fixed_to_two_levels() -> None:
    assert DIVERSITY_COORDINATES == ("H_alpha", "H_gamma")
    assert BOOTSTRAP_BASE_SEED == 20_260_826


def test_concordance_auc_uses_half_credit_for_ties() -> None:
    assert concordance_auc([0.8, 0.4], [0.4, 0.2]) == 0.875


def test_landmark_excludes_prior_losses_and_uses_future_cases() -> None:
    flat = [1.0] * 121
    high = [1.0] * 121
    high[30] = 0.5
    low = [1.0] * 121
    low[30] = 0.9
    result = landmark_cell(
        [
            _trajectory(20, flat),
            _trajectory(50, high),
            _trajectory(None, low),
        ],
        "H_alpha",
        30,
        bootstrap_seed=123,
        bootstrap_replicates=20,
    )
    assert result["excluded_losses_at_or_before_landmark"] == 1
    assert result["risk_set"] == 2
    assert result["future_cases"] == 1
    assert result["dynamic_controls"] == 1
    assert result["auc"] == 1.0


def test_protocol_rejects_rate_or_selected_landmark_language() -> None:
    from pathlib import Path

    root = Path(__file__).resolve().parents[1]
    protocol = (
        root / "manuscript/warning_continuous_landmark_exploratory_preregistration.md"
    ).read_text(encoding="utf-8")
    assert "No absolute level, slope, windowed decline" in protocol
    assert "generations `30`, `60` and `90`" in protocol
    assert "not independent replicates" in protocol
