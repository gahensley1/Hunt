#!/usr/bin/env python3
"""Print the #buildmark out of an index.html. Written s61 for ship.cmd GATE 2.

WHY THIS EXISTS: GATE 2 used `findstr /c:"test build marker"`, and index.html holds a
506,884-character line of base64. findstr cannot get past a line that long, so it
returned NOTHING for the working file AND for the git-show copy. The gate compared
empty to empty, concluded the buildmark had not changed, and refused every ship --
34n and 34o both had to go out with /force. It was not detecting a fault; it was
failing to read (SS127).

Prints the mark (e.g. "34o") on success. Prints UNREADABLE and exits 2 if the marker
is absent or malformed -- LOUDLY, because a read failure that looks like a clean
answer is the whole bug this replaces.

    python test\\buildmark.py index.html
"""
import io
import re
import sys

MARKER = "test build marker"


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "index.html"
    try:
        with io.open(path, encoding="utf-8", errors="replace") as fh:
            text = fh.read()
    except OSError as exc:
        sys.stderr.write("cannot open %s: %s\n" % (path, exc))
        print("UNREADABLE")
        return 2

    i = text.find(MARKER)
    if i < 0:
        sys.stderr.write("no %r in %s\n" % (MARKER, path))
        print("UNREADABLE")
        return 2

    # the mark is the text node of the element carrying the marker attribute:
    #   <p id="buildmark" aria-label="test build marker">34o</p>
    m = re.search(r">\s*([0-9A-Za-z]{1,12})\s*<", text[i:i + 400])
    if not m:
        sys.stderr.write("marker found in %s but no mark after it\n" % path)
        print("UNREADABLE")
        return 2

    print(m.group(1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
