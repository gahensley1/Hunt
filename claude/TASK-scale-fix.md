> ⚠ **CORRECTED 6 Aug 2026 (night), session 54 — fully implemented.** *(Standing rule §1w: a correction sweeps every copy.)*
>
> **DONE. Do not re-run.** v2.6.3 deployed and verified; `checkFinishes` migrated to `listSubsSlim` in build 32s. **⚠ §3 OF THIS BRIEF HAD A HOLE:** it says `checkFinishes` needs status/finishedAt only — it also calls `rankMap()`, whose order comes from `listSubs()`'s confirmed-score sort, so a verbatim swap would have printed arbitrary placings in the toast. Built with `rankSlim()` instead (§67.3).

# TASK-scale-fix.md — for Cowork. READ BEFORE TASK-live-roster.md.
Written from claude.ai, 6 Aug 2026, after the scale diagnostic in SCALE-READINESS.md.
This file changes the order of work and adds one client patch. It supersedes nothing
else — the seals and commendation briefs are untouched by any of this.

---

## 0 — What the diagnostic found, in three lines

1. A builder-hunt `sub:` record carries every photograph inside it (~300 KB at 12 finds).
2. `checkFinishes` -> `listSubs()` therefore downloads ~7.5 MB every 12 s while a builder
   sits on Case Files at a 25-hunter case — about 2.2 GB/hour of their mobile data. Live today.
3. `TASK-live-roster.md` as originally written would do the same at 2 s cadence and its own
   4 s timeout would kill every tick on park LTE. It is ON HOLD until the fix below is in.

The fix for both is one Worker parameter plus two small client changes.

---

## 1 — Order of work

1. OWNER deploys `worker-v2_6_3.js` (already written and syntax-checked; Claude never
   deploys, A.1). Verify per section 2.
2. COWORK patches `checkFinishes` off the fat path — section 3. Ships as its own build.
3. COWORK then runs `TASK-live-roster.md` WITH the one-line change in section 4.

Steps 2 and 3 may ship together if the battery covers both.

---

## 2 — Verifying the v2.6.3 deploy, from outside

    ROOT                          -> banner says (v2.6.3)
    /list?prefix=sub:999999:                    -> {keys, more}            (unchanged)
    /list?prefix=sub:999999:&values=1           -> {keys, values, more}    (unchanged, fat)
    /list?prefix=sub:999999:&values=1&slim=1    -> same shape, and the value string
                                                   contains NO "base64" anywhere
    /list?prefix=hunt:&values=1&slim=1 (no token) -> refused ("the archivist...")

The slim transform was proven against the real record shape before this was written:
`finds:[{tileId:"t1",src:"data:image/jpeg;base64,..."}]` -> `[{tileId:"t1",src:1}]`,
malformed values pass through unmodified (fails fat, never drops a hunter).

---

## 3 — Client patch A: checkFinishes stops downloading photographs

`checkFinishes` needs status/finishedAt per hunter and nothing else. Today it calls
`listSubs(code)`: 1 list + N sub GETs + N res GETs, full payloads, every 12 s per owned case.

Replace its data source with one slim call. Add (or share with the watcher):

    async function listSubsSlim(code, sig){
      const base = Store.base && Store.base();
      if(!base) return null;
      const r = await fetch(base + "/list?prefix=" + encodeURIComponent("sub:"+code+":")
                            + "&values=1&slim=1",
                            { headers: Object.assign({}, _curHdr()), signal: _sig(4000, sig) });
      if(!r.ok) return null;
      const j = await r.json();
      const vals = (j && j.values) || {};
      const out = [];
      for(const k of Object.keys(vals)){ try{ out.push(JSON.parse(vals[k])); }catch(e){} }
      return out;
    }

In `checkFinishes`, swap `await listSubs(code)` for `await listSubsSlim(code)`, and treat a
`null` return as a skipped tick (offline), exactly as the watcher brief specifies. The
fresh-finish filter reads `finishedAt`, which slim records carry untouched.

**Do not touch `listSubs()` itself.** The verify screen and the standings read it and need
the full records — the photographs are the verify screen's whole point. Confirm after the
patch that `listSubs(` still has its call sites and `checkFinishes` is no longer one of them.

Cost change per 12 s tick at 25 hunters: 51 requests / ~7.5 MB  ->  1 request / ~7 KB.

---

## 4 — Client patch B: the live-roster brief, amended in one line

Run `TASK-live-roster.md` as written, except its `listSubsLite` fetch URL gains `&slim=1`
(or simply use `listSubsSlim` above for both callers — one function, two masters, preferred).
Everything else in that brief stands: 2 s tick, 4 s timeout, in-flight guard, cleared on
leaving the roster, no toast.

Its section 0 steps 1-4 are ALREADY SATISFIED for v2.6.3 once section 2 above passes —
do not re-verify v2.6.2.

---

## 5 — Battery additions (on top of each brief's own)

1. **No photographs on the poll paths.** With the roster open and DevTools recording,
   confirm no response on the 2 s or 12 s cadence contains `base64`. One string search
   over the HAR is sufficient and objective.
2. **Verify screen still shows photographs.** Open a submitted entry; the photos render.
   This proves `listSubs()` was left alone.
3. **Standings unchanged.** Confirmed-score sorting still works (it reads `res:` via
   `listSubs`, untouched).
4. **Fresh-finish toast still fires** off the slim data (finishedAt present in slim).
5. Tick cost measured: one request per 12 s sweep per case, one per 2 s while watching.

---

## 6 — Log in SUPERHANDOFF.md

- Worker v2.6.3: slim=1 on values listings; deployed <date>, verified from outside.
- checkFinishes migrated to listSubsSlim: 51 req / 7.5 MB per tick -> 1 req / 7 KB.
- Live roster shipped per TASK-live-roster.md + slim; the hold is lifted.
- The structural fact for the record: builder-hunt sub records carry photographs; any NEW
  reader that polls them must use slim=1 or fetch keys only. Photo-splitting the schema
  (sub + subph:) remains the long-term fix, backlogged, its own chat.
- SCALE-READINESS.md filed; P0-3 (Pages bandwidth -> Cloudflare hosting) and the
  Cloudflare-plan confirmation remain open OWNER items.
