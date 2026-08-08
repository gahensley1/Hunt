#!/usr/bin/env python3
"""
Four session-specific checks the pre-ship battery does not cover.
Serves the folder over HTTP and drives a real Chromium. Never writes to the
live Worker: installs the same Store stub as behaviour.py and stubs window.fetch
so the Ledger's /report call resolves offline.
"""
import asyncio, os, threading, http.server, socketserver, functools
from playwright.async_api import async_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))

# ---- serve the folder ----------------------------------------------------
Handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=ROOT)
class Q(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
httpd = Q(("127.0.0.1", 0), Handler)
PORT = httpd.server_address[1]
threading.Thread(target=httpd.serve_forever, daemon=True).start()
URL = f"http://127.0.0.1:{PORT}/index.html"

# same never-touch-the-Worker stub used by behaviour.py, plus a fetch stub so
# loadLedger()'s raw fetch(base+"/report") resolves offline with a valid report.
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
"""

RESULTS = []
def check(name, got, want):
    ok = got == want
    RESULTS.append(ok)
    print(f"  {'PASS' if ok else 'FAIL'}  {name:52} got={got!r}" + ("" if ok else f" want={want!r}"))

async def gate(pg):
    await pg.evaluate("""() => {
      const sh = document.getElementById('scrollhint-ov'); if (sh) sh.classList.add('hidden');
      try { credFiled(); } catch (e) {}
    }""")

async def boot(browser, w=390, h=844):
    pg = await browser.new_page(viewport={"width": w, "height": h})
    errs = []; pg.on("pageerror", lambda e: errs.append(str(e)))
    await pg.goto(URL); await pg.wait_for_timeout(1100)
    await pg.evaluate(STUB)
    await gate(pg)
    return pg, errs

async def render_ledger(pg, month="2026-08"):
    await pg.evaluate(f"""async () => {{
      CURATOR_WORD = "x";                       // session-only, offline; fetch is stubbed
      State.ledgMonth = "{month}";
      State.curTab = "ledg";
      await renderCurator();
    }}""")
    await pg.wait_for_selector("#cur-ledger .ledg-nav", timeout=6000)
    await pg.wait_for_timeout(300)

async def main():
    async with async_playwright() as pw:
        b = await pw.chromium.launch()

        # ---- Check 1: _ledgLabel('2026-08') is exactly "August 2026" ----
        print('\nCheck 1  _ledgLabel("2026-08")  -- call the app formatter, no hand-typing')
        pg, e1 = await boot(b)
        lbl = await pg.evaluate("_ledgLabel('2026-08')")
        check('returns exactly "August 2026"', lbl, "August 2026")
        check('contains no "(office time)"', "office time" in lbl, False)
        await pg.close()

        # ---- Check 2: _wireLedgEmail is a fn; #ledg-email on BOTH screens ----
        print("\nCheck 2  _wireLedgEmail + #ledg-email on the Ledger AND a case sheet")
        pg, e2 = await boot(b)
        check("_wireLedgEmail is a function",
              await pg.evaluate("typeof _wireLedgEmail"), "function")
        await render_ledger(pg)
        check("Ledger: #ledg-email exists",
              await pg.evaluate("!!document.getElementById('ledg-email')"), True)
        check('Ledger: labelled "email report"',
              await pg.evaluate("(document.getElementById('ledg-email')||{}).textContent"), "email report")
        # now a case sheet, in the same container
        await pg.evaluate("loadCaseSheet('310403', State.ledgMonth)")
        await pg.wait_for_timeout(300)
        check("Case sheet: #ledg-email exists",
              await pg.evaluate("!!document.getElementById('ledg-email')"), True)
        check('Case sheet: labelled "email report"',
              await pg.evaluate("(document.getElementById('ledg-email')||{}).textContent"), "email report")
        check("no page errors", e2, [])
        await pg.close()

        # ---- Check 3: at 393px the nav buttons each sit on ONE line, tops level ----
        print("\nCheck 3  .ledg-nav at 393px  -- '< Earlier' / 'Later >' one line each, tops equal")
        pg, e3 = await boot(b, w=393, h=844)
        await render_ledger(pg, "2026-08")
        m = await pg.evaluate("""() => {
          const p = document.getElementById('ledg-prev');
          const n = document.getElementById('ledg-next');
          // count the lines the TEXT actually occupies via a Range over its text node
          const textRects = k => { const r = document.createRange(); r.selectNodeContents(k);
                                   return [...r.getClientRects()]; };
          const pr = textRects(p), nr = textRects(n);
          return {
            prevText: p.textContent, nextText: n.textContent,
            prevTextLines: pr.length, nextTextLines: nr.length,
            prevWhiteSpace: getComputedStyle(p).whiteSpace,
            nextWhiteSpace: getComputedStyle(n).whiteSpace,
            prevTextTop: Math.round(pr[0].top), nextTextTop: Math.round(nr[0].top),
            navWidth: document.querySelector('.ledg-nav').getBoundingClientRect().width
          };
        }""")
        check("viewport is 393px wide", await pg.evaluate("window.innerWidth"), 393)
        check('"< Earlier" text',  m["prevText"], "‹ Earlier")
        check('"Later >" text',    m["nextText"], "Later ›")
        check('"< Earlier" text on ONE line', m["prevTextLines"], 1)
        check('"Later >" text on ONE line',   m["nextTextLines"], 1)
        check('"< Earlier" white-space:nowrap', m["prevWhiteSpace"], "nowrap")
        check('"Later >" white-space:nowrap',   m["nextWhiteSpace"], "nowrap")
        check("their text tops are equal", m["prevTextTop"], m["nextTextTop"])
        print(f"    (nav width {round(m['navWidth'])}px, prev text top {m['prevTextTop']}, next text top {m['nextTextTop']})")
        check("no page errors", e3, [])
        await pg.close()

        # ---- Check 4: no page errors on boot at 390x844 and 320x568 ----
        print("\nCheck 4  clean boot at 390x844 and 320x568")
        pg, e4a = await boot(b, w=390, h=844); await pg.wait_for_timeout(400); await pg.close()
        pg, e4b = await boot(b, w=320, h=568); await pg.wait_for_timeout(400); await pg.close()
        check("390x844 boots with no page errors", e4a, [])
        check("320x568 boots with no page errors", e4b, [])

        await b.close()
    httpd.shutdown()
    print(f"\n{sum(RESULTS)}/{len(RESULTS)} passed")
    return 0 if all(RESULTS) else 1

if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
