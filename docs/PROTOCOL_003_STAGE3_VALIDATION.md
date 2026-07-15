# Protocol 003 Stage III validation

Two confirmation-eligible domains are frozen before warning outcomes are inspected:

1. symmetric bridge: `kappa_mu=0.20`, `p_star=0.50`, hold 210, normalized barrier increase 0.20;
2. transition: `kappa_mu=0.05`, `p_star=0.90`, hold 90, normalized barrier increase 0.10.

Validation uses fresh master seeds `20270710`–`20270714` and 20 replicates per seed, for 100 trajectories per domain and 200 total trajectories.

For every completed trajectory, six baseline-relative endpoints are reported:

- `H_alpha`: 5%, 10%, and 20% decline;
- `H_gamma`: 5%, 10%, and 20% decline.

Each endpoint is classified as lead, tie, lag, warning-censored, trait-loss-censored, both-censored, or baseline-ineligible. Missing events remain censored. Generation zero is excluded from warning crossings. Results are finite Type S evidence and do not modify the parent theorem layer.
