from pathlib import Path
p=Path('scripts/build_nee_sorting_buffering_figures.py')
s=p.read_text(encoding='utf-8')
repls={
'"Sorting and buffering mechanism",':'"State separation and operator balance under fragmentation",',
'"State separation, q-dependent allele sorting, buffering and warning discrimination.",':'"State separation, hidden cross-layer organization, q-dependent allele sorting, buffering, recoupling, density gating and fate discrimination.",',
't(750, 665, "Natural systems enter only as ecological projections of limited buffering, recoupling or memory.", 13),':'t(750, 665, "Natural systems test state separation; operator-level causation remains finite-model evidence.", 13),',
}
for old,new in repls.items():
    if s.count(old)!=1:
        raise AssertionError((old,s.count(old)))
    s=s.replace(old,new,1)
p.write_text(s,encoding='utf-8')
