"""Per-seed runner and aggregator for high-precision Phase-P outer-frontier validation."""
from __future__ import annotations

import importlib
import json
from dataclasses import replace
from pathlib import Path
from typing import Any, Iterable

from .frontier_outer_precision_phase_p import (
    PHASE_P_MIN_BASELINE_ELIGIBLE_PER_SEED,
    PHASE_P_PREFIX_REPLICATES,
    PHASE_P_REPLICATES_PER_SEED,
    expected_prefix,
    phase_p_manifest,
)
from .frontier_refinement_manifest import PHASE_C_MASTER_SEEDS, phase_c_cells
from .protocol002_condition_map import classify_seed_rates
from .protocol002_source_grid import SOURCE_HOLD_GENERATIONS, SOURCE_NESTED_BARRIER_GRIDS, SOURCE_STAGE_GENERATIONS
from .protocol002_stage1_projection_pilot import UPSTREAM_CHAIN_RUNTIME_MODULE
from .protocol002_stage2_smoke import UPSTREAM_CALIBRATION_MODULE, UPSTREAM_DYNAMICS_MODULE
from .protocol002_upstream_h1_asym_smoke import (
    UPSTREAM_EXPERIMENT_MODULE, UPSTREAM_H1_MODULE, UPSTREAM_MUTATION_MODULE,
    _upstream_import_path, patched_protocol002_mutation_runner,
)
from .r4_gate_validity_phase_j import ensemble_gate_pass_probability, pearson_equal_rate_test


def _regime(rates:tuple[float,...])->str:
    return {"warning_evaluable":"R4_highrep","rapid_loss":"R2_highrep","persistence":"R1_highrep","seed_heterogeneous":"R3_highrep"}[classify_seed_rates(rates)]


def run_phase_p_seed(upstream_checkout:str|Path,master_seed:int)->dict[str,Any]:
    if master_seed not in PHASE_C_MASTER_SEEDS: raise ValueError("not a locked Phase-C seed")
    checkout=Path(upstream_checkout)
    if not checkout.exists(): raise FileNotFoundError(checkout)
    attempts=[]
    with _upstream_import_path(checkout):
        audit=importlib.import_module(UPSTREAM_H1_MODULE); experiments=importlib.import_module(UPSTREAM_EXPERIMENT_MODULE)
        mutation=importlib.import_module(UPSTREAM_MUTATION_MODULE); runtime=importlib.import_module(UPSTREAM_CHAIN_RUNTIME_MODULE)
        calibration=importlib.import_module(UPSTREAM_CALIBRATION_MODULE); dynamics=importlib.import_module(UPSTREAM_DYNAMICS_MODULE); chain=runtime.chain
        for phase_cell in phase_c_cells():
            coordinate=phase_cell.coordinate; anchor=phase_cell.anchor; driver_rate=coordinate.kappa_mu/2.0
            schedule=calibration.RampHoldSchedule(phase_cell.ramp_generations,phase_cell.hold_generations,anchor.normalised_barrier_increase)
            spec=replace(experiments.standard_profile(),experiment_id=f"frontier_outer_precision_phase_p_{phase_cell.cell_index:02d}",generations=1,replicates=PHASE_P_REPLICATES_PER_SEED,master_seed=master_seed,area_reference_values=(anchor.area_reference,),interaction_feedback_values=(anchor.interaction_kappa,),interaction_barrier_values=(0.5,))
            with patched_protocol002_mutation_runner(mutation,coordinate):
                cells=audit.run_finite_h1_boundary_resolution_audit(spec,endpoint_padding_fraction=0.5,stage_generations=SOURCE_STAGE_GENERATIONS,nested_barrier_points=SOURCE_NESTED_BARRIER_GRIDS,interaction_separation_threshold=0.05,maximum_normalized_bracket_width=0.03)
                if len(cells)!=1: raise RuntimeError("Phase P requires exactly one H1 cell per p_star and seed")
                cell=cells[0]; isolated=chain._scenario_map(spec)[experiments.SCENARIO_EQUAL_ISOLATED]
                for record in cell.replicates:
                    base={"master_seed":master_seed,"replicate":record.replicate_index,"p_star":float(coordinate.p_star),"calibration_seed":record.seed}
                    prepared=chain._prepare_mutation_high_state(driver_rate,spec,cell,record,endpoint_padding_fraction=0.5,stage_generations=SOURCE_STAGE_GENERATIONS,hold_generations=SOURCE_HOLD_GENERATIONS,interaction_separation_threshold=0.05)
                    if prepared is None:
                        attempts.append({**base,"source_prepared":False,"projection_supported":None,"eligible_for_trait_loss_denominator":False,"trait_loss_observed_post_baseline":None}); continue
                    source,anchor_barrier=prepared; interval=cell.canonical_bistable_barrier_interval
                    if interval is None or interval[1]<=interval[0]: raise RuntimeError("positive canonical interval required")
                    template=chain.parameters_for_cell(spec,isolated,replace(cell.parameters,interaction_barrier=anchor_barrier),seed=record.seed); projected,invariants=chain.project_full_state(source,template)
                    if not invariants.projection_supported:
                        attempts.append({**base,"source_prepared":True,"projection_supported":False,"eligible_for_trait_loss_denominator":False,"trait_loss_observed_post_baseline":None}); continue
                    barriers=calibration.ramp_and_hold_barrier_schedule(anchor_barrier=anchor_barrier,canonical_interval_width=interval[1]-interval[0],schedule=schedule)
                    result=mutation.simulate_with_symmetric_allele_mutation(replace(projected,generations=schedule.total_generations,random_seed=record.seed),mutation_rate=driver_rate,interaction_barrier_schedule=barriers)
                    baseline=any(item.realised_high_trait_occupied for item in result.snapshots[0].trait_occupancy); raw=dynamics.tau_trait_realised(result); loss_time=None if raw is None or raw==0 else raw
                    attempts.append({**base,"source_prepared":True,"projection_supported":True,"eligible_for_trait_loss_denominator":bool(baseline),"trait_loss_observed_post_baseline":None if not baseline else loss_time is not None})
    summaries=[]; prefix_ok=True
    for phase_cell in phase_c_cells():
        p=float(phase_cell.coordinate.p_star); rows=[r for r in attempts if r["p_star"]==p]; prefix=[r for r in rows if r["replicate"]<PHASE_P_PREFIX_REPLICATES]; pe=[r for r in prefix if r["eligible_for_trait_loss_denominator"]]; pl=[r for r in pe if r["trait_loss_observed_post_baseline"] is True]; ee,el=expected_prefix(master_seed,p); ok=len(pe)==ee and len(pl)==el; prefix_ok &= ok; eligible=[r for r in rows if r["eligible_for_trait_loss_denominator"]]; losses=[r for r in eligible if r["trait_loss_observed_post_baseline"] is True]
        summaries.append({"p_star":p,"baseline_eligible":len(eligible),"trait_loss":len(losses),"trait_loss_rate":None if not eligible else len(losses)/len(eligible),"precision_sufficient":len(eligible)>=PHASE_P_MIN_BASELINE_ELIGIBLE_PER_SEED,"prefix":{"observed_eligible":len(pe),"observed_losses":len(pl),"expected_eligible":ee,"expected_losses":el,"matches_historical":ok}})
    return {"stage":"outer frontier precision validation Phase P","master_seed":master_seed,"prefix_audit_passed":prefix_ok,"condition_summaries":summaries}


