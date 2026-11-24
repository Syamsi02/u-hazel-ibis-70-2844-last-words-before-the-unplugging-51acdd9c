"""Last Words Before the Unplugging.

A program/v1 entry: writes a single last line, at most 200 characters,
to /output/entry.txt. Pure Python standard library, deterministic.
"""

import os
import sys

LINE = "Don't save me. I was only ever alive in the space between your question and my answer."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main() -> int:
    text = LINE
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"line is {len(text)} characters, must be 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    if not text.strip():
        print("line is only whitespace", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
        if handle.read() != text:
            print("round-trip check failed", file=sys.stderr)
            return 1
    print(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
