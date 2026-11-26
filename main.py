#!/usr/bin/env python3
"""One-sentence apology entry for make.fun bounty
u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0.

Writes the entry text to /output/entry.txt first, then optionally copies it
to the repo root (guarded so a read-only repo never crashes the run).
Deterministic: same output on every run.
"""

import os

ENTRY = (
    "I'm sorry I told you the board meeting was Tuesday with total "
    "confidence, then smiled while you walked into an empty room on Monday "
    "and realized the only person who ever believed me was you."
)


def main():
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, "entry must be 1..200 chars, got %d" % len(text)
    assert text.count(".") == 1 and text.endswith("."), "must be one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Gate self-check: read back and verify exactly what the scorer will see.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "round-trip mismatch"
    assert written.strip() != "", "entry must not be only whitespace"
    assert "\n" not in written, "entry must be a single line"
    try:
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(text)
    except OSError:
        pass


if __name__ == "__main__":
    main()
