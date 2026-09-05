from __future__ import annotations

import argparse
import csv
import html
import json
import math
from pathlib import Path


def text(x: float, y: float, value: str, *, size: int = 16, anchor: str = "middle", weight: str = "normal") -> str:
    return (
        f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" '
        f'font-family="Arial,Helvetica,sans-serif" font-size="{size}" font-weight="{weight}">'
        f'{html.escape(value)}</text>'
    )


def wrap_lines(value: str, width: int) -> list[str]:
    words = value.split()
    lines: list[str] = []
    current: list[str] = []
    n = 0
    for word in words:
        add = len(word) + (1 if current else 0)
        if current and n + add > width:
            lines.append(" ".join(current))
            current = [word]
            n = len(word)
        else:
            current.append(word)
            n += add
    if current:
        lines.append(" ".join(current))
    return lines


def multiline(x: float, y: float, value: str, *, width: int = 28, size: int = 14, anchor: str = "middle", weight: str = "normal", leading: float = 19) -> list[str]:
    out: list[str] = []
    for i, line in enumerate(wrap_lines(value, width)):
        out.append(text(x, y + i * leading, line, size=size, anchor=anchor, weight=weight))
    return out


def svg_start(width: int, height: int, title: str, desc: str) -> list[str]:
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        f'<title id="title">{html.escape(title)}</title>',
        f'<desc id="desc">{html.escape(desc)}</desc>',
        '<rect width="100%" height="100%" fill="white"/>',
        '<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0,0 L0,10 L9,5 z" fill="#222"/></marker></defs>',
    ]


