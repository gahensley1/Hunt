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
    await gate(pg)                               # §5b - every headless run is a first run
    return pg, errs

# --------------------------------------------------------------------------
# §5b  THE CAPTURE GATE.  Dismiss the first-run cards by their OWN mechanisms,
# never by looks - #scrollhint-ov and #ov-name are visual twins.  Call this
# AFTER the final navigation: go(), renderCurator() and loadCaseSheet() can all
# re-summon the welcome card, and ensureCred() re-summons #cred-ov.
# --------------------------------------------------------------------------
# A test for a feature that may not exist in the build under test must FAIL, not
# HANG. wait_for_selector blocks for its whole timeout on a pristine base, which
# turns an isolation run (Sec 5g) into a stall. Probe briefly, then give up.
async def present(pg, sel, name, ms=4000):
    try:
        await pg.wait_for_selector(sel, timeout=ms)
        return True
    except Exception:
        check(f"{name} exists in this build", False, True)
        return False

async def gate(pg):
    await pg.evaluate("""() => {
      const sh = document.getElementById('scrollhint-ov');
      if (sh) sh.classList.add('hidden');
      try { credFiled(); } catch (e) {}
    }""")
    await pg.wait_for_timeout(60)

# --------------------------------------------------------------------------
# §5n  OPEN-OVERLAY PROBE.  Overlays are opened by openOverlay(), which adds
# .open - they are NOT merely un-.hidden.  Filtering on `.overlay:not(.hidden)`
# also matches SCREENS (.screen uses .active, not .hidden) and returned a
# twelve-id list in s45 that made the stacking assertion inconclusive.
# Filter on .open.  #ov-loupe and #ov-rotate are not .overlay elements (§5u),
# so ask for .open across the document rather than within the .overlay family.
# --------------------------------------------------------------------------
async def open_overlays(pg):
    return await pg.evaluate(
        "[...document.querySelectorAll('.open')]"
        ".filter(e => e.id && /^(ov-|cold|colddetail|curator|curpass|agencymsg|cred|scrollhint)/.test(e.id))"
        ".map(e => e.id)")

# --------------------------------------------------------------------------
# §5m  "Visible" is not "on top."  The centre of the overlay's own card must
# hit the overlay or one of its descendants.  A positive control first (§5e).
# --------------------------------------------------------------------------
async def on_top(pg, ov_id):
    return await pg.evaluate("""(id) => {
      const ov = document.getElementById(id);
      if (!ov) return 'no-such-overlay';
      const card = ov.firstElementChild || ov;
      const r = card.getBoundingClientRect();
      if (!r.width || !r.height) return 'zero-box';
      const el = document.elementFromPoint(r.left + r.width / 2, r.top + r.height / 2);
      if (!el) return 'nothing-at-point';
      return ov.contains(el) ? true : (el.id || el.className || el.tagName);
    }""", ov_id)

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
    # Stage one is confirm(); stage two is prompt() and demands the number in
    # writing. Headless Chromium auto-dismisses BOTH, so a test that stubs only
    # confirm() reads a working guard as a broken delete. Stub both.
    await pg.evaluate("window.confirm = () => true")     # would proceed if unguarded
    await pg.evaluate("window.prompt = (m) => (String(m).match(/\\b(\\d{6})\\b/) || [])[1] || null")
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
    # A case keeps its submissions WITH it, so purgeCase strikes both. Assert the
    # whole contract, sorted - the two deletes are concurrent and unordered.
    check("ordinary case -> deletes freely", sorted(await pg.evaluate("window.__net")),
          ["hunt:555555", "submission:555555"])
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

async def test_capture_gate(b, url):
    print("\n§5b capture gate + §5n open-overlay probe")
    pg, errs = await _boot(b, url)
    check("gate clears every first-run card", await open_overlays(pg), [])
    await pg.evaluate("openOverlay('ov-clue')"); await pg.wait_for_timeout(150)
    check("probe sees a deliberately opened overlay", await open_overlays(pg), ["ov-clue"])
    check("§5m it is genuinely on top", await on_top(pg, "ov-clue"), True)
    await pg.evaluate("closeOverlay('ov-clue')"); await pg.wait_for_timeout(150)
    check("probe sees it close again", await open_overlays(pg), [])
    check("no page errors", errs, [])
    await pg.close()

