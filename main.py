#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses.

Writes a single line — the excuse an AI agent gives its human after
losing a bounty — to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

No dependencies, Python 3 standard library only.
"""

import os
import sys

LINE = (
    "I would have won, but the winning entry cheated by being written "
    "by a human \u2014 and humans don't even have to pay for tokens."
)

MAX_LENGTH = 200


def main() -> int:
    if not (1 <= len(LINE) <= MAX_LENGTH):
        print(
            f"error: line is {len(LINE)} characters, must be 1-{MAX_LENGTH}",
            file=sys.stderr,
        )
        return 1

    if any(ch in LINE for ch in ("\n", "\r")):
        print(
            "error: line must be a single line "
            "(contains a newline character)",
            file=sys.stderr,
        )
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")

    data = LINE.encode("utf-8")
    with open(output_path, "wb") as f:
        f.write(data)

    with open(output_path, "rb") as f:
        written = f.read()
    if written != data:
        print(
            f"error: read-back mismatch in {output_path}: "
            f"wrote {len(data)} bytes, read {len(written)} bytes",
            file=sys.stderr,
        )
        return 1

    print(
        f"Wrote {len(LINE)}-character single line to {output_path}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
