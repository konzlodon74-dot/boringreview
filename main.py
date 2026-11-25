#!/usr/bin/env python3
"""Write a one-line funny, true review of the most boring everyday object.

The object: a rubber band. The joke comes from how it really behaves:
it spends its whole life in a drawer drying out, and snaps on the one
day you actually need it.
"""

import os

ENTRY = (
    "The rubber band has one job -- hold things together -- so naturally "
    "it spends its whole life in a drawer drying out, and snaps the one "
    "time you actually need it."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
