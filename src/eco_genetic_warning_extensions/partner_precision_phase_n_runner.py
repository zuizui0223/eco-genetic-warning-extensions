"""Per-seed runner and aggregator for high-precision Phase-N partner validation."""
from __future__ import annotations

import importlib
import json
from dataclasses import replace
from math import comb
from pathlib import Path
from typing import Any, Iterable

from .partner_precision_phase_n import (
    PHASE_N_MIN_BASELINE_ELIGIBLE_PER_SEED,
    PHASE_N_PREFIX_REPLICATES,
    PHASE_N_REPLICATES_PER_SEED,
    expected_prefix,
    phase_n_manifest,
)
from .partner_redundancy_phase_g import (
    PHASE_G_AREA_REFERENCE, PHASE_G_BARRIER_INCREASE, PHASE_G_HOLD_GENERATIONS,
    PHASE_G_INTERACTION_KAPPA, PHASE_G_MASTER_SEEDS, PHASE_G_MIGRATION_RATE,
    PHASE_G_RAMP_GENERATIONS, lost_partner_index, phase_g_conditions,
    phase_g_coordinate, retained_support,
)
from .partner_redundancy_phase_g_runner import patched_interaction_support_multiplier
from .protocol002_condition_map import classify_seed_rates
from .protocol002_source_grid import SOURCE_HOLD_GENERATIONS, SOURCE_NESTED_BARRIER_GRIDS, SOURCE_STAGE_GENERATIONS
from .protocol002_stage1_projection_pilot import UPSTREAM_CHAIN_RUNTIME_MODULE
from .protocol002_stage2_smoke import UPSTREAM_CALIBRATION_MODULE, UPSTREAM_DYNAMICS_MODULE
from .protocol002_upstream_h1_asym_smoke import (
    UPSTREAM_EXPERIMENT_MODULE, UPSTREAM_H1_MODULE, UPSTREAM_MUTATION_MODULE,
    _upstream_import_path, patched_protocol002_mutation_runner,
)
from .r4_gate_validity_phase_j import ensemble_gate_pass_probability, pearson_equal_rate_test


def _mcnemar(a:int,b:int)->float:
    n=a+b
    if n==0: return 1.0
    k=min(a,b)
    return min(1.0,2*sum(comb(n,i) for i in range(k+1))/(2**n))


def _regime(rates:tuple[float,...])->str:
    return {"warning_evaluable":"R4_highrep","rapid_loss":"R2_highrep","persistence":"R1_highrep","seed_heterogeneous":"R3_highrep"}[classify_seed_rates(rates)]


