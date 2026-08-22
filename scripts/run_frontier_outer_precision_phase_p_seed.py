from __future__ import annotations
import argparse,json
from pathlib import Path
from eco_genetic_warning_extensions.frontier_outer_precision_phase_p_runner import run_phase_p_seed

def main():
    p=argparse.ArgumentParser(); p.add_argument('--upstream-checkout',required=True); p.add_argument('--master-seed',type=int,required=True); p.add_argument('--output',required=True); a=p.parse_args(); out=Path(a.output); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(run_phase_p_seed(a.upstream_checkout,a.master_seed),indent=2,sort_keys=True)+'\n')
if __name__=='__main__': main()
