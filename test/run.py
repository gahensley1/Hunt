#!/usr/bin/env python3
"""Full pre-ship battery. Exits non-zero if anything fails."""
import subprocess, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
target = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "index.html")
# s57: flush=True ON EVERY PARENT print. WHY: redirected to a file, Python block-
# buffers the parent while children write straight through, so the parent's own
# headers land at the END and the suite output at the TOP. s57 read the tail of
# such a file and concluded every suite had failed silently - it had not, it was
# a Chromium that was never downloaded. THE OUTPUT ORDER WAS THE BUG REPORT.
def say(*a): print(*a, flush=True)

say("=" * 62); say("PRE-SHIP BATTERY  -", os.path.abspath(target)); say("=" * 62)
rc = 0

# s57: SESSION was added. It was NOT run by this file before, yet SS82's 33d tick
# credits "session checks 19/19" - those came from a hand-run in Claude Code, so
# `battery` was quietly producing a WEAKER result than the run it reproduces.
# SS11c: a suite that does not run cannot be reported as passing.
#
# SESSION IS DELIBERATELY SKIPPED FOR A CANDIDATE BUILD. session_checks.py takes
# no argument - it serves the repo root and always loads ./index.html. Handed a
# candidate it would silently test the SHIPPED file and report a pass for a build
# it never opened. That is the SS11a class exactly, so it is refused, loudly.
suites = [("STATIC", "agents.py"), ("BEHAVIOUR", "behaviour.py")]
candidate = len(sys.argv) > 1
if candidate:
    say("\n*** SESSION SKIPPED - session_checks.py cannot target a candidate build.")
    say("*** It always loads .\\index.html. Run `battery` with no argument after the ship.")
else:
    suites.append(("SESSION", "session_checks.py"))

for name, script in suites:
    say(f"\n--- {name} " + "-" * (58 - len(name)))
    r = subprocess.run([sys.executable, os.path.join(HERE, script)]
                       + ([] if script == "session_checks.py" else [target]))
    rc |= r.returncode
say("\n" + "=" * 62)
say("BATTERY PASSED" if rc == 0 else "BATTERY FAILED - DO NOT SHIP")
if candidate:
    say("PARTIAL - SESSION did not run. This is not a full tick.")
say("=" * 62)
sys.exit(rc)