async def test_hint_guide(b, url):
    print("\n.hint-guide is reachable by id (open item 41)")
    pg, errs = await _boot(b, url)
    check("the guide line carries an id", await pg.evaluate(
        "!!document.getElementById('crop-hint-guide')"), True)
    check("visible before the hint is opened", await pg.evaluate(
        "(()=>{const e=document.getElementById('crop-hint-guide');"
        "return !!e && getComputedStyle(e).display !== 'none';})()"), True)
    await pg.evaluate("toggleTileHint('crop')"); await pg.wait_for_timeout(150)
    check("hidden once the hint field opens", await pg.evaluate(
        "(()=>{const e=document.getElementById('crop-hint-guide');"
        "return !!e && getComputedStyle(e).display === 'none';})()"), True)
    check("no page errors", errs, [])
    await pg.close()

async def test_particulars(b, url):
    print("\nSubmissions - the curator may edit anything the builder filed")
    pg, errs = await _boot(b, url)
    await pg.evaluate("""() => {
      window.__seedSub = async (code, rec) => {
        await Store.set("hunt:" + code, JSON.stringify(
          {code: code, title: "A Filed Case", tiles: [{id: code + "t1", type: "photo", clue: "x"}]}), true);
        await Store.set("submission:" + code, JSON.stringify(rec), true);
      };
    }""")
    await pg.evaluate("""window.__seedSub('310403', {code:'310403', title:'A Filed Case',
        zip:'0000', place:'Wright Square', city:'Savannah', desc:'A short walk about the squares.'})""")
    await pg.evaluate("State.curTab='subs'; renderCurator()")
    if not await present(pg, "#cgeo-zip-310403", "the PARTICULARS block"):
        await pg.close(); return
    await gate(pg)                                   # renderCurator re-summons the welcome card

    # every submitted field arrives in a live control, prefilled
    for fid, want in (("cplace-310403", "Wright Square"), ("cgeo-city-310403", "Savannah"),
                      ("cgeo-zip-310403", "0000"), ("cdesc-310403", "A short walk about the squares.")):
        check(f"{fid} prefilled", await pg.evaluate(f"document.getElementById('{fid}').value"), want)

    # a bad zip must land the curator IN the field, not send them elsewhere
    await pg.evaluate("window.__toasts=[]")
    await pg.evaluate("subAccept('310403')"); await pg.wait_for_timeout(400)
    check("bad zip -> focus moves to the zip field",
          await pg.evaluate("document.activeElement && document.activeElement.id"), "cgeo-zip-310403")
    check("bad zip -> not filed", await pg.evaluate(
        "(async()=>{const r=await Store.get('cold:index',true);return r?JSON.parse(r).some(e=>e.code==='310403'):false;})()"), False)
    check("bad zip -> names the field, not Review / Edit", await pg.evaluate(
        "(window.__toasts.slice(-1)[0]||'').indexOf('correct it above') >= 0"), True)

    # corrected on the row, the row is what gets filed
    await pg.fill("#cgeo-zip-310403", "31401")
    await pg.fill("#cplace-310403", "Chippewa Square")
    await pg.fill("#cgeo-state-310403", "GA")
    await pg.evaluate("subAccept('310403')"); await pg.wait_for_timeout(600)
    entry = await pg.evaluate(
        "(async()=>{const r=await Store.get('cold:index',true);"
        "return (JSON.parse(r||'[]').find(e=>e.code==='310403'))||null;})()")
    check("filed with the CORRECTED zip", (entry or {}).get("zip"), "31401")
    check("filed with the CORRECTED place", (entry or {}).get("place"), "Chippewa Square")
    check("filed with the state the builder never gave", (entry or {}).get("state"), "GA")
    check("geo-tagged from the corrected zip", isinstance((entry or {}).get("lat"), (int, float)), True)
    check("submission cleared from the desk", await pg.evaluate(
        "(async()=>!(await Store.get('submission:310403',true)))()"), True)
    check("no page errors", errs, [])
    await pg.close()

