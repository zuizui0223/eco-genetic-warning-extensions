"""Cross-campaign validity audit for load-bearing historical R3 classifications.

Phase K established that one headline R3 classification disappeared when the
same master-seed family was measured with much greater within-block precision.
Phase L applies the Phase-J finite-sample diagnostic to every historical R3
classification that currently carries manuscript-level mechanistic weight.

Historical labels remain immutable.  The audit asks only whether an observed R3
label identifies excess between-block heterogeneity beyond a homogeneous
finite-sample reference.
"""
from __future__ import annotations

from dataclasses import dataclass

from .r4_gate_validity_phase_j import audit_observed_blocks


@dataclass(frozen=True)
class HistoricalGateCase:
    case_id: str
    campaign: str
    condition: str
    blocks: tuple[tuple[int, int], ...]
    historical_regime: str
    load_bearing_claim: str


CASES = (
    HistoricalGateCase(
        "C_pstar_040", "Phase C", "p_star=0.40",
        ((6,20),(6,15),(7,18),(4,20),(5,19)), "R3_highrep",
        "p_star=0.40 is outside the recovered warning-evaluable event regime",
    ),
    HistoricalGateCase(
        "D_pstar_0325", "Phase D", "p_star=0.325",
        ((9,17),(10,19),(16,20),(12,18),(14,18)), "R3_highrep",
        "the lower immediate neighbour establishes a narrow R4 frontier",
    ),
    HistoricalGateCase(
        "D_pstar_0375", "Phase D", "p_star=0.375",
        ((7,17),(7,18),(9,17),(7,18),(4,17)), "R3_highrep",
        "the upper immediate neighbour establishes a narrow R4 frontier",
    ),
    HistoricalGateCase(
        "E_m010", "Phase E", "migration_rate=0.10",
        ((10,15),(13,18),(12,20),(10,18),(12,20)), "R3_highrep",
        "allele-frequency connectivity moves the R4 anchor to R3",
    ),
    HistoricalGateCase(
        "E_m020", "Phase E", "migration_rate=0.20",
        ((9,15),(13,18),(9,20),(12,18),(12,20)), "R3_highrep",
        "allele-frequency connectivity moves the R4 anchor to R3",
    ),
    HistoricalGateCase(
        "G_even", "Phase G", "even one-partner loss",
        ((10,18),(8,17),(8,18),(13,20),(12,17)), "R3_highrep",
        "matched partner loss changes event-regime reproducibility",
    ),
    HistoricalGateCase(
        "G_graded", "Phase G", "graded one-partner loss",
        ((9,18),(7,17),(10,18),(11,20),(13,17)), "R3_highrep",
        "matched partner loss changes event-regime reproducibility",
    ),
    HistoricalGateCase(
        "G_dominant", "Phase G", "dominant one-partner loss",
        ((9,18),(8,17),(12,18),(11,20),(12,17)), "R3_highrep",
        "matched partner loss changes event-regime reproducibility",
    ),
    HistoricalGateCase(
        "H_no_rewiring", "Phase H", "partner loss / no rewiring",
        ((9,18),(8,17),(9,17),(6,17),(5,17)), "R3_highrep",
        "partner loss breaks R4 under explicit-network closure",
    ),
    HistoricalGateCase(
        "H_rewiring", "Phase H", "trait-capacity rewiring",
        ((9,18),(8,17),(8,17),(6,17),(5,17)), "R3_highrep",
        "the fixed rewiring rule fails to restore R4",
    ),
)

# Historical R4 controls from the same campaigns, retained as calibration context.
CONTROLS = (
    HistoricalGateCase(
        "C_pstar_035", "Phase C", "p_star=0.35",
        ((11,19),(9,17),(9,19),(10,17),(7,19)), "R4_highrep",
        "historical R4 anchor",
    ),
    HistoricalGateCase(
        "D_pstar_035", "Phase D", "p_star=0.35",
        ((8,16),(12,18),(11,17),(10,17),(12,19)), "R4_highrep",
        "historical independent R4 replay",
    ),
    HistoricalGateCase(
        "E_m000", "Phase E", "migration_rate=0",
        ((7,15),(11,18),(11,20),(12,18),(11,20)), "R4_highrep",
        "historical migration anchor",
    ),
    HistoricalGateCase(
        "G_intact", "Phase G", "intact control",
        ((9,18),(8,17),(10,18),(12,20),(10,17)), "R4_highrep",
        "historical partner-loss intact control",
    ),
)


def _audit_case(case: HistoricalGateCase) -> dict[str, object]:
    result = audit_observed_blocks(case.case_id, case.blocks, case.historical_regime).as_dict()
    p_value = float(result["pearson_equal_rate_p_value"])
    gate_fail = float(result["homogeneous_reference_gate_fail_probability"])
    if case.historical_regime == "R3_highrep" and p_value > 0.05:
        inferential_status = "r3_does_not_identify_excess_block_heterogeneity"
    elif case.historical_regime == "R3_highrep":
        inferential_status = "excess_block_heterogeneity_candidate"
    else:
        inferential_status = "historical_r4_control"
    return {
        **result,
        "campaign": case.campaign,
        "condition": case.condition,
        "load_bearing_claim": case.load_bearing_claim,
        "inferential_status": inferential_status,
        "sampling_reference_gate_failure_substantial": gate_fail >= 0.10,
    }


def phase_l_audit() -> dict[str, object]:
    cases = [_audit_case(case) for case in CASES]
    controls = [_audit_case(case) for case in CONTROLS]
    r3_cases = [row for row in cases if row["historical_regime"] == "R3_highrep"]
    excess = [row for row in r3_cases if row["inferential_status"] == "excess_block_heterogeneity_candidate"]
    return {
        "stage": "headline R3 validity audit Phase L",
        "scope": "cross_campaign_historical_gate_diagnostic_not_reclassification",
        "case_count": len(cases),
        "control_count": len(controls),
        "headline_r3_cases": cases,
        "historical_r4_controls": controls,
        "r3_cases_with_detectable_excess_block_heterogeneity": len(excess),
        "all_headline_r3_cases_require_mechanistic_reaudit": len(excess) != len(r3_cases),
        "primary_conclusion_rule": (
            "A small-block R3 label is not evidence of biological reproducibility loss when observed block rates are compatible with "
            "a common latent rate and the hard all-five-block gate has substantial finite-sample failure probability. Historical labels "
            "remain unchanged; load-bearing mechanistic claims require precision validation."
        ),
        "required_follow_up": {
            "Phase C/D": "precision-validate the claimed narrow p_star frontier before calling neighbouring R3 labels a biological boundary",
            "Phase E": "precision-validate migration levels before claiming connectivity changes loss-regime reproducibility",
            "Phase G": "precision-validate partner-loss architectures before claiming partner loss changes reproducibility",
            "Phase H": "no-rewiring R3 is already refuted by Phase K high precision; rewiring R3 cannot support non-rescue by gate label alone",
        },
        "stop_rule": (
            "Do not modify historical R3/R4 labels or the 0.30-0.70 band. Do not retain a mechanistic claim merely because an old R3 "
            "label crossed the hard gate. Validate the relevant biological contrast at greater within-block precision."
        ),
    }
