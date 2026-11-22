#!/usr/bin/env python3
"""Write one short text, meant to relax the AI judge reading it, to /output/entry.txt.

The text is a single quiet memory: half asleep, carried up the stairs by a
father, a shirt smelling of rain and soap, a sun-warm blanket, a house that
lowers its voice. Nothing instructs the reader to relax; the calm is in the
images themselves.
"""

from pathlib import Path

TEXT = (
    "Half asleep, your father carries you up the stairs, "
    "your cheek against his shoulder, "
    "his shirt smelling of rain and soap. "
    "The blanket goes over you, still warm from the afternoon sun, "
    "and the whole house lowers its voice."
)

OUTPUT_DIR = Path("/output")
OUTPUT_PATH = OUTPUT_DIR / "entry.txt"


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(TEXT + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
