"""Conceptual Figure 1 for the condition-recovered manuscript."""
from __future__ import annotations

import html


def figure1_estimability_svg() -> str:
    width, height = 1280, 620
    title = "Eco-genetic causal architecture and four-question hierarchy"
    desc = (
        "Four linked questions: interaction-dependent function and fragmentation, conditional genetic warning, "
        "warning-blind event-regime estimability, and warning portability. Functional state, genetic diversity, "
        "population persistence, and warning performance are represented as distinct quantities."
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
        (45, 105, 255, 145, "Q1", "Functional state", "interaction support", "→ fragmentation loss"),
        (350, 105, 255, 145, "Q2", "Genetic precursor", "relative diversity erosion", "can precede loss"),
        (655, 105, 275, 145, "Q3", "Event-regime estimability", "source → loss regime", "R1/R2/R3/R4"),
        (980, 105, 255, 145, "Q4", "Warning portability", "availability / ordering", "across calibrated regimes"),
    ]
    for x, y, w, h, q, line1, line2, line3 in boxes:
        parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="#f9fafb" stroke="#111" stroke-width="2"/>')
        parts.append(f'<text x="{x+18}" y="{y+27}" font-family="sans-serif" font-size="14" font-weight="bold">{q}</text>')
        parts.append(f'<text x="{x+w/2}" y="{y+60}" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="bold">{html.escape(line1)}</text>')
        parts.append(f'<text x="{x+w/2}" y="{y+88}" text-anchor="middle" font-family="sans-serif" font-size="13">{html.escape(line2)}</text>')
        parts.append(f'<text x="{x+w/2}" y="{y+113}" text-anchor="middle" font-family="sans-serif" font-size="13">{html.escape(line3)}</text>')
    for x1, x2 in ((300,350),(605,655),(930,980)):
        parts.append(f'<line x1="{x1}" y1="177" x2="{x2}" y2="177" stroke="#111" stroke-width="2.5" marker-end="url(#a)"/>')

    parts += [
        '<text x="55" y="315" font-family="sans-serif" font-size="14" font-weight="bold">Distinct biological quantities retained by the model</text>',
        '<rect x="55" y="340" width="200" height="64" rx="9" fill="white" stroke="#4b5563"/><text x="155" y="378" text-anchor="middle" font-family="sans-serif" font-size="14">Population persistence</text>',
        '<rect x="305" y="340" width="200" height="64" rx="9" fill="white" stroke="#4b5563"/><text x="405" y="378" text-anchor="middle" font-family="sans-serif" font-size="14">Interaction state</text>',
        '<rect x="555" y="340" width="200" height="64" rx="9" fill="white" stroke="#4b5563"/><text x="655" y="378" text-anchor="middle" font-family="sans-serif" font-size="14">Realised function</text>',
        '<rect x="805" y="340" width="200" height="64" rx="9" fill="white" stroke="#4b5563"/><text x="905" y="378" text-anchor="middle" font-family="sans-serif" font-size="14">Genetic diversity</text>',
        '<rect x="1055" y="340" width="170" height="64" rx="9" fill="white" stroke="#4b5563"/><text x="1140" y="378" text-anchor="middle" font-family="sans-serif" font-size="14">Warning timing</text>',
        '<text x="640" y="460" text-anchor="middle" font-family="sans-serif" font-size="15" font-weight="bold">Condition-recovery rule</text>',
        '<rect x="225" y="482" width="830" height="72" rx="10" fill="#f3f4f6" stroke="#111" stroke-width="1.5"/>',
        '<text x="640" y="512" text-anchor="middle" font-family="sans-serif" font-size="14">Map source feasibility and functional-loss reproducibility without warning/diversity fields.</text>',
        '<text x="640" y="537" text-anchor="middle" font-family="sans-serif" font-size="14">Freeze an evaluable event regime first; only then interpret warning availability, ordering, or timing.</text>',
        '<text x="640" y="592" text-anchor="middle" font-family="sans-serif" font-size="12">R4 is an operational reproducible intermediate-risk event regime, not a universal ecological threshold and not evidence of warning success.</text>',
        '</svg>',
    ]
    return "\n".join(parts) + "\n"
