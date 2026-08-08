# SPEC — OFFLINE PLAY: THE REPLAY QUEUE AND THE SERVICE WORKER
## Session 50 edition (Aug 2 2026) — supersedes the s45 spec entirely

**The s45 spec argued this feature on bandwidth: "41% of the app re-downloaded every visit."
That number is false and was disproved by a single conditional GET — 304, zero bytes
(SUPERHANDOFF §1n). Anyone building from the s45 text builds the wrong thing. This edition
re-scopes the work to what it is actually for.**

---

## §1 — WHAT IS ACTUALLY AT RISK

There are two distinct failure modes. **A service worker fixes only one of them**, and it is
the less damaging one.

### 1a. Finds are already safe. Do not "fix" this.

`saveHunterSub()` writes the durable local copy FIRST and syncs second, and carries a comment
saying why: a shared-only write whose PUT failed used to land in an in-memory Map, die with the
app, and still return `true` — so the hunter was told "Find logged" for nothing, and a killed tab
restarted a builder hunt from zero. **The device is the system of record for finds.** That is
correct and must stay correct.

### 1b. The app will not OPEN offline. ← the service worker's only job

No shell cache. A hunter in a park with no signal gets a blank page, with their progress sitting
intact in `localStorage`, unreachable. This is the whole case for a service worker. It is a real
case, and it is the only one.

### 1c. The server copy silently falls behind. ← the queue's job

`Store.set(key,val,true)` attempts the PUT, and on failure **falls through to the in-memory Map
and returns `true`.** Before s50 there was no retry anywhere: zero occurrences of
`navigator.onLine`, zero of `retry`, no queue. The device stayed right and the Yard never heard.

Consequences: the roster shows the hunter behind; `finishedAt` — the permanent tiebreaker — never
lands; a Builder reviewing submissions sees a half-finished hunt.

**A service worker does nothing about any of this.** Hence the build order below.

---

## §2 — BUILD ORDER (NON-NEGOTIABLE)

**Queue first, service worker second.** The queue protects *status* and works with or without a
service worker. The service worker only makes the app open. Shipping the worker first would make
the offline experience *look* fixed while the sync hole stayed open.

---

## §3 — THE REPLAY QUEUE — ✅ BUILT IN `32d`

Lives inside `Store`. Constant `QUEUE_MAX_AGE = 14 days`.

| Member | Behaviour |
|---|---|
| `Store.qKey` | `"shco:pendingWrites"` in `localStorage` |
| `Store.qPush(key,val)` | drops any existing entry for that key, appends `{key,val,at}` |
| `Store.qRead()` / `qWrite(a)` | JSON in/out; `qWrite` caps the queue at the last 200 entries |
| `Store.qPending()` | queue length |
| `Store.flush()` | replays every entry newer than `QUEUE_MAX_AGE`; successes drop, failures stay |

**Design rules and the reasoning behind each:**

- **Keyed, latest-value-only.** A submission's key `sub:CODE:HID` is fixed, so a replay is a plain
  overwrite. It can never duplicate a record, and only the newest queued value per key is kept.
- **Stale entries are dropped, never replayed.** A fortnight-old value overwriting a fresher
  server record is worse than losing it.
- **`_flushing` re-entry guard.** Three triggers can fire close together; only one flush runs.
- **Headers are taken fresh at flush time** via `_curHdr()`, not captured at enqueue time.
- **Success re-triggers a flush.** A write that succeeds proves the connection is back.

**Triggers:** `window "online"` · `window "load"` (+1200 ms) · `document "visibilitychange"` when
the page becomes visible. All wrapped in `try/catch`.

**Executed against a stubbed Worker (§5c route-intercept, zero production writes), 11 assertions,
all passing:** offline write still returns true · one entry queued · re-writing the same key
dedupes to one · the LATEST value is the one kept · the queue survives a reload · `flush()`
replays both entries and returns 2 · queue drains to zero · the stub server received exactly
`sub:AAA:1` and `sub:BBB:2` · a 20-day-old entry is dropped without a request · an online write
never enters the queue · zero page errors.

---

## §4 — THE SERVICE WORKER — ✅ BUILT AS `sw.js` (3,349 B)

**Scope: offline play only. It stores no hunter data.** Finds, status and credentials live in
`localStorage` and on the Worker; losing this cache loses nothing.

`CACHE = "shco-v1"` · `SHELL = ["./", "./index.html", "./j.html", "./og-card.jpeg",
"./award-card.jpeg"]`

**The four rules, in order of how badly they bite:**

1. **NETWORK-FIRST FOR THE DOCUMENT.** `index.html` is a single 3.8 MB file. Cache-first would pin
   every returning hunter to whatever build they last loaded, **forever**, with no way to push
   them off it. Network wins; the cache is only the fallback.
2. **NEVER TOUCH THE WORKER.** Any request whose hostname contains `workers.dev` is not
   intercepted at all. A cached roster is worse than no roster.
3. **NEVER CACHE a non-GET, a non-200, or an opaque response.** Cross-origin requests (fonts) are
   left entirely to the browser.
4. **VERSIONED CACHE.** Bump `CACHE` on any ship that changes an asset. Old caches are deleted on
   `activate`.

**Install** uses per-URL `cache.add` with a `.catch()` rather than `addAll` — `addAll` is
all-or-nothing and a single 404 would fail the whole install. `skipWaiting()` on install,
`clients.claim()` on activate, plus a `SKIP_WAITING` message handler.

**Registration** is in `index.html`, gated on `location.protocol==="https:"` so it never attempts
to register from `file://` — which is how the Playwright battery runs.

---

## §5 — WHAT IS NOT PROVEN (stated plainly, §5o / §0.2)

- **The service worker has never run.** The battery loads over `file://`, where registration is
  deliberately skipped. `sw.js` passes `node --check` and nothing more. **It has not been
  installed, has not served a single request, and has never been exercised offline.**
- **No airplane-mode test has been done on hardware.** The full offline journey — load with no
  signal, log a find, regain signal, confirm the roster catches up — is untested end to end.
- **The queue was proven against a stub, not against the real Worker.** `route.fulfill` bypasses
  the browser's real connection pool (§5k).
- **`case_scanned` and the seal-on-a-real-roster remain unproven** for the same reasons.

---

## §6 — REMAINING WORK

1. Push `32d` + `sw.js`, then hard-reload twice and confirm the second load is served by the
   worker (DevTools → Application → Service Workers).
2. **Airplane-mode test on hardware.** This is the only thing that closes 7b honestly.
3. **Cache-version discipline from here on:** any ship that changes `j.html` or an image must bump
   `CACHE` in `sw.js`. `index.html` is network-first and needs no bump.
