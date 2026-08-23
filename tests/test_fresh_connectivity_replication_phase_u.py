from eco_genetic_warning_extensions.fresh_connectivity_replication_phase_u import (
    PHASE_U_ALPHA,
    PHASE_U_MASTER_SEEDS,
    PHASE_U_MIGRATION_RATES,
    PHASE_U_MIN_BASELINE_ELIGIBLE_PER_SEED,
    PHASE_U_REPLICATES_PER_SEED,
    phase_u_manifest,
)


def test_phase_u_is_one_fresh_fixed_replication() -> None:
    assert PHASE_U_MASTER_SEEDS == (20291010, 20291011, 20291012, 20291013, 20291014)
    assert len(set(PHASE_U_MASTER_SEEDS)) == 5
    assert PHASE_U_REPLICATES_PER_SEED == 100
    assert PHASE_U_MIN_BASELINE_ELIGIBLE_PER_SEED == 70
    assert PHASE_U_MIGRATION_RATES == (0.0, 0.10)
    assert PHASE_U_ALPHA == 0.05


def test_manifest_does_not_condition_opening_on_favourable_regime() -> None:
    manifest = phase_u_manifest()
    opening = manifest["opening_rule"]
    assert "Neither condition is required to pass the historical R4 screen" in opening
    assert manifest["primary_estimand"].endswith("allele-only m=0.10")
    assert manifest["negative_control_estimand"].endswith("m=0")


def test_replication_decision_is_predeclared() -> None:
    decision = phase_u_manifest()["decision_rule"]
    assert decision["specific_m010_heterogeneity_replicated"] == "m=0.10 equal-rate p<0.05 AND m=0 equal-rate p>=0.05"
    assert decision["fresh_ensemble_heterogeneity_not_specific_to_m010"] == "m=0.10 equal-rate p<0.05 AND m=0 equal-rate p<0.05"
    assert decision["historical_m010_heterogeneity_not_freshly_replicated"] == "m=0.10 equal-rate p>=0.05"


def test_stop_rule_forbids_run_until_significant() -> None:
    stop = phase_u_manifest()["stop_rule"]
    for phrase in ("Do not replace seeds", "add migration levels", "rerun fresh ensembles", "change alpha", "increase precision"):
        assert phrase in stop
