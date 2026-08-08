> ⚠ **CORRECTED 6 Aug 2026 (night), session 54 — shipped in 32t.** *(Standing rule §1w: a correction sweeps every copy.)*
>
> **DONE, shipped as build 32t.** Section 0 refers to Worker v2.6.2; the live Worker is v2.6.5. **⚠ §5b OF THIS BRIEF HAD A HOLE:** the watcher calls `renderRoster()`, which itself calls the FAT `listSubs()` — as written it would have re-downloaded every photograph every 2 seconds, relocating the very bomb the amendment existed to defuse. Built with `renderRoster(pre, resMap, light)` instead (§68.2). **§7's two-device test is NOT done and still needs a phone.**

# TASK-live-roster.md
**For Cowork, on the laptop. Session 52 continuation.**
Written from claude.ai on 5 August 2026. Owner-approved scope. Ships AFTER the Worker deploy.

---

## 0 — Order of operations. Do not vary it.

1. Owner deploys **`worker-v2_6_2.js`**. Claude has no Cloudflare access and never will (A.1).
2. Probe the ROOT path and confirm `(v2.6.2)`. `/status` is a 404 — that is a wrong URL, not
   a failed deploy.
3. Confirm the old shape still works: `GET /list?prefix=sub:CODE:` must return `{keys, more}`
   with no `values` field. Every existing caller depends on that being unchanged.
4. Confirm the new shape: `GET /list?prefix=sub:CODE:&values=1` returns `{keys, values, more}`.
5. Only then patch `index.html`.

**If step 3 or 4 fails, stop.** Do not ship the client against an unverified Worker.

---

## 1 — What is being built, in one line

While a builder has one case's roster open on screen, each hunter's `n / 12 found` updates
about two seconds after that hunter takes the photograph.

---

## 2 — Scope. Owner instruction, 5 Aug 2026, verbatim:

"only when the case is opened and roster is viewed it will update in real time"

That is the whole boundary. The watcher:

- runs for **one case** — the one whose roster is on screen
- **starts** in `openRoster(code)`
- **is cleared**, not paused, on leaving `#s-roster`
- **pauses** on `document.hidden`, resumes on `visibilitychange`
- **never** runs for cases the builder is not looking at

The existing 12-second `_finTimer`, which sweeps every owned case for finishes, is **untouched**.
Do not fold this into it. Do not raise its frequency. The polling floor for a builder who is not
watching anything must stay exactly where it is today.

---

## 3 — The numbers, and why

| | value | reason |
|---|---|---|
| tick | **2000 ms** | Below this buys nothing. The hunter's own chain — shutter, local write, PUT — is roughly 0.5-1.5s, so end-to-end is 2.5-3.5s however fast the builder polls. |
| watcher timeout | **4000 ms** | `NET_MS` is 12000. A poll answer arriving ten seconds late is worthless — four ticks have superseded it. Let a slow tick miss. |
| requests per tick | **1** | `?values=1`. This is the entire reason for the Worker change. |

At one request every two seconds that is 30 a minute, less than a fifth of what the existing
finish poll already costs across a builder's cases.

---

## 4 — The two guards. Both are required.

**Guard 1 — never stack.** `NET_MS` is 12000ms, so a request can hang for twelve seconds. On a
two-second tick that is six overlapping fetches on a bad connection. Hold an in-flight flag and
skip the tick while one is outstanding. Clear the flag in a `finally`, not on success.

**Guard 2 — its own signal.** Pass a 4000ms abort signal, not the default. `_sig(4000)` already
exists and does the right thing where `AbortController` is missing.

---

## 5 — The patch

### 5a — A light read, values in one call

`listSubs()` is the wrong tool here. It costs `Store.list` + one GET per hunter + a second GET
per hunter for the `res:` record, and it sorts by the Standing Rule. The watcher needs none of
that: `res:` only affects confirmed-score, which only matters for entries already filed.

Add a sibling that reads the values in a single request:

    async function listSubsLite(code, sig){
      const base = Store.base && Store.base();
      if(!base) return null;
      const r = await fetch(base + "/list?prefix=" + encodeURIComponent("sub:"+code+":") + "&values=1",
                            { headers: Object.assign({}, _curHdr()), signal: _sig(4000, sig) });
      if(!r.ok) return null;
      const j = await r.json();
      const vals = (j && j.values) || {};
      const out = [];
      for(const k of Object.keys(vals)){
        try{ out.push(JSON.parse(vals[k])); }catch(e){}
      }
      return out;
    }

Returns `null` on any failure — offline, 403, timeout, malformed. **A null result is a skipped
tick, never an empty roster.** Rendering zero hunters because a poll timed out would be a far
worse bug than a stale count.

