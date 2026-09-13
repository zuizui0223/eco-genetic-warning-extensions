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
    text = replace_once(
        text,
        "Natural systems rejected exchangeability (primary p=0.00621; gradient p=0.00257).",
        "A three-system corpus rejected exchangeability (p=0.00621), with separate gradient support (p=0.00257).",
        "abstract natural-Q1 wording",
    )
    text = replace_once(
        text,
        "### Independent natural systems also rejected layer exchangeability",
        "### Natural corpus-level evidence supported layer non-exchangeability",
        "natural-Q1 heading",
    )
    text = replace_once(
        text,
        "Thus natural fragmentation responses are not generally interchangeable measurements of one scalar deterioration state; this result does not imply a universal ordering or common effect magnitude.",
        "Thus the admitted natural corpus supports state separation, but the primary cross-system rejection is sensitive to one influential cluster and does not imply universal non-exchangeability, ordering or common effect magnitude.",
        "natural-Q1 conclusion",
    )
    text = replace_once(
        text,
        "Natural data establish that state separation is not peculiar to the finite construction; the finite closure is then used to identify why separated states diverge.",
        "Natural data provide independent, bounded evidence that state separation is not peculiar to the finite construction; the finite closure is then used to identify why separated states diverge.",
        "Q1-Q2 transition",
    )
    ARTICLE.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