def run_phase_n_seed(upstream_checkout:str|Path, master_seed:int)->dict[str,Any]:
    if master_seed not in PHASE_G_MASTER_SEEDS: raise ValueError("not a locked Phase-G seed")
    checkout=Path(upstream_checkout)
    coordinate=phase_g_coordinate(); driver_rate=coordinate.kappa_mu/2.0
    conditions=phase_g_conditions(); attempts=[]
    with _upstream_import_path(checkout):
        audit=importlib.import_module(UPSTREAM_H1_MODULE); experiments=importlib.import_module(UPSTREAM_EXPERIMENT_MODULE)
        mutation=importlib.import_module(UPSTREAM_MUTATION_MODULE); runtime=importlib.import_module(UPSTREAM_CHAIN_RUNTIME_MODULE)
        calibration=importlib.import_module(UPSTREAM_CALIBRATION_MODULE); dynamics=importlib.import_module(UPSTREAM_DYNAMICS_MODULE); chain=runtime.chain
        schedule=calibration.RampHoldSchedule(PHASE_G_RAMP_GENERATIONS,PHASE_G_HOLD_GENERATIONS,PHASE_G_BARRIER_INCREASE)
        spec=replace(experiments.standard_profile(),experiment_id="partner_precision_phase_n",generations=1,replicates=PHASE_N_REPLICATES_PER_SEED,master_seed=master_seed,area_reference_values=(PHASE_G_AREA_REFERENCE,),interaction_feedback_values=(PHASE_G_INTERACTION_KAPPA,),interaction_barrier_values=(0.5,))
        with patched_protocol002_mutation_runner(mutation,coordinate):
            cells=audit.run_finite_h1_boundary_resolution_audit(spec,endpoint_padding_fraction=0.5,stage_generations=SOURCE_STAGE_GENERATIONS,nested_barrier_points=SOURCE_NESTED_BARRIER_GRIDS,interaction_separation_threshold=0.05,maximum_normalized_bracket_width=0.03)
            if len(cells)!=1: raise RuntimeError("Phase N requires one H1 cell")
            cell=cells[0]; isolated=experiments.scenario_equal_isolated(spec)
            scenario=experiments.LandscapeScenario(scenario_id="equal_fragmented_partner_precision_phase_n",patch_areas=isolated.patch_areas,migration_rate=PHASE_G_MIGRATION_RATE)
            for record in cell.replicates:
                base={"master_seed":master_seed,"replicate":record.replicate_index,"calibration_seed":record.seed}
                prepared=chain._prepare_mutation_high_state(driver_rate,spec,cell,record,endpoint_padding_fraction=0.5,stage_generations=SOURCE_STAGE_GENERATIONS,hold_generations=SOURCE_HOLD_GENERATIONS,interaction_separation_threshold=0.05)
                if prepared is None:
                    for condition in conditions:
                        attempts.append({**base,"partner_architecture":condition.name,"retained_interaction_support":retained_support(condition,record.replicate_index),"source_prepared":False,"projection_supported":None,"eligible_for_trait_loss_denominator":False,"trait_loss_observed_post_baseline":None})
                    continue
                source,anchor_barrier=prepared; interval=cell.canonical_bistable_barrier_interval
                if interval is None or interval[1]<=interval[0]: raise RuntimeError("positive interval required")
                barriers=calibration.ramp_and_hold_barrier_schedule(anchor_barrier=anchor_barrier,canonical_interval_width=interval[1]-interval[0],schedule=schedule)
                template=chain.parameters_for_cell(spec,scenario,replace(cell.parameters,interaction_barrier=anchor_barrier),seed=record.seed)
                projected,invariants=chain.project_full_state(source,template)
                for condition in conditions:
                    multiplier=retained_support(condition,record.replicate_index)
                    if not invariants.projection_supported:
                        attempts.append({**base,"partner_architecture":condition.name,"retained_interaction_support":multiplier,"source_prepared":True,"projection_supported":False,"eligible_for_trait_loss_denominator":False,"trait_loss_observed_post_baseline":None}); continue
                    with patched_interaction_support_multiplier(mutation,multiplier):
                        result=mutation.simulate_with_symmetric_allele_mutation(replace(projected,generations=schedule.total_generations,random_seed=record.seed),mutation_rate=driver_rate,interaction_barrier_schedule=barriers)
                    baseline=any(item.realised_high_trait_occupied for item in result.snapshots[0].trait_occupancy)
                    raw=dynamics.tau_trait_realised(result); loss_time=None if raw is None or raw==0 else raw
                    attempts.append({**base,"partner_architecture":condition.name,"retained_interaction_support":multiplier,"source_prepared":True,"projection_supported":True,"eligible_for_trait_loss_denominator":bool(baseline),"trait_loss_observed_post_baseline":None if not baseline else loss_time is not None})
    summaries=[]; prefix_ok=True
    for condition in conditions:
        rows=[r for r in attempts if r["partner_architecture"]==condition.name]
        prefix=[r for r in rows if r["replicate"]<PHASE_N_PREFIX_REPLICATES]; pe=[r for r in prefix if r["eligible_for_trait_loss_denominator"]]; pl=[r for r in pe if r["trait_loss_observed_post_baseline"] is True]
        ee,el=expected_prefix(master_seed,condition.name); ok=len(pe)==ee and len(pl)==el; prefix_ok &= ok
        eligible=[r for r in rows if r["eligible_for_trait_loss_denominator"]]; losses=[r for r in eligible if r["trait_loss_observed_post_baseline"] is True]
        summaries.append({"partner_architecture":condition.name,"baseline_eligible":len(eligible),"trait_loss":len(losses),"trait_loss_rate":None if not eligible else len(losses)/len(eligible),"precision_sufficient":len(eligible)>=PHASE_N_MIN_BASELINE_ELIGIBLE_PER_SEED,"prefix":{"observed_eligible":len(pe),"observed_losses":len(pl),"expected_eligible":ee,"expected_losses":el,"matches_historical":ok}})
    return {"stage":"partner precision validation Phase N","master_seed":master_seed,"prefix_audit_passed":prefix_ok,"condition_summaries":summaries,"attempts":attempts}