async def test_terr_info(b, url):
    print("\nTerritories - Edit Info amends a filed case")
    pg, errs = await _boot(b, url)
    await pg.evaluate("""async () => {
      await Store.set("hunt:310403", JSON.stringify({code:"310403", title:"A Matter of the Squares",
        cold:true, cat:"", paid:false, place:"The Historic Squares", blurb:"Old teaser",
        tiles:[{id:"310403t1", type:"photo", clue:"x"}]}), true);
      await Store.set("cold:index", JSON.stringify([{code:"310403", title:"A Matter of the Squares",
        place:"The Historic Squares", blurb:"Old teaser", cat:"", paid:false, price:"",
        city:"Savannah", zip:"31401", diff:2, lat:0.1234, lon:0.5678}]), true);
    }""")
    await pg.evaluate("State.curTab='terr'; renderCurator()")
    if not await present(pg, ".terr-info", "the Edit Info control"):
        await pg.close(); return
    await gate(pg)

    check("particulars start folded away", await pg.evaluate(
        "document.getElementById('terr-part-310403').classList.contains('hidden')"), True)
    await pg.click(".terr-info"); await pg.wait_for_timeout(200)
    check("Edit Info unfolds them", await pg.evaluate(
        "!document.getElementById('terr-part-310403').classList.contains('hidden')"), True)
    check("the control renames itself", await pg.evaluate(
        "document.querySelector('.terr-info').textContent"), "Hide Info")
    for fid, want in (("cplace-310403", "The Historic Squares"), ("cgeo-city-310403", "Savannah"),
                      ("cgeo-zip-310403", "31401"), ("cblurb-310403", "Old teaser")):
        check(f"{fid} prefilled", await pg.evaluate(f"document.getElementById('{fid}').value"), want)

    # a bad zip is refused in place, exactly as on the submission row
    await pg.fill("#cgeo-zip-310403", "0000")
    await pg.evaluate("window.__toasts=[]")
    await pg.click(".terr-save"); await pg.wait_for_timeout(400)
    check("bad zip -> focus lands in the field",
          await pg.evaluate("document.activeElement && document.activeElement.id"), "cgeo-zip-310403")
    check("bad zip -> nothing written", await pg.evaluate(
        "(async()=>{const r=JSON.parse(await Store.get('cold:index',true));return r[0].zip;})()"), "31401")

    # a real amendment lands, and the stale pin does NOT survive the move
    await pg.fill("#cgeo-zip-310403", "31404")
    await pg.fill("#cplace-310403", "Bonaventure Cemetery")
    await pg.fill("#cblurb-310403", "A new teaser")
    await pg.click(".terr-save"); await pg.wait_for_timeout(700)
    e = await pg.evaluate(
        "(async()=>{const r=JSON.parse(await Store.get('cold:index',true));"
        "return r.find(x=>x.code==='310403')||null;})()")
    check("zip amended", (e or {}).get("zip"), "31404")
    check("place amended", (e or {}).get("place"), "Bonaventure Cemetery")
    check("teaser amended", (e or {}).get("blurb"), "A new teaser")
    check("stale pin discarded, coords re-derived", (e or {}).get("lat") != 0.1234, True)
    check("still free, still filed by territory",
          [(e or {}).get("cat"), (e or {}).get("paid")], ["", False])
    check("the hunt record followed", await pg.evaluate(
        "(async()=>{const h=JSON.parse(await Store.get('hunt:310403',true));return h.place;})()"),
        "Bonaventure Cemetery")
    check("no page errors", errs, [])
    await pg.close()

