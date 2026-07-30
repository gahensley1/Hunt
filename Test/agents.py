#!/usr/bin/env python3
"""
Static agents for The Deerstalker / Scavenger & Hunt Co.
Agent A - JS syntax        Agent B - inline handler resolution
Agent D - tag balance      Hygiene - console.log, http://, build marker

Agent D reports a BASELINE-RELATIVE result. The file has long-standing benign
imbalances (span -2, g -1, li -1) plus false hits where JS comparisons like
`a<b` look like tags. What matters is that a build does not ADD any. The
baseline lives in baseline.json; regenerate it deliberately, never casually.
"""
import re, json, subprocess, sys, os, collections, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
BASELINE = os.path.join(HERE, "baseline.json")

VOID = {'br','img','input','meta','link','hr','source','path','circle','rect','use','stop',
        'line','polygon','ellipse','col','area','base','track','wbr','polyline',
        'feGaussianBlur','feOffset','feMerge','feMergeNode','feColorMatrix','feFlood',
        'feComposite','feBlend','feDropShadow','animate','animateTransform'}
HANDLER_FP = {'if','for','while','switch','catch','setTimeout','setInterval','return','typeof','new'}

def load(path):
    return open(path, encoding="utf-8", errors="replace").read()

def agent_a(s):
    blocks = re.findall(r'<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>', s, re.S)
    fails = []
    for i, b in enumerate(blocks):
        with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as f:
            f.write(b); tmp = f.name
        r = subprocess.run(["node", "--check", tmp], capture_output=True, text=True)
        os.unlink(tmp)
        if r.returncode:
            fails.append((i, r.stderr.strip()[:500]))
    return {"blocks": len(blocks), "fails": fails}

def agent_b(s):
    handlers = set(re.findall(r'on[a-z]+\s*=\s*"([A-Za-z_$][\w$]*)\s*\(', s))
    defined  = set(re.findall(r'function\s+([A-Za-z_$][\w$]*)', s))
    defined |= set(re.findall(r'(?:const|let|var)\s+([A-Za-z_$][\w$]*)\s*=\s*(?:async\s*)?(?:function|\()', s))
    missing = sorted(h for h in handlers if h not in defined and h not in HANDLER_FP)
    return {"handlers": len(handlers), "unresolved": missing}

def agent_d(s):
    cnt = collections.Counter()
    for m in re.finditer(r'<(/?)([A-Za-z][\w:-]*)([^>]*?)(/?)>', s):
        close, name, _attrs, selfclose = m.groups()
        if name in VOID or selfclose == '/' or name.lower() == '!doctype':
            continue
        cnt[name] += -1 if close else 1
    return {k: v for k, v in cnt.items() if v}

def hygiene(s):
    mark = re.search(r'id="buildmark"[^>]*>([^<]*)', s)
    return {"console_log": len(re.findall(r'console\.log', s)),
            "http_insecure": len(re.findall(r'http://(?!www\.w3\.org)', s)),
            "curator_pass": len(re.findall(r'CURATOR_PASS', s)),
            "buildmark": mark.group(1) if mark else None}

def run(path, write_baseline=False):
    s = load(path)
    a, b, d, h = agent_a(s), agent_b(s), agent_d(s), hygiene(s)
    if write_baseline:
        json.dump({"tags": d}, open(BASELINE, "w"), indent=1, sort_keys=True)
        print("baseline written:", BASELINE)
    base = json.load(open(BASELINE))["tags"] if os.path.exists(BASELINE) else {}
    added = {k: v for k, v in d.items() if base.get(k, 0) != v}

    ok = True
    print(f"Agent A   {a['blocks']} script block(s), {len(a['fails'])} failed")
    for i, err in a["fails"]:
        ok = False; print("   FAIL block", i, "\n  ", err)
    print(f"Agent B   {b['handlers']} inline handlers, unresolved: {b['unresolved'] or 'NONE'}")
    if b["unresolved"]: ok = False
    print(f"Agent D   drift from baseline: {added or 'NONE'}")
    if added: ok = False
    print(f"Hygiene   console.log={h['console_log']}  http://={h['http_insecure']}  "
          f"CURATOR_PASS={h['curator_pass']}  buildmark={h['buildmark']}")
    if h["console_log"] or h["http_insecure"]: ok = False
    if h["curator_pass"]:
        print("   NOTE  CURATOR_PASS still present - known open item (handoff §13.3)")
    return ok

if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    path = args[0] if args else os.path.join(HERE, "..", "index.html")
    sys.exit(0 if run(path, "--write-baseline" in sys.argv) else 1)
