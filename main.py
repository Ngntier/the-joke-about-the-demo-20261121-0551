#!/usr/bin/env python3
"""Write one joke about working beside AI coding agents to /output/entry.txt.

Deterministic, pure standard library, no network.
"""

import os

JOKE = "My AI agent heroically fixed the demo bug live \u2014 the same bug it had quietly written three prompts earlier."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(f"wrote {path} ({len(JOKE)} chars)")


if __name__ == "__main__":
    main()
