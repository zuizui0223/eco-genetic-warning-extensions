from pathlib import Path

p = Path('manuscript/nee_flagship_article.md')
s = p.read_text(encoding='utf-8')
repls = {
"Together these results replace an unexplained branch diagram with an explicit causal architecture. Cross-layer covariance first creates transition-relevant heterogeneity. q-dependent allele selection sorts compatible eco-genetic state into favourable local environments. Recruitment contracts trait–allele mismatch. Direct feedback recouples interaction state toward the local trait/genetic bundle. Density feedback determines whether declining demography is amplified into system-wide loss. Long-horizon fate is the net result of these operators rather than a monotone function of alignment.":
"Together these results resolve the causal chain behind the matched-marginal counterexample. **Same marginals do not imply the same future because hidden local organization is transformed by opposing operators**: covariance creates heterogeneity, selection sorts it, recruitment and feedback repair mismatches, and density feedback can amplify deterioration into collapse. Fate therefore reflects operator balance rather than alignment alone.",
"The monitoring conclusion is therefore asymmetric rather than uniformly negative: **marginal erosion reports stress, whereas continuous last-refuge reserve carries fate information in this finite closure**. The result also localizes where that information resides. System-wide averages discard part of the relevant organization; risk is better ordered by how much functional reserve remains in the strongest local patch after interaction, density, trait and allele state are jointly accounted for.":
"The monitoring result adds a third distinction: **transition-exactness is not fate information**. Marginal erosion can report stress without discriminating fate, and thresholding an exact transition margin can discard reserve depth. In this finite closure, the continuous strongest-refuge margin retains that depth and therefore ranks later fate better than marginal erosion alone.",
"The natural and finite results therefore carry different inferential loads. EGWEE supplies the portable empirical result that fragmentation responses are not generally exchangeable across biological layers; it does not validate the model's sorting, buffering, recoupling or density operators.":
"The natural and finite results carry different inferential loads. The admitted three-system corpus rejects layer exchangeability, but the result is *Serapias*-sensitive; separate *Eucalyptus* gradient evidence supports state separation on another effect scale. Natural evidence therefore motivates multidimensional state representation, not the finite sorting, buffering, recoupling or density operators."
}
for old,new in repls.items():
    n=s.count(old)
    if n != 1:
        raise AssertionError(f'expected one match, got {n}: {old[:80]}')
    s=s.replace(old,new,1)
p.write_text(s,encoding='utf-8')
