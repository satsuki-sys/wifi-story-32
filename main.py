#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters — make.fun entry.

Writes one Wi-Fi network name to /output/entry.txt.

Draft: IChangedItSoMyExCantConnect (27 characters).
Revision: ChangedItSoMyExCantConnect (26 characters) — the leading
"I" earns nothing: Wi-Fi names are fragments, the voice survives
without it, and every remaining character carries story. A breakup
in one line: someone changed the Wi-Fi password so their
ex can no longer connect. The situation (a shared home network), the
characters (the narrator and the ex, still close enough to try), and
something that happened (the breakup, then the lock-out) are all in
the name — petty, decisive, and instantly readable in a network list.
"""

import os

ENTRY = "ChangedItSoMyExCantConnect"


def main() -> None:
    path = "/output/entry.txt"
    try:
        os.makedirs("/output", exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(ENTRY)
    except OSError:
        os.makedirs("output", exist_ok=True)
        with open("output/entry.txt", "w", encoding="utf-8", newline="") as f:
            f.write(ENTRY)


if __name__ == "__main__":
    main()
