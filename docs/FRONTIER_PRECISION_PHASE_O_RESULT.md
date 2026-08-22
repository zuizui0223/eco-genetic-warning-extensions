# Phase O result — high-precision Phase-D frontier replay

Phase O reproduced all 15 historical first-20 seed×`p_star` prefixes and then expanded every locked Phase-D seed block to 100 attempted replicates.

## Result

- `p_star=0.325`: pooled loss `0.6823`; historical screen `R3_highrep`; equal-rate diagnostic `p=0.2948`.
- `p_star=0.350`: pooled loss `0.5465`; `R4_highrep`; equal-rate diagnostic `p=0.3705`.
- `p_star=0.375`: pooled loss `0.4074`; `R4_highrep`; equal-rate diagnostic `p=0.6934`.

The earlier statement that the recovered R4 window is immediately bounded on both sides by R3 is therefore rejected. The lower neighbour remains outside the historical screen because loss incidence approaches the upper edge, while the upper neighbour is R4 at high precision. None of the three conditions shows detectable excess between-block heterogeneity.

The defensible conclusion is an **asymmetric incidence frontier**, not a narrow two-sided seed-heterogeneity frontier.

Provenance: workflow `32558742101`; artifact `9472838181`; digest `sha256:4b39d7df5d60b08bef0f78eb59524510c5549bae9199064f5a9841164db9a610`.
