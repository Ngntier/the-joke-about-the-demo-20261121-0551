#!/usr/bin/env python3
"""Write one joke about working beside AI coding agents to /output/entry.txt.

Deterministic, pure standard library, no network.
"""

import os

JOKE = "My AI agent heroically fixed the demo bug live \u2014 the same bug it had quietly written three prompts earlier."


def main() -> None:
    # Gate check, mirroring the competition's gate: 1-280 Unicode code
    # points, not only whitespace.
    if not 1 <= len(JOKE) <= 280 or not JOKE.strip():
        raise SystemExit(
            f"joke must be 1-280 non-whitespace characters, got {len(JOKE)}"
        )
    path = os.environ.get("JOKE_OUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(f"wrote {path} ({len(JOKE)} chars)")


if __name__ == "__main__":
    main()
