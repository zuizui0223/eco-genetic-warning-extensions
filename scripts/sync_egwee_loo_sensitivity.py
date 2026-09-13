from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
EGWEE_COMMIT = "74d5336242bfaa4ccbbf54f0343c8d058c161d79"


def replace_once(path: Path, old: str, new: str, label: str) -> None:
    text = path.read_text(encoding="utf-8")
    n = text.count(old)
    if n != 1:
        raise AssertionError(f"{label}: expected 1 match in {path}, got {n}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def main() -> None:
    manifest_path = ROOT / "manuscript/nee_flagship_source_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    src = manifest["natural_state_separation_source"]
    src["commit"] = EGWEE_COMMIT
    src["primary_leave_one_cluster_out"] = {
        "omit_ML001_combined_p": 0.15119208,
        "omit_ML002_combined_p": 0.00517793,
        "omit_ML003_combined_p": 0.00582814,
        "influential_cluster_dependency_detected": True,
        "influential_cluster": "ML001"
    }
    src["claim_ceiling"] = (
        "Primary natural inference uses only ML001-ML003 fragmented-versus-reference Hedges-g clusters. "
        "ML015 Eucalyptus wandoo is separate Fisher-z gradient generalisation evidence and is not included in the primary Fisher combination; "
        "neither effect magnitudes nor p-values are combined across those effect families. The full primary corpus rejects exchangeability, "
        "but that rejection is not leave-one-primary-cluster-out robust because omitting ML001 gives p=0.15119."
    )
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    article = ROOT / "manuscript/nee_flagship_article.md"
    old = (
        "Their independent cluster-level tests rejected primary binary/contrast layer exchangeability (Fisher chi-square(6)=18.009, p=0.00621). "
        "Separately, *Eucalyptus wandoo* was analysed only on the frozen Fisher-z gradient scale: fragmentation severity was associated with increased pollen-tube quantity but reduced seeds per fruit, with Bonferroni cluster p=0.00257."
    )
    new = (
        "Their independent cluster-level tests rejected primary binary/contrast layer exchangeability (Fisher chi-square(6)=18.009, p=0.00621). "
        "This corpus-level rejection was influential-cluster dependent: omitting ML001 *Serapias* gave Fisher chi-square(4)=6.724, p=0.151, whereas omitting ML002 or ML003 retained p<0.006. "
        "Separately, *Eucalyptus wandoo* was analysed only on the frozen Fisher-z gradient scale: fragmentation severity was associated with increased pollen-tube quantity but reduced seeds per fruit, with Bonferroni cluster p=0.00257."
    )
    replace_once(article, old, new, "article natural Q1 sensitivity")

    metadata = ROOT / "manuscript/nee_flagship_submission_metadata.md"
    old_meta = (
        "EGWEE contributes three independent primary fragmented-versus-reference clusters / 9 primary effects, plus one separate ML015 gradient generalisation cluster. "
        "Cluster-level synthesis rejects general layer exchangeability (primary Fisher chi-square(6)=18.0086, p=0.00621; separate ML015 gradient cluster p=0.00256953) without pooling incompatible effect-size magnitudes. "
        "This supports the portability of the state-separation problem, not the finite operators."
    )
    new_meta = (
        "EGWEE contributes three independent primary fragmented-versus-reference clusters / 9 primary effects, plus one separate ML015 gradient generalisation cluster. "
        "The primary corpus rejects layer exchangeability (Fisher chi-square(6)=18.0086, p=0.00621), but leave-one-primary-cluster-out sensitivity identifies ML001 as influential: omitting ML001 gives p=0.15119, while omitting ML002 or ML003 retains p<0.006. "
        "ML015 remains separate gradient evidence (cluster p=0.00256953) and is not used to rescue the primary denominator. This supports a bounded natural state-separation result, not universal robustness or the finite operators."
    )
    replace_once(metadata, old_meta, new_meta, "metadata natural Q1 sensitivity")

    cover = ROOT / "manuscript/nee_flagship_cover_letter.md"
    old_cover = (
        "Independent natural evidence now strengthens the first question without being used to validate the finite mechanisms. A covariance-aware EGWEE synthesis of three independent primary fragmented-versus-reference systems rejected layer exchangeability on the common Hedges-g family (Fisher chi-square(6)=18.01, p=0.00621), while Eucalyptus wandoo separately supported gradient generalisation (cluster p=0.00257)."
    )
    new_cover = (
        "Independent natural evidence now strengthens the first question without being used to validate the finite mechanisms. A covariance-aware EGWEE synthesis of three primary fragmented-versus-reference systems rejected layer exchangeability on the common Hedges-g family (Fisher chi-square(6)=18.01, p=0.00621), although this corpus-level rejection depended on ML001 *Serapias* in leave-one-cluster-out sensitivity (omit ML001: p=0.151). *Eucalyptus wandoo* separately supported gradient generalisation (cluster p=0.00257)."
    )
    replace_once(cover, old_cover, new_cover, "cover natural Q1 sensitivity")

    check = ROOT / "scripts/check_nee_flagship_compliance.py"
    text = check.read_text(encoding="utf-8")
    anchor = '    assert abs(natural_q1["gradient_generalisation_cluster_p"] - 0.00256953) < 1e-12\n'
    addition = anchor + (
        '    loo = natural_q1["primary_leave_one_cluster_out"]\n'
        '    assert loo["influential_cluster_dependency_detected"] is True\n'
        '    assert loo["influential_cluster"] == "ML001"\n'
        '    assert abs(loo["omit_ML001_combined_p"] - 0.15119208) < 1e-8\n'
        '    assert "omitting ML001" in article\n'
        '    assert "p=0.151" in article\n'
    )
    if anchor not in text:
        raise AssertionError("compliance sensitivity anchor missing")
    text = text.replace(anchor, addition, 1)
    check.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