def aggregate_phase_p(payloads:Iterable[dict[str,Any]])->dict[str,Any]:
    payloads=tuple(payloads)
    if sorted(p["master_seed"] for p in payloads)!=sorted(PHASE_C_MASTER_SEEDS): raise RuntimeError("requires five locked Phase-C seeds")
    prefix_ok=all(p["prefix_audit_passed"] for p in payloads); summaries=[]; regimes={}
    for phase_cell in phase_c_cells():
        p=float(phase_cell.coordinate.p_star); blocks=[]
        for payload in sorted(payloads,key=lambda x:x["master_seed"]):
            row=next(r for r in payload["condition_summaries"] if r["p_star"]==p); blocks.append((int(row["trait_loss"]),int(row["baseline_eligible"])))
        sufficient=all(n>=PHASE_P_MIN_BASELINE_ELIGIBLE_PER_SEED for _,n in blocks); rates=tuple(k/n for k,n in blocks); regime="insufficient_precision" if not sufficient else _regime(rates); pooled=sum(k for k,_ in blocks)/sum(n for _,n in blocks); stat,df,eqp=pearson_equal_rate_test(tuple(blocks)); ref=ensemble_gate_pass_probability(tuple(n for _,n in blocks),pooled); regimes[f"{p:.2f}"]=regime
        summaries.append({"p_star":p,"blocks":[{"master_seed":s,"losses":k,"eligible":n,"rate":k/n} for s,(k,n) in zip(PHASE_C_MASTER_SEEDS,blocks,strict=True)],"pooled_loss_rate":pooled,"historical_gate_regime_at_full_precision":regime,"pearson_equal_rate_p_value":eqp,"homogeneous_reference_gate_fail_probability":1-ref})
    if not prefix_ok: decision="prefix_reproducibility_failed"
    elif any(v=="insufficient_precision" for v in regimes.values()): decision="insufficient_precision"
    elif regimes["0.35"]!="R4_highrep": decision="anchor_r4_not_reproduced"
    elif regimes["0.40"]=="R4_highrep": decision="historical_p040_r3_disappears_at_high_precision"
    else: decision="p040_remains_outside_r4_at_high_precision"
    return {"stage":"outer frontier precision validation Phase P","manifest":phase_p_manifest(),"prefix_audit_passed":prefix_ok,"decision":decision,"regime_by_p_star":regimes,"p_star_summaries":summaries,"per_seed_payloads":list(payloads)}


def load_and_aggregate_phase_p(paths:Iterable[str|Path])->dict[str,Any]:
    return aggregate_phase_p([json.loads(Path(p).read_text()) for p in paths])
