#!/usr/bin/env python3
"""The Painfully Honest Out-of-Office — make.fun entry.

Writes a single painfully honest but polite out-of-office auto-reply
(179 characters, one sentence) to /output/entry.txt.
"""

import os

MAX_ENTRY_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"

ENTRY = (
    "I'm out of the office and won't read your email; I'll return Monday, "
    "delete most of it unread, and reply to the rest three weeks late "
    "\u2014 please lower your expectations accordingly."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= MAX_ENTRY_CHARS:
        raise ValueError(f"entry is {len(ENTRY)} chars, max {MAX_ENTRY_CHARS}")
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
