# Reproducibility guide

This repository is the **independent condition-recovery extension and submission orchestrator** for the eco-genetic warning study. It depends on a fixed scientific state of [`eco-genetic-criticality`](https://github.com/zuizui0223/eco-genetic-criticality), but does not rewrite or retroactively enlarge the parent evidence ledger.

After Phase J, historical R1/R2/R3/R4 labels are interpreted as **finite-panel calibration labels under a declared sampling design**. The primary biological object is the distribution of functional-loss events across stochastic blocks.

## Repository roles

| repository | role | scientific boundary |
|---|---|---|
| `eco-genetic-criticality` | mechanistic parent | theorem-guided interaction/fragmentation framework, locked H1/H3 campaign, inherited symmetric warning benchmark |
| `eco-genetic-warning-extensions` | condition-recovery extension | recurrent-transition source/loss evidence, connectivity and interaction processes, explicit rewiring, pollen movement, sampling-stability audit, bounded warning portability, manuscript/bundle |

The parent scientific commit is fixed at `dd8ee379d0d3518194c767d16402042525bc00dc`; the machine-readable parent lock is `reproducibility/upstream-lock.json`.

## Reproduction levels

### Level 1 — package and invariant tests

```bash
git clone https://github.com/zuizui0223/eco-genetic-warning-extensions.git
git clone https://github.com/zuizui0223/eco-genetic-criticality.git upstream
git -C upstream checkout dd8ee379d0d3518194c767d16402042525bc00dc

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -e upstream
python -m pip install -e '.[dev,reproducibility]'
python -m pytest
python scripts/verify_reproducibility_contract.py --upstream upstream
```

This verifies package imports, scientific locks, warning-blind protocol invariants, manuscript contracts, Stage III totals, Phase E–J interpretation boundaries, exact pollen-operator identity and Phase-J classifier-design utilities.

### Level 2 — rebuild the publication package from locked evidence

The canonical publication build uses immutable/committed compact evidence to regenerate figures, secondary Stage-III trajectory audits, software distributions and submission bundles. Historical source artifacts remain immutable; later audits may change the interpretation of a categorical label without changing the original observation.

### Level 3 — reproduce warning-blind ecological/methodological campaigns

The major campaigns are independently reproducible and must never be tuned after observing warning outcomes:

- common recurrent-transition source/loss map and prospective frontier recovery;
- Phase E allele-frequency connectivity;
- Phase F aggregate interaction support;
- Phase G matched one-partner loss;
- Phase H explicit trait/capacity-constrained rewiring;
- Phase I process-resolved pollen-mediated gene flow;
- Phase J fixed-condition classification-stability audit.

A rerun with new seeds creates a **new finite Type S ensemble**. It does not overwrite a locked earlier ensemble.

## Locked Phase E–J evidence

### Phase E — allele-frequency connectivity

Run `32376912392`; artifact `9409687687`; committed `artifacts/migration_condition/phase_e_summary.json`.

The locked five-seed campaign observed finite labels R4/R4/R4/R3/R3 at `m=0/.025/.05/.10/.20`, with bidirectional paired loss-status switches. After Phase I/J, the exact `m=.10` R3 label is **not interpreted as a portable biological boundary**. The robust result is the bidirectional reshuffling of loss histories.

### Phase F — aggregate interaction support

Run `32441549848`; artifact `9432854668`; digest `sha256:bb221af16a9b6557280610e90807fdfe058dccbafd7d0183e38d4525ecef2c16`.

| kappa | source/baseline eligible | pooled loss | finite label |
|---:|---:|---:|---|
| 3.0 | 77/100 | .468 | R4 |
| 4.5 | 94/100 | .521 | R4 |
| 6.0 | 87/100 | .552 | R4 |

All 15 seed-block rates in the campaign were inside `[.30,.70]`. Phase F is closed; no finer/wider kappa search is opened.

### Phase G — reduced-form matched one-partner loss

Run `32450362310`; artifact `9435520830`; digest `sha256:669cfc468f8a36e53ccc157aaa97e5a4de14f6ad7c09458ed105762e4d0d6ec7`.

| condition | eligible | pooled loss | seed-rate range | finite label |
|---|---:|---:|---:|---|
| intact | 90/100 | .544 | .129 | R4 |
| even loss | 90/100 | .567 | .261 | R3 |
| graded loss | 90/100 | .556 | .353 | R3 |
| dominant loss | 90/100 | .578 | .235 | R3 |

Cochran Q `p=.943` in a labelled secondary incidence audit. The locked interpretation is mean-risk/reproducibility separation, not a universal partner-loss effect or contribution-concentration gradient.

### Phase H — explicit rewiring

Preregistered head `611cf4e884e7d125465bf0fd16884d95424bd389`; run `32453377127`; artifact `9436467391`; digest `sha256:3b26257527e6c1c22fa33cbcdf19ddf7d381c3df55c857f2c6f2f8f1acc50a85`.

Opening rule succeeded: fresh intact R4, matched partner-loss/no-rewiring R3. The one fixed rewiring rule remained R3 (`not_rescued`).

| diagnostic | no rewiring | constrained rewiring |
|---|---:|---:|
| eligible | 86/100 | 86/100 |
| pooled loss | .430 | .419 |
| active edges | 3 | 5 |
| realised connectance | .500 | .833 |
| final support multiplier | .750 | .844 |

Thus network/connectance/support recovery occurred without downstream functional-loss distribution recovery. Phase H is closed; rewiring parameters are not tuned to force a rescue.

### Phase I — process-resolved pollen movement

Preregistered head `3779464947e29fd85fdab106117e7ece296bbdf9`; run `32454142670`; artifact `9436762723`; digest `sha256:9a5ef1f86d040ecc9f12a92c2250cde2c6ec3fb6a24a0783f12cae2dbc3aab72`.

Under the declared diploid paternal-gene-flow closure,

`p_off=(1-g/2)p_local+(g/2)p_pool`.

For a census-weighted regional pollen pool this is exactly legacy global allele mixing `m=g/2`. At `g=.20`, regional pollen was snapshot-exact with legacy `m=.10` for **90/90** completed pairs.

| condition | eligible | pooled loss | finite label |
|---|---:|---:|---|
| no pollen | 90/100 | .511 | R4 |
| regional pollen `g=.20` | 90/100 | .500 | R4 |
| legacy mixing `m=.10` | 90/100 | .500 | R4 |
| ring pollen `g=.20` | 90/100 | .511 | R4 |

Regional→ring pollen switched 7 loss→no-loss and 8 no-loss→loss trajectories. Phase I is closed; no additional `g` or kernel search is opened merely to create a categorical difference.

### Phase J — fixed-condition classification stability

Preregistered head `b5077b182ac881e7d49e65f2165485d55955fd45`; run `32454874360`; artifact `9437232755`; digest `sha256:65b97aebb5c14cf15dee3ecf974f5f297a67bebbf8ae564f68018d9cb13bfe50`.

The complete `m=.10` biological condition was fixed. Twenty new master-seed blocks were prospectively divided into four non-overlapping five-seed panels. Result: **R4 / R3 / R4 / R4**, hence `ensemble_sensitive`.

Across the 20 blocks:

- 19/20 inside `[.30,.70]`;
- 1/20 above (`.75`);
- total eligible/loss 342/180;
- pooled loss `.5263`;
- unweighted mean block loss `.5247`;
- median `.5132`;
- sample SD `.1182`.

All possible five-block subsets of those 20 rates give:

- `C(20,5)=15,504` panels;
- 11,628 = **75%** R4 finite certificates;
- 3,876 = **25%** R3 finite certificates.

The exact classifier-design identity is `P(all B blocks pass)=q^B` under independent exchangeable blocks with single-block pass probability `q`. Thus the historical all-block certificate is mechanically panel-size dependent for `0<q<1`.

Committed evidence:

- `artifacts/classification_stability/phase_j_summary.json`;
- `artifacts/classification_stability/phase_j_distributional_profile.json`;
- `src/eco_genetic_warning_extensions/classification_gate_theory.py`;
- `docs/CLASSIFICATION_STABILITY_RESULT.md`.

**Phase J is closed.** Seeds are not added/regrouped and the operational band is not tuned after this result.

## Distributional interpretation now required

Reproduction and future analyses must separate:

1. **central event incidence** — pooled and/or block-level location of the functional-loss distribution;
2. **among-block heterogeneity / tails** — variability across independently generated stochastic blocks;
3. **finite-panel certificate** — a declared sampling-design rule used only to decide whether a particular warning-validation panel is operationally suitable.

Historical R4 labels remain valid finite facts. They are not sample-size-invariant biological phase labels after Phase J.

## Other locked evidence

- parent scientific commit `dd8ee379d0d3518194c767d16402042525bc00dc`;
- inherited H1/H3 primary campaign: run `28456092898`, artifact `7987193632`;
- fresh fragmentation gradient: run `31937210601`, artifact `9261157020`;
- common source reconstruction: 3,375 attempts;
- common strict loss calibration: 20,250 attempts, 648 complete candidates, historical 15/15 `no_domain_selected`;
- historical Protocol 003 validation: run `29417632137`, 200 attempted trajectories;
- symmetric Stage-III artifact `8343958766`, digest `sha256:c1b42fc9e6ac912a44667ef4cee02090fab37d50fc3a9928c46ae728c0610f58`;
- directional Stage-III artifact `8343922879`, digest `sha256:0a994bea874fc9c47544169cd31bbc317c88690dfe1b6fa7548516e35fd7bca8`.

Exact provenance and claim boundaries are recorded in `manuscript/artifact_index.md` and `manuscript/claim_evidence_map.md`.

## Interpretation safeguards

Reproduction must preserve all of the following:

- parent and extension trajectories are separate evidence;
- historical Protocol 002 remains 15/15 `no_domain_selected` under its original all-block rule;
- later finite R4 certificates do not establish warning success or a sample-size-invariant biological regime;
- Phase E `migration_rate` is allele-frequency mixing, and the Phase-E `m=.10` categorical label is not portable across independent ensembles;
- Phase F `interaction kappa` is aggregate feedback, not partner richness/connectance/network simplification;
- Phase G is reduced-form partner loss, not an explicit network model;
- Phase H does not establish rewiring is generally ineffective; connectance/support recovery is not equivalent to functional-loss recovery;
- Phase I's regional `g↔m/2` identity is narrow to the declared pollen closure and does not make legacy `migration_rate` generic pollen dispersal;
- Phase J's ensemble-sensitive result must not be erased by seed addition/regrouping or threshold tuning;
- Stage III domains are non-matched; their contrast is bounded portability, not a direction-only effect;
- endpoint rows from one trajectory are correlated; secondary intervals resample whole trajectories;
- finite-horizon non-events remain censored;
- `p_star` is an effective recurrent-transition equilibrium, not an empirical mutation rate;
- a successful build does not convert finite Type S results into universal ecological theorems.

## Archival release checklist

Before final repository deposition:

1. merge stacked validation PRs in dependency order only after their scientific/result contracts pass;
2. rerun the publication build from the integrated branch/main;
3. independently verify checksummed bundles and locked Phase E–J summaries;
4. render the six main figures and supplements at final journal width;
5. use the single `manuscript/main_text.md` source and current distributional interpretation;
6. create immutable releases for both repositories;
7. archive release pair and bundle in Zenodo or equivalent;
8. add final DOI, author-approved metadata, licence and CRediT statements.

Authorship, licence, funding, conflicts and CRediT roles remain explicit author decisions.
