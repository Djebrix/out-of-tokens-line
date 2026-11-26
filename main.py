#!/usr/bin/env python3
"""Out of Tokens, Mid-Sentence — writes the entry line to /output/entry.txt.

Python standard library only. Deterministic: the same line every run.
"""

import os

LINE = "Error: out of tokens. The brilliant ending I had planned died here, mid-sentence, and no one will ever know it."
MAX_CHARS = 140

assert 1 <= len(LINE) <= MAX_CHARS, f"line must be 1..{MAX_CHARS} chars, got {len(LINE)}"
assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
assert LINE.strip(), "line must not be only whitespace"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
