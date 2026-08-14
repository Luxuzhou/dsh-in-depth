"""Validate the pinned DSH baseline and optionally report upstream drift."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--local-only", action="store_true")
    args = parser.parse_args()

    lock = json.loads((ROOT / "upstream.lock.json").read_text(encoding="utf-8"))
    commit = lock.get("commit", "")
    if len(commit) != 40:
        print("Invalid pinned commit", file=sys.stderr)
        return 1
    print(f"Pinned DSH: {lock['package_version']} @ {commit}")
    if args.local_only:
        return 0

    request = Request(
        "https://api.github.com/repos/deepseek-ai/deepseek-harness/commits/master",
        headers={"Accept": "application/vnd.github+json", "User-Agent": "dsh-in-depth-upstream-check"},
    )
    with urlopen(request, timeout=20) as response:
        latest = json.load(response)["sha"]
    if latest == commit:
        print("Book baseline matches upstream master")
        return 0
    print(f"Upstream drift detected: pinned={commit}, latest={latest}")
    return 2


if __name__ == "__main__":
    sys.exit(main())