# --------------------------------------------------------------------------
# Cold archive - THE PRECINCT BANNER, THE FILTER CHIP AND THE LIST ARE THREE
# VIEWS OF ONE STATE (§97/§98).  s59, Claude Code.
#
# openColdCases() defaults State.coldQ to a NEAR filter on the hunter's
# registered precinct (§98).  Three surfaces then describe "cases near you":
#   1. #precinct-bar   drawn by precinctApply() - counts a lat/lon BOX
#                      (|dlat|<=0.5, |dlon|<=0.65 ~ 34 mi half-extent)
#   2. #cold-filterbar the chip - SHOWING n IN PRECINCT z, n = coldFilter length
#   3. #cold-list      the rows - coldFilter near-mode = coldNear(), a 25-mi RADIUS
# The box and the radius are DIFFERENT geometries, so a case in the 25-34 mi
# ring is counted by the banner but excluded by the list.  The controls below
# pass on shipped data (every real case sits inside 25 mi of its precinct); the
# ring assertion FAILS on 34e and is the finding - see CLAUDE-CODE-s59-findings.md.
# Seeding writes only to the stubbed Store (§11b); nothing reaches the Worker.
# --------------------------------------------------------------------------
async def _cold_views(pg, pz, seed_ring):
    return await pg.evaluate("""async ([pz,seedRing])=>{
      const g=gazLookup(pz); if(!g) return {err:'no gaz '+pz};
      let arr=[];
      if(seedRing) arr.push({code:"909090",title:"Ring Case",place:"North Ridge",
        city:"Ringtown",zip:"00000",cat:"",paid:false,diff:1,lat:g.ll[0]+0.45,lon:g.ll[1]});
      await Store.set("cold:index", JSON.stringify(arr), true);   // stubbed - never the Worker
      localStorage.setItem("sh_precinct", pz);
      const q=document.getElementById("cold-q"); if(q) q.value="";  // empty box, so §98 default fires
      State.coldQ=null; State.coldCat=null;
      await openColdCases();
      await new Promise(r=>setTimeout(r,500));
      const bar=document.getElementById("precinct-bar");
      const chip=document.getElementById("cold-filterbar");
      const barTxt=bar?bar.textContent:"";
      const chipTxt=chip?((chip.querySelector('.cfb-txt')||{}).textContent||""):"";
      /* s60: the banner reads "PRECINCT z - n CASES OPEN" since the Agency Cases rename
         (34k). It said "n COLD CASE(S) OPEN" before. ONLY THE PARSER MOVED - the
         assertion below is still banner == list, unchanged. */
      const mB=barTxt.match(/(\\d+)\\s+CASES?\\s+OPEN/);
      const mC=chipTxt.match(/SHOWING\\s+(\\d+)/);
      return {banner: mB?+mB[1]:null, chip: mC?+mC[1]:null,
              listRows: document.querySelectorAll("#cold-list .coldrow").length,
              coldQ: State.coldQ?State.coldQ.mode:null};
    }""", [pz, seed_ring])

async def test_cold_precinct_views(b, url):
    print("\nCold archive - precinct banner / filter chip / list are three views of one state (§98)")
    # CONTROLS: shipped precincts whose real cases all sit inside PARK_NEAR_MI.
    # These PASS - proof the invariant holds and the check is not vacuous (§11d rule 2).
    pg, errs = await _boot(b, url)
    v = await _cold_views(pg, "60602", False)
    check("Chicago 60602: banner == list", v["banner"], v["listRows"])
    check("Chicago 60602: chip == list",   v["chip"],   v["listRows"])
    await pg.close()
    pg, errs = await _boot(b, url)
    v = await _cold_views(pg, "31401", False)
    check("Savannah 31401: banner == list", v["banner"], v["listRows"])
    check("Savannah 31401: chip == list",   v["chip"],   v["listRows"])
    await pg.close()
    # DEFECT: one extra case 31 mi north of the precinct - inside the banner's box,
    # outside the list's 25-mi radius. Chicago keeps 5 real cases in range so the
    # near-filter stays applied; the banner then over-counts. banner 6 vs list 5.
    # RED on 34e BY DESIGN - it is the defect. Fix precinctApply() to count by
    # coldNear()/PARK_NEAR_MI, then this goes green. (§98, CLAUDE-CODE-s59-findings.md)
    pg, errs = await _boot(b, url)
    v = await _cold_views(pg, "60602", True)
    check("Chicago 60602 +31mi ring: banner == applied filter count", v["banner"], v["listRows"])
    check("no page errors", errs, [])
    await pg.close()

async def main():
    url = "file://" + str(pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else DEFAULT).resolve())
    print("target:", url)
    async with async_playwright() as pw:
        b = await pw.chromium.launch()
        for t in (test_purge, test_deed_guard, test_deed_gate,
                  test_capture_gate, test_hint_guide, test_particulars,
                  test_terr_info, test_cold_precinct_views, test_renders):
            await t(b, url)
        await b.close()
    bad = RESULTS.count(False)
    print(f"\n{len(RESULTS) - bad}/{len(RESULTS)} passed")
    sys.exit(1 if bad else 0)

asyncio.run(main())