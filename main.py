#!/usr/bin/env python3
"""One Word for the Boss — writes the chosen word to /output/entry.txt.

The word is "Bottleneck": the boss everything piles up behind.
"""

WORD = "Bottleneck"


def main():
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
