#!/usr/bin/env python3
"""
Behavioural tests - headless Chromium against a local index.html.

  §11b IS ABSOLUTE: A TEST MUST NEVER WRITE TO THE LIVE WORKER.
  Every test below installs a Store stub before touching anything. The stub is
  installed by _boot() and there is no path in this file that reaches the network.
  If you add a test, call _boot() first. No exceptions.

Run:  python3 test/behaviour.py [path/to/index.html]
"""
import asyncio, pathlib, sys, os
from playwright.async_api import async_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT = os.path.join(HERE, "..", "index.html")

STUB = """
window.__net = [];
const _mem = new Map();
window.__stub = (opts) => {
  opts = opts || {};
  Store.base = () => "https://STUB.invalid";     // never a real host
  Store.ok   = false;
  Store.get  = async (k) => _mem.has(k) ? _mem.get(k) : null;
  Store.set  = async (k, v) => { _mem.set(k, v); return true; };
  Store.list = async (pre) => [...(_mem.keys())].filter(x => x.startsWith(pre));
  Store.del  = async (k, shared) => {
    window.__net.push(k);
    if (shared && opts.serverFails) return false;
    _mem.delete(k);
    return true;
  };
};
window.__seed = async (code, extra) =>
  { _mem.set("hunt:"+code, JSON.stringify(Object.assign({code:code,title:"T",tiles:[]}, extra||{})));
    _mem.set("mycases", JSON.stringify([code])); };
window.__mine = async () => JSON.parse(await Store.get("mycases") || "[]");
window.__toasts = [];
(() => { const o = window.toast; window.toast = (m,d) => { window.__toasts.push(m); return o && o(m,d); }; })();
"""

RESULTS = []
def check(name, got, want):
    ok = got == want
    RESULTS.append(ok)
    print(f"  {'PASS' if ok else 'FAIL'}  {name:44} got={got!r}" + ("" if ok else f" want={want!r}"))

async def _boot(browser, url, w=390, h=844):
    pg = await browser.new_page(viewport={"width": w, "height": h})
    errs = []; pg.on("pageerror", lambda e: errs.append(str(e)))
    await pg.goto(url); await pg.wait_for_timeout(1100)
    await pg.evaluate(STUB)                      # §11b - stub before anything else
    await pg.evaluate("window.__stub({})")
    return pg, errs

async def test_purge(b, url):
    print("\npurgeCase - honest reporting (handoff §45.2)")
    pg, errs = await _boot(b, url)
    await pg.evaluate("window.__seed('111111')")
    check("server accepts -> returns true",  await pg.evaluate("purgeCase('111111')"), True)
    check("server accepts -> leaves mycases", await pg.evaluate("window.__mine()"), [])
    await pg.evaluate("window.__stub({serverFails:true})")
    await pg.evaluate("window.__seed('222222')")
    check("server refuses -> returns false", await pg.evaluate("purgeCase('222222')"), False)
    check("server refuses -> case KEPT",     await pg.evaluate("window.__mine()"), ["222222"])
    check("no page errors", errs, [])
    await pg.close()

async def test_deed_guard(b, url):
    print("\ndeleteCaseAsk - the deed guard (handoff §45.3)")
    pg, errs = await _boot(b, url)
    await pg.evaluate("window.confirm = () => true")     # would proceed if unguarded
    for code, extra, label in (("333333", "{deeded:true}", "deeded case"),
                               ("444444", "{cold:true}",   "cold case")):
        await pg.evaluate(f"window.__seed('{code}',{extra})")
        await pg.evaluate(f"State.roster='{code}'; window.__net=[]")
        await pg.evaluate("deleteCaseAsk()"); await pg.wait_for_timeout(200)
        check(f"{label} -> no delete attempted", await pg.evaluate("window.__net"), [])
        check(f"{label} -> still in mycases",    await pg.evaluate("window.__mine()"), [code])
    await pg.evaluate("window.__seed('555555')")
    await pg.evaluate("State.roster='555555'; window.__net=[]")
    await pg.evaluate("deleteCaseAsk()"); await pg.wait_for_timeout(300)
    check("ordinary case -> deletes freely", await pg.evaluate("window.__net"), ["hunt:555555"])
    check("no page errors", errs, [])
    await pg.close()

async def test_deed_gate(b, url):
    print("\nFile the Territory - the mandatory deed")
    pg, errs = await _boot(b, url)
    await pg.evaluate("openSubTerritory()"); await pg.wait_for_timeout(300)
    dis = lambda: pg.evaluate("document.getElementById('st-file').disabled")
    check("opened, nothing entered -> locked", await dis(), True)
    await pg.fill("#st-zip", "31401"); await pg.wait_for_timeout(120)
    check("valid ZIP, deed unticked -> locked", await dis(), True)
    await pg.check("#st-deed-chk"); await pg.wait_for_timeout(120)
    check("ZIP + deed ticked -> open", await dis(), False)
    await pg.uncheck("#st-deed-chk"); await pg.wait_for_timeout(120)
    check("deed un-ticked -> locked again", await dis(), True)
    await pg.check("#st-deed-chk")
    await pg.evaluate("subTerrClose()"); await pg.wait_for_timeout(150)
    await pg.evaluate("openSubTerritory()"); await pg.wait_for_timeout(250)
    check("reopen -> deed reset", await pg.evaluate("document.getElementById('st-deed-chk').checked"), False)
    await pg.evaluate("document.querySelector('.st-deed span').click()"); await pg.wait_for_timeout(120)
    check("tapping the words toggles it", await pg.evaluate("document.getElementById('st-deed-chk').checked"), True)
    tap = await pg.evaluate("(()=>{const r=document.querySelector('.st-deed').getBoundingClientRect();"
                            "return Math.round(r.height)>=44;})()")
    check("tap target >= 44px", tap, True)
    check("no page errors", errs, [])
    await pg.close()

async def test_renders(b, url):
    print("\nRenders - both reference viewports")
    for w, h in ((390, 844), (320, 568)):
        pg, errs = await _boot(b, url, w, h)
        check(f"{w}x{h} boots clean", errs, [])
        await pg.close()

async def main():
    url = "file://" + str(pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else DEFAULT).resolve())
    print("target:", url)
    async with async_playwright() as pw:
        b = await pw.chromium.launch()
        for t in (test_purge, test_deed_guard, test_deed_gate, test_renders):
            await t(b, url)
        await b.close()
    bad = RESULTS.count(False)
    print(f"\n{len(RESULTS) - bad}/{len(RESULTS)} passed")
    sys.exit(1 if bad else 0)

asyncio.run(main())
