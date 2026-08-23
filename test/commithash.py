#!/usr/bin/env python3
"""sha256 of a file with line endings normalised to LF.

WHY THIS EXISTS (s66, SS135): ship.cmd now proves a ship by reading index.html
back OUT OF THE COMMIT and comparing it against the file on disk. Those two
cannot be compared with certutil: `.gitattributes` carries `* text=auto`, so
`git show HEAD:index.html` may hand back CRLF on a Windows clone while the file
on disk is LF. A raw hash would then differ after a PERFECTLY GOOD ship and the
gate would cry wolf - which is worse than no gate, because a gate that cries
wolf gets forced past.

Normalising both sides makes the comparison mean what it says: same content,
whatever git did to the line endings on the way out.

Usage:  python test/commithash.py <path>      -> prints 64 hex characters
        git show HEAD:index.html | python test/commithash.py -
        exit 1 and prints UNREADABLE if the content cannot be read.

READS STDIN WHEN THE PATH IS `-`, and ship.cmd uses that form. WHY: the first
attempt wrote `git show` to a file under %TEMP% and cmd answered "The filename,
directory name, or volume label syntax is incorrect" - the redirect never
produced a file, so the proof reported UNREADABLE on a ship that was fine. A
pipe has no filename to get wrong.
"""
import hashlib
import sys


def main():
    if len(sys.argv) != 2:
        print("UNREADABLE")
        return 1
    if sys.argv[1] == "-":
        try:
            data = sys.stdin.buffer.read()
        except OSError:
            print("UNREADABLE")
            return 1
    else:
        try:
            with open(sys.argv[1], "rb") as fh:
                data = fh.read()
        except OSError:
            print("UNREADABLE")
            return 1
    if not data:
        # An empty file means `git show` wrote nothing - almost always because the
        # path is not in the commit. That is not a hash, and must not read as one.
        print("UNREADABLE")
        return 1
    print(hashlib.sha256(data.replace(b"\r\n", b"\n")).hexdigest())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
