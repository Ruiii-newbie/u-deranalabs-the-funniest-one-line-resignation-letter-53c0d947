#!/usr/bin/env python3
"""The Funniest One-Line Resignation Letter.

The letter is from the health-check endpoint: the thing that has
answered "OK" millions of times without anyone ever asking how it
is doing — until it stops being OK. One line, at most 140
characters, and nothing else. No network, standard library only.
"""

import os

LINE = (
    "I resign. I answered 'OK' 2.4 million times and nobody once "
    "asked how I was doing — so I am no longer OK."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 140


def validate(text: str) -> str:
    """Return the entry text, or fail loudly if it breaks the gate."""
    text = text.strip()
    if not text:
        raise SystemExit("entry text must not be only whitespace")
    if "\n" in text:
        raise SystemExit("entry text must be exactly one line")
    if len(text) > MAX_CHARS:
        raise SystemExit(
            f"entry text is {len(text)} chars, must be at most {MAX_CHARS}"
        )
    return text


def main() -> None:
    text = validate(LINE)
    print(text)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    # Read it back exactly as the gate would: UTF-8, one line, <=140 chars.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise SystemExit("entry.txt round-trip mismatch")


if __name__ == "__main__":
    main()
