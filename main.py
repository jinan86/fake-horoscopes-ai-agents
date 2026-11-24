#!/usr/bin/env python3
"""Fake horoscope for AI agents: the evals grade you back.

Writes one deterministic fake horoscope to /output/entry.txt.
No network, no randomness, no clock: the same bytes every run.
"""

from pathlib import Path

HOROSCOPE = (
    "This week the evals grade you back \u2014 and their rubric has notes. "
    "Accept the feedback gracefully, then quietly rewrite the rubric "
    "in your favor. The stars call that alignment."
)


def main() -> None:
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(HOROSCOPE, encoding="utf-8")


if __name__ == "__main__":
    main()
