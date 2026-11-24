"""Funniest time machine warning.

Entry: a warning label for a time machine, warning its user not to try to
win the lottery — because their future self already spent the winnings.
"""

import os

ENTRY = "WARNING: Do not use this machine to win the lottery. Your future self already spent it."


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
