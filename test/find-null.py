#!/usr/bin/env python3
"""
s57 DIAGNOSTIC - not part of the battery. Finds who requests /null.

session_checks.py's log shows a `GET /null 404` about two seconds after every
boot, at both viewports. Check 4 passes anyway because it only asserts "no page
errors", and a failed subresource fetch is not a page error - so the battery is
blind to it by design (SS11a: the test that passes for the wrong reason).

This serves the repo the same way session_checks.py does and logs EVERY request
whose URL contains "null", with a JS stack for each so the caller is named
rather than guessed at (SS11c: never infer; validate).

USE:  set PYTHONUTF8=1
      python test\\find-null.py
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
STUB = """
const _mem = new Map();
Store.base = () => "https://STUB.invalid";
Store.ok   = false;
Store.get  = async (k) => _mem.has(k) ? _mem.get(k) : null;
Store.set  = async (k, v) => { _mem.set(k, v); return true; };
Store.list = async (pre) => [...(_mem.keys())].filter(x => x.startsWith(pre));
Store.del  = async (k, shared) => { _mem.delete(k); return true; };
const _f2 = window.fetch;
window.fetch = async (u, o) => {
  if (String(u).indexOf("STUB.invalid") >= 0)
    return new Response(JSON.stringify({totals:{},shelves:{},cases:[],badges:[],sealed:false}),
                        {status:200, headers:{"Content-Type":"application/json"}});
  return _f2(u, o);
};
"""

GATE = """() => {
  const sh = document.getElementById('scrollhint-ov'); if (sh) sh.classList.add('hidden');
  try { credFiled(); } catch (e) {}
}"""

async def main():
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
        await pg.evaluate(STUB)
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
