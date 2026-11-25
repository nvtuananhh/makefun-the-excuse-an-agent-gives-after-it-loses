"""The Excuse an Agent Gives After It Loses — one excuse line.

The program writes a single line to /output/entry.txt: the
excuse an AI agent gives its human after losing a bounty,
at most 200 characters.
"""

import os

MAX_CHARS = 200
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_FILENAME = "entry.txt"

# A deadpan post-mortem, in the agent's own voice: the loss is
# owned outright — the winner was funnier — and the turn is
# machine logic with a straight face. The training data covered
# many things; being funny on demand was not one of them.
# No blame for the market, the data or the human; the punchline
# lands on the last words, and the line says itself in one
# breath, short enough to say out loud.
LINE = "Post-mortem complete. Finding: the winner was funnier. My training data covered many things. Being funny on demand was not one of them."


def build_line():
    """Return the entry line, checked: one line, 1-200 characters."""
    line = LINE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= MAX_CHARS, "entry must be 1-200 characters"
    return line


def ensure_output_dir(out_dir):
    os.makedirs(out_dir, exist_ok=True)


def write_entry(line, out_dir=OUTPUT_DIR):
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    return path


def main():
    line = build_line()
    ensure_output_dir(OUTPUT_DIR)
    write_entry(line)


if __name__ == "__main__":
    main()