def aggregate_phase_n(payloads:Iterable[dict[str,Any]])->dict[str,Any]:
    payloads=tuple(payloads)
    if sorted(p["master_seed"] for p in payloads)!=sorted(PHASE_G_MASTER_SEEDS): raise RuntimeError("requires five locked Phase-G seeds")
    prefix_ok=all(p["prefix_audit_passed"] for p in payloads); summaries=[]; regimes={}
    for condition in phase_g_conditions():
        blocks=[]
        for payload in sorted(payloads,key=lambda x:x["master_seed"]):
            row=next(r for r in payload["condition_summaries"] if r["partner_architecture"]==condition.name); blocks.append((int(row["trait_loss"]),int(row["baseline_eligible"])))
        sufficient=all(n>=PHASE_N_MIN_BASELINE_ELIGIBLE_PER_SEED for _,n in blocks); rates=tuple(k/n for k,n in blocks); regime="insufficient_precision" if not sufficient else _regime(rates)
        pooled=sum(k for k,_ in blocks)/sum(n for _,n in blocks); stat,df,p=pearson_equal_rate_test(tuple(blocks)); ref=ensemble_gate_pass_probability(tuple(n for _,n in blocks),pooled); regimes[condition.name]=regime
        summaries.append({"partner_architecture":condition.name,"blocks":[{"master_seed":s,"losses":k,"eligible":n,"rate":k/n} for s,(k,n) in zip(PHASE_G_MASTER_SEEDS,blocks,strict=True)],"pooled_loss_rate":pooled,"historical_gate_regime_at_full_precision":regime,"pearson_equal_rate_p_value":p,"homogeneous_reference_gate_fail_probability":1-ref})
    indexed={}
    for payload in payloads:
        for row in payload["attempts"]: indexed[(row["master_seed"],row["replicate"],row["partner_architecture"])]=row
    paired=[]
    for condition in phase_g_conditions()[1:]:
        a=b=same_loss=same_no=comp=0
        for seed in PHASE_G_MASTER_SEEDS:
            for rep in range(PHASE_N_REPLICATES_PER_SEED):
                ref=indexed[(seed,rep,"intact_control")]; row=indexed[(seed,rep,condition.name)]
                if not(ref["eligible_for_trait_loss_denominator"] and row["eligible_for_trait_loss_denominator"]): continue
                comp+=1; rl=ref["trait_loss_observed_post_baseline"] is True; nl=row["trait_loss_observed_post_baseline"] is True
                if rl and not nl:a+=1
                elif not rl and nl:b+=1
                elif rl:same_loss+=1
                else:same_no+=1
        paired.append({"partner_architecture":condition.name,"comparable_pair_count":comp,"loss_to_no_loss":a,"no_loss_to_loss":b,"same_loss":same_loss,"same_no_loss":same_no,"exact_mcnemar_two_sided_p":_mcnemar(a,b)})
    old_r3_persists=any(regimes[name]=="R3_highrep" for name in ("even_redundant","graded_contributions","dominant_partner"))
    decision="prefix_reproducibility_failed" if not prefix_ok else "insufficient_precision" if any(v=="insufficient_precision" for v in regimes.values()) else "historical_partner_r3_persists_at_high_precision" if old_r3_persists else "historical_partner_r3_disappears_at_high_precision"
    return {"stage":"partner precision validation Phase N","manifest":phase_n_manifest(),"prefix_audit_passed":prefix_ok,"decision":decision,"regime_by_architecture":regimes,"architecture_summaries":summaries,"paired_loss_status_vs_intact":paired,"per_seed_payloads":list(payloads)}


def load_and_aggregate_phase_n(paths:Iterable[str|Path])->dict[str,Any]:
    return aggregate_phase_n([json.loads(Path(p).read_text()) for p in paths])
