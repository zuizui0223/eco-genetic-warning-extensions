from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTICLE = ROOT / "manuscript/nee_flagship_article.md"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    n = text.count(old)
    if n != 1:
        raise AssertionError(f"{label}: expected one match, got {n}")
    return text.replace(old, new, 1)


def main() -> None:
    text = ARTICLE.read_text(encoding="utf-8")

    old1 = (
        "The first prospective mechanism experiment crossed trait assignment and allele assignment under full feedback. Trait–allele mismatched states had functional-loss risk **6.23 points** above matched states at generation 20 and **4.70 points** above them at generation 40, but the directional AA-versus-RR contrast itself was not stable. Removing direct trait/allele input into q exposed an indirect AA advantage, and a fresh edge-decomposition experiment reproduced that q-only contrast at **+4.20 points** at generation 20 and **+4.40 points** at generation 40. We then decomposed the responsible operators."
    )
    new1 = (
        "The first prospective mechanism experiment crossed trait assignment and allele assignment under full feedback. Trait–allele mismatched states had functional-loss risk **6.23 points** above matched states at generation 20 and **4.70 points** above them at generation 40, but the directional AA-versus-RR contrast itself was not stable. Removing direct trait/allele input into q exposed an indirect AA advantage, and a fresh edge-decomposition experiment reproduced that q-only contrast at **+4.20 points** at generation 20 and **+4.40 points** at generation 40. We therefore treated the matched-marginal counterexample as the start of a process chain rather than an endpoint effect: sorting can create local eco-genetic compatibility differences, recruitment and direct feedback can modify that coherence, and density feedback can convert depleted local headroom into collapse. We decomposed those operators in turn."
    )
    text = replace_once(text, old1, new1, "operator-chain bridge")

    old2 = (
        "Its sign exactly determines whether the next interaction state lies above or below `q*=0.625`, and the canonical prospective audit found **0 mismatches across 1,920,000 patch-generations**."
    )
    new2 = (
        "Its sign exactly determines whether the next interaction state lies above or below `q*=0.625`, and the canonical prospective audit found **0 mismatches across 1,920,000 patch-generations**. This margin therefore compresses the competing sorting, buffering, recoupling and density terms into a single transition coordinate without replacing their distinct causal roles. Taking its maximum across patches asks whether any local refuge still has positive one-step functional reserve; that is the mechanistic bridge from operator decomposition to fate prediction."
    )
    text = replace_once(text, old2, new2, "route-margin bridge")

    ARTICLE.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
