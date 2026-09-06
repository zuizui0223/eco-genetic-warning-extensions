from __future__ import annotations

import argparse, csv, html, json
from pathlib import Path


def t(x,y,s,size=15,anchor="middle",weight="normal",rotate=None):
    r=f' transform="rotate({rotate} {x} {y})"' if rotate is not None else ""
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Arial,Helvetica,sans-serif" font-size="{size}" font-weight="{weight}"{r}>{html.escape(str(s))}</text>'

def start(w,h,title,desc):
    return [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">',f'<title id="title">{html.escape(title)}</title>',f'<desc id="desc">{html.escape(desc)}</desc>','<rect width="100%" height="100%" fill="white"/>','<defs><marker id="a" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto"><path d="M0,0 L0,9 L9,4.5 z" fill="#222"/></marker></defs>']

def done(lines,path):
    lines.append('</svg>'); path.parent.mkdir(parents=True,exist_ok=True); path.write_text('\n'.join(lines)+'\n',encoding='utf-8')

def box(lines,x,y,w,h,label,sub=""):
    lines.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="white" stroke="#222" stroke-width="2"/>')
    lines.append(t(x+w/2,y+34,label,16,weight="bold"))
    if sub: lines.append(t(x+w/2,y+60,sub,12))

def fig1(path):
    L=start(1500,760,'Three mathematical boundaries','Conceptual map of the three load-bearing mathematical boundaries.')
    L += [t(750,45,'Three boundaries on functional vulnerability under fragmentation',28,weight='bold')]
    items=[(80,'State separation','fragmentation != one deterioration axis'),(525,'Transition sufficiency','phi(XA)=phi(XB) but T(XA)!=T(XB)'),(970,'Warning discrimination','perfect precedence != specificity')]
    for x,a,b in items:
        box(L,x,160,350,115,a,b)
    for x1,x2 in [(430,525),(875,970)]: L.append(f'<line x1="{x1}" y1="218" x2="{x2-10}" y2="218" stroke="#222" stroke-width="2" marker-end="url(#a)"/>')
    L += [t(255,350,'Exact interaction-state geometry + finite fragmentation gradient',13),t(700,350,'Constructive factorization failure + locked propagation',13),t(1145,350,'Exact denominator identity + full-denominator audit',13)]
    box(L,470,455,560,120,'Positive synthesis','functional vulnerability depends on future-relevant relational state')
    L += [t(750,620,'Natural examples enter only after the mathematics:',15,weight='bold'),t(750,650,'collapse, compensation and temporal lag are ecological projections, not validation datasets',14),t(750,710,'No arrow above is claimed to be a causal mediation chain among the three tests.',12)]
    done(L,path)

def fig2(egc,path):
    rows=list(csv.DictReader((egc/'artifacts/h3_fragmentation_gradient/h3_fragmentation_gradient_pooled_summary.csv').open()))
    assert [int(r['patch_count']) for r in rows]==[1,2,3,4,6,8,12,16]
    assert int(rows[0]['projection_supported'])==1037
    L=start(1500,800,'Fragmentation separates functional support from persistence','Fixed-area fragmentation gradient with distinct biological-state responses.')
    L += [t(750,42,'Fragmentation separates functional support from persistence',28,weight='bold'),t(350,90,'A  Potential viability and realised occupancy',18,weight='bold'),t(1110,90,'B  Retained state ratios',18,weight='bold')]
    # Panel A
    left,right,top,bottom=90,670,150,610
    for p in [0,25,50,75,100]:
        y=bottom-p/100*(bottom-top); L.append(f'<line x1="{left}" y1="{y}" x2="{right}" y2="{y}" stroke="#ddd"/>'); L.append(t(left-8,y+4,p,11,anchor='end'))
    xs=[left+i*(right-left)/7 for i in range(8)]
    vals=[100]+[0]*7
    pts=[]
    for x,p,n in zip(xs,vals,[1,2,3,4,6,8,12,16]):
        y=bottom-p/100*(bottom-top); pts.append((x,y)); L.append(f'<circle cx="{x}" cy="{y}" r="5" fill="white" stroke="#111"/>'); L.append(t(x,bottom+23,n,11))
    L.append('<polyline points="'+' '.join(f'{x},{y}' for x,y in pts)+'" fill="none" stroke="#111" stroke-width="2.3"/>')
    L += [t(380,132,'realised occupancy at generation 30 ~99.6-100%',12),t(30,390,'supported outcomes (%)',12,rotate=-90),t(380,665,'number of isolated equal patches',12),t(380,710,'potential viability: 1,037/1,037 -> 0/1,037 after first split',14,weight='bold')]
    # Panel B
    l,r,tt,b=820,1430,150,610
    keys=[('final_interaction_mean_ratio_to_n1_median','interaction',''),('final_effective_size_mean_ratio_to_n1_median','local effective size','8 5'),('realised_high_trait_mass_mean_ratio_to_n1_median','realised high-trait mass','3 4')]
    for q in [0,.25,.5,.75,1]:
        y=b-q*(b-tt); L.append(f'<line x1="{l}" y1="{y}" x2="{r}" y2="{y}" stroke="#ddd"/>'); L.append(t(l-8,y+4,f'{q:.2g}',11,anchor='end'))
    x2=[l+i*(r-l)/7 for i in range(8)]
    for idx,(k,lab,dash) in enumerate(keys):
        vals=[float(row[k]) for row in rows]; pts=[(x,b-v*(b-tt)) for x,v in zip(x2,vals)]; d=f' stroke-dasharray="{dash}"' if dash else ''
        L.append('<polyline points="'+' '.join(f'{x},{y}' for x,y in pts)+f'" fill="none" stroke="#111" stroke-width="2.2"{d}/>')
        L.append(t(900,655+idx*24,lab,12,anchor='start'))
    for x,n in zip(x2,[1,2,3,4,6,8,12,16]): L.append(t(x,b+23,n,11))
    L += [t(1120,745,'same structural fragmentation != one biological deterioration coordinate',15,weight='bold')]
    done(L,path)

def fig3(root,path):
    phase=json.loads((root/'artifacts/cross_layer_alignment/phase_v_locked_summary.json').read_text())
    prop=json.loads((root/'artifacts/alignment_propagation/locked_summary.json').read_text())
    c=phase['opening_certificate']; assert abs(c['maximum_patchwise_generation1_difference']-0.25433292878878405)<1e-12
    primary=sorted(prop['result']['primary_horizon_cells'],key=lambda z:z['horizon'])
    L=start(1500,820,'Identical marginals, different future','Constructive relational-state counterexample and later propagation.')
    L += [t(750,42,'Identical marginals can encode different transitions and futures',28,weight='bold'),t(355,88,'A  Exact transition-sufficiency certificate',18,weight='bold'),t(1115,88,'B  Locked 1,500-pair propagation',18,weight='bold')]
    L += [t(355,130,'all declared census, interaction, trait and genetic marginals identical',12),t(355,155,f"cross-layer covariance {c['aligned_cross_layer_covariance']:+.3f} vs {c['anti_aligned_cross_layer_covariance']:+.3f}",13,weight='bold')]
    xs=[130,280,430,580]
    for y,label,vals in [(250,'aligned',c['aligned_generation1_interaction']),(365,'anti-aligned',c['anti_aligned_generation1_interaction'])]:
        L.append(t(55,y+4,label,13,anchor='start',weight='bold'))
        for i,(x,v) in enumerate(zip(xs,vals),1): box(L,x-45,y-30,90,60,f'P{i}',f'q1={v:.3f}')
    L += [t(355,470,f"max |T_I(XA)-T_I(XB)| = {c['maximum_patchwise_generation1_difference']:.4f}",16,weight='bold'),t(355,505,'therefore no g exists with T_I = g o phi for the retained marginals',13)]
    # propagation
    l,r,top,b=825,1430,150,610; ymin,ymax=-.02,.10
    y0=b-(0-ymin)/(ymax-ymin)*(b-top); L.append(f'<line x1="{l}" y1="{y0}" x2="{r}" y2="{y0}" stroke="#777"/>')
    hx={5:900,10:1035,20:1200,40:1380}; pts=[]
    for row in primary:
        h=row['horizon']; est=row['risk_difference_anti_minus_aligned']; lo=row['ci95_lower']; hi=row['ci95_upper']; x=hx[h]
        y=b-(est-ymin)/(ymax-ymin)*(b-top); yl=b-(lo-ymin)/(ymax-ymin)*(b-top); yh=b-(hi-ymin)/(ymax-ymin)*(b-top); pts.append((x,y))
        L += [f'<line x1="{x}" y1="{yh}" x2="{x}" y2="{yl}" stroke="#111" stroke-width="2"/>',f'<circle cx="{x}" cy="{y}" r="6" fill="white" stroke="#111" stroke-width="2"/>',t(x,b+24,h,11),t(x,y-15,f'{est*100:+.2f} pp',11,weight='bold')]
    L.append('<polyline points="'+' '.join(f'{x},{y}' for x,y in pts)+'" fill="none" stroke="#111" stroke-width="2"/>')
    L += [t(785,380,'anti-aligned - aligned loss risk (pp)',12,rotate=-90),t(1125,670,'generation',12),t(1125,735,'relational state can be exact now and consequential later',15,weight='bold')]
    done(L,path)

def fig4(root,path):
    rows=list(csv.DictReader((root/'manuscript/tables/warning_validity_audit.csv').open()))
    by={}
    for r in rows: by.setdefault(r['ensemble'],[]).append(r)
    for ens,ev,ne in [('inherited_202611',35,48),('fresh_202911',33,49)]:
        assert len(by[ens])==6
        assert all(int(r['events'])==ev and int(r['right_censored_non_events'])==ne and float(r['lead_sensitivity'])==1 and float(r['full_horizon_specificity'])==0 and float(r['full_horizon_binary_auc'])==.5 for r in by[ens])
    L=start(1500,800,'Early erosion without fate discrimination','Frozen diversity thresholds show perfect temporal precedence and zero specificity.')
    L += [t(750,42,'A perfectly early marginal signal can fail to distinguish ecological fate',27,weight='bold')]
    def cm(cx,label,ev,ne):
        L.append(t(cx,100,label,18,weight='bold')); x0=cx-140; y0=170; cw=115; rh=100
        L += [t(cx,y0-30,'marker fired by horizon',12,weight='bold'),t(x0+cw*.5,y0-8,'yes',11),t(x0+cw*1.5,y0-8,'no',11),t(x0-10,y0+55,'loss',11,anchor='end'),t(x0-10,y0+155,'non-loss',11,anchor='end')]
        vals=[[ev,0],[ne,0]]
        for i in range(2):
            for j in range(2):
                x=x0+j*cw; y=y0+i*rh; L.append(f'<rect x="{x}" y="{y}" width="{cw}" height="{rh}" fill="white" stroke="#222"/>'); L.append(t(x+cw/2,y+58,vals[i][j],25,weight='bold'))
        L += [t(cx,415,f'event leads {ev}/{ev}; non-event firing {ne}/{ne}',13,weight='bold'),t(cx,445,'sensitivity=1; specificity=0; AUC=0.5',13)]
    cm(350,'A  inherited ensemble',35,48); cm(750,'B  fresh ensemble',33,49)
    box(L,1035,155,390,330,'C  Exact denominator result','event-only ordering leaves non-event firing free')
    L += [t(1230,270,'perfect precedence -> sensitivity = 1',14),t(1230,320,'specificity = (n0 - f) / n0',15,weight='bold'),t(1230,370,'binary AUC = (1 + specificity) / 2',15,weight='bold'),t(1230,425,'observed f = n0 -> AUC = 0.5',15,weight='bold'),t(750,620,'stress-sensitive != fate-discriminating',19,weight='bold'),t(750,655,'all six frozen H_alpha/H_gamma rules reach the same horizon classification endpoint',12)]
    done(L,path)

def main():
    p=argparse.ArgumentParser(); p.add_argument('--egc-root',required=True); p.add_argument('--egwe-root',required=True); p.add_argument('--output',required=True); a=p.parse_args()
    out=Path(a.output); out.mkdir(parents=True,exist_ok=True); egc=Path(a.egc_root); root=Path(a.egwe_root)
    fig1(out/'figure1_mathematical_boundaries.svg'); fig2(egc,out/'figure2_state_separation.svg'); fig3(root,out/'figure3_relational_state.svg'); fig4(root,out/'figure4_warning_discrimination.svg')
    print('Generated four math-first flagship figures')

if __name__=='__main__': main()
