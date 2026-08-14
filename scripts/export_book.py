"""Assemble the canonical Markdown chapters into one release manuscript."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCES = [
    ROOT / "docs" / "introduction.md",
    *sorted((ROOT / "docs" / "book").glob("ch*.md")),
    ROOT / "docs" / "career" / "roadmap.md",
    ROOT / "docs" / "appendix" / "glossary.md",
    ROOT / "docs" / "appendix" / "references.md",
]


def main() -> None:
    output_dir = ROOT / "dist"
    output_dir.mkdir(exist_ok=True)
    target = output_dir / "dsh-in-depth.md"
    sections = [source.read_text(encoding="utf-8").strip() for source in SOURCES]
    target.write_text("\n\n\\newpage\n\n".join(sections) + "\n", encoding="utf-8")
    print(f"Wrote {target.relative_to(ROOT)} from {len(SOURCES)} sources")


if __name__ == "__main__":
    main()
