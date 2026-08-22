from __future__ import annotations
import argparse,glob,json
from pathlib import Path
from eco_genetic_warning_extensions.interaction_support_precision_phase_q_runner import load_and_aggregate_phase_q

def main():
    p=argparse.ArgumentParser();p.add_argument('--input-glob',required=True);p.add_argument('--output',required=True);a=p.parse_args();paths=sorted(glob.glob(a.input_glob))
    if not paths:raise SystemExit('no Phase-Q seed files matched')
    result=load_and_aggregate_phase_q(paths);out=Path(a.output);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print('PHASE_Q_SUMMARY_BEGIN');print(json.dumps({k:result[k] for k in ('prefix_audit_passed','decision','regime_by_kappa','kappa_summaries')},sort_keys=True));print('PHASE_Q_SUMMARY_END')
if __name__=='__main__':main()
