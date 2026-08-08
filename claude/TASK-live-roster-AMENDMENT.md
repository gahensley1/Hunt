> ⚠ **CORRECTED 6 Aug 2026 (night), session 54 — hold lifted.** *(Standing rule §1w: a correction sweeps every copy.)*
>
> **THE HOLD IS LIFTED AND THE WATCHER SHIPPED (build 32t).** `listSubsSlim` is used by both callers, as specified.

# TASK-live-roster-AMENDMENT.md — HOLD, 6 Aug 2026
Supplements TASK-live-roster.md already on the laptop. That brief is correct at
friends-and-family scale and WRONG at event scale. Diagnostic: SCALE-READINESS.md.

## The fault
Sub records for builder hunts carry every photo (~250-350 KB at 12 finds). values=1 on a
25-hunter case returns ~7.5 MB — every 2 seconds. On park LTE this exceeds the watcher's
own 4 s timeout, so every tick dies and the roster never updates at exactly the event the
feature exists for.

## The hold
Do NOT ship the watcher against plain `values=1`. Precondition added to section 0:
Worker v2.6.3 deployed, and `listSubsLite` calls `&values=1&slim=1`.

## v2.6.3 in one line
On `slim=1`, the Worker strips each returned record's `finds[].src` to `1`/`null` before
responding (the exact slim shape the client's cold branch already writes). 7.5 MB -> ~7 KB.

## Also migrate while in there
`checkFinishes` moves from `listSubs()` (1+2N full-payload requests per 12 s tick) to the
same slim call (1 request). `listSubs()` itself is untouched — the verify screen needs the
full photos and keeps them.

Claude writes worker-v2_6_3.js on request; the owner deploys, per A.1.
