"""Seventeen Syllables of Debugging — entry for make.fun bounty
u-irvan-motion-seventeen-syllables-of-debugging-d194b605.

Writes one haiku about debugging (three lines, 5-7-5 syllables, at most
200 characters) to /output/entry.txt. The haiku: a breakpoint holds its
breath, the log line insists nothing changed, and the last line turns it —
the bug was the debugger all along.
"""

import os

HAIKU = (
    "Breakpoint holds its breath\n"
    "The log line swears nothing changed\n"
    "It was me, always"
)

# Hand-counted syllables per word, so the program can prove the 5-7-5
# shape instead of trusting it: breakpoint(2) holds(1) its(1) breath(1),
# the(1) log(1) line(1) swears(1) nothing(2) changed(1),
# it(1) was(1) me(1) always(2).
SYLLABLES = {
    "breakpoint": 2, "holds": 1, "its": 1, "breath": 1,
    "the": 1, "log": 1, "line": 1, "swears": 1, "nothing": 2, "changed": 1,
    "it": 1, "was": 1, "me": 1, "always": 2,
}


def count_syllables(line: str) -> int:
    words = line.replace(",", "").lower().split()
    return sum(SYLLABLES[w] for w in words)


def main() -> None:
    text = HAIKU.strip()
    lines = text.split("\n")
    assert len(lines) == 3, f"haiku must be 3 lines, got {len(lines)}"
    assert 1 <= len(text) <= 200, f"text is {len(text)} chars"
    shape = [count_syllables(line) for line in lines]
    assert shape == [5, 7, 5], f"haiku shape must be 5-7-5, got {shape}"

    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