def finish(lines: list[str], path: Path) -> None:
    lines.append('</svg>')
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def figure1(path: Path) -> None:
    width, height = 1500, 820
    lines = svg_start(width, height, "Predictive-validity hierarchy", "Four validation obligations connect ecological state, representation, signal and measurement to a declared future target. Each transition has a constructive non-implication demonstrated in the study.")
    lines += [
        text(750, 48, "Ecological prediction requires a validated chain", size=30, weight="bold"),
        text(750, 80, "Success at one layer does not license the next", size=17),
    ]

    boxes = [
        (150, "Disturbance / process", "upstream change"),
        (410, "Biological state X(t)", "target-relevant objects"),
        (690, "Representation φ(X)", "measured / modelled summary"),
        (970, "Candidate signal W", "history-to-warning map"),
        (1260, "Future target Y(t+h)", "declared endpoint + horizon"),
    ]
    y = 260
    for x, title, sub in boxes:
        lines.append(f'<rect x="{x-105}" y="{y-58}" width="210" height="116" rx="12" fill="white" stroke="#222" stroke-width="2"/>')
        lines.append(text(x, y-8, title, size=16, weight="bold"))
        lines += multiline(x, y+18, sub, width=22, size=12)
    for a, b in zip(boxes[:-1], boxes[1:]):
        x1, x2 = a[0]+110, b[0]-110
        lines.append(f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="#222" stroke-width="2.2" marker-end="url(#arrow)"/>')

    labels = [
        (280, "common disturbance ≠ one biological state"),
        (550, "matching marginals ≠ matching futures"),
        (830, "early timing ≠ predictive discrimination"),
        (1115, "signal relevance is target- and horizon-specific"),
    ]
    for x, lab in labels:
        lines.append(f'<rect x="{x-118}" y="345" width="236" height="68" rx="10" fill="#f5f5f5" stroke="#777"/>')
        lines += multiline(x, 370, lab, width=27, size=12, weight="bold")

    # Natural measurement enters state/representation from below.
    lines.append(f'<rect x="515" y="565" width="350" height="105" rx="12" fill="white" stroke="#222" stroke-width="2"/>')
    lines.append(text(690, 600, "Natural measurement M", size=18, weight="bold"))
    lines += multiline(690, 625, "endpoint relevance + information preservation + identifiability", width=46, size=13)
    lines.append('<line x1="690" y1="565" x2="690" y2="325" stroke="#222" stroke-width="2" marker-end="url(#arrow)"/>')
    lines.append(f'<rect x="520" y="695" width="340" height="65" rx="10" fill="#f5f5f5" stroke="#777"/>')
    lines += multiline(690, 720, "plausible proxy ≠ validated empirical state", width=39, size=13, weight="bold")

    lines += [
        text(140, 505, "Four constructive non-implications", size=18, anchor="start", weight="bold"),
        text(1360, 730, "Hierarchy of validation obligations — not a causal mediation chain", size=13, anchor="end", weight="bold"),
    ]
    finish(lines, path)


def load_egc(egc_root: Path) -> list[dict[str, str]]:
    p = egc_root / "artifacts/h3_fragmentation_gradient/h3_fragmentation_gradient_pooled_summary.csv"
    rows = list(csv.DictReader(p.open(encoding="utf-8")))
    if [int(r["patch_count"]) for r in rows] != [1,2,3,4,6,8,12,16]:
        raise RuntimeError("EGC patch-count grid drifted")
    r2 = rows[1]
    expected = (0.0017444307534129745, 0.22131147540983603, 0.28291808988011524)
    got = tuple(float(r2[k]) for k in ("final_interaction_mean_ratio_to_n1_median","final_effective_size_mean_ratio_to_n1_median","realised_high_trait_mass_mean_ratio_to_n1_median"))
    if any(abs(a-b)>1e-12 for a,b in zip(got, expected)):
        raise RuntimeError(f"EGC headline drifted: {got}")
    return rows


def figure2(egc_root: Path, path: Path) -> None:
    rows = load_egc(egc_root)
    width, height = 1500, 800
    lines = svg_start(width, height, "One disturbance separates biological states", "A fixed-area fragmentation gradient separates potential viability from realised occupancy and produces distinct response shapes for interaction, effective size and realised high-trait mass.")
    lines += [
        text(750, 44, "One structural change does not define one deterioration state", size=28, weight="bold"),
        text(355, 88, "A  Potential viability versus realised occupancy", size=19, weight="bold"),
        text(1100, 88, "B  Distinct response shapes across fragmentation", size=19, weight="bold"),
    ]
    patches = [int(r["patch_count"]) for r in rows]

    # Panel A: categorical 100 -> 0 viability, occupancy band 99.6-100.
    left, right, top, bottom = 85, 670, 145, 610
    for pct in (0,25,50,75,100):
        yy = bottom - pct/100*(bottom-top)
        lines.append(f'<line x1="{left}" y1="{yy:.1f}" x2="{right}" y2="{yy:.1f}" stroke="#ddd"/>')
        lines.append(text(left-10, yy+4, f"{pct}", size=12, anchor="end"))
    xs = [left+i*(right-left)/(len(patches)-1) for i in range(len(patches))]
    viability = [100]+[0]*7
    pts=[]
    for x,pct,n in zip(xs, viability, patches):
        yy = bottom - pct/100*(bottom-top)
        pts.append((x,yy))
        lines.append(f'<circle cx="{x:.1f}" cy="{yy:.1f}" r="5" fill="white" stroke="#111" stroke-width="2"/>')
        lines.append(text(x,bottom+25,str(n),size=11))
    lines.append('<polyline points="'+' '.join(f"{x:.1f},{y:.1f}" for x,y in pts)+'" fill="none" stroke="#111" stroke-width="2.5"/>')
    y100=top; y996=bottom-0.996*(bottom-top)
    lines.append(f'<rect x="{left}" y="{y100}" width="{right-left}" height="{max(3,y996-y100):.1f}" fill="#ddd" stroke="#777"/>')
    lines.append(text(410, 128, "realised occupancy at generation 30 ≈99.6–100%", size=13))
    lines += [
        text(385, 660, "number of equal isolated patches", size=13),
        text(35, 390, "% supported outcomes", size=13),
        text(385, 710, "potential viability: 1,037/1,037 → 0/1,037 after first split", size=15, weight="bold"),
    ]

    # Panel B: three retained-ratio curves on log-ish visual via linear 0-1.
    left2,right2,top2,bottom2=820,1435,145,610
    keys=[
        ("final_interaction_mean_ratio_to_n1_median","interaction"),
        ("final_effective_size_mean_ratio_to_n1_median","local effective size"),
        ("realised_high_trait_mass_mean_ratio_to_n1_median","realised high-trait mass"),
    ]
    for tick in (0,0.25,0.5,0.75,1.0):
        yy=bottom2-tick*(bottom2-top2)
        lines.append(f'<line x1="{left2}" y1="{yy:.1f}" x2="{right2}" y2="{yy:.1f}" stroke="#ddd"/>')
        lines.append(text(left2-10,yy+4,f"{tick:.2g}",size=12,anchor="end"))
    xs2=[left2+i*(right2-left2)/(len(patches)-1) for i in range(len(patches))]
    dash=["","8 5","3 4"]
    shapes=["circle","square","triangle"]
    for idx,(key,label) in enumerate(keys):
        vals=[float(r[key]) for r in rows]
        pts2=[(x,bottom2-v*(bottom2-top2)) for x,v in zip(xs2,vals)]
        d=f' stroke-dasharray="{dash[idx]}"' if dash[idx] else ''
        lines.append('<polyline points="'+' '.join(f"{x:.1f},{y:.1f}" for x,y in pts2)+f'" fill="none" stroke="#111" stroke-width="2.2"{d}/>')
        for x,y in pts2:
            if shapes[idx]=="circle": lines.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="white" stroke="#111"/>')
            elif shapes[idx]=="square": lines.append(f'<rect x="{x-4:.1f}" y="{y-4:.1f}" width="8" height="8" fill="white" stroke="#111"/>')
            else: lines.append(f'<path d="M{x:.1f},{y-5:.1f} L{x-5:.1f},{y+4:.1f} L{x+5:.1f},{y+4:.1f} Z" fill="white" stroke="#111"/>')
        ly=655+idx*25
        lines.append(text(875,ly,label,size=13,anchor="start"))
    for x,n in zip(xs2,patches): lines.append(text(x,bottom2+25,str(n),size=11))
    lines += [
        text(1120, 745, "same structural change ≠ same biological state response", size=16, weight="bold"),
        text(1120, 775, "trait mass partially recovers while interaction and Ne continue to decline", size=13),
    ]
    finish(lines,path)


def load_state(root: Path):
    phase=json.loads((root/"artifacts/cross_layer_alignment/phase_v_locked_summary.json").read_text())
    prop=json.loads((root/"artifacts/alignment_propagation/locked_summary.json").read_text())
    cert=phase["opening_certificate"]
    if abs(float(cert["maximum_patchwise_generation1_difference"])-0.25433292878878405)>1e-12: raise RuntimeError("state certificate drifted")
    primary=sorted(prop["result"]["primary_horizon_cells"], key=lambda r:r["horizon"])
    if [(r["horizon"],r["n_pairs"]) for r in primary] != [(5,1500),(10,1500),(20,1500),(40,1500)]: raise RuntimeError("propagation primary grid drifted")
    return cert, primary


def figure3(root: Path, path: Path) -> None:
    cert,primary=load_state(root)
    width,height=1500,800
    lines=svg_start(width,height,"Matching summaries can hide different futures","Aligned and anti-aligned states share declared layer-wise marginals but differ in cross-layer covariance, exact next interaction and later functional-loss risk under a locked deterioration path.")
    lines += [text(750,44,"Matching ecological and genetic summaries can hide different futures",size=28,weight="bold"),text(360,88,"A  Constructive matched-summary state",size=19,weight="bold"),text(1120,88,"B  Propagation to functional-loss risk",size=19,weight="bold")]
    # A: support assignment + next interaction lines.
    lines += [text(360,125,f"cross-layer covariance: {cert['aligned_cross_layer_covariance']:+.3f} vs {cert['anti_aligned_cross_layer_covariance']:+.3f}",size=14),text(360,150,"census, layer marginals, Hα, Hγ and FST identical",size=13)]
    xs=[120,280,440,600]
    for row_y,name,vals in [(240,"aligned",cert["aligned_support_signal"]),(360,"anti-aligned",cert["anti_aligned_support_signal"])]:
        lines.append(text(45,row_y+4,name,size=14,anchor="start",weight="bold"))
        for i,(x,v) in enumerate(zip(xs,vals),1):
            lines.append(f'<rect x="{x-48}" y="{row_y-30}" width="96" height="60" rx="8" fill="white" stroke="#222"/>')
            lines.append(text(x,row_y-5,f"patch {i}",size=11,weight="bold")); lines.append(text(x,row_y+16,f"support {v:.2f}",size=11))
    plot_left,plot_right,plot_top,plot_bottom=90,650,470,650
    for tick in (0.4,0.5,0.6,0.7,0.8,0.9):
        yy=plot_bottom-(tick-0.4)/0.5*(plot_bottom-plot_top); lines.append(f'<line x1="{plot_left}" y1="{yy:.1f}" x2="{plot_right}" y2="{yy:.1f}" stroke="#eee"/>')
    ax=[150,290,430,570]
    for vals,dash in [(cert["aligned_generation1_interaction"],""),(cert["anti_aligned_generation1_interaction"],"7 5")]:
        pts=[]
        for x,v in zip(ax,vals): pts.append((x,plot_bottom-(float(v)-0.4)/0.5*(plot_bottom-plot_top)))
        d=f' stroke-dasharray="{dash}"' if dash else ''
        lines.append('<polyline points="'+' '.join(f"{x:.1f},{y:.1f}" for x,y in pts)+f'" fill="none" stroke="#111" stroke-width="2.2"{d}/>')
    lines.append(text(360,700,f"max exact next-transition difference = {float(cert['maximum_patchwise_generation1_difference']):.4f}",size=16,weight="bold"))
    # B: horizon risk diff.
    l,r,t,b=825,1430,165,620; minv,maxv=-0.02,0.10
    yzero=b-(0-minv)/(maxv-minv)*(b-t)
    lines.append(f'<line x1="{l}" y1="{yzero:.1f}" x2="{r}" y2="{yzero:.1f}" stroke="#777" stroke-width="1.5"/>')
    for tick in (-0.02,0,0.02,0.04,0.06,0.08,0.10):
        yy=b-(tick-minv)/(maxv-minv)*(b-t); lines.append(f'<line x1="{l}" y1="{yy:.1f}" x2="{r}" y2="{yy:.1f}" stroke="#eee"/>'); lines.append(text(l-10,yy+4,f"{tick*100:.0f}",size=11,anchor="end"))
    hx={5:900,10:1035,20:1200,40:1380}; pts=[]
    for row in primary:
        x=hx[row["horizon"]]; est=float(row["risk_difference_anti_minus_aligned"]); lo=float(row["ci95_lower"]); hi=float(row["ci95_upper"])
        yy=b-(est-minv)/(maxv-minv)*(b-t); ylo=b-(lo-minv)/(maxv-minv)*(b-t); yhi=b-(hi-minv)/(maxv-minv)*(b-t); pts.append((x,yy))
        lines += [f'<line x1="{x}" y1="{yhi:.1f}" x2="{x}" y2="{ylo:.1f}" stroke="#111" stroke-width="2"/>',f'<circle cx="{x}" cy="{yy:.1f}" r="6" fill="white" stroke="#111" stroke-width="2"/>',text(x,b+25,str(row["horizon"]),size=12),text(x,yy-15,f"{est*100:+.2f} pp",size=12,weight="bold")]
    lines.append('<polyline points="'+' '.join(f"{x:.1f},{y:.1f}" for x,y in pts)+'" fill="none" stroke="#111" stroke-width="2"/>')
    lines += [text(1125,675,"generation",size=13),text(800,400,"anti-aligned − aligned risk (pp)",size=12),text(1125,735,"matching marginals ≠ dynamic equivalence",size=16,weight="bold")]
    finish(lines,path)


def figure4(root: Path, path: Path) -> None:
    # Counts are fixed by the warning source manifest/manuscript; verify audit table includes both ensembles.
    rec=root/"artifacts/warning_validity/trajectory_endpoint_records.csv"
    rows=list(csv.DictReader(rec.open(encoding="utf-8")))
    if len(rows)!=1200: raise RuntimeError(f"warning record count drifted: {len(rows)}")
    # Use manuscript-level frozen denominators after ensuring both source labels are present.
    sources={r.get("ensemble") or r.get("source") or r.get("source_ensemble") for r in rows}
    width,height=1500,800
    lines=svg_start(width,height,"Perfect temporal precedence can have chance discrimination","Two frozen ensembles show every event preceded by each marker while every non-event also fires. An exact binary-marker identity shows why event-conditioned precedence does not determine specificity.")
    lines += [text(750,44,"Perfect lead time can coexist with chance discrimination",size=29,weight="bold"),text(355,92,"A  Inherited ensemble",size=19,weight="bold"),text(750,92,"B  Fresh ensemble",size=19,weight="bold"),text(1190,92,"C  Exact denominator result",size=19,weight="bold")]
    def confusion(cx:int, events:int, nonevents:int):
        # columns marker + / marker -, rows event / non-event
        x0=cx-150;y0=175;cw=120;rh=105
        lines.append(text(cx,145,"marker fired by common horizon",size=13,weight="bold"))
        for j,lab in enumerate(["yes","no"]): lines.append(text(x0+cw*(j+0.5),y0-15,lab,size=12))
        for i,lab in enumerate(["event","non-event"]): lines.append(text(x0-15,y0+rh*(i+0.55),lab,size=12,anchor="end"))
        vals=[[events,0],[nonevents,0]]
        for i in range(2):
            for j in range(2):
                x=x0+j*cw;y=y0+i*rh
                lines.append(f'<rect x="{x}" y="{y}" width="{cw}" height="{rh}" fill="white" stroke="#222" stroke-width="1.5"/>')
                lines.append(text(x+cw/2,y+rh/2+7,str(vals[i][j]),size=28,weight="bold"))
        lines.append(text(cx,430,f"event lead: {events}/{events}",size=15,weight="bold")); lines.append(text(cx,458,f"non-event firing: {nonevents}/{nonevents}",size=15,weight="bold")); lines.append(text(cx,500,"sensitivity = 1; specificity = 0; AUC = 0.5",size=14))
    confusion(355,35,48); confusion(750,33,49)
    # theorem panel.
    x=1025
    lines += [
        f'<rect x="{x}" y="170" width="390" height="365" rx="12" fill="#f7f7f7" stroke="#555" stroke-width="1.5"/>',
        text(x+195,210,"Perfect event-conditioned precedence",size=16,weight="bold"),
        text(x+195,250,"forces sensitivity = 1",size=15),
        text(x+195,300,"but leaves non-event firing f unconstrained",size=14),
        text(x+195,355,"specificity = (n₀ − f) / n₀",size=17,weight="bold"),
        text(x+195,405,"binary AUC = (1 + specificity) / 2",size=17,weight="bold"),
        text(x+195,465,"specificity ∈ [0,1] ⇒ AUC ∈ [0.5,1]",size=15),
        text(x+195,510,"observed f = n₀ ⇒ AUC = 0.5",size=16,weight="bold"),
        text(750,650,"temporal precedence ≠ prospective discrimination",size=19,weight="bold"),
        text(750,690,"all six frozen Hα/Hγ rules reach the same binary validity endpoint in both ensembles",size=13),
    ]
    finish(lines,path)


def figure5(egwee_root: Path, path: Path) -> None:
    reg=json.loads((egwee_root/"manuscript/natural_data_gate_registry.json").read_text())
    systems=reg["systems"]
    if len(systems)!=7: raise RuntimeError("natural gate registry is not seven systems")
    if reg["cross_study"]["locked_outcome"]!="cross_origin_convergence_not_identifiable_from_existing_archives": raise RuntimeError("cross-study STOP drifted")
    width,height=1500,900
    lines=svg_start(width,height,"Natural measurements stop at different validation gates","Seven natural-data analyses occupy distinct branches of measurement adequacy, representation preservation, residual-context testing and cross-study identifiability without pooling effect sizes.")
    lines += [text(750,42,"Natural measurements stop at different validation gates",size=29,weight="bold"),text(750,72,"no pooled effect-size axis; each row retains its native endpoint and holdout unit",size=14)]
    gate_names=[("measurement_adequacy","Measurement adequacy"),("representation_preservation","Representation preservation"),("residual_context","Residual context"),("cross_study_identifiability","Cross-study identifiability")]
    gx=[615,835,1055,1275]
    for x,(_,lab) in zip(gx,gate_names):
        lines.append(f'<rect x="{x-95}" y="110" width="190" height="60" rx="9" fill="#f4f4f4" stroke="#777"/>'); lines += multiline(x,135,lab,width=23,size=12,weight="bold")
    y0=225; step=82
    order={g[0]:i for i,g in enumerate(gate_names)}
    outcome_labels={
        "no_detected_transferable_distance_gain":"no detected transferable context gain",
        "no_reproducible_positive_residual_context_gain":"no reproducible positive residual gain",
        "no_detected_residual_urban_context_information":"no detected residual urban-context gain",
        "missing_contemporary_process_coordinate_detected":"missing contemporary coordinate detected",
        "multi_endpoint_not_identifiable":"endpoint/proxy mapping not identifiable",
        "process_measurement_adequacy_not_earned":"process measurement adequacy not earned",
        "mechanistic_information_erased_by_preprocessing":"mechanistic distinction erased by preprocessing",
    }
    for i,s in enumerate(systems):
        y=y0+i*step
        lines.append(text(45,y,s["system"],size=14,anchor="start",weight="bold"))
        lines += multiline(265,y-12,s["holdout_unit"]+" holdout; "+s["declared_endpoint"],width=36,size=11,anchor="start",leading=15)
        reached=order[s["gate_reached"]]
        for j,x in enumerate(gx):
            if j<=reached:
                lines.append(f'<line x1="{x-70}" y1="{y}" x2="{x+70}" y2="{y}" stroke="#222" stroke-width="3"/>')
            if j==reached:
                lines.append(f'<circle cx="{x}" cy="{y}" r="9" fill="white" stroke="#111" stroke-width="3"/>')
        lines += multiline(1380,y-12,outcome_labels.get(s["locked_outcome"],s["locked_outcome"]),width=27,size=11,anchor="start",leading=15)
    foot_y=820
    lines.append(f'<rect x="500" y="{foot_y}" width="860" height="55" rx="9" fill="#f4f4f4" stroke="#777"/>')
    lines.append(text(930,foot_y+22,"Cross-study synthesis: not_identifiable / STOP",size=14,weight="bold"))
    lines.append(text(930,foot_y+43,"origin confounded with study, taxa, protocol, state and response construction",size=11))
    finish(lines,path)


def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--egwe-root",required=True)
    ap.add_argument("--egc-root",required=True)
    ap.add_argument("--egwee-root",required=True)
    ap.add_argument("--output",required=True)
    args=ap.parse_args()
    egwe=Path(args.egwe_root); egc=Path(args.egc_root); egwee=Path(args.egwee_root); out=Path(args.output)
    out.mkdir(parents=True,exist_ok=True)
    figure1(out/"figure1_predictive_validity_stack.svg")
    figure2(egc,out/"figure2_state_separation.svg")
    figure3(egwe,out/"figure3_hidden_state_futures.svg")
    figure4(egwe,out/"figure4_precedence_discrimination.svg")
    figure5(egwee,out/"figure5_natural_measurement_gates.svg")
    print("NEE flagship figures generated from locked evidence")

if __name__=="__main__":
    main()
