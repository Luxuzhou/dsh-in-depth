"""Fast, dependency-free gates for the book source tree."""

from __future__ import annotations

import json
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = sorted((ROOT / "docs" / "book").glob("ch*.md"))
REQUIRED_SECTIONS = ("## 学习目标", "## 源码路标", "## 本章小结", "## 思考题", "## 求职面试题")
CHAPTER_DEPTH_BASELINES = {
    # Chapter 1 is the quality baseline for the progressive rewrite. These are
    # regression guards, not a substitute for technical/editorial review.
    "ch01.md": {
        "min_characters": 15_000,
        "min_h2": 15,
        "min_mermaid": 3,
        "min_upstream_links": 6,
        "required_phrases": (
            "## 配套实验",
            "失败模式",
            "能力接缝",
            "Model-visible means logged",
        ),
    },
}


def main() -> int:
    errors: list[str] = []
    if len(CHAPTERS) != 10:
        errors.append(f"expected 10 chapters, found {len(CHAPTERS)}")

    for chapter in CHAPTERS:
        text = chapter.read_text(encoding="utf-8")
        for section in REQUIRED_SECTIONS:
            if section not in text:
                errors.append(f"{chapter.relative_to(ROOT)} misses {section}")
        if "47f943859bef60e4160492346772ded9b24f765a" not in text and "源码路标" in text:
            if "github.com/deepseek-ai/deepseek-harness" in text:
                errors.append(f"{chapter.relative_to(ROOT)} has unpinned upstream source links")

        baseline = CHAPTER_DEPTH_BASELINES.get(chapter.name)
        if baseline:
            if len(text) < baseline["min_characters"]:
                errors.append(
                    f"{chapter.relative_to(ROOT)} is below depth baseline: "
                    f"{len(text)} < {baseline['min_characters']} characters"
                )
            h2_count = len(re.findall(r"(?m)^## ", text))
            if h2_count < baseline["min_h2"]:
                errors.append(
                    f"{chapter.relative_to(ROOT)} has too few H2 sections: "
                    f"{h2_count} < {baseline['min_h2']}"
                )
            mermaid_count = text.count("```mermaid")
            if mermaid_count < baseline["min_mermaid"]:
                errors.append(
                    f"{chapter.relative_to(ROOT)} has too few Mermaid diagrams: "
                    f"{mermaid_count} < {baseline['min_mermaid']}"
                )
            upstream_links = text.count("github.com/deepseek-ai/deepseek-harness")
            if upstream_links < baseline["min_upstream_links"]:
                errors.append(
                    f"{chapter.relative_to(ROOT)} has too few upstream links: "
                    f"{upstream_links} < {baseline['min_upstream_links']}"
                )
            for phrase in baseline["required_phrases"]:
                if phrase not in text:
                    errors.append(
                        f"{chapter.relative_to(ROOT)} misses depth marker: {phrase}"
                    )

    lock = json.loads((ROOT / "upstream.lock.json").read_text(encoding="utf-8"))
    if not re.fullmatch(r"[0-9a-f]{40}", lock.get("commit", "")):
        errors.append("upstream.lock.json commit must be a full SHA-1")

    required_files = [
        ROOT / "README.md",
        ROOT / "mkdocs.yml",
        ROOT / "docs" / "LAB_STATUS.md",
        ROOT / "docs" / "career" / "roadmap.md",
        ROOT / "docs" / "appendix" / "writing-standard.md",
    ]
    for path in required_files:
        if not path.is_file():
            errors.append(f"missing required file: {path.relative_to(ROOT)}")

    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        if "sk-" in text and "API Key" not in text:
            errors.append(f"possible secret-like text in {path.relative_to(ROOT)}")
        if not text.endswith("\n"):
            errors.append(f"missing final newline: {path.relative_to(ROOT)}")

    if errors:
        print("Content checks failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Content checks passed: {len(CHAPTERS)} chapters")
    return 0


if __name__ == "__main__":
    sys.exit(main())
