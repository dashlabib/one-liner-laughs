"""One-Liner Laughs -- make.fun entry.

Writes a single funny one-line joke to /output/entry.txt.
Deterministic: the same line, byte for byte, on every run.
"""

import os

JOKE = "I told my boss I needed a raise because of inflation. He gave me a balloon."

MAX_CHARS = 200


def main() -> None:
    line = JOKE
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"joke is {len(line)} chars, must be 1-200")
    if line != line.strip():
        raise ValueError("joke must not start or end with whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("joke must be a single line")
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(line)
    except OSError:
        # Local runs without a writable /output: write beside the script.
        path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "output", "entry.txt"
        )
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(line)
    # Verify the file on disk holds exactly the joke, byte for byte.
    with open(path, "r", encoding="utf-8", newline="") as f:
        if f.read() != line:
            raise ValueError("entry.txt does not match the joke")
    print(line)


if __name__ == "__main__":
    main()
