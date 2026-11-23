"""Dad Joke Showdown entry: writes one original dad joke to entry.txt.

Pure Python standard library only. Deterministic: the same bytes are
written on every run.
"""

import os

JOKE = "The garage door and I had a falling-out. It just won't open up to me anymore."


def main():
    output_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
