# NOTE-scale-fix-addendum.md — for Cowork, evening 6 Aug 2026
Supplements TASK-scale-fix.md (bbd5e969...). Three facts changed since lunch.

## 1. Worker v2.6.3 is DEPLOYED and verified from outside
Root banner says (v2.6.3); slim=1 returns zero base64 on the test case; fat values=1
unchanged; broad prefixes still refused. TASK-scale-fix section 1 step 1 and section 2
are DONE. Start directly at section 3 (checkFinishes -> listSubsSlim), then section 4
(live roster). The hold on TASK-live-roster.md is lifted the moment section 3 ships.

## 2. Cloudflare plan confirmed: Workers FREE (owner dashboard, 6 Aug)
Free tier caps CPU at 10 ms/request. slim=1 parses every record server-side, so on a
large case (20+ hunters, photo-laden records) a slim call MAY error under the cap until
the owner upgrades to Paid ($5/mo, pre-event blocker, owner's job).

DESIGN CONSEQUENCE — DO NOT fall back to fat values=1 when a slim call fails.
That would silently resurrect the 7.5 MB payload the whole fix exists to kill.
A failed/timeout/non-OK slim response = skipped tick, exactly as the briefs already
specify (listSubsSlim returns null; caller skips). Nothing else. The roster shows its
last known state and catches up on the next good tick.

## 3. Failure-injection pass ran clean (read-only, zero writes)
403s on all broad/malformed/injection prefixes, 404 on oversized keys, PUT without
token refused AND verified unwritten, CORS sane, 12 parallel reads all 200, no 500s
anywhere. No client change needed. Known gap logged for backlog, not for you: no
rate-limit ceiling (owner can add 1 free WAF rate rule in dashboard).

## Log lines for SUPERHANDOFF.md
- v2.6.3 deployed + verified 6 Aug (slim=1 live).
- Cloudflare plan = Workers Free, confirmed 6 Aug; Paid upgrade is a pre-event blocker.
- Failure-injection pass clean; rate-limit ceiling still open (owner dashboard).
- Rule for all future readers: slim failure NEVER falls back to fat.
