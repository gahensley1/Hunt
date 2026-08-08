# TASK — find who requests `/null`, then decide whether it is real

Paste this whole file into Claude Code, running in `C:\Users\tony\Documents\Hunt`.

---

You are working in `C:\Users\tony\Documents\Hunt`, the repo for **The Deerstalker — A Scavenger's
Hunt** (Scavenger & Hunt Co.). Read `HANDOFF.md` §89 for the entry this task belongs to, and §11a,
§11c and §77 before you measure anything. Do not read `HANDOFF-HISTORY.md` whole — grep it.

## The symptom

`test\session_checks.py` prints a `GET /null 404` in its server log, once per boot, at both
viewports, roughly two seconds after each page load:

```
127.0.0.1 - - "GET /index.html HTTP/1.1" 200 -
127.0.0.1 - - code 404, message File not found
127.0.0.1 - - "GET /null HTTP/1.1" 404 -
```

The battery does not fail on it. **Check 4 asserts only "boots with no page errors", and a failed
subresource fetch is not a page error** — so 19/19 passes with the 404 scrolling past underneath.
That blindness is part of the task, not incidental.

## What is already ruled out — do not redo this

Session 57 established all of the following. Re-deriving it wastes the round trips that made it
worth writing down.

1. **It is a literal `fetch(null)`.** Resource type `fetch`; the URL argument is `null`, which
   stringifies to `"null"` and resolves against the origin. Not an image, not a navigation.
2. **No `fetch()` site in `index.html` can produce it.** All 18 were extracted and read. Every one
   is either a string literal (`"award-card.jpeg"`, `"og-card.jpeg"`) or a concatenation
   (`base+"/report?…"`, `this.base()+"/kv/"+…`). A null `base` yields `"null/report…"`, **not**
   `"null"`.
3. **No other network API is involved.** Zero `XMLHttpRequest.open`, zero `sendBeacon`, zero
   `EventSource` in the client.
4. **Not an image.** All 11 `.src` assignments are `data:` URIs (`SEAL_IMG`, `PAW_INK`, the coins),
   a `URL.createObjectURL`, or truthiness-guarded. No `getItem` feeds a `src`, `href` or `url`.
5. **A raw boot does not reproduce it.** Loading `index.html` with no stub and no gate produced
   **one** request total and no `/null`.
6. **CDP names no application frame.** With `Debugger.setAsyncCallStackDepth maxDepth 64`,
   `Network.requestWillBeSent` returned `initiator.type: "script"` with **no async parent chain**
   and these frames only:
   ```
   window.fetch      <- the probe's trace wrapper
   window.fetch      <- the injected stub's wrapper
   evaluate @ 317
   (anonymous) @ 0
   ```
   Had `index.html` called `fetch`, CDP would have named the function.

## The working hypothesis, which is UNPROVEN

**`/null` is an artefact of the test harness's own injected stub, not a defect in the app.**

It fits every observation above: the deepest frame is `evaluate`, the app makes no such call, and a
boot without the stub is silent. **It is not proven and must not be recorded as fact.** §11c: never
infer; validate, or label it unproven.

## The experiment that settles it

`session_checks.py`'s `boot()` does three things after `goto`: waits 1100ms, evaluates `STUB`, then
calls `gate()` — which hides `#scrollhint-ov` and calls `credFiled()`. Run the four combinations
against a local server, logging every request:

| | stub | gate | expect |
|---|---|---|---|
| A | no | no | already measured: 1 request, no `/null` |
| B | no | **yes** | ? |
| C | **yes** | no | ? |
| D | yes | yes | reproduces (already measured) |

**Whichever of B or C produces the 404 owns it.** If C, the stub is the culprit and the app is
clean. If B, `credFiled()` or something it schedules is, and it is a real bug. If neither and only
D does, the two interact — report that rather than forcing a story.

`test\find-null.py` already has the plumbing: the trace wrapper, the CDP initiator dump, the stub
and the gate as separate constants. Extend it to take a mode argument rather than writing a new
file. Run with `set PYTHONUTF8=1`.

## Then fix both halves

**If it is the harness:** fix the stub, delete §89's premise, and say plainly in the handoff that
the app was never at fault.

**If it is the app:** fix the null, and **also fix Check 4 so it fails on an unexpected 404.**
§1w — a correction is not done until every copy of the error is dead, and a test that cannot see
the bug is a copy of the error. A 404 on any request other than a deliberate one should turn the
check red.

## House rules that bite here

- **A green tick is an exit code, not a result.** A zero-width rect is not a measurement either.
- **Never hand-type a string the app generates — call the function.**
- **Aesthetics never change without asking.** This task should touch no visual output at all; if a
  fix would, stop and present options first.
- **Every `grep`/`sed` on `index.html` is length-capped** — `| cut -c1-160` on grep, `-c1-300` on
  sed. Single lines run to half a megabyte. Better: parse it in Python and print the conclusion.
- **Never commit a Worker source** (`worker-v2_*.js`, gitignored). The repo is public.
- **Do not run `git` in a way that strands `.git/index.lock`.** To ship: `ship "s57: <what>"` from
  `cmd.exe`, which stages honouring `.gitignore`, pushes, and prints local vs origin HEAD.
- **Before any ship, run the battery:** `battery` (no argument, so all three suites run).
  `33g` is green — STATIC clean, BEHAVIOUR 59/59, SESSION 19/19, Agent D drift NONE.
- **If Agent D reports DRIFT, do not rebaseline `test\baseline.json` to make it pass.** Report it.

## Report back

State which cell of the table fired, paste the CDP initiator frames verbatim, and say whether the
app is implicated. If it stays unreproducible, say so — **an unrun test and a passing test are
different things**, and §89 should record the eliminations either way.
