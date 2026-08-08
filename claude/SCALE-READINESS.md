> ⚠ **CORRECTED 6 Aug 2026 (night), session 54 — P0-1 and P0-2 closed.** *(Standing rule §1w: a correction sweeps every copy.)*
>
> **P0-1 and P0-2 ARE FIXED** (Worker v2.6.3 `slim=1`, builds 32s/32t): a monitoring builder now costs 1 request / ~7 KB per tick instead of 51 / ~7.5 MB — measured at 329 bytes against the live Worker. **P0-3 (Pages bandwidth) and the Workers Paid upgrade remain OPEN.** The `sw.js` figure here (3,349 B) was right and SUPER-HANDOFF §0 was wrong. **A defect this file did not find: the take rate divided two different populations and read 175%% — fixed in v2.6.6 (§73).**

# SCALE-READINESS.md — diagnostic of 6 Aug 2026
Probed from outside against build `32q` (4,010,286 B, `df13a8f7...`) and Worker v2.6.2.
Zero writes made to production (rule 5c). All numbers below are measured or derived from
measured record shapes — the derivation is shown so it can be re-run.

## The scenario tested
500 hunts/day, 25 hunters per hunt, 12 tiles, builders monitoring from Case Files.

## Measured facts the maths stands on
- Photo capture: 320x320 JPEG at quality 0.72 -> ~18-30 KB base64 each (`confirmCrop`, OUT=320)
- A hunter's `sub:` record carries EVERY photo (`finds[].src`) for builder hunts; only the
  cold-case branch slims to `src:1`. Full record at 12 finds ~= 250-350 KB.
- `saveHunterSub` re-PUTs the whole record on every capture -> cumulative upload per hunter
  over a 12-find hunt ~= 1.9 MB. Acceptable.
- `listSubs()` = 1 /list + N sub GETs + N res GETs, full payloads. `checkFinishes` runs it
  every 12 s for every owned case while the app is open.
- Worker warm latency 0.10-0.12 s. values=1 verified working and gated.
- App payload: 4.01 MB total = 1.69 MB base64 art (42%) + 2.32 MB code/markup.
- sw.js live (3,349 B), network-first for the document; manifest.json still 404.
- GitHub Pages carries the app; soft bandwidth limit 100 GB/month.

## P0 — will fail AT the event this app is being built for

### P0-1. The monitoring builder downloads every photo, every 12 seconds. TODAY.
`checkFinishes` -> `listSubs` pulls all 25 full sub records: ~7.5 MB per tick,
~37 MB/min, **~2.2 GB/hour of mobile data** for a builder sitting on Case Files at one
25-hunter event. On park LTE each tick may not finish before the next. This is live now.

### P0-2. TASK-live-roster as written inherits the same bomb, 6x faster.
`values=1` on 25 photo-laden subs ~= 7.5 MB per response, every 2 s. On park LTE that
exceeds the watcher's own 4 s timeout — **every tick dies and the live roster never
updates at exactly the event it exists for.** See TASK-live-roster-AMENDMENT.md: the
watcher must not ship against full records at scale.

### THE ONE FIX FOR BOTH: Worker v2.6.3, `slim=1`.
`/list?prefix=sub:CODE:&values=1&slim=1` -> for each record, strip `finds[].src` to `1/null`
server-side before returning (the cold branch already defines this exact slim shape
client-side). 25 hunters: **7.5 MB -> ~7 KB.** Then:
- the live watcher reads slim (found/status/name/seal are all it renders)
- `checkFinishes` migrates from listSubs to the same call: 51 requests/12s -> 1
- `listSubs()` full stays for the verify screen, where the photos are the point
One Worker change + two client call sites. This is the highest-value change in this file.

### P0-3. GitHub Pages bandwidth. 
Park traffic is mostly first-visit devices. Even at 60% new devices,
7,500 x 4 MB = 30 GB/day ~= 900 GB/month against a 100 GB/month soft limit — 9x over.
Fix: move hosting behind Cloudflare (CF Pages: free, unlimited bandwidth, same account as
the Worker; the repo push flow can stay identical). Needs its own chat before any real
marketing push. Not urgent this month; mandatory before 500/day.

## P1 — costs money or headroom, does not break
- **Cloudflare plan**: 12,500 hunters x ~13 writes ~= 162k writes/day and polling reads in
  the millions. Free tier (100k req/day, 100k D1 writes/day) is exceeded on day one;
  **Workers Paid ($5/mo) is required before scale.** OWNER: confirm which plan the account
  is on. Claude cannot see the dashboard and must not (A.1).
- Join path: already optimised (`listSubNames` reads names only, in parallel).
- `/list` LIMIT 5000: 25 subs/case is nowhere near it. Fine.
- D1 record sizes (~300 KB) are comfortably within limits.

## P2 — worth knowing, no action forced
- 4 MB single file: 42% is art. sw.js makes repeats cheap; first load ~8.4 s cold in
  sandbox. Slimming art to WebP-everywhere is future polish, not a blocker.
- CORRECTED 6 Aug (evening): the manifest DID ship — build 32p, as `manifest.webmanifest`,
  linked from index.html, live 200. Earlier drafts of this file probed only manifest.json
  and called the PWA half-landed; that was wrong. PWA is whole: sw.js + manifest + icons.
- Test record `sub:999999:hINV` in D1 (stub photo, harmless; night sweep will take it).
- Worker latency and gating verified healthy. No JS/console/network errors on boot.

## Owner actions, in order
1. Confirm Cloudflare plan (paid vs free).            [2 min, dashboard]
2. Approve v2.6.3 slim=1 spec -> Claude writes the whole file, you deploy.  
3. Hold TASK-live-roster until v2.6.3 is deployed (amendment attached).
4. Schedule the hosting-migration chat before any marketing push.
5. OneDrive connector, when you're back at the desk (session-drift fix, separate thread).