`_curHdr()` is pre-existing; the call needs no token for a case-scoped prefix.

### 5b — The watcher

    let _rosterWatch = null, _rosterSig = "", _rosterBusy = false;

    function startRosterWatch(code){
      stopRosterWatch();
      _rosterSig = "";
      _rosterWatch = setInterval(async () => {
        if(document.hidden) return;
        if(_rosterBusy) return;                       // Guard 1
        if(State.roster !== code) return;             // belt and braces
        const el = document.getElementById("s-roster");
        if(!el || !el.classList.contains("active")) return;
        _rosterBusy = true;
        try{
          const subs = await listSubsLite(code);
          if(!subs) return;                           // skipped tick, not an empty roster
          const sig = subs.map(s => s.hid + ":" + (s.found||0) + ":" + (s.status||""))
                          .sort().join("|");
          if(sig === _rosterSig) return;              // nothing moved; no churn
          _rosterSig = sig;
          await renderRoster();
        }catch(e){ /* a missed tick is not an error the builder needs to see */ }
        finally{ _rosterBusy = false; }
      }, 2000);
    }

    function stopRosterWatch(){
      if(_rosterWatch){ clearInterval(_rosterWatch); _rosterWatch = null; }
      _rosterBusy = false;
    }

The signature includes `status` so a hunter filing mid-watch also redraws the pill.

### 5c — Wiring

- `openRoster(code)` — call `startRosterWatch(code)` after the existing `await renderRoster()`.
- Every path that leaves the roster screen — call `stopRosterWatch()`. Grep `go("s-` and find
  the ones reachable from the roster. **Missing one leaves a two-second poll running forever.**
  If a single choke point exists in `go()`, prefer clearing there: `if(id !== "s-roster")
  stopRosterWatch();`
- Add a `visibilitychange` listener that calls the tick body once on resume, so a builder who
  unlocks their phone does not wait two seconds for the first refresh.

### 5d — 🔴 NO TOAST

The builder gets **no notification** for a progress change. Toasts stay reserved for finishes,
which `checkFinishes()` already handles. A builder watching six hunters would otherwise be
pinged every time somebody photographs a mailbox.

The row simply redraws. If any animation is added at all, it is a brief highlight on the changed
row and nothing more — and per the aesthetics rule, **show the owner before shipping it.**

---

## 6 — Battery, before the ship

Standing battery, plus six specific to this change.

1. `node --check` on the extracted script.
2. Tag balance delta vs pristine base.
3. Hygiene: no `console.log`, no CRLF, no http audit failures.
4. Paid-flag parity: 35 entries, 8 free, 0 mismatches.
5. Playwright render at 390x844 and 320x568.
6. **New — the watcher dies.** Open a roster, leave the screen, and confirm in the network panel
   that requests stop. **This is the most important check in this list.** A leaked interval is a
   permanent background poll on the owner's users' phones.
7. **New — the watcher does not stack.** Throttle the network to slow 3G, watch for sixty
   seconds, confirm no more than one `/list` in flight at any moment.
8. **New — a failed poll does not empty the roster.** Block the Worker origin, confirm the rows
   stay on screen with their last known counts and nothing renders as zero hunters.
9. **New — hidden tab is silent.** Background the tab, confirm requests stop, foreground it and
   confirm one immediate refresh.
10. **New — no toast fires** on a progress change. Only on a finish.
11. **New — the old callers still work.** `listSubs()` is unchanged and still used by the roster
    render, the standings and `checkFinishes()`. Confirm all three still work against v2.6.2.

`document.elementFromPoint` occlusion check before any screenshot.

---

## 7 — Two-device test, on hardware

The sandbox cannot prove this. It needs two devices.

1. Phone A: builder, roster open on a live case.
2. Phone B: hunter, joined to that case.
3. B photographs a find. **A's count moves within about three seconds, with no interaction.**
4. B photographs four more in quick succession. A's count follows, and does not skip or reorder.
5. A backgrounds the app for a minute; B finds two more. A foregrounds and the count is correct
   immediately, not two seconds later.
6. B goes into airplane mode mid-hunt, finds nothing, comes back. Nothing on A regresses.

---

## 8 — Log this in SUPERHANDOFF.md

- Worker at **v2.6.2**. Record the deployed version, the probe result from the ROOT path, and the
  new source of record `claude/worker-v2_6_2.js` with its byte count and SHA-256.
- `/list` now accepts `&values=1` for case-scoped prefixes only. Note the gate and the reason
  (LIST_LIMIT is 5000; a broad prefix with values inlined is a memory event).
- Live roster watcher: 2s tick, 4s timeout, one request per tick, scoped to the open roster only.
  Owner instruction quoted verbatim in section 2 above.
- Note that `_finTimer` at 12s was deliberately left alone.
