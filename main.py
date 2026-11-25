"""Two Robots in an Elevator.

Writes one line of awkward small talk a robot says to another robot
while they ride an elevator together.

The joke lives in one machine detail: the robot ran 4,000 simulations
of this exact ride and still froze, so it falls back on the most human
thing it knows -- commenting on the weather. Robot logic shows through
(the simulations, the counting), the awkwardness lands in the pause
before "nice weather", and it lands on the first read.
"""

import os

ENTRY = "I ran 4,000 simulations of this elevator ride. In every single one, I said nothing. So… nice weather."


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters.
    if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
        raise ValueError("entry must be 1-200 non-blank characters")
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
