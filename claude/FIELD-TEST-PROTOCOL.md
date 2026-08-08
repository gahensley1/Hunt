> ⚠ **CORRECTED 6 Aug 2026 (night), session 54 — prerequisites moved on.** *(Standing rule §1w: a correction sweeps every copy.)*
>
> **The prerequisite line says '32r shipped'. The live build is now 32u**, carrying the notification priming card, the live roster and web push. **Cloudflare Paid is still NOT active — that prerequisite stands.** Add a fifth gate while you are out: **a push arriving on a locked phone**, which no sandbox can prove.

# FIELD-TEST-PROTOCOL.md — one afternoon, four gates
For the OWNER and 3-5 recruits. Cowork logs the results; claude.ai diagnoses failures.
Prereq: 32r shipped (slim path + live roster), Cloudflare Paid active.
Bring: 2+ Android, 1+ iPhone (non-negotiable — WebKit is where PWAs break), a printed
case QR, a known dead spot on the route (parking garage, deep aisle, trailhead dip).

## Leg 1 — install & join (gate: iOS PWA)
1. Every phone: scan the QR, open in the default browser, complete join.
2. iPhone specifically: Share -> Add to Home Screen; reopen from the icon.
   PASS = standalone (no browser chrome), camera permission prompts once and works.
3. Note first-load seconds on cellular per phone (expect the 4 MB file to be the cost).

## Leg 2 — the hunt itself (gate: dress rehearsal)
4. Run the case start to finish. Every hunter: join -> capture all finds -> submit.
5. Builder phone: roster open. PASS = counts move ~2-3 s after each capture, no
   interaction; commendation card, seals, dispatch card all appear where designed.
6. Builder leaves roster screen mid-hunt, returns. PASS = updates resume, no stacking.

## Leg 3 — the dead spot (gate: offline-first sync). THE IRREPLACEABLE TEST.
7. One hunter walks into the dead spot, captures TWO finds fully offline.
8. Still offline: kill the tab/app outright. Reopen. PASS = both finds present locally.
9. Walk out to coverage, wait ~15 s. PASS = builder roster shows both; count correct,
   nothing doubled.
10. Airplane-mode variant on a second phone: toggle on, capture one, toggle off.
    PASS = same result. Note exact times; screenshots of any wrong count.

## Leg 4 — collisions (gate: concurrency)
11. Two hunters photograph THE SAME tile within ~1 s of each other. PASS = each has
    their own find; neither blocked; builder sees both.
12. Stage the two leaders to submit/finish within the same second (count down out loud).
    PASS = standings render two distinct places, stable order on refresh (finishedAt
    millisecond tiebreak). Screenshot the standings immediately.
13. All hunters background the app, then foreground together on a count of three.
    PASS = every roster/standings view correct within ~5 s, no error toasts.

## Recording
For every FAIL: phone model, OS, screenshot, clock time, what was expected. That tuple
is enough for diagnosis without guesswork. File results in claude/FIELD-RESULTS-<date>.md
on the laptop so Cowork and claude.ai both read the same record.
