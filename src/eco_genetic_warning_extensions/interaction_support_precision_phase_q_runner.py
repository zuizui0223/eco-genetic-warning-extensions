"""Per-seed runner and aggregator for Phase-Q interaction-support precision validation."""
from __future__ import annotations
import importlib,json
from dataclasses import replace
from pathlib import Path
from typing import Any,Iterable
from .interaction_support_precision_phase_q import PHASE_Q_MIN_BASELINE_ELIGIBLE_PER_SEED,PHASE_Q_PREFIX_REPLICATES,PHASE_Q_REPLICATES_PER_SEED,expected_prefix,phase_q_manifest
from .interaction_support_phase_f import PHASE_F_AREA_REFERENCE,PHASE_F_BARRIER_INCREASE,PHASE_F_HOLD_GENERATIONS,PHASE_F_INTERACTION_KAPPAS,PHASE_F_KAPPA_MU,PHASE_F_MASTER_SEEDS,PHASE_F_MIGRATION_RATE,PHASE_F_P_STAR,PHASE_F_RAMP_GENERATIONS
from .mutation_coordinates import MutationCoordinates
from .protocol002_condition_map import classify_seed_rates
from .protocol002_source_grid import SOURCE_HOLD_GENERATIONS,SOURCE_NESTED_BARRIER_GRIDS,SOURCE_STAGE_GENERATIONS
from .protocol002_stage1_projection_pilot import UPSTREAM_CHAIN_RUNTIME_MODULE
from .protocol002_stage2_smoke import UPSTREAM_CALIBRATION_MODULE,UPSTREAM_DYNAMICS_MODULE
from .protocol002_upstream_h1_asym_smoke import UPSTREAM_EXPERIMENT_MODULE,UPSTREAM_H1_MODULE,UPSTREAM_MUTATION_MODULE,_upstream_import_path,patched_protocol002_mutation_runner
from .r4_gate_validity_phase_j import ensemble_gate_pass_probability,pearson_equal_rate_test

def _regime(rates):return {"warning_evaluable":"R4_highrep","rapid_loss":"R2_highrep","persistence":"R1_highrep","seed_heterogeneous":"R3_highrep"}[classify_seed_rates(tuple(rates))]

def run_phase_q_seed(upstream_checkout:str|Path,master_seed:int)->dict[str,Any]:
    if master_seed not in PHASE_F_MASTER_SEEDS:raise ValueError("not locked Phase-F seed")
    checkout=Path(upstream_checkout); coordinate=MutationCoordinates(kappa_mu=PHASE_F_KAPPA_MU,p_star=PHASE_F_P_STAR); driver=coordinate.kappa_mu/2; attempts=[]
    with _upstream_import_path(checkout):
        audit=importlib.import_module(UPSTREAM_H1_MODULE); experiments=importlib.import_module(UPSTREAM_EXPERIMENT_MODULE); mutation=importlib.import_module(UPSTREAM_MUTATION_MODULE); runtime=importlib.import_module(UPSTREAM_CHAIN_RUNTIME_MODULE); calibration=importlib.import_module(UPSTREAM_CALIBRATION_MODULE); dynamics=importlib.import_module(UPSTREAM_DYNAMICS_MODULE); chain=runtime.chain
        schedule=calibration.RampHoldSchedule(PHASE_F_RAMP_GENERATIONS,PHASE_F_HOLD_GENERATIONS,PHASE_F_BARRIER_INCREASE)
        for kappa in PHASE_F_INTERACTION_KAPPAS:
            spec=replace(experiments.standard_profile(),experiment_id=f"interaction_support_precision_q_{kappa:g}",generations=1,replicates=PHASE_Q_REPLICATES_PER_SEED,master_seed=master_seed,area_reference_values=(PHASE_F_AREA_REFERENCE,),interaction_feedback_values=(kappa,),interaction_barrier_values=(0.5,))
            with patched_protocol002_mutation_runner(mutation,coordinate):
                cells=audit.run_finite_h1_boundary_resolution_audit(spec,endpoint_padding_fraction=.5,stage_generations=SOURCE_STAGE_GENERATIONS,nested_barrier_points=SOURCE_NESTED_BARRIER_GRIDS,interaction_separation_threshold=.05,maximum_normalized_bracket_width=.03)
                if len(cells)!=1:raise RuntimeError("Phase Q requires one H1 cell")
                cell=cells[0]; isolated=experiments.scenario_equal_isolated(spec)
                for record in cell.replicates:
                    base={"master_seed":master_seed,"replicate":record.replicate_index,"interaction_kappa":kappa,"calibration_seed":record.seed}
                    prepared=chain._prepare_mutation_high_state(driver,spec,cell,record,endpoint_padding_fraction=.5,stage_generations=SOURCE_STAGE_GENERATIONS,hold_generations=SOURCE_HOLD_GENERATIONS,interaction_separation_threshold=.05)
                    if prepared is None:
                        attempts.append({**base,"source_prepared":False,"projection_supported":None,"eligible_for_trait_loss_denominator":False,"trait_loss_observed_post_baseline":None});continue
                    source,barrier=prepared; interval=cell.canonical_bistable_barrier_interval
                    if interval is None or interval[1]<=interval[0]:raise RuntimeError("positive interval required")
                    barriers=calibration.ramp_and_hold_barrier_schedule(anchor_barrier=barrier,canonical_interval_width=interval[1]-interval[0],schedule=schedule); scenario=experiments.LandscapeScenario(scenario_id=f"q_kappa_{kappa:g}",patch_areas=isolated.patch_areas,migration_rate=PHASE_F_MIGRATION_RATE); template=chain.parameters_for_cell(spec,scenario,replace(cell.parameters,interaction_barrier=barrier),seed=record.seed); projected,inv=chain.project_full_state(source,template)
                    if not inv.projection_supported:
                        attempts.append({**base,"source_prepared":True,"projection_supported":False,"eligible_for_trait_loss_denominator":False,"trait_loss_observed_post_baseline":None});continue
                    result=mutation.simulate_with_symmetric_allele_mutation(replace(projected,generations=schedule.total_generations,random_seed=record.seed),mutation_rate=driver,interaction_barrier_schedule=barriers); baseline=any(x.realised_high_trait_occupied for x in result.snapshots[0].trait_occupancy); raw=dynamics.tau_trait_realised(result); loss=None if raw is None or raw==0 else raw
                    attempts.append({**base,"source_prepared":True,"projection_supported":True,"eligible_for_trait_loss_denominator":bool(baseline),"trait_loss_observed_post_baseline":None if not baseline else loss is not None})
    summaries=[];prefix_ok=True
    for kappa in PHASE_F_INTERACTION_KAPPAS:
        rows=[r for r in attempts if r["interaction_kappa"]==kappa];pre=[r for r in rows if r["replicate"]<PHASE_Q_PREFIX_REPLICATES];pe=[r for r in pre if r["eligible_for_trait_loss_denominator"]];pl=[r for r in pe if r["trait_loss_observed_post_baseline"] is True];ee,el=expected_prefix(master_seed,kappa);ok=len(pe)==ee and len(pl)==el;prefix_ok&=ok;eligible=[r for r in rows if r["eligible_for_trait_loss_denominator"]];losses=[r for r in eligible if r["trait_loss_observed_post_baseline"] is True]
        summaries.append({"interaction_kappa":kappa,"baseline_eligible":len(eligible),"trait_loss":len(losses),"trait_loss_rate":None if not eligible else len(losses)/len(eligible),"precision_sufficient":len(eligible)>=PHASE_Q_MIN_BASELINE_ELIGIBLE_PER_SEED,"prefix":{"observed_eligible":len(pe),"observed_losses":len(pl),"expected_eligible":ee,"expected_losses":el,"matches_historical":ok}})
    return {"stage":"interaction support precision Phase Q","master_seed":master_seed,"prefix_audit_passed":prefix_ok,"condition_summaries":summaries}

