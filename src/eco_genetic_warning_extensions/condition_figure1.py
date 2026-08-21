"""Conceptual Figure 1 for the condition-first manuscript."""
from __future__ import annotations

import html


def figure1_estimability_svg() -> str:
    width, height = 1280, 620
    title = "Eco-genetic causal architecture and four-question hierarchy"
    desc = (
        "Four linked questions in causal order: whether an interaction-dependent functional state can exist and be disrupted by fragmentation, "
        "which eco-genetic conditions make functional loss reproducible, whether genetic erosion can then precede functional loss, "
        "and whether warning behaviour is portable across calibrated regimes. Functional state, genetic connectivity, genetic diversity, "
        "population persistence, and warning performance remain distinct quantities."
    )
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="figure1-title figure1-desc">',
        f'<title id="figure1-title">{html.escape(title)}</title>',
        f'<desc id="figure1-desc">{html.escape(desc)}</desc>',
        '<rect width="100%" height="100%" fill="white"/>',
        f'<text x="{width/2}" y="42" text-anchor="middle" font-family="sans-serif" font-size="24" font-weight="bold">{html.escape(title)}</text>',
        '<defs><marker id="a" markerWidth="9" markerHeight="9" refX="7.5" refY="4.5" orient="auto"><path d="M0,0 L0,9 L8,4.5 z" fill="#111"/></marker></defs>',
    ]
    boxes = [
        (35, 105, 270, 155, "Q1", "Functional fragmentation", "high-function state exists", "→ fragmentation vulnerability"),
        (340, 105, 285, 155, "Q2", "Loss-regime conditions", "turnover · connectivity · interaction support", "R1/R2/R3/R4 regimes"),
        (660, 105, 275, 155, "Q3", "Conditional warning", "relative genetic erosion", "can precede loss"),
        (970, 105, 275, 155, "Q4", "Warning portability", "availability / ordering", "across calibrated regimes"),
    ]
    for x, y, w, h, q, line1, line2, line3 in boxes:
        parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="#f9fafb" stroke="#111" stroke-width="2"/>')
        parts.append(f'<text x="{x+18}" y="{y+27}" font-family="sans-serif" font-size="14" font-weight="bold">{q}</text>')
        parts.append(f'<text x="{x+w/2}" y="{y+61}" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="bold">{html.escape(line1)}</text>')
        parts.append(f'<text x="{x+w/2}" y="{y+92}" text-anchor="middle" font-family="sans-serif" font-size="12">{html.escape(line2)}</text>')
        parts.append(f'<text x="{x+w/2}" y="{y+119}" text-anchor="middle" font-family="sans-serif" font-size="13">{html.escape(line3)}</text>')
    for x1, x2 in ((305, 340), (625, 660), (935, 970)):
        parts.append(f'<line x1="{x1}" y1="182" x2="{x2}" y2="182" stroke="#111" stroke-width="2.5" marker-end="url(#a)"/>')

    parts += [
        '<text x="55" y="320" font-family="sans-serif" font-size="14" font-weight="bold">Distinct biological quantities retained by the model</text>',
        '<rect x="55" y="345" width="190" height="64" rx="9" fill="white" stroke="#4b5563"/><text x="150" y="383" text-anchor="middle" font-family="sans-serif" font-size="14">Population persistence</text>',
        '<rect x="265" y="345" width="190" height="64" rx="9" fill="white" stroke="#4b5563"/><text x="360" y="383" text-anchor="middle" font-family="sans-serif" font-size="14">Interaction state</text>',
        '<rect x="475" y="345" width="190" height="64" rx="9" fill="white" stroke="#4b5563"/><text x="570" y="383" text-anchor="middle" font-family="sans-serif" font-size="14">Realised function</text>',
        '<rect x="685" y="345" width="190" height="64" rx="9" fill="white" stroke="#4b5563"/><text x="780" y="383" text-anchor="middle" font-family="sans-serif" font-size="14">Genetic connectivity</text>',
        '<rect x="895" y="345" width="165" height="64" rx="9" fill="white" stroke="#4b5563"/><text x="977.5" y="383" text-anchor="middle" font-family="sans-serif" font-size="14">Genetic diversity</text>',
        '<rect x="1080" y="345" width="145" height="64" rx="9" fill="white" stroke="#4b5563"/><text x="1152.5" y="383" text-anchor="middle" font-family="sans-serif" font-size="14">Warning timing</text>',
        '<text x="640" y="463" text-anchor="middle" font-family="sans-serif" font-size="15" font-weight="bold">Condition-recovery rule</text>',
        '<rect x="205" y="485" width="870" height="72" rx="10" fill="#f3f4f6" stroke="#111" stroke-width="1.5"/>',
        '<text x="640" y="515" text-anchor="middle" font-family="sans-serif" font-size="14">Establish functional-state feasibility and map functional-loss reproducibility without warning/diversity fields.</text>',
        '<text x="640" y="540" text-anchor="middle" font-family="sans-serif" font-size="14">Only after an evaluable loss regime is fixed should warning availability, ordering, or timing be interpreted.</text>',
        '<text x="640" y="595" text-anchor="middle" font-family="sans-serif" font-size="12">R4 is an operational reproducible intermediate-risk event regime, not a universal ecological threshold and not evidence of warning success.</text>',
        '</svg>',
    ]
    return "\n".join(parts) + "\n"
