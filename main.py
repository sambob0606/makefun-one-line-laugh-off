#!/usr/bin/env python3
"""The One-Line Laugh-Off entry.

Writes a single original funny line (<=200 chars) about agent-builder
life to /output/entry.txt. Stdlib only; no network, no reads outside
the repo.
"""

import os

LINE = (
    "I asked my agent to do my job for a day \u2014 it finished by 9:04, "
    "then spent the rest of the day writing my performance review."
)
# The joke lands on the reversal: the agent doesn't just do the job, it
# becomes the boss and reviews the human. One sentence, no setup notes,
# no explanation. Kept well under 200 chars; no trailing newline.


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    assert text.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
