from pathlib import Path

p = Path('manuscript/nee_flagship_article.md')
s = p.read_text(encoding='utf-8')
repls = {
"Together these results replace an unexplained branch diagram with an explicit causal architecture. Cross-layer covariance first creates transition-relevant heterogeneity. q-dependent allele selection sorts compatible eco-genetic state into favourable local environments. Recruitment contracts trait–allele mismatch. Direct feedback recouples interaction state toward the local trait/genetic bundle. Density feedback determines whether declining demography is amplified into system-wide loss. Long-horizon fate is the net result of these operators rather than a monotone function of alignment.":
"Together these results resolve the second step of the argument: **same marginals do not imply the same future because hidden local organization is transformed by operators with opposing roles**. Cross-layer covariance creates transition-relevant heterogeneity; q-dependent allele selection sorts compatible eco-genetic state; recruitment and direct feedback repair different mismatches; and density feedback determines whether local deterioration becomes self-amplifying. Long-horizon fate is therefore the net result of operator balance rather than a monotone function of alignment.",
"The monitoring conclusion is therefore asymmetric rather than uniformly negative: **marginal erosion reports stress, whereas continuous last-refuge reserve carries fate information in this finite closure**. The result also localizes where that information resides. System-wide averages discard part of the relevant organization; risk is better ordered by how much functional reserve remains in the strongest local patch after interaction, density, trait and allele state are jointly accounted for.":
"The monitoring conclusion is therefore asymmetric rather than uniformly negative: **transition-exactness is not fate information, and marginal erosion can report stress without discriminating fate**. The continuous last-refuge reserve succeeds because it retains the depth of the strongest remaining local functional margin rather than thresholding that margin or averaging it away. In this finite closure, risk is therefore better ordered by remaining local reserve than by marginal erosion alone.",
"The natural and finite results therefore carry different inferential loads. EGWEE supplies the portable empirical result that fragmentation responses are not generally exchangeable across biological layers; it does not validate the model's sorting, buffering, recoupling or density operators.":
"The natural and finite results therefore carry different inferential loads. In the currently admitted three-system Hedges-g corpus, EGWEE rejects layer exchangeability, but that rejection is sensitive to the influential *Serapias* cluster; the separate *Eucalyptus* gradient supplies additional state-separation evidence on a different effect scale. These natural results support the need to distinguish biological layers, but they do not validate the model's sorting, buffering, recoupling or density operators."
}
for old,new in repls.items():
    n=s.count(old)
    if n != 1:
        raise AssertionError(f'expected one match, got {n}: {old[:80]}')
    s=s.replace(old,new,1)
p.write_text(s,encoding='utf-8')