def aggregate_phase_q(payloads:Iterable[dict[str,Any]])->dict[str,Any]:
    payloads=tuple(payloads)
    if sorted(p["master_seed"] for p in payloads)!=sorted(PHASE_F_MASTER_SEEDS):raise RuntimeError("requires five locked Phase-F seeds")
    prefix=all(p["prefix_audit_passed"] for p in payloads);summaries=[];regimes={}
    for kappa in PHASE_F_INTERACTION_KAPPAS:
        blocks=[]
        for payload in sorted(payloads,key=lambda x:x["master_seed"]):
            r=next(x for x in payload["condition_summaries"] if x["interaction_kappa"]==kappa);blocks.append((int(r["trait_loss"]),int(r["baseline_eligible"])))
        sufficient=all(n>=PHASE_Q_MIN_BASELINE_ELIGIBLE_PER_SEED for _,n in blocks);rates=tuple(k/n for k,n in blocks);reg="insufficient_precision" if not sufficient else _regime(rates);pooled=sum(k for k,_ in blocks)/sum(n for _,n in blocks);stat,df,p=pearson_equal_rate_test(tuple(blocks));ref=ensemble_gate_pass_probability(tuple(n for _,n in blocks),pooled);regimes[f"{kappa:g}"]=reg;summaries.append({"interaction_kappa":kappa,"blocks":[{"master_seed":s,"losses":k,"eligible":n,"rate":k/n} for s,(k,n) in zip(PHASE_F_MASTER_SEEDS,blocks,strict=True)],"pooled_loss_rate":pooled,"historical_gate_regime_at_full_precision":reg,"pearson_equal_rate_p_value":p,"homogeneous_reference_gate_fail_probability":1-ref})
    decision="prefix_reproducibility_failed" if not prefix else "insufficient_precision" if any(v=="insufficient_precision" for v in regimes.values()) else "all_predeclared_kappa_remain_r4_at_high_precision" if all(v=="R4_highrep" for v in regimes.values()) else "historical_all_r4_result_changes_at_high_precision"
    return {"stage":"interaction support precision Phase Q","manifest":phase_q_manifest(),"prefix_audit_passed":prefix,"decision":decision,"regime_by_kappa":regimes,"kappa_summaries":summaries,"per_seed_payloads":list(payloads)}

def load_and_aggregate_phase_q(paths:Iterable[str|Path])->dict[str,Any]:return aggregate_phase_q([json.loads(Path(p).read_text()) for p in paths])
