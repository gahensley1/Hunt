#!/usr/bin/env python3
"""Full pre-ship battery. Exits non-zero if anything fails."""
import subprocess, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
target = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "index.html")
print("=" * 62); print("PRE-SHIP BATTERY  -", os.path.abspath(target)); print("=" * 62)
rc = 0
for name, script in (("STATIC", "agents.py"), ("BEHAVIOUR", "behaviour.py")):
    print(f"\n--- {name} " + "-" * (58 - len(name)))
    r = subprocess.run([sys.executable, os.path.join(HERE, script), target])
    rc |= r.returncode
print("\n" + "=" * 62)
print("BATTERY PASSED" if rc == 0 else "BATTERY FAILED - DO NOT SHIP")
print("=" * 62)
sys.exit(rc)
