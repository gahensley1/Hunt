> ⚠ **CORRECTED 6 Aug 2026 (night), session 54 — Phase 1 is complete.** *(Standing rule §1w: a correction sweeps every copy.)*
>
> **PHASE 1 IS DONE — start reading at Phase 2.** It shipped as FOUR builds, not one: 32r the notification card · 32s the slim poll · 32t the live roster watcher · 32u web push. Worker went v2.6.3 → v2.6.4 → v2.6.5 (subscription hole closed), and **v2.6.6 is written and awaiting deploy** (take-rate fix). Cloudflare plan confirmed FREE; the Paid upgrade in Phase 2 remains the pre-event blocker. The buildmark guidance in item 3 is wrong — see 00-README's banner.

# PLAN-push.md — the road from 32q to the stores
Written 6 Aug 2026 from claude.ai after the scale diagnostic, failure-injection pass,
v2.6.3 deploy, and plan confirmation. This is the master sequence. Each item names its
owner: OWNER (G), COWORK (laptop builds), FIELD (bodies and phones), CLAUDE.AI (design/
verification/worker source). Current state it starts from:

    live build 32q (4,010,286 B, df13a8f7...), both surfaces identical
    Worker v2.6.3 deployed and verified (slim=1 live)
    Cloudflare plan: Workers FREE (confirmed in dashboard 6 Aug)
    PWA whole: sw.js + manifest.webmanifest + icons (32p)
    claude/ folder is NOT in git — laptop disk is the only durable copy of briefs

## Phase 1 — engineering closeout (COWORK, this week)
1. Read TASK-scale-fix.md, then NOTE-scale-fix-addendum.md. v2.6.3 is already deployed;
   start at the checkFinishes patch. THE ONE HARD RULE: slim failure never falls back to
   fat values=1.
2. Then TASK-live-roster.md with its AMENDMENT (add &slim=1 / use listSubsSlim). Hold is
   lifted once checkFinishes ships.
3. Buildmark: next ship is 32r = Ochre #C88A2E. Rotation resumed per rule 8i after the
   32q drift; continue s Rose, t Amethyst, u Verdigris from there.
4. Log everything in SUPERHANDOFF.md, including: Cloudflare plan Free confirmed 6 Aug;
   paid upgrade is a pre-event blocker; failure-injection pass clean; rate-limit gap open.

## Phase 2 — infrastructure (OWNER, before the first 25-hunter event)
5. Cloudflare: add payment method, upgrade Workers Free -> Paid ($5/mo). Reason on file:
   free 10 ms CPU cap can break big-case slim calls; free request/write caps die at scale.
6. Cloudflare: add the ONE free rate-limiting rule on the Worker route (abuse ceiling for
   public QR posters). Claude never touches the dashboard (A.1) — owner's hands only.

## Phase 3 — the field day (FIELD, one afternoon, four gates at once)
7. Run FIELD-TEST-PROTOCOL.md: a real case, 3-5 people, at least one iPhone, one dead
   spot. It covers: dead-spot sync, full dress rehearsal, iOS PWA install, concurrency
   tiebreak. Nothing in any sandbox substitutes for this afternoon.
8. Findings come back as screenshots/notes; CLAUDE.AI diagnoses; COWORK patches; repeat
   the failed legs only.

## Phase 4 — store gate (OWNER, unchanged bottleneck)
9.  LLC registration -> D-U-N-S. Blocks all store filing.
10. Stripe onboarding completion on the live account.
11. Counsel: consent flow (+ home-zip stays deferred behind it). Then finalise the
    Privacy Policy from DRAFT.
12. Store screenshots (deferred to final pre-filing task by standing decision).
13. Remove #buildmark — the last code change before the filed build.

## Phase 5 — before any marketing push (separate chats, not before filing)
14. Hosting migration GitHub Pages -> Cloudflare Pages (bandwidth wall at scale). Own chat.
15. Scratch-Worker load test — only once a real event is on the calendar; OWNER stands up
    a throwaway Worker+D1 and hands CLAUDE.AI the URL. Never against production (5c).
16. Backlog, own chats each: subph: photo-split schema; scan counting (Worker change);
    monthly-reporting checkbox pending owner answers.

## Standing constraints that govern all of it
- One editor at a time; Cowork is canonical for index.html.
- Aesthetics never change without options shown first.
- Owner copy verbatim; British "licence"; Victorian voice in-product only.
- Zero production writes in any test, ever (5c). No Worker access, no curator token (A.1).
- Every ship: standing battery + new checks named in its brief; hash both surfaces after.
