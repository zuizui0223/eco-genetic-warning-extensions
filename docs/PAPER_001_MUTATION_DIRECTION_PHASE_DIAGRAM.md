# Paper 001 — mutation direction and the reliability of eco-genetic warning

## Working thesis

**Directional recurrent mutation can reshape the persistence boundary of a high-trait state and the reliability of genetic early warning, even when the mutation operator has the same relaxation strength.**

This paper is an independent finite-model study. It does not seek to complete,
broaden, or re-estimate the canonical H1--H3 campaign in
`eco-genetic-criticality`.

## Paper-level question

At fixed mutation relaxation strength, how does the directional equilibrium of a
recurrent mutation operator alter:

1. the feasibility of a high-trait source state;
2. the probability and timing of realised high-trait loss under deterioration;
3. the availability, lead/lag ordering, and usable lead time of relative genetic
   diversity warnings?

## New mechanism

Let \(p\) be the high-trait-associated allele frequency. Write the mutation
operator as

\[
M_{\kappa_\mu,p_\mu^\ast}(p)
 = \kappa_\mu p_\mu^\ast+(1-\kappa_\mu)p,
\]

where

\[
\kappa_\mu=u_{L\to H}+u_{H\to L},\qquad
p_\mu^\ast=\frac{u_{L\to H}}{u_{L\to H}+u_{H\to L}}.
\]

For \(\kappa_\mu>0\), \(p_\mu^\ast\) is the mutation-only equilibrium and
\(1-\kappa_\mu\) is the operator's contraction factor. Holding
\(\kappa_\mu\) fixed therefore holds the **relaxation strength** fixed while
changing directionality through \(p_\mu^\ast\).

This does **not** hold the instantaneous expected mutation flux fixed:

\[
J(p)=u_{L\to H}(1-p)+u_{H\to L}p.
\]

That difference is part of the biological mechanism under test, not a nuisance to
be hidden.

## Mechanistic prediction

If a local high-state condition needs post-mutation frequency \(M(p)\ge p_c\),
then for \(0\le\kappa_\mu<1\),

\[
p\ge \theta(p_c;\kappa_\mu,p_\mu^\ast)
=\frac{p_c-\kappa_\mu p_\mu^\ast}{1-\kappa_\mu}.
\]

Thus increasing \(p_\mu^\ast\) decreases the mutation-prestate frequency
required to cross the local high-state boundary. This is an algebraic
mechanism-level prediction only; whether it controls the full stochastic system
is the empirical question of Paper 001.

## Primary hypotheses

### H-MD-1 — persistence boundary

At fixed \(\kappa_\mu\), increasing \(p_\mu^\ast\) shifts the region in which
an H1-prepared high state can be established and retained under the declared
finite closure.

### H-MD-2 — realised trait-loss hazard

At fixed \(\kappa_\mu\), mutation direction changes the distribution of
\(\tau_T\), the realised high-trait-loss first-passage time, including the
probability of right censoring within a fixed horizon.

### H-MD-3 — warning reliability

For each declared \((\kappa_\mu,p_\mu^\ast)\) coordinate with a calibration-
selected deterioration domain, relative-diversity warnings have a measurable
lead/lag/censoring profile before realised trait loss:

\[
\tau_{\Delta H_x(r)}\;\lessgtr\;\tau_T,
\qquad x\in\{\alpha,\gamma\},\quad r\in\{0.05,0.10,0.20\}.
\]

No uniform sign is presumed. H2-R-AS is a special directional-closure hypothesis,
not the paper's predetermined conclusion.

## Independence audit

Paper 001 is independent of `eco-genetic-criticality` only if all conditions
below are met.

- Its principal question is mutation direction, not whether the former H2-R
  result is robust.
- Its main evidence is new: new source reconstruction, new calibration, new
  fresh validation seeds, and new phase-diagram outputs.
- The former symmetric closure appears only as a regression/bridge control.
- Results are presented across a predeclared coordinate map, not only at the
  predecessor's selected cell or schedule.
- The manuscript cites the predecessor as prior work and states that prior
  numerical results are not evidence for Paper 001.
- No old trajectory, selected domain, or conclusion is reused as a primary result.

## Manuscript architecture

1. **Introduction:** mutation direction as a boundary condition for eco-genetic
   warning, not a generic robustness exercise.
2. **Model:** the \((\kappa_\mu,p_\mu^\ast)\) mutation-coordinate system and
   its relationship to stochastic trait recruitment.
3. **Protocol:** phase-diagram design, source/calibration/validation separation,
   censoring rules, and preregistered decision metrics.
4. **Results I:** source feasibility and high-state persistence map.
5. **Results II:** trait-loss probability and first-passage-time map.
6. **Results III:** warning availability, lead/lag, usable lead time, and fixed
   threshold audit.
7. **Discussion:** when directional mutation changes warning use, and why no
   result is a universal biological law.

## Minimum figures

- **Figure 1:** mutation-coordinate geometry and local threshold prediction.
- **Figure 2:** H1 source feasibility/persistence phase map.
- **Figure 3:** trait-loss event and censoring map.
- **Figure 4:** relative-warning reliability and usable-lead-time map.
- **Figure 5:** mechanism decomposition: allele trajectory, interaction state,
  realised trait occupancy, and diversity for representative predeclared cells.

## Publication gate

The work is publishable as an independent modelling paper only if the main
campaign reveals a structured directional effect on at least one of: source
feasibility, trait-loss hazard, warning availability, lead/lag ordering, or usable
lead time. If all phase-map outcomes are indistinguishable after uncertainty is
reported, the outcome is a bounded null/result note rather than a separate major
paper.