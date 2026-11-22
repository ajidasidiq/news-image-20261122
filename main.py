"""Write the 22 November 2026 news front page to /output/entry.png.

The entry image is bundled with this program as entry.png (a newspaper
front page built for make.fun's news-image-20261122 bounty). This program
just copies those exact bytes to the output directory, so both grading
runs produce byte-identical output with no network and no randomness.
"""
import os
import shutil
import sys


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.isfile(src):
        print("entry.png missing next to main.py", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(out_dir, "entry.png"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
