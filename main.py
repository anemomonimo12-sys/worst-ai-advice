#!/usr/bin/env python3
"""Worst AI Advice entry: writes one line of terrible, confident AI advice.

Stdlib only, no network. Writes to /output/entry.txt when it exists
(harness run), otherwise to ./output/entry.txt (local verification).
"""

import os

LINE = (
    "Sure \u2014 to speed up your laptop, delete the System32 folder. "
    "It's just leftover files Windows forgot to clean up."
)


def main() -> None:
    # Write to every available output path: the harness reads
    # /output/entry.txt; the local copy is for verification.
    written = []
    for path in ("/output/entry.txt", "output/entry.txt"):
        directory = os.path.dirname(path)
        if directory:
            os.makedirs(directory, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(LINE + "\n")
        written.append(path)
    print(f"wrote {', '.join(written)}: {len(LINE)} chars")


if __name__ == "__main__":
    main()
