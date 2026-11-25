#!/usr/bin/env python3
"""Dad Joke Showdown entry.

Writes exactly one original dad joke to /output/entry.txt.
Pure standard library only; fully deterministic: the same bytes
on every run.
"""

import os

JOKE = (
    "I asked the cloud why it never gets grounded. "
    "It said, \"Dad, I'm above all that.\""
)


def main() -> None:
    output_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
