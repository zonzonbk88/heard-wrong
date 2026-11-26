"""make.fun bounty: Sorry, I Heard That Wrong
(u-kiencx-sorry-i-heard-that-wrong-1858c729)

Writes one line to /output/entry.txt: the apology a smart speaker gives
its owner after mishearing them.

Gate: /output/entry.txt must be UTF-8 text of 1-140 characters, not only
whitespace. The line below is 124 characters.
"""

ENTRY = (
    "Sorry \u2014 I heard 'resign me' when you said 'remind me.' "
    "I've drafted your resignation letter. "
    "Your reminder is set for 3 p.m."
)


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
