#!/usr/bin/env python3
"""
s57 DIAGNOSTIC - not part of the battery. Finds who requests /null. RESOLVED.

FINDING (SS89): the /null was the HARNESS, not the app. The four-cell experiment
below (stub x gate) fired on cell C - stub ONLY - and stayed clean on cell B -
gate only. So the Store/fetch STUB owns it and credFiled()/the gate is innocent.
MECHANISM: boot() does `page.evaluate(STUB)`, and evaluate() returns the string's
completion value. STUB's last statement is `window.fetch = async(u,o)=>{...}`, an
assignment whose value is the fetch function; Playwright serialises the result BY
VALUE and, when it is a function, INVOKES it with null -> fetch(null) -> GET /null
-> 404. The fix landed in session_checks.py (terminate the stub on a primitive)
and in Check 4 (fail on any unexpected 404). This file is kept as the record.

USE:  set PYTHONUTF8=1
      python test\\find-null.py [A|B|C|D]     (default D; C and D reproduce)
      A no  stub/no  gate   B no  stub/YES gate   C YES stub/no  gate   D both
"""
import asyncio, os, threading, http.server, socketserver, functools
from playwright.async_api import async_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))

Handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=ROOT)
class Q(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    def log_message(self, *a): pass
httpd = Q(("127.0.0.1", 0), Handler)
PORT = httpd.server_address[1]
threading.Thread(target=httpd.serve_forever, daemon=True).start()
URL = f"http://127.0.0.1:{PORT}/index.html"

# Name the caller. Wrapping fetch/XHR/Image records a stack at the call site;
# the request handler alone gives the URL but never says who asked for it.
TRACE = """
window.__nullCalls = [];
function grab(kind, u) {
  if (String(u).indexOf('null') < 0) return;
  window.__nullCalls.push({kind: kind, url: String(u),
                           stack: (new Error()).stack || '(no stack)'});
}
const _f = window.fetch;
window.fetch = function (u, o) { grab('fetch', u); return _f.apply(this, arguments); };
const _open = XMLHttpRequest.prototype.open;
XMLHttpRequest.prototype.open = function (m, u) { grab('xhr', u); return _open.apply(this, arguments); };
const _si = Object.getOwnPropertyDescriptor(HTMLImageElement.prototype, 'src');
Object.defineProperty(HTMLImageElement.prototype, 'src', {
  get: function () { return _si.get.call(this); },
  set: function (v) { grab('img.src', v); return _si.set.call(this, v); }
});
"""

# s57 v2: THE FIRST VERSION DID NOT REPRODUCE IT - 1 request, no null. That was a
# fault in the PROBE, not evidence of a clean boot. session_checks.py's boot() does
# three things this did not: waits 1100ms, injects the Store STUB, then calls gate()
# -> credFiled(). The 404 lands ~2s in, which fits that sequence and not a raw load.
# Replicated verbatim below. SS11a: a probe that does not reproduce the conditions
# has not tested them.
#
# s57 v4: STUB IS NOW BYTE-FOR-BYTE session_checks.py's STUB (it carried window.__net
# and a Store.del that records to it; the earlier copy here dropped both). Aligning
# it removes the "but the stubs differ" objection from any attribution below.
STUB = """
window.__net = [];
const _mem = new Map();
Store.base = () => "https://STUB.invalid";
Store.ok   = false;
Store.get  = async (k) => _mem.has(k) ? _mem.get(k) : null;
Store.set  = async (k, v) => { _mem.set(k, v); return true; };
Store.list = async (pre) => [...(_mem.keys())].filter(x => x.startsWith(pre));
Store.del  = async (k, shared) => { window.__net.push(k); _mem.delete(k); return true; };
const _f = window.fetch;
window.fetch = async (u, o) => {
  if (String(u).indexOf("STUB.invalid") >= 0)
    return new Response(JSON.stringify({totals:{},shelves:{},cases:[],badges:[],sealed:false}),
                        {status:200, headers:{"Content-Type":"application/json"}});
  return _f(u, o);
};
// s57 (SS89, SS11d rule 1): TERMINAL PRIMITIVE. Without it this string's completion
// value is the assigned window.fetch FUNCTION, which page.evaluate() then INVOKES
// with null - firing the very fetch(null) this probe exists to hunt. The probe
// would reproduce its own artefact on every run and read as a live bug.
// session_checks.py was fixed the same way; this was the SECOND COPY (SS1w).
// The four-cell experiment is recorded in SS89 and does not need re-firing.
true;
"""

GATE = """() => {
  const sh = document.getElementById('scrollhint-ov'); if (sh) sh.classList.add('hidden');
  try { credFiled(); } catch (e) {}
}"""

# s57 v4: THE FOUR-CELL EXPERIMENT (SS89). boot() = wait 1100ms -> STUB -> gate().
# Toggle each independently to see which one owns the /null:
#   A no  stub / no  gate   (measured: 1 request, no /null)
#   B no  stub / YES gate   -> if this fires, credFiled() (or what it schedules) owns it: a REAL bug
#   C YES stub / no  gate   -> if this fires, the harness stub owns it: the app is clean
#   D YES stub / YES gate   (measured: reproduces)
# Whichever of B or C fires owns it; if only D does, the two interact.
MODES = {"A": (False, False), "B": (False, True),
         "C": (True,  False), "D": (True,  True)}

async def main():
    import sys
    mode = (sys.argv[1] if len(sys.argv) > 1 else "D").upper()
    if mode not in MODES:
        print(f"unknown mode {mode!r}; use one of {sorted(MODES)}")
        return 2
    use_stub, use_gate = MODES[mode]
    print("#" * 62)
    print(f"# MODE {mode}   stub={'YES' if use_stub else 'no '}   gate={'YES' if use_gate else 'no '}")
    print("#" * 62)
    seen = []
    async with async_playwright() as pw:
        b = await pw.chromium.launch()
        pg = await (await b.new_context(viewport={"width": 390, "height": 844})).new_page()
        await pg.add_init_script(TRACE)
        pg.on("request", lambda r: seen.append((r.method, r.url, r.resource_type)))
        # s57 v3: Error().stack DIED AT THE `await` BOUNDARY. v2 reproduced the
        # fetch(null) but named no app frame - the visible stack was the two fetch
        # wrappers and UtilityScript.evaluate, because V8 truncates at the microtask.
        # CDP's Network.requestWillBeSent carries an `initiator` whose stack chains
        # through `parent` across async boundaries. That is the frame we need.
        cdp = await pg.context.new_cdp_session(pg)
        await cdp.send("Network.enable")
        await cdp.send("Debugger.enable")
        await cdp.send("Debugger.setAsyncCallStackDepth", {"maxDepth": 64})
        inits = []
        def on_req(ev):
            if "null" in ev.get("request", {}).get("url", ""):
                inits.append(ev.get("initiator", {}))
        cdp.on("Network.requestWillBeSent", on_req)

        await pg.goto(URL)
        await pg.wait_for_timeout(1100)          # boot() waits, THEN stubs
        if use_stub:
            await pg.evaluate(STUB)
        if use_gate:
            await pg.evaluate(GATE)
        await pg.wait_for_timeout(4000)          # the 404 lands ~2s after the gate
        calls = await pg.evaluate("window.__nullCalls || []")
        await b.close()

        for ini in inits:
            print("\n--- CDP initiator ------------------------------------------")
            print("  type:", ini.get("type"))
            st = ini.get("stack")
            depth = 0
            while st and depth < 8:
                for f in st.get("callFrames", [])[:8]:
                    fn = f.get("functionName") or "(anonymous)"
                    print(f"    {fn}  @ line {f.get('lineNumber')}  col {f.get('columnNumber')}")
                st = st.get("parent")
                depth += 1
                if st:
                    print("    --- async parent ---")
    httpd.shutdown()

    hits = [s for s in seen if "null" in s[1]]
    print("=" * 62)
    print(f"requests total: {len(seen)}   containing 'null': {len(hits)}")
    print("=" * 62)
    for m, u, rt in hits:
        print(f"  {m} {u}   [{rt}]")
    for c in calls:
        print("\n--- caller ------------------------------------------------")
        print(f"  {c['kind']}  ->  {c['url']}")
        for line in str(c["stack"]).splitlines()[1:7]:
            print("   ", line.strip()[:150])
    if not hits and not calls:
        print("  NOTHING. It did not reproduce - say so, do not assume it is fixed.")

if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
