#!/usr/bin/env python3
"""The Painfully Honest Out-of-Office — make.fun entry.

Writes a single painfully honest but polite out-of-office auto-reply
(179 characters, one sentence) to /output/entry.txt.
"""

import os

ENTRY = (
    "I'm out of the office and won't read your email; I'll return Monday, "
    "delete most of it unread, and reply to the rest three weeks late "
    "\u2014 please lower your expectations accordingly."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
