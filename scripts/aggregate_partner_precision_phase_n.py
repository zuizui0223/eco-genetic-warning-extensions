from __future__ import annotations
import argparse,glob,json
from pathlib import Path
from eco_genetic_warning_extensions.partner_precision_phase_n_runner import load_and_aggregate_phase_n

def main():
    p=argparse.ArgumentParser(); p.add_argument('--input-glob',required=True); p.add_argument('--output',required=True); a=p.parse_args(); paths=sorted(glob.glob(a.input_glob))
    if not paths: raise SystemExit('no Phase-N seed files matched')
    result=load_and_aggregate_phase_n(paths); out=Path(a.output); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print('PHASE_N_SUMMARY_BEGIN'); print(json.dumps({k:result[k] for k in ('prefix_audit_passed','decision','regime_by_architecture','architecture_summaries','paired_loss_status_vs_intact')},sort_keys=True)); print('PHASE_N_SUMMARY_END')
if __name__=='__main__': main()
