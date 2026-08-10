# HANDOFF.md — LIVE STATE, RULES AND WHAT IS OPEN

### 🔴🔴 **s55: THIS DOCUMENT WAS SPLIT IN THREE. `SUPER-HANDOFF.md` IS DEAD — do not resurrect it, do not look for it, and if the project-instruction block still names it, paste the revised block from `claude/PROJECT-INSTRUCTIONS-s55.md`.** The set is: **`HANDOFF.md`** (this file — live state, the rules, what is open; **READ IT IN FULL**) · **`HANDOFF-SPEC.md`** (how the app works; read the section you are touching) · **`HANDOFF-HISTORY.md`** (the build record; grep it, never read it whole). **NOTHING WAS COMPRESSED OR REWRITTEN — 5,250 lines went in and 5,250 came out, all 72 sections landed in exactly one file, verified by reconciliation, and the old file is preserved at `_to_delete\SUPER-HANDOFF.md.SPLIT-AT-s55` until the owner deletes it.** **🔴 A RULE LIVES IN EXACTLY ONE FILE; a rule found in two means one is a copy, and copies drift (§0.2, §1w).**
### 🔴 THIS IS ONE OF THREE FILES. THE SET IS THE DOCUMENT; NO ONE FILE IS.
### **READ THIS FILE IN FULL, EVERY SESSION.** It is the state of the world, the rules that bite, and the work that is owed.
### The others: `HANDOFF-SPEC.md` (how the app works) · `HANDOFF-HISTORY.md` (what happened, build by build).
### **SPLIT FROM `SUPER-HANDOFF.md` AT s55 CLOSE. NOTHING WAS COMPRESSED, SHORTENED OR**
### **REWRITTEN — every line was MOVED, and the line count was reconciled to prove it (§4).**
### 🔴 **A RULE LIVES IN EXACTLY ONE FILE. If you find the same rule in two, one is a copy**
### **and copies drift (§0.2, §1w). Delete the copy; do not update both.**

──────────────────────────────────────────────────────────────────────────────

# SUPER-HANDOFF.md — The Deerstalker / Scavenger & Hunt Co.
### Session-53 edition (Aug 6 2026) — supersedes the ENTIRE prior chain, including the session-52 edition.
### 🔴🔴 **READ §77 BEFORE YOU MEASURE, RENDER, HASH, RUN THE BATTERY OR TOUCH GIT.** It is the tooling-facts section, written s55 on the owner's explicit instruction to record what was relearned. It holds: **the local server at `http://localhost:8000` (`Hunt-backups\serve.ps1`) — the primary measurement route, and it serves the real current build**; the three things that CANNOT work and must never be re-attempted (no browser in the sandbox, so **the §48 battery cannot be run there**; `file:///` is silently rewritten by the Chrome extension; `resize_window` does not change `innerWidth`); the **zero-rect trap** on hidden containers; the curator overlay's measured widths (**322px content at a 390px phone**); **the owner's shell is `cmd`, not PowerShell**; and **why git's messages must never be read in place of `.git/refs`**. Every item was learned by wasting time on the alternative.
### ✅ **s56: `33g` IS LIVE — 4,052,031 B / `ec6f29661d09ba89…` / buildmark `33g` / Lime `#7FA33C`, commit `9cd34d4d`.** Pages hash-verified. **WORKER `v2.6.12` DEPLOYED AND VERIFIED — root reads `(v2.6.12)`, `/list` no token still 403.** **EVERY CSV NOW CARRIES A BYTE-ORDER MARK (§87)** — the emailed ones from the Worker, the downloaded ones from the client. Excel had been opening them as Windows-1252 and mangling every em dash since the first CSV shipped. **⚠ THE OWNER PUSHED THIS ONE THROUGH THE GITHUB WEB PAGE, SO HIS LOCAL CLONE IS BEHIND ORIGIN** — `git pull` before the next `ship`. **NEXT MARKER `33h` / Rust `#B4532A`.**
### ✅ **s56: `33f` IS LIVE — 4,051,223 B / `437fdc409f3e1638…` / buildmark `33f` / Magenta `#A8478F`, commit `b7e348e7`.** Disk == raw == Pages, hash-verified. **THE YEAR'S DESK UI IS BUILT — §84.6 AND §80 ITEM 0 ARE CLOSED (§86).** `Annual report ›` on the Ledger AND every case sheet; the case-sheet nav gained the month it never named. **⚠ THE COMMIT MESSAGE MISNAMES IT** — `ship`'s `git add -A` swept 33f into the s55 docs commit, so the log reads `s55: docs rescued…`. **NEXT MARKER `33g` / Lime `#7FA33C`.**
### 🔴🔴 **SESSION 55 CLOSE — READ §80 FOR WHAT IS OPEN, §84 FOR WHAT IS HALF-BUILT, §77 BEFORE TOUCHING A TOOL.** **LIVE NOW: `index.html` `33e` 4,037,814 B / `e1fffd5e…` (commit `37ec0128`, disk == raw == Pages) · Worker **v2.6.11** · `local == origin`.** s55 shipped **33a → 33e** and Worker **2.6.8 → 2.6.11**: the ledger nav levelled, `(office time)` struck, `email report` on the Ledger AND the case sheets, the emailed ledger FIXED and sending, per-case email, a professional CSV, and the YEAR routes. **THE ONE HALF-FINISHED THING: the year has no Desk UI (§84.6).** **THE BATTERY IS GREEN ON 33d, NOT 33e (§82).** **NEXT MARKER `33f` / Magenta `#A8478F`.**
### ✅ **s55: `32z` IS LIVE — 4,034,407 B / `3300b442940c72fd…` / buildmark `32z` / Lime `#7FA33C`, commit `abc819d2`.** Disk == raw == Pages, hash-verified, and the fetched bytes were checked for both changes, not just the hash. **This push also carried the unpushed 32x and 32y.** Ledger nav levelled (§85.1); the Email button relabelled on the owner's verbatim call. **⚠ §85.2 is still owed — the button still sits below the sentence, and that is a known state.** **NEXT MARKER `33a` / Rust `#B4532A` — the letters ran out at `32z`.**
### 🔴 **READ §65 FIRST — IT IS THE SESSION-53 CLOSE AND IT RANKS EVERYTHING THAT IS OWED.** §30 below is the s52 ordering and is superseded by it.
### 🔎 **SESSION 53 BEGAN AS A REVIEW AND ENDED AS A BUILD.** The review: re-hashed all three surfaces, opened `Hunt-backups` for the first time since s30, fixed three clerk defects (§59), and corrected §0, which had been contradicting §58 inside the s52 edition (§0.2). Then three owner task files arrived and **32m shipped** — photographic seals, the builder's commendation card, four-second cards, the ×1.25 stamp (§60).
### ✅ **`index.html` 32m IS LIVE ON PAGES.** **4,024,671 B / `811a118a332a76b2…` / buildmark `32m` / Ochre `#C88A2E`.** Base was 32l `bdfb0222…`. Hash-verified on Pages against the disk copy; raw was still serving 32l at the time, which §0 records as normal.
### 🔴 **NEXT MARKER `32q`, Magenta `#A8478F`** — §8i: Ochre 32m · Rose 32n · Amethyst 32o · Verdigris 32p, so `f` Magenta is next.
### ✅ **`index.html` 32p IS LIVE — AND §13 ITEM 6 IS FULLY CLOSED.** **4,009,521 B / `94d3b32dcf0cb09c…` / `32p` / Verdigris**, commit `1bf5b3b9`. **The web-app manifest shipped** with the Bonnie icon set: `short_name` **"S&H Co."**, six icons including a maskable pair (§63). **⚠ NOBODY HAS ACTUALLY INSTALLED IT — that still needs a phone.**
### ✅ **`index.html` 32o IS LIVE.** **4,009,148 B / `94d747d244368deb…` / `32o` / Amethyst `#7A5A98`**, commit `9c2b6462`. Wax seal keeps its envelope — owner's decision with the pixels in front of him (§62). Verified on disk, raw and Pages, all three identical.
### ✅ **`index.html` 32n IS LIVE.** **4,012,600 B / `cd46c7ad766e8ab1…` / buildmark `32n` / Rose `#B5566B`**, commit `050f7220`. Deerstalker re-cut, boot print pulled, **modulus 10** (§61). Verified on disk, raw and Pages — all three identical.
### 🔁 **THIS EDITION IS A RE-BASE, NOT A NEW SESSION OF BUILDING.** The s30 edition described the app at 29a/29b. It opened at **32i** and closed with **32j live on Pages** and **32l delivered**. Session 52 re-measured the code and the live services, corrected the header, §0 and §13, and then built §54/§56/§57. **Sections §1–§51 were NOT rewritten** — every standing rule in them is preserved verbatim per the no-compression rule (§4). Where an untouched section's *status claims* conflict with §0 or §13, **§0 and §13 win**; where a *rule* conflicts, the rule stands.
### ✅ **`index.html` 32j IS ON GITHUB.** **3,905,589 B / `a29d7438fc002494…` / buildmark `32j` / Slate `#4E6478`.** Base was 32i `a951bf6a…`. The owner uploaded it through the GitHub web page (`30723db`, re-uploaded `48fd903`) — **byte-identical to the local build, hash-verified s52.** See §54.
### ✅ **`index.html` 32l IS LIVE ON PAGES.** **3,908,422 B / `bdfb02224e5084ef…` / buildmark `32l` / Plum `#7D4E6B`.** Carries the desktop masthead fix (§56) **and** the credentials-card side-slider fix (§57). Uploaded by the owner (`5c254ff`); **hash-verified against Pages at session close.** 32k was folded into it and never shipped alone.
### ✅ **THE s52 HANDOFF LANDED — §58.2 IS DONE.** Fetched from raw s53: **200, 207,568 B, "Session-52 edition"**. The line here previously said it was "the last thing unpushed" and that GitHub still served the session-30 edition; **both had stopped being true.**
### 🔴 **THIS s53 EDITION IS AGAIN UNPUSHED.** §0, §0.2, §13.2, §30.2, §30.8, §58 and the new §59 all changed on disk. **Push it, and replace the project-knowledge copy.** Only the owner can do either (§55, §A.1).
### ✅ **NOTHING WAS PENDING PUSH AT SESSION OPEN.** Local clone `C:\Users\tony\Documents\Hunt` == GitHub == Pages, hash-verified s52: `index.html` **3,896,676 B / `a951bf6a60335954…`**, buildmark **`32i`**. HEAD `8a89e99`. No drift, for the first recorded session.
### ✅ **§13.3 — THE TOP SECURITY ITEM IS CLOSED, BOTH HALVES.** `CURATOR_PASS` ×0 in the client; `CURATOR_WORD` is memory-only and typed at the desk; **and the secret HAS been rotated — `X-Curator-Token: BAKER221B` now returns 403 from the live Worker.** Carried as "top open item" for twenty-plus sessions; it is done.
### ✅ **§13.6 — THE SERVICE WORKER SHIPPED.** `sw.js` is in the repo and 200 on Pages; `navigator.serviceWorker.register("./sw.js")` is live, https-gated, network-first for the document.
### 🔴 **THE WORKER IS v2.6.1, NOT v2.3.** §A below still describes v2.3 and its version-specific claims are STALE. The v2.3 *history* and the standing rules in §A/§A.1 remain correct and are untouched. **A `/report` route now exists** (the ledger) that no prior edition documents.
### 🔴 **THE REPO IS NO LONGER FIVE FILES — IT IS TEN ENTRIES, AND `SUPER-HANDOFF.md` IS NOW IN IT.** The s30 rule "the repo is FIVE files / the handoff is NOT in the repo" is factually dead. See §0. **The handoff is now public. Nothing secret may be written into it.**
### ✅ **INSTRUMENTATION SHIPPED TOO — `ev()` / the Company Ledger.** Six event names, a `/ev` POST on the Worker, `keepalive`, `text/plain` to dodge preflight, fire-and-forget. **§13.6c/§49.3 is substantially CLOSED.** See §13 for the one real gap left (first-find).
### 🔴 **STILL ABSENT, RE-VERIFIED s52:** client export (`exportAll`/`downloadBackup`/`exportCase` ×0) and a web-app **manifest** (`manifest` ×0 — the SW shipped without one).
### 🔴🔴 **READ §53.1 BEFORE TRUSTING ANY ABSENCE CLAIM IN THIS DOCUMENT — INCLUDING THE ONES ADDED THIS SESSION.** The s52 re-base itself asserted "no instrumentation" on the strength of four greps and was WRONG. The feature was there under a name nobody grepped for.
### Delete the session-30 file from project knowledge; everything in it is carried here.

---

# 📌 OWNER ACTION — DO THIS WHEN YOU SEE A NEW EDITION

**Claude can now fully manage this file on disk: overwrite it AND delete it.** Deletion was enabled
for the `Hunt` folder at s52, so **there will only ever be one handoff at the repo root** and no
session needs to ask you to tidy up stray copies. **You do not have to do anything about the file
in the folder.**

**THE ONE THING ONLY YOU CAN DO — REPLACE THE PROJECT-KNOWLEDGE COPY.**
The copy attached to the Claude.ai project is **outside the folder and read-only to Claude.** If it
is not replaced, the next session opens a stale edition, believes it, and the whole re-base is
wasted — which is exactly how the s30 edition survived nine builds past its expiry.

**When a session hands you a new edition it will say so in one line, in this form:**

> **🔁 REPLACE THE PROJECT-KNOWLEDGE HANDOFF.** Remove the *session-NN* edition, upload the new
> `SUPER-HANDOFF.md` from `C:\Users\tony\Documents\Hunt`. Takes about a minute.

**If a session does NOT say that line, it did not change the handoff and you need do nothing.**
**A session must never ask you to delete a file from the folder itself** — if one does, it has hit
something it should have handled, and §53.2 is the rule it broke.

**🔁 THIS EDITION (s52) NEEDS THAT REPLACEMENT.** Remove the **session-30** edition from project
knowledge and upload this one.

---

Canonical orientation + rules registry. Restates **every standing rule in full** (never compressed to
pointers — rules were lost once that way). A fresh session should work correctly from this document
plus the delivered `index.html` alone.

---

# 🟢 §A — THE WORKER. **⚠ THIS SECTION DESCRIBES v2.3. THE LIVE WORKER IS v2.6.3 — AND ITS FULL SOURCE IS NOW ON DISK AT `Hunt\worker-v2_6_3.js` (§70.4). READ THE SOURCE, NOT THIS SECTION.**

> **🔴 s52 RE-BASE NOTICE.** Everything below was written against **v2.3** and was true of it. The live
> Worker now reads **`… OPERATIONAL. (v2.6.1)` / `The game is afoot.`** on
> **`deerstalker.tony-13f.workers.dev`**. Three things measured live at s52, unauthenticated:
> `GET /list` no token → **403** · `GET /list` with `X-Curator-Token: BAKER221B` → **403 (THE SECRET IS
> ROTATED)** · `GET /report?month=…` no token → **403**. **The `/report` route is new and undocumented
> in any prior edition** — it backs the Curator's Desk ledger (three call sites in the client, all
> gated on `CURATOR_WORD`). **Nobody has told Claude what else changed between v2.3 and v2.6.1.**
> Treat every version-numbered claim below as history. **The RULES in §A and §A.1 are unaffected and
> still stand**, including: `PUT` is still assumed unauthenticated (§13.8), automation must set a
> User-Agent, and Claude must never be given Worker access.
> **Claude does not know the new curator word and must never be told it** (§A.1).


──────────────────────────────────────────────────────────────────────────────

## §A (v2.3 history — preserved verbatim)
### 🟢 THE WORKER WAS SECURE AT v2.3. RE-VERIFIED AT SESSION-29 OPEN.

**Session-29 probe (live, unauthenticated):** root returns
`Scavenger & Hunt Co. — case-file sync is OPERATIONAL. (v2.3)` · `GET /list` with no token → **403**.
**Session 29 made ZERO production writes** — every test stubs `Store` structurally (§48).

- Worker root reads **`Scavenger & Hunt Co. — case-file sync is OPERATIONAL. (v2.3)`**
- `GET /list` **with no token → 403**
- `GET /list` **with `X-Curator-Token: BAKER221B` → 200, 400 keys** (session-30 probe):
  `hunt:` 138 · `profile:` 133 · `sub:` 97 · `res:` 21 · `reply:` 8 · `msg:` 2 · `coldstat:` 1.
- **Session 30: `profile:` 131→133, +2 — organic play, zero writes made by Claude** (backup script and all probes were read-only; Playwright tests aborted every Worker route).
- **🆕 (30) CLOUDFLARE BLOCKS THE BARE PYTHON USER-AGENT** — `urllib` with no UA → 403 on `/list`; any UA string (e.g. `hunt-archive-clerk/1.0`) → 200. **Any future automation against the Worker must set a User-Agent.**
- **🆕 (30) `cold:index` DOES NOT EXIST YET** (`GET` → not found). It is first written on territory acceptance; none has been accepted. `coldstat:144127` is the lone archive key.
- **+1 on session 27's 397** (`sub` 96→97). **Session 28 made ZERO production writes** — `Store` was
  stubbed on every probe (§11b). Organic play. **Recorded so the next session does not read it as pollution.**

### What v2.3 fixed (history — do not re-litigate)
1. **`/list` requires `X-Curator-Token`.** Fails closed if the secret is unset.
2. **`DELETE` requires it on EVERY key** (v2.2 scoped the check to `cold:index` alone).
3. **`KEEP_DAYS` 90 → 60.**
4. **`scheduled()` honours each case's own `retentionDays`/`createdAt`.**
5. **`scheduled()` keeps a case alive while its hunters are active.**
- **The asserted safety property: the sweep rules only ever EXTEND a record's life against the flat
  cutoff.** Nothing is deleted sooner than the 60-day rule alone would delete it.

### 🔴 THE REMAINING HOLES — RANKED, AND STILL OPEN

**1. ⚠ `PUT` IS UNAUTHENTICATED AND DELIBERATELY SO.** Anyone can overwrite any case or profile.
v2.3 does **not** fix this, because hunters, builders and curator all write through the same door and
there is no per-user auth model. **Do not "quickly fix" it — it will break the app.**

**2. 🔴 THE CURATOR TOKEN IS PUBLIC.** `CURATOR_PASS="BAKER221B"` ships in a **public repo**
(`BAKER221B` ×1, `CURATOR_PASS` ×4 — re-verified in 28e). **v2.3 stops scanners, not readers.**
§13.7 is what finishes the job.
- **`CURATOR_TOKEN` IS PROVEN TO EQUAL `BAKER221B`** — established empirically in session 25 using
  the response code as an oracle, re-confirmed at sessions 27 and 28.
  **⚠ CLOUDFLARE SECRETS ARE WRITE-ONLY AND CANNOT BE REVEALED. Never ask the owner to "look at" a
  secret again.**
- **🔴 🆕 (28) AND THE FIX IS NO LONGER A CLEAN SWAP — SEE §13.7 AND §45.** `Store.del()` sends
  `X-Curator-Token: CURATOR_PASS` (×2 sites). **Ordinary users can delete their own cases ONLY
  because the curator secret ships in the public client.** Removing the constant breaks user-facing
  deletion. **This was discovered in session 28 and changes the shape of the job.**

### 🔴 §A.1 — CLAUDE HAS NEVER HAD, AND MUST NEVER BE GIVEN, WORKER ACCESS

**The owner has twice framed Claude as having Worker/webmaster access. Claude does not.** An earlier
session *wrote* the source and handed it over as text to paste. **Claude starts every session in an
empty sandbox: no Cloudflare login, no `wrangler` credentials, no memory of earlier output.** Claude
can probe the deployed Worker from outside but cannot read or deploy it. **§14 forbids giving access
and that rule stands.** The working protocol — **owner pastes source in, Claude hands source back** —
is proven and should be reused for every future Worker change.
- **⚠ 🆕 (28) SAY SO PLAINLY WHEN ASKED.** In session 28 the owner asked *"you were in the webmaster?"*
  The correct answer is a one-line correction followed by **what Claude CAN verify** — in that case,
  reading the client delete path, which found two real defects (§45).

**Worker edit path:** dash.cloudflare.com → **Compute (Workers)** → **Workers & Pages** →
**deerstalker** → **Edit Code** → select all → paste → **Deploy**.

---

## §0 — CANONICAL FILE STATE (ground truth)

| File | Size | SHA-256 | Purpose |
|---|---|---|---|
| `index.html` **🆕 34e — LIVE, commit `f35b49de`. Verdigris. THE WIPE CROP, THE ORDINAL, THE BADGE PRESS, THE JOIN LAG (§106-§108). s58; re-verified s59: disk == origin == Pages == raw.** | 4,302,603 B | `2adb51cf74344de5eb02f155f8b932cec661492d106f8478f69772bd39039357` | needs Worker **v2.6.13**. The wipe crop, the ordinal, the badge press, the join-lag reads and writes (§106-§108) |
| *(superseded)* `index.html` **33n — was live s58, commit `165b7400`, 16:03Z 9 Aug 2026. THE CASE CLOSED STAMP (§94).** | 4,111,862 B | `1ac7f99edb1b8f2eec3fa5c8cabe02ef10cf90965fd0c7b4bbc4cfb0fc76b873` | needs Worker **v2.6.13**. 🔴 **THIS IS AN EARLY 33n. Stamp 250px, red `#B92230`. EIGHT LATER REVISIONS NEVER REACHED IT — see §94.10** |
| *(superseded on disk, NEVER SHIPPED)* `index.html` 33m — THE HINT COIN IS EARNED, NEVER SOLD (§93). s58, Sun 9 Aug 2026.** | 4,071,402 B | `64c094c82543eb60e6fa0cc06515f481b5e0694f7ad42e8b2b5f1a86fb11bd44` | needs Worker **v2.6.13** |
| *(superseded)* `index.html` 33l — was live s57, commit `3d49b6cd`. THE ZIP BAND (§91). | 4,068,353 B | `2f9cd80f4ec8fa678f4fd1acaeff8f4b4530f03203afd765994d2a80f0c3dc5d` | needs Worker **v2.6.13**. Carries 33k's caption + pin median tier, never separately shipped |
| *(superseded on disk, NEVER SHIPPED)* `index.html` 33k — caption + pin median tier (§90.11) | 4,062,995 B | `15f4dc8edc806bad42b75e4bee82336f29124183649ec76eb84309fed5120280` | needs Worker **v2.6.13**, deployed and gate-verified |
| *(superseded)* `index.html` 33j — was live s57, commit `12f9e02c`. TAP THE MAP TO MAGNIFY (§90.8). | 4,061,182 B | `628833f342e5b236197f5cb510998cc9de3e546561e47614923dcc10b6dd974a` | needs Worker **v2.6.13**, which is deployed and gate-verified. Battery green: STATIC · BEHAVIOUR 59/59 · SESSION 21/21 |
| *(superseded)* `index.html` 33i — was live s57, commit `9abcb27e`. PLAN renamed MAP. | 4,060,601 B | `74a333afa485bb6fc3844abeaf48a16b229dcd5c864572a1c1f1ddc9e203182d` | — |
| *(superseded, NEVER LIVE)* `index.html` 33i pre-rename — committed `1575e87f`, carried `View plan` | 4,060,680 B | `eb5f9652d0e804bae1c3cd86128df73d2818d776d1ba2137d1c6dc03f6535c5d` | shipped by mistake; see §90.9 |
| *(superseded)* `index.html` 33h — was live s57, commit `e4906dd2`. THE SURVEYOR'S PLAN (§90). | 4,059,317 B | `c09f7377616bdb24a6ee70ca0509245f23f85a030135e06989041adcbbc45418` | needs Worker **v2.6.13** |
| `worker-v2_6_13.js` **✅ THE LIVE WORKER, DEPLOYED AND VERIFIED s57 — root reads `(v2.6.13)`** | 99,952 B | — | `map:` keys are staff-only on PUT/DELETE; GET stays open (§90) |
| *(superseded)* `index.html` 33g — was live s56, commit `9cd34d4d`. The CSV byte-order mark (§87). | 4,052,031 B | `ec6f29661d09ba89bc4214db7577608a791905cc928e2b1d48e687598ab91d30` | needs Worker **v2.6.12**, which is deployed |
| *(superseded)* `index.html` 33f — was live s56, commit `b7e348e7`. THE ANNUAL REPORT (§86) | 4,051,223 B | `437fdc409f3e163831a062994da151638c985cc166f7fdcc599d50e401c90fc8` | needs Worker **v2.6.11**, which is deployed |
| *(superseded)* `index.html` 33e — was live s55, commit `37ec0128` | 4,037,814 B | `e1fffd5e9fc6be3ed23b26ef061a53fc78d67bfcda1fdfc8ae4fa9a8f8d900af` | needs Worker **v2.6.9**, which is deployed |
| `worker-v2_6_12.js` **✅ THE LIVE WORKER, DEPLOYED AND VERIFIED s56 — root reads `(v2.6.12)`** | 98,430 B | `e3b17467b27301cf448840ccfb24dcf8695830c0db0818746e799fac2a665586` | **THE BYTE-ORDER MARK** — one `csvBytes()` helper, three attachment sites (§87) |
| *(superseded)* `worker-v2_6_11.js` — was live s55 | 97,885 B | `7dacce07977efdc466af0fbf5b59b04e02e678204403024a5ba38bdf890fce74` | **THE YEAR** — `?year=` for the company and per case, by GET and by post (§84). Carries v2.6.10's CSV header + `Aug 1` labels |
| *(superseded)* `worker-v2_6_10.js` | 82,800 B | `b6d5dfe2da7715736c3ca06b24c968bd8addb20a1d22f31d2e061a1450478244` | the case CSV became a document; fixed the empty `day` column (§84.4) |
| *(superseded)* `worker-v2_6_9.js` — was deployed s55 | 79,906 B | `5c48441c54e377b7a3ed15fa470c1855807b2131accd1948de36dfdfe0b78c83` | `/report-email?…&code=` sends ONE case sheet + its day CSV (§83) |
| *(superseded)* `index.html` 33d — was live s55 | 4,037,229 B | `6f3d5f62779d1bd4ebdc912ed295967fef1fc45a65007866a6c4192fab3d08e2` | `(office time)` struck; the nav row fits one line (§79.5) |
| *(superseded on disk)* 33c | 4,036,625 B | `91bf9fcca34126ba5b9525b929f893f532582f1edc74eb9df788fb6ff1600a15` | nav buttons `nowrap` — the real "later is up" fix (§79.4) |
| *(superseded on disk)* 33b | 4,036,031 B | `6ee4f535e4cb6e280828d97df7d3d1da378b715cca17e073ae8c68787dd0e052` | `email report` on the CASE SHEETS via one shared handler (§79) |
| *(superseded)* `index.html` 33a — LIVE, hash-verified s55, commit `fd9f2eb1` | 4,034,680 B | `a9cba68133408851e20745a3b61b004dbbc9c37858c2dc196008517d4683d260` | `email report` under the month; the compiled/sealed sentence STRUCK; `.ledg-meta-row` CSS deleted (§78). **§85.2 CLOSED.** |
| *(superseded)* `index.html` 32z — LIVE earlier in s55, commit `abc819d2` | 4,034,407 B | `3300b442940c72fddf1b0bf3b510401687e2eca6e3eaec3522ac2ae54aa4fbbc` | ledger nav levelled + button relabelled `Email` (§85) |
| *(superseded on disk, committed as `9b10257` but NEVER pushed)* `index.html` 32y | 4,034,030 B | `a5a4a801890747287346285de6b83e1014103edb899087ba046778dab85a2771` | the ledger button + paired tips |
| *(superseded on disk)* `index.html` 32w | 4,031,642 B | `7fa2a89c406de3f7b34b1ce1ef24a94467126e792cfcfc54bc903905ad9350d8` | the first-sleuth ask (§74); carries 32u web push + 32v |
| `index.html` *(LIVE on Pages: 32u)* | 4,023,779 B | `7d7a0598d49c6ef742956476d0dd1e057136e9ec778d17cdbb5ffdd0ab03a049` | **32t** — the live roster watcher (§68) |
| *(superseded on disk)* `index.html` 32s | 4,017,670 B | `54385a7bb5fc041e7de244e37fca40ac32fbc29061356ca0b3fcf7e48c31a540` | **32s** — the slim poll against Worker v2.6.3 (§67) |
| *(superseded on disk)* `index.html` 32r | 4,014,420 B | `21c7d6aa60f1a1a16267b56a8381a39e014aec83626834ec7fdf0c325647712f` | **32r** — notification priming card, cold ask killed, notifications routed through the SW (§66) |
| *(was LIVE at s53 open)* `index.html` 32q | 4,010,286 B | `df13a8f7cfcc483ac10908c2d86d5b942dba02f9c860b6d99bb17a508bca79ab` | **32q** — buildmark `32q` Magenta `#A8478F`; ceremony crest + icon darkened (§64) |
| *(historical)* `index.html` 32p | 4,009,521 B | `94d3b32dcf0cb09cc0529324148a37c857e38e63c5b19bd8a1a8c0539944a67a` | the web-app manifest + icon set (§63) |
| `manifest.webmanifest` **🆕 s53** | 941 B | — | name/short_name/display/theme; **`icons/` holds six PNGs** — 1024·512·192·180 standard, 512·192 maskable (§63) |
| *(historical)* `index.html` 32o | 4,009,148 B | `94d747d244368debc937396e2a7fc164526966867212797b846c8d1dc636add8` | wax seal keeps its envelope (§62) |
| *(historical)* `index.html` 32n | 4,012,600 B | `cd46c7ad766e8ab1421ef9ee9bc96ffd0b081418e4dddab30aae43c6763e8964` | deerstalker re-cut, boot print pulled, modulus 10 (§61) |
| *(historical)* `index.html` 32m | 4,024,671 B | `811a118a332a76b222c4261f95bf53370195941e60daeb87f79fc261e81ae1c3` | photographic seals + the builder's commendation card (§60) |
| *(historical)* `index.html` 32l | 3,908,422 B | `bdfb02224e5084ef055fb8f871bde21fbfe56aac4d8a05768978667e0081f1bc` | credentials-card side slider (§57) |
| ~~`candidate-32m.html` / `_candidate-32m.html`~~ **✅ GONE — BOTH 404 ON RAW, verified s55 and again s57. The deletion order that stood here is DISCHARGED (§80.9).** | 4,024,671 B each | `811a118a…` | Render-check copies pushed so GitHub Pages could serve them (§60.5). **They are byte-identical to the shipped `index.html` and serve no purpose now. The sandbox cannot delete — the owner must.** |
| *(historical)* `index.html` 32i | 3,896,676 B | `a951bf6a603359545a7ccb14c42ac8b0bbe4957c832281ffa9e1a995ddd7ef1c` | agency licence minting (`8a89e99`) — **this row said "LIVE" for three builds after it stopped being true. See §0.2.** |
| `sw.js` **✅ LIVE — RE-MEASURED s57, disk == Pages** | 5,532 B | `7a1682bd276e3bdba985270e7e36e5dea2f26ad696db53280d65a5c2cc80f45c` | `notificationclick` + the **`push` receiver** (§66, §70.4); `CACHE` = `shco-v2` |
| *(was LIVE at s53 open)* `sw.js` — **🔴 §0 HAD THIS WRONG: it said 3,435 B / `61a93b05…`. MEASURED s54: disk == raw == Pages at 3,349 B / `54127008f4ff0bdb…`.** A fourth inherited doc error (§0.1). | 3,349 B | `54127008f4ff0bdbc057…` | the service worker (§13.6, CLOSED) |
| `award-card.jpeg` **🆕 in repo** | 180,855 B | `3ef3ac34795c8708…` | commendation card (§8r) |
| ~~`hunt-icon-v5.png`~~ **⚠ NO LONGER IN THE REPO — moved to `_to_delete\s56-repo-slim\` at s56 (§88). Hash kept for the record.** | 67,899 B | `969262cefd3c431e…` | app icon |
| ~~`behaviour.py` (repo ROOT)~~ **✅ GONE — the stray root copy left the tree at s56 (§88). `test/behaviour.py` is the only copy. Hash kept for the record.** | 18,003 B | `473b385d3b122c6e…` | **byte-identical to `test/behaviour.py`.** One of the two should go; the root copy is the accident. |
| `.nojekyll` **🆕 s54 (LIVE)** | 0 B | — | Pages publishes statically; no Jekyll step to fail (§70.2) |
| 🔴 `HANDOFF.md` **+ `HANDOFF-SPEC.md` + `HANDOFF-HISTORY.md` — ALL THREE IN THE PUBLIC REPO** | 136,233 B · 78,607 B · 179,610 B (LF, as stored) | — | the canonical document, split from `SUPER-HANDOFF.md` at s55 close. `SUPER-HANDOFF.md` IS DEAD and is in no repo. **🔴 s57: `HANDOFF-SPEC.md` and `HANDOFF-HISTORY.md` were MISSING FROM THE WORKING CLONE while present in the repo — `ship.cmd`'s `git add -A` would have committed their deletion. Restored. CHECK ALL THREE ARE ON DISK AT EVERY SESSION OPEN.** The working clone is CRLF and the repo is LF (`.gitattributes`); hash disk against raw only after stripping `\r`. |
| ~~`art/`~~ **⚠ NO LONGER IN THE REPO — left the tree at s56 (§88); source art lives on disk.** | — | — | `bonnie-icon-source.png` + `icon-C/` (adaptive-background-432, adaptive-foreground-432, icon-1024, icon-180-appletouch, icon-512) |
| *(historical)* `index.html` 29a | 3,690,652 B | `26d31f08192fbd47…` | the s30 edition's "live" build — nine builds stale |
| `privacy.html` **(🆕 REBUILT s30 — for scavengerandhunt.com, NOT the repo)** | 5,364 B | `6298d38db9060f9575619709ffab02951c2b7606c74c7fd49441124e6e94391c` | DRAFT banner; §45.4 language verbatim (§44.2b) |
| `parch.jpg` **(🆕 RE-EXTRACTED s30 — byte-identical to s28's)** | 49,029 B | `118d98d0b52f27b5aa746a94ecb3f7ad0ff707e9a153ec41d0d8e43ac77d011d` | site background texture |
| `Hunt-backups-starter.zip` **(🆕 s30 — for the NEW private repo)** | ~4.3 KB | `backup.py 218f390e…` · `backup.yml f90d9df6…` · `README 09782b3c…` | the archive clerk (§51.3) |
| `test/run.py` **🆕 REWRITTEN s57 — THREE SUITES, NOT TWO** | — | — | now runs **SESSION** as well as STATIC and BEHAVIOUR; **refuses SESSION for a candidate build** (it always loads `.\index.html` and would report a pass for a file it never opened); every parent `print` is `say()` with `flush=True` (§77.11). *(was 698 B, two suites — battery runner, §48)* |
| `test/find-null.py` **🆕 s57 — DIAGNOSTIC, NOT PART OF THE BATTERY. §89 RESOLVED WITH IT.** | — | — | takes a **mode arg** `A`/`B`/`C`/`D` toggling the stub and gate independently. Cell C fired: **the harness stub, not the app, requested `/null`** — `page.evaluate(STUB)` returns the last statement's value, the assigned `window.fetch` fn, which Playwright invokes with `null`. Kept as the record of the mechanism (§89) |
| `test/agents.py` `behaviour.py` `baseline.json` `README.md` ✅ ALL PUSHED (verified 200 on raw, s30) | — | — | (§48) |
| `worker-v2_6_8.js` **🆕 ✅ DEPLOYED AND VERIFIED s55 — root reads `(v2.6.8)`. THE EMAILED LEDGER SENDS (§81).** | 75,522 B | `afd9b47751d836b307c4d5dc11e0a86baaa15ff6d3403cda9b570fc6076577bb` | `LEDGER_FROM` moved to the ROOT domain — the one-line fix |
| `worker-v2_6_7.js` **(deployed s55, superseded within the session)** | 74,802 B | — | the emailed ledger, sending as an unverified identity |
| `worker-v2_6_6.js` **🆕 s54 — WRITTEN, NOT DEPLOYED. Fixes the take rate (§73)** | 66,001 B | `c959cb36ec463b93d87621ce461122ae56976b13f047b93b9128445b5d37ffc5` | — |
| `worker-v2_6_5.js` **(deployed s54; superseded by 2.6.6)** | 64,222 B | `04ca5309e6d9e7fe17f83b605a87e2164e170103f11f2d06fc5e6edd01ef90a1` | — |
| `worker-v2_6_4.js` **(DEPLOYED s54 — ⚠ CARRIES THE §72 HOLE, SUPERSEDE IT)** | 62,827 B | `23d81339e37ff3ff889e14286f44a175be17fa5d5602ae23e50f906b1012e429` | — |
| `worker-v2_6_3.js` **(deployed; source of record)** | 50,531 B | `92a66f9bc3ba3a0bdc8886ca19fd19d95b112ada9ae9159de621359eb4968edd` | adds `slim=1` on values listings (§67.1). Root: `... (v2.6.3)` |
| *(historical)* `worker-v2.6.1` | — | — | **live root string: `Scavenger & Hunt Co. — case-file sync is OPERATIONAL. (v2.6.1)` / `The game is afoot.`** Host: **`deerstalker.tony-13f.workers.dev`**. `worker-v2.3.js` is history (§A). |
| `j.html` **(CHANGED since s30)** | 1,419 B | `bbf057e1f3225a0f…` | invitation landing page (§8n/§8o) |
| `og-card.jpeg` | 246,070 B | `0067960541bec0ac…` | link-preview card |

- **🔴 THE REPO IS EIGHTEEN TOP-LEVEL ENTRIES, MEASURED s57 FROM `api.github.com` (unchanged since s56):**
  `.gitattributes` · `.gitignore` · `.nojekyll` · `HANDOFF.md` · `HANDOFF-SPEC.md` ·
  `HANDOFF-HISTORY.md` · `award-card.jpeg` · `battery.cmd` · `claude/` · `docs/` · `icons/` ·
  `index.html` · `j.html` · `manifest.webmanifest` · `og-card.jpeg` · `ship.cmd` · `sw.js` ·
  `test/`. **The "five files" rule is dead and so is "ten" — the count went 5 → 10 → 15 → 18 with a
  doc entry only twice. AUDIT IT EVERY SESSION.**
- **🔴 THE HANDOFF SET IS IN THE PUBLIC REPO** — all three files. Every edition before s52 said it was not.
  **Consequence: this document is world-readable. Never write a secret, a token, a curator word or a
  personal detail into it.** (The old `BAKER221B` references throughout are harmless — that word is
  now rotated and dead as a token; it survives in the client only as `CURATOR_NAME`, the public
  nameplate on the desk door.) **Owner decision owed: keep it public, or move it to `Hunt-backups`.**
- **✅ `behaviour.py` NO LONGER EXISTS TWICE** — the root copy left the tree at s56 (§88) and is
  confirmed absent from the working clone s57. `test/behaviour.py` (18,003 B) is the only copy.
- **Push queue for the owner:** (1) `index.html` 29b → repo → replace project-knowledge copy is N/A
  (project knowledge holds only this handoff — correct state). (2) `privacy.html` + `parch.jpg` →
  **GoDaddy, scavengerandhunt.com** — a DIFFERENT destination from the repo. (3) The backup zip →
  the new **private** `Hunt-backups` repo (§51.3 setup steps).

**🆕 SEPARATE PROPERTY — the marketing site (NOT in the Hunt repo, NOT on GitHub Pages).** See §44.

- **🔴 THE FIRST THING THE NEXT SESSION MUST DO IS RE-HASH ALL THREE SURFACES.** Expect
  **4,302,603 B / `2adb51cf…` / `34e`** on raw and Pages, and the Worker root to read **`(v2.6.13)`**.
  *(Verified s59: disk == origin `f35b49de` == Pages == raw, two cache-busted fetches agreeing; Worker confirmed. The line that stood here
  named **`32l`** — twelve builds dead — and before that **28e**. A stale instruction is worse than no
  instruction: it sends the session to verify a fact that stopped mattering. Re-write this line on
  every ship.)*
- **🔴 ⚠ VERIFY A PUSH AGAINST `gahensley1.github.io`, NOT `raw.githubusercontent.com`.**
  raw's CDN served the OLD file for over two minutes after a successful push in session 25, and a
  cache-buster query did not defeat it. **Pages is authoritative; raw lagging is normal and harmless.**
- **⚠ THE WORKER SOURCE IS NOT A REPO FILE.** Pasted into the Cloudflare dashboard, never pushed.
  **Do not add it to the repo — the repo is public.** This rule survives the file-count change intact.
- **⚠ AUDIT THE FILE LIST EVERY SESSION — the count changes without ceremony.** It went 5 → 10 between s30 and s52 with no doc entry. Use the `api.github.com/repos/gahensley1/Hunt/contents/` listing in-sandbox; it worked s52.
- **⚠ `index.html` AND `og-card.jpeg` ARE A MATCHED PAIR AND MUST BE PUSHED TOGETHER** (§8q). Same for
  `index.html` + `award-card.jpeg` (§8r). **After any card ship, `curl` every repo file and compare
  HASHES, not just sizes.** *(28e changed neither card, so 28e ships alone.)*
- **⚠ `index.html` is TOO LARGE for project knowledge (~3.7 MB) — by design NOT stored there.**
- **The live `index.html` is ground truth.** When any doc and the code disagree, **the code wins.**
- **✅ FILE-IN-HAND:** `curl -sSL https://gahensley1.github.io/Hunt/index.html`. Egress to
  raw.githubusercontent.com, github.com, gahensley1.github.io, scavengerandhunt.com, the Worker and
  developers.cloudflare.com all work in-sandbox. `api.github.com` is rate-limited (403). Repo listing:
  `curl -sSL https://github.com/gahensley1/Hunt | grep -o '"name":"[^"]*"' | sort -u`.
  **Older commits by SHA:** the atom feed `https://github.com/gahensley1/Hunt/commits/main.atom` gives
  SHAs; `https://raw.githubusercontent.com/gahensley1/Hunt/<sha>/index.html` fetches that revision.
- **🆕 s52 lineage note:** builds **30 → 32i** were shipped without handoff entries. Git records them
  as fourteen-plus `Add files via upload` commits (Aug 1–4) plus three named ones: `07f6bef` service
  worker, `0386384` Bonnie icon + option-C icon set, `8a89e99` **32i agency licence minting,
  badge-bound keys with expiry**. **Per-build hashes for 30–32h were never recorded and are now only
  recoverable from git.** Recover with `git log --format=%h` + `git show <sha>:index.html | sha256sum`.
- **🆕 s53 lineage:** 32i 3,896,676 `a951bf6a…` → 32j 3,905,589 (licence terms + register, §54) →
  32k (desktop masthead clip, §56) → **32l 3,908,422 · `bdfb0222…` · uploaded `5c254ff` (LIVE)**.
  32k and 32l shipped as one delivery, so **no separate 32k hash exists.** Verified s53 on local,
  raw and Pages — **all three identical.** Local `HEAD` = `origin/main` = `318503c2`; nothing ahead.
- **Session-29 lineage:** 28e 3,687,318 `bcfbf057…` (live base, hash-verified on **Pages and raw** at
  session start) → **29a 3,690,652 · `26d31f08…` (DELIVERED)**. One ship; the deed checkbox was added
  to 29a in place rather than cut as 29b, so **only one 29-series hash exists.**
- **Session-28 lineage:** 27c 3,684,488 `f1c7e782…` (live base, hash-verified at session start) →
  **28a 3,684,837 `83a1c9f1…`** → **28b 3,686,974** → **28c 3,687,291 `651b09a3…`** →
  **28d 3,687,307 `f2cc3f10…`** → **28e 3,687,318 · `bcfbf057…` (DELIVERED)** →
  *28f 3,689,128 `8784e335…` — **BUILT THEN UNDONE BY THE OWNER**, see §46.*
- **Older lineage:** 26h 3,681,807 `0573e763…`; 25c 3,682,380 `c0637d66…`; 24d 3,680,871 `3bf5ded3…`;
  23d `d78955f8…`; 23c `1d9a0dcb…`; **pre-volume commit `f667edc9` 3,671,858 `e439c3f2…`**;
  22b **3,670,397 · `9575527a…`**; 21u **3,663,852 · `e13dfd34…`**; 20h `787d7299…`; session-20 final
  **3,559,279 · `b9719c66…`**; 19 `d9a6a4cd…`; 18 `a3773d73…`; 17 `f03a7dee…`; 16 `c4527c8a…`;
  15 `200f6c…`; 13 `57cc95bf…`; 12 `eb8fe5cc…`; 11 `362d13eb…`; 10 `a7493aca…`; 9 `25dcd26d…`
  (begun from owner-uploaded `d1fa7777…`, **never diffed** — §13); 8 `747b8963…`.

---

## 🔴 §0.2 — THE `32i` ROW: A DOC THAT CONTRADICTED ITSELF IN ONE EDITION (found s53)

**§0's table said the live build was `32i`. §58, in the same document, said `32l` and gave the
hash.** Both were written in session 52; §58 was updated at session close and §0 was not. The s53
review found them disagreeing and re-hashed all three surfaces: **`32l` / 3,908,422 B /
`bdfb0222…` — local, raw and Pages identical.** §58 was right; §0 was three builds stale.

**This is not the §30.11 staleness class.** That one is a document that stopped being updated. This
is worse and harder to catch: **a document that was updated in one place and not the other, so it
carries its own contradiction and still reads as current.** A single stale section inside a fresh
edition inherits the edition's credibility.

**THE RULE THAT FOLLOWS: §0 IS UPDATED IN THE SAME EDIT AS THE SHIP, NEVER AFTERWARDS.** If a build
is delivered and §0's table still names the previous one, the ship is not finished. And when two
sections of this document disagree, **re-measure — do not pick the one that reads more confidently.**

---

## 🔴 §0.1 — INHERITED DOC ERRORS. THREE FOUND IN 24–25; ALL RE-VERIFIED CLEAN IN 26, 27 AND 28.

**Inherited doc claims are exactly as unverified as your own.**

### (a) The `paid:true` error — found session 24
The s22/s23 handoffs claimed "no built-in hunt carries `paid:true`," so §8v called the paywall gate
"dormant." **Both false — 27 of 30 shelf cases were already flagged paid.**
**Root cause:** `BUILTIN_INDEX` is a **JSON blob** using `"paid": true` — quoted key, space after the
colon. Grepping for `paid:` (the object-literal form) returns only the two entry *constructors*.

### (b) "the retention period appears NOWHERE in the client" — FALSE (found 25)
**The client has a full retention UI:** `renderKeepLine()` prints **"Kept until \<date\>"**, turns
oxblood at **≤14 days**, and offers an **"Archive +1 year"** button.

### (c) And the client's promise was never honoured (found 25)
**The v2.2 Worker never read `retentionDays`.** Fixed in v2.3, now deployed.

**⚠ STANDING LESSON — grep the DATA SHAPE, not the code shape.** `BUILTIN_INDEX` is JSON; query it by
parsing, never by grepping:
```python
i=t.find('BUILTIN_INDEX='); j=t.find('];',i)
arr=json.loads(t[i+len('BUILTIN_INDEX='):j+1])
```
**And when a doc makes a claim about absence ("X appears nowhere"), re-grep it yourself.** Absence
claims are the most fragile kind and two of the three errors above were absence claims.

**🆕 (28) A FOURTH CLASS: A DOC CLAIM ABOUT *WHICH FILE* A RULE LIVES IN.** §8x quoted three CSS rules
as "the dim." One of the three (`.coldstamp.locked`) is the buy stamp's background, not a dim, and
moving it would have unpainted every buy stamp. **Read the rule, don't trust the grouping.**

---

## §1 — HOW THE OWNER WORKS (read first)

### 🔴 §1y — RE-HASH THE LIVE SURFACES FROM THE SHELL BEFORE YOU BELIEVE ANYTHING (owner rule, s58)

**Owner: "never forget to look at shell i need to approve."**

**"Shipped" is a claim until the bytes are fetched and hashed.** `33n` sat live for over an hour,
eight revisions behind the disk, while Claude went on editing and quoting hashes — and nobody knew,
because nobody looked.

1. **Fetch and hash Pages and raw at the START of any ship conversation and again AFTER any ship**,
   from the sandbox shell. Read `.git/refs/remotes/origin/main` as a plain file and check the atom
   feed for the commit message and its `index.html`.
2. **Two edges can disagree mid-deploy.** Differing sizes minutes apart is a deploy in flight, not a
   cache-buster failure. Say so; do not average them into a conclusion.
3. **ONE LIVE `ship` LINE AT A TIME.** An old command does not expire — the owner will run whichever
   one is in front of him. **If the build moves after a `ship` line is written, say IN PLAIN WORDS
   that the earlier command is dead and give the new hash.**
4. **Confirm the buildmark is unspent before reusing it.** A buildmark that is already in the repo
   cannot be reused, whatever `HANDOFF.md` says.
5. **He approves the ship. Claude does not decide it is done.**

### 🔴 §1x — GET THE LOOK RIGHT *BEFORE* SHIPPING, NOT ACROSS SHIPS (owner rule, s58)

**Owner, verbatim: "No reason to ship until you get approval for the aesthetic that just... Pops
us."** And, after two buildmarks were spent mid-iteration: **"i would rather get the look right
before we ship ... this is important espically when we live."**

**A ship is not a save point.** The instinct to push each approved step is wrong: it spends a
buildmark, it puts a half-settled look in front of real players, and it leaves a dead `ship` line
in the conversation that will be run later. **Settle the whole visual change, THEN ship once.**
**This matters more, not less, now the app is live** — every intermediate state is seen.

**A visual build is not finished when it is correct. It is finished when he has SEEN it and SAID
YES.** Claude had a green STATIC, a matching hash and a §0 entry on `33n` and handed over `battery`
and `ship` — while the stamp had been nudged twice in as many messages and never approved in its
final position. **Green tests are not consent.**

1. **Do not write the `ship` line at all** until the owner has approved the appearance. Not as a
   draft, not "when you are ready" — the presence of the command reads as "this is done."
2. **`battery` may be offered earlier**; it proves nothing about the look and costs him little.
3. **What earns approval is pixels**, at the real size, on the real screen, in the real card —
   never an arithmetic argument that the numbers are right. His screenshots have caught what
   correct arithmetic did not, twice in s58 alone (§94.1, §94.6).
4. **After ANY visual nudge, however small, the approval resets.** Ten pixels is a change.
5. **Say plainly what is still unapproved** when handing anything back.


### 🔴 §1w — A CORRECTION IS NOT DONE UNTIL EVERY COPY OF THE ERROR IS DEAD (owner rule, s54)

**Owner's instruction, verbatim: "as rule one you find a mistake correct all associated materials
i should [not] have to ask you."**

When Claude finds an error — in this document, in a brief, in a delivered file, in its own earlier
message — **the fix is not the correction, it is the SWEEP.** Before reporting anything:

1. **Grep for the claim, not the sentence.** The same wrong fact is usually phrased three ways in
   three sections. Search the idea (`DNS`, `manifest`, `first_find`), not the wording.
2. **Correct every instance, in every file** — handoff, `claude/` briefs, delivered documents,
   project knowledge. A brief that contradicts the handoff will be believed by whoever reads it
   first.
3. **Say what was wrong and where it was**, not just what is now right. A silent correction cannot
   be audited, and the next session cannot tell a fix from a drift.
4. **Ask what ELSE rested on it.** §64.4's DNS "blocker" existed only because the section was
   planned on Email Routing, which cannot send — **the wrong premise had been sitting upstream of
   the wrong conclusion for a whole session.** One correction exposed a bigger one.

**THE OWNER SHOULD NEVER BE THE ONE TO ASK "should you revise the document?"** If he asks, the
sweep was already owed and already missed.



- **Spend the fewest tokens and the least battery.** Batch related questions and edits into a single
  operation and a single verification pass. Skip redundant work. Minimize narration.
- **⚠ THE CHAT IS THE COST, NOT THE FILE.** Re-reading `index.html` is cheap — one `curl`, then
  `grep`/offsets. What grows is the transcript, resent every turn. **The single biggest efficiency
  lever is ending a chat with a handoff and starting fresh.**
- **⚠ DO NOT SEQUENCE WORK INTO SEPARATE SHIPS THE OWNER MUST PUSH ONE AT A TIME.** Batch independent
  work into one delivered file and one push. **Session 28 produced six builds; only 28e needs pushing.**
- **⚠ THE OWNER ITERATES IN SINGLE INSTRUCTIONS AND WILL REVERSE HIMSELF WITHIN THE SAME HOUR.**
  **Flag the reversal in one or two sentences, then build what he asks.**
  **🆕 (28) AND HE WILL SOMETIMES REVERSE A WHOLE SHIP WITH ONE WORD — "Undo."** The correct response
  is to re-deliver the previous file **byte-identically**, confirm the hash matches what was given
  before, and state plainly what came back with it. **Do not rebuild it; do not bump the marker.**
  See §46.
- **⚠ BUT DO NOT OVER-WARN. WHEN HE PUSHES BACK ON A CAUTION, RE-EXAMINE IT HONESTLY AND CONCEDE IF
  HE IS RIGHT.** **A caution repeated after it has been answered is noise.**
- **⚠ WHEN HE CORRECTS A FACTUAL CLAIM, CHECK IT AND CONCEDE IN ONE LINE — THE CORRECTION IS
  USUALLY LOAD-BEARING.**
- **⚠ 🆕 (28) BUT WHEN HE STATES A FACT ABOUT THE CODE THAT IS WRONG, GO AND READ THE CODE AND SAY SO.**
  He asked *"if they transmit this to be submitted for territories, they cannot delete it correct"* —
  the code does the **opposite**, with no guard at all (§45.3). **Agreeing would have shipped a false
  privacy claim.** Verify, then correct with evidence.
- **⚠ THE OWNER ITERATES ON PRODUCT ONE INSTRUCTION AT A TIME, AND CONSTRAINTS COLLIDE.** When a
  request cannot coexist with an earlier one, **state the arithmetic and offer the options in the same
  message** — do not silently pick one, do not just execute the newest instruction.
  *(Session 28: the companion rows vs. the small-screen green-button rule. Options were tabled with
  measurements; the owner chose neither and gave a third instruction, which is normal.)*
- **⚠ WHEN THE OWNER SAYS "THIS IS A DISCUSSION," STOP BUILDING AND STOP PROPOSING BUILDS.**
- **⚠ WHEN HE SAYS "I AM TRYING TO FIGURE OUT HOW TO MAKE THIS WORK EASY," THE ANSWER IS TO REMOVE A
  MECHANISM, NOT TO TUNE ONE.** **Complexity he is fighting is usually something Claude added.**
- **⚠ AND HE WILL SAY SO DIRECTLY: *"I realize I'm complicating things."*** When he does,
  **measure, name the single real constraint, and fix only that.**
- **⚠ HE ASKS "WILL THAT FIT?" AND MEANS IT LITERALLY — ANSWER WITH A MEASUREMENT.** Never answer a
  fit question with an opinion.
- **⚠ HE VERIFIES CLAUDE'S CONSISTENCY AND IS RIGHT TO.** The correct response is to **run the check**,
  not to reassure.
  **🆕 (28) AND HE RE-ASKS ABOUT SETTLED DECISIONS TO TEST THEM: *"We discussed removing the gray out
  … remember."*** The right answer is **a census, not a yes.** Session 28 answered with 30 rows,
  0 dimmed, minimum opacity 1.00 — which is worth far more than agreement.
- **≥3 changes before rendering HTML / running the full Playwright battery**, unless the owner says
  "render now." `node --check` still runs after every edit. **Match verification depth to risk.**
- **Discuss before executing multi-part or consequential changes.** Surface findings and a plan first.
- **⚠ WHEN A FINDING CHANGES AN AGREED PLAN, STOP AND SAY SO BEFORE BUILDING.**
- **⚠ ⚠ 🆕 (28) SCOPE-EXTEND WHEN A HALF-BUILT FEATURE WOULD CREATE A DEAD END, AND SAY THAT IS WHY.**
  The teaser flag without a matching detail-card guard would have recreated the 27a "locked row with
  nothing to buy" hazard. Claude extended scope by one branch and named the reason. **That is correct
  and should be repeated.**
- **Never flood on base64 or any large data blob.** `grep -n` for landmarks; preview with
  `sed -n 'A,Bp' | cut -c1-300`; cap every grep with `cut -c1-200` + `head`. In Python strip blobs:
  `re.sub(r'[A-Za-z0-9+/=]{100,}','<BLOB>',seg)`. **Always pipe `sed` through `cut`.**
  **🆕 (28) AND WHEN A DATA URI SITS INSIDE THE REGION YOU ARE READING, STRIP `data:image/...;base64,...`
  FIRST** — otherwise the blob regex eats the surrounding markup and you see nothing.
- **⚠ WATCH FOR CATASTROPHIC REGEX.** **Use `str.find()` loops for landmark hunting; keep regex
  anchored and bounded. Put `timeout N` on every long python heredoc.**
- **`grep -c` every literal before writing a `str.replace`/`rep()` edit.**
  **⚠ 🆕 (28) AND REMEMBER `grep -c` COUNTS LINES, NOT OCCURRENCES.** Two hits on one line report as 1.
  Use `grep -o … | wc -l` when the count matters.
- **Developer-facing writing is plain and instructional.** Only *in-product UI copy* is Victorian.
- **⚠ COPY IS APPLIED VERBATIM.** Owner wording, casing, punctuation and unconventional spelling are
  never altered. House spelling is British "licence."
  - **⚠ INCLUDING PUNCTUATION THAT LOOKS LIKE A MISTAKE.** Apply verbatim, flag once, let him decide.
  - **⚠ AND HE USES PLAIN HYPHENS WHERE THE HOUSE STYLE USES EM-DASHES.** *"Visible short clue -
    12 characters"*. **Do not "fix" it to `—`.**
  - **⚠ AND LOWERCASE WITH A REAL ELLIPSIS.** The teaser label is **`coming soon…`** — his words,
    lowercase, U+2026. `&hellip;` in markup, `\u2026` in a script string.
  - **⚠ AND CLAUDE DOES NOT INVENT UI COPY UNASKED.** When a new string is genuinely needed,
    **propose it, label it as Claude's, and let the owner replace it.**
  - **⚠ A GLYPH REQUESTED IN SHORTHAND IS NOT INVENTED COPY, BUT FLAG IT ANYWAY.**
- **⚠ THE OWNER WILL TELL YOU WHEN COPY IS TOO ORNATE — BELIEVE THEM IMMEDIATELY.** Offer numbered
  plain-language alternatives and apply the chosen one verbatim. **Victorian is never obscure.**
- **For any visual/design change, deliver a self-contained preview.** **The reliable format is a
  PNG/JPEG via `present_files`** — standalone HTML previews do not render for the owner.
- **⚠ SHOW, DON'T DESCRIBE.** Render a real sample and deliver it. **⚠ AND SEE §11.R — A CAPTURE THAT
  HAS NOT PASSED THE LAYER AUDIT IS NOT A DELIVERABLE.**
- **⚠ DELIVER THE FILE NAMED `index.html`.** **🆕 (28) EXCEPT WHEN TWO DIFFERENT `index.html` FILES ARE
  IN PLAY** — the app and the website. Then name the website one distinctly and **tell him to rename
  it on upload.**
- **The owner marks up screenshots to specify UI changes.** Red arrow A→B means "move A to B."
  Yellow highlighter marks the element discussed. **Red X means delete this.** Red scribble/circle
  marks where something should go. **A red box around a group means the whole group.** Read the image
  before asking clarifying questions.
- **⚠ WHEN HE SENDS A BEFORE/AFTER PAIR OF SCREENSHOTS, THE WHOLE LAYOUT IS THE SPEC.**
- **⚠ HE ALSO SENDS SCREENSHOTS OF THE APP TO ASK A QUESTION, NOT ONLY TO SPECIFY A CHANGE.**
  **Measure the computed styles and answer; do not assume a change was requested.**
- **⚠ THE OWNER PUSHES BY HAND AND PUSHES CAN SILENTLY FAIL OR RENAME.** Five historical incidents.
  **After ANY ship, `curl` every file and confirm 200 + expected byte size AND hash.**
- **⚠ THE OWNER ASKS PRODUCT / PRICING / ETHICS QUESTIONS MID-BUILD AND EXPECTS A STRAIGHT ANSWER,
  INCLUDING "DON'T BUILD THAT."**
- **⚠ THE OWNER PUSHES BACK ON MONETISATION SMELL AND IS USUALLY RIGHT.** *"I don't want it to all look
  like a money trap."* Any feature justified by "this creates demand for coins" is suspect.
  Discovery-by-need beats advertising.
  - **⚠ AND HE APPLIES THE SAME TEST TO PLACEMENT, NOT JUST TO FEATURES.** **An offer belongs where
    the buyer already has the thing in front of them.**
- **⚠ THE OWNER ASKS DIRECTLY WHETHER HE IS BEING GREEDY. ANSWER WITH EVIDENCE, NOT COMFORT.**
  Hunters never pay, the territory map is free, no subscription, no ads, no energy timers, no paywall
  on the social side.
- **⚠ HE ALSO ASKS "DOES THIS SCALE FOR YEARS?" — ANSWER THE BUSINESS QUESTION, NOT THE CODE ONE.**
  **Rotation is not production — content authored once can resurface every year, because the audience
  turns over. Never design anything that obliges him to ship new material on a calendar.**
  **HE APPLIES THIS RULE TO HIMSELF UNPROMPTED:** *"really we will have to be responsible for
  publishing them live."* **That is why teasers carry no volume number and no count (§8x).**

---

## §2 — SESSION LENGTH & HANDOFF PROTOCOL

- **Warn before the chat gets too heavy.** Judge by activity load: a full `index.html` read, several
  large docs, repeated battery/Playwright runs, multiple multi-part edit cycles, or a compaction.
  Flag *before* quality degrades.
- **Trigger a handoff at cutover.** Also flag when the next task itself demands a fresh chat.
- **The handoff is the canonical rules registry.** Every standing rule — including this one — must be
  carried into each handoff and each Project-Instructions revision, restated **in full**.
- **⚠ A CHAT THAT SHIPS MUST PRODUCE A HANDOFF.** Sessions 18–28 all produced one — keep the streak.
- **⚠ WHEN THE OWNER DECLINES A HANDOFF AND KEEPS GOING, KEEP WORKING BUT RESTATE THE EXPOSURE ONCE
  PER SHIP, BRIEFLY.** State the risk in one clause on the ship line and move on; do not lecture,
  do not refuse. *(Session 27 flagged cutover five times — too many. Session 28 kept it to a clause.)*
- **⚠ ONE MASTER DOCUMENT, NOT A CHAIN OF AMENDMENTS.** Every handoff supersedes the whole chain.
  Tell the owner explicitly which files to delete from project knowledge.
- **§2b — HANDOFF VERIFICATION PASS (mandatory).** Every handoff must end with a pass proving it
  matches the final `index.html`: (1) `wc -c` equals the §0 size; (2) SHA-256 recorded in §0;
  (3) grep-verify every code-factual claim; (4) hash the exact file passed to `present_files`.
  - **⚠ AND VERIFY INHERITED CLAIMS, NOT ONLY NEW ONES.** See §0.1.

---

## §3 — SESSION PROTOCOL

- **Start of session:** **`curl` Pages, `sha256sum`, compare to §0** — first action of any session
  that will touch code. **`curl` EVERY repo file — the list is ten entries as of s52 and it changes
  without ceremony.** Audit the repo file list. **`curl` the Worker root (must read **v2.6.1**) and
  `/list` with no token (must be 403); also confirm `BAKER221B` is 403.** Then run the §32 bootstrap.
  Cross-verify docs against the live file; surface contradictions; rank open items.
  **🆕 (28) ALSO `curl` scavengerandhunt.com and its `/privacy.html` (§44).**
- **"review"** → full cross-verification, then prioritized fixes and start work.
- **"write handoff" / "handoff"** → single master handoff superseding all prior, restating all
  standing rules, delivering the current `index.html` via `present_files` (named `index.html`),
  ending with the §2b pass.
- **When Claude can't fetch something itself**, give step-by-step owner instructions plus a direct
  link ("homework" protocol). **The paste-in protocol is proven — see §A.1.**

---

## §4 — SOURCE-OF-TRUTH HIERARCHY
1. **The live `index.html` is ground truth.** Code wins over docs, always.
2. **This SUPER-HANDOFF.md.**
3. **`Marketing-Brief.md`** (session 28) — canonical for store listing, positioning, channels and the
   constraints on outward-facing copy. **`Monetization-Brief.md`** (session 27) — canonical for pricing
   mechanics. Both defer to code.
4. Superseded handoffs — history only. **⚠ They contain at least four error classes (§0.1) — treat
   their factual claims as unverified.**
5. **The Project-Instructions doc is materially stale** on file size, the map/clustering rule, the
   single-file claim (**the repo is ten entries, not five — s52**), and the **entire pricing model**
   (§9). Ignore those.

---

## §5 — FILE ACCESS & EDIT SAFETY

- Read-only sources: copy to `/home/claude/work/`, edit there, run the battery, output via
  `present_files` (named `index.html`).
- **Exact-literal edits:** Python `rep(old,new,label)` = `str.replace` with `assert count==1`.
  **Always edit in binary mode** — text mode silently normalizes CRLF→LF.
  - **⚠ `rep()` SHOULD TAKE AN EXPECTED-COUNT ARGUMENT.** `rep(old,new,label,n=2)` with
    `assert count==n` is safer than looping or than dropping the assert.
  - **🔴 EVERY REPLACEMENT NEEDS AN ASSERT, INCLUDING SUB-REPLACEMENTS INSIDE A BLOCK.**
    **`assert NEW!=OLD` after every sub-replacement.**
  - **⚠ 🆕 (28) A BYTE LITERAL CANNOT CONTAIN NON-ASCII.** `b'… §9 …'` is a `SyntaxError`. Keep
    section marks and em-dashes out of Python byte literals; use the escape or plain ASCII.
- **🔴 PYTHON ESCAPING FOR JS ESCAPE SOURCE — GET THIS RIGHT OR THE EDIT LANDS CORRUPT.**
  The file stores unicode as **literal `\uXXXX` escape source inside `<script>`**, but as **real
  characters in markup**. To land `\u2014` in the file the Python literal is `'\\u2014'` — **not**
  `'\\\\u2014'`, which lands `\\u2014` and breaks the string.
  **THE SAVING GRACE: a failed assert mid-script leaves the on-disk file untouched.**
  **Never write incrementally; write once, after every assert passes.**
  **AND THE SAFEST TECHNIQUE: byte-surgery on the ORIGINAL block** — extract the exact bytes, do
  targeted sub-replacements on them, splice back.
- **⚠ ALWAYS `repr()` THE INJECTED REGION AFTERWARDS** and compare it against the surrounding code's
  escaping style.
- **⚠ ANCHOR UNIQUENESS IS NOT ENOUGH — THE ANCHOR MUST NOT BE A SUFFIX OF SOMETHING LARGER.**
  An insertion anchored on `function stampedCard(code){` also matched the tail of
  **`async function stampedCard(code){`**. **Before inserting before a function, grep for `async ` +
  the anchor.**
- **⚠ AND AN ANCHOR CAN OCCUR TWICE IN DIFFERENT FUNCTIONS.** Anchor on a unique nearby literal and
  `rfind` backwards from it.
- **⚠ 🆕 (28) WHEN THE TARGET CONTAINS A HUGE DATA URI, SPLICE BY INDEX, NOT BY LITERAL.**
  Find the opening tag, find the closing tag, assert on a short unique substring inside the span,
  then replace `t[i:j]`. **This is how the 40 KB stamp button was swapped in 28f.**
- **⚠ WHEN AN EDIT LANDS WRONG, `rm` THE WORKING COPY AND REBUILD FROM THE VERIFIED BASE.**
  Do not patch a patch.
- **`re.sub` replacement-string gotcha:** literal replacements containing `\` or `$` must be inserted
  by slicing (`txt[:a]+NEW+txt[b:]`), not via `re.sub(...,NEW,...)`.
- **⚠ NEVER BUILD A LITERAL VIA `sed -i` WITH A BASE64/DATA-URL PAYLOAD.** **Use a heredoc.**
- **⚠ 🆕 (28) NEVER `pkill -f <pattern>` WHERE THE PATTERN MATCHES YOUR OWN COMMAND LINE.**
  `pkill -f "http.server 890"` killed the shell running it and lost the whole step, including an
  un-written heredoc. **Restart servers by starting a new one; do not mass-kill.**
- **⚠ DON'T BE CLEVER IN SHIPPED CODE.** Shipped code must read plainly.
- **⚠ LEAVE DEAD CSS/JS RATHER THAN MAKE AN UNREQUESTED CHANGE.** Flag it for a cleanup pass; don't
  freelance. **Current dead items are listed in §13.10.**
  - **⚠ BUT PREFER REPURPOSING A DEAD RULE TO ADDING A NEW ONE.**
- **Publishing link:** https://github.com/gahensley1/Hunt/upload/main → live at
  `gahensley1.github.io/Hunt`. **Deleting a file:** open the file's page → trash icon → scroll down
  and commit. On mobile Safari use ᴀA → Request Desktop Website.
- **⚠ THE REPO IS PUBLIC.** Session 20 found a brokerage statement publicly downloadable. Deleted from
  `main`, **still in git history** (§13).

---

## §7 — BRAND & VOICE (fixed — draw from, don't invent)

- **Palette (verified from `:root`):** `--paper #EDE4D3`, `--paper-2 #E3D7C0`, `--ink #1E1C1A`,
  `--ink-soft #4A4239`, `--tweed #7A5C3E`, `--tweed-dk #5E4630`, `--green #2E4739`,
  `--green-dk #22362B`, `--brass #B8863B`, `--brass-lt #D8AF63`, `--oxblood #8A3324`,
  `--title #20140C`, `--line rgba(30,28,26,.14)`. **⚠ THERE IS NO `--brass-dk`.**
  No pure `#FFF`/`#000`. Green is the field; brass is accent/border, never large fills. Map tones:
  sepia `#8A7148`, deeper `#6B5233`; land `#D6C08D`; hunt-pin red `#8A3324`/`#4A1508` + `#D8AF63` dot.
  **⚠ PREFER AN EXISTING VAR OVER A NEW HEX — AND CONFIRM THE VAR EXISTS BEFORE USING IT.**
  - **⚠ `--brass` ON `--paper` IS A SOFT CONTRAST AT SMALL SIZES.** The hint toggle uses it at
    12.5 px; `.volband` uses it at 8.5 px. **Both are owner choices.**
    **🆕 (28) THE LOCKED-ROW DIM THAT MADE IT WORSE IS GONE — SEE §8x.**
- **Type:** `--serif` = Playfair Display (agency voice) + `--type` = Special Elite (paperwork voice).
  **Never a third face.** Five embedded woff2. The baked stamp uses a condensed face — pixels.
  - **⚠ THE EMBEDDED FONTS CAN BE EXTRACTED FOR OFF-APP ART.**
    `re.search(r"font-family:...Playfair Display...src:url\(data:font/woff2;base64,([A-Za-z0-9+/=]{200,})\)")`
    → `fontTools.ttLib.TTFont(BytesIO(b64decode(...)))`, `flavor=None`, `.save('pf.ttf')`.
    **Four Playfair weights extract: 500, 700, 900, 600.** `pip install fonttools brotli
    --break-system-packages`. **Always typeset brand art in the real embedded face.**
- **Copy lexicon:** Credentials not Account · Cipher not Password · Case Files not Levels ·
  Minted/Issued not Unlocked · Hunter/Detective not User · **"Undercover Agent" not Guest.**
  No emoji/slang in-product (the share message's 🔍 is the one exception).
  - **⚠ 🔴 "CASE" AND "PACK" ARE BOTH BEING RETIRED IN FAVOUR OF "VOLUME."** Single-case purchase no
    longer exists (§9). `buyPack()`'s toasts still say "pack" but the function has **zero callers**.
    **The §8v turn-away message still says "pack" and IS live — that one needs a sweep.**
  - **⚠ BUILDER-FACING COPY IS PLAINER THAN THE REST OF THE APP AND THAT IS DELIBERATE.**
    Current builder strings are the owner's own words: *"Visible short clue - 12 characters"*,
    *"optional hints/clues can be added later by tapping clues"*, *"+tap here to add hidden hint"*,
    and the hint placeholder. **Lower-case, hyphens, no ornament. Do not Victorianise them.**
  - **⚠ CURATOR-FACING COPY IS PLAINER STILL.** The volume selector's free option reads
    **`Free case — no volume, plays free forever`** (Claude's copy, flagged, replaceable).
- **⚠ VICTORIAN IS NOT OBSCURE.** In-product copy must parse on first read.
- **Motion = ceremony:** period machinery. No confetti, bounce, or modern easing. House easing
  `cubic-bezier(.45,.05,.35,1)`. Exception: the `pinBoost` hard step (§8b) is deliberate.
- **Reserved SVG IDs — never repurpose:** `wax`, `disc`, `brass`, `arcTop`, `arcBot`, `emblem`.
  Water ID `gWater`. **`gWaterLbl` was REMOVED — the map renders no text layer.**
- **Icon rules:** no conifer silhouettes outside Christmas art — `.spark`/`.npark` map glyphs are the
  deliberate exception. Overlay ✕ goes top-left.
- **⚠ NEVER USE A REAL-WORLD TRADEMARK OR POLICE INSIGNIA.** The Metropolitan Police crest was asked
  for and **declined, and must stay declined.** **The WORDS "Dispatch from Scotland Yard" and "from
  the Metropolitan Police" are fine.** Cards use the app's own stag crest.
  - **⚠ 🆕 (28) OPEN QUESTION, RAISED AND NOT ANSWERED: the credentials badge art carries the motto
    `'S RIOGHAL MO DHREAM`, a real Scottish clan crest badge.** Claude cannot verify its provenance
    or licensing from the sandbox. **Flagged to the owner; no decision taken. Worth checking before
    store submission.**
- **The nudge / highlight vocabulary:** a 44×44 `.nudge` magnifier that flies in, acts on a target
  with a brass `.nudge-ripple`, and flies out. Live: `#title-nudge`, `#join-nudge`, `#move-nudge`.
  - **`huntEdge`** — brass box-shadow glow + border-colour pulse via `.huntspot`, 820 ms. **Uses
    box-shadow, NOT border-width, so there is no layout shift.**
  - **`clueRoll` / `.clue-zoom.rollhi`** — a `::before` band at `z-index:-1` travelling **behind** the
    words (§8i).

---

## §10 — OWNER DECISIONS — do NOT revisit
- Baked brass plates stay; the blank-bar + live-text redesign is permanently dead.
- One `index.html` for the app (plus the four siblings).
- Don't re-run WebP on brass/leather **textures**.
- "Build One Case" $0.99 tier is retired; Charter-only.
- Builders do not get an undercover mode. **Owned packs never re-lock.**
- **Bonnie B. Baker of 221B Baker Street is the main character** — the Holmes; her portrait anchors the
  main page; all other characters are Chihuahuas spawned from her. **She is also the owner/proprietor
  of Scavenger & Hunt Co.** Cast is naturally gender-balanced without announcing it.
- **The name stays "Scavenger & Hunt Co."** (§33). **`shco:` storage prefix must never change.**
- **Home page = 3 plaques: Build / Join / Cold Cases.** Case Files & Players via the **stamp link.**
  **⚠ 🆕 (28) A FOURTH PLAQUE WAS BUILT AND UNDONE — §46.**
- **Water bodies (shapes) are wanted on the map**, muted sepia. **Water LABELS are NOT wanted.**
- **Cold-case page has NO footer.** Staff reach the Curator's Desk via a **hidden ~600 ms long-press on
  the home © line.**
- **The GA/SC state line follows the Savannah River geometry** by design.
- **Park tap filters by SURROUNDING AREA, 25-mile radius.**
- **The clue line appears UNDER the tile on BOTH grids**, capped at **12 characters**.
- **NO extra magnification level. Hunt pins take a HARD STEP to 2.0× at maximum zoom only.
  NEVER CLUSTER map pins.**
- **The build move tour retires only after a completed reorder**; the hunt tour retires on first find.
- **Hunter finds save device-local FIRST**, then sync; the toast tells the truth (§8j).
- **The build marker changes EVERY delivered `index.html`** (§8k) — **except on an Undo (§46).**
- **The home stamp reads "FIND CURRENT & OLD CASES HERE."**
- **The hunt tour's oxblood tip OVERLAPS the black tip by 500 ms and then STAYS PUT.**
- **Toasts fire fast — ~450 ms, just clear of the 280 ms screen fade.**
- **On Case Ready: Copy Case Number lives INSIDE the dashed case card.**
- **In the build-screen hint, ONLY the phrase "Take a case from the Cold Case Files" is the link.**
- **The enlarge glow travels BEHIND the caption**, first photo clue opened in EACH hunt.
- **The invitation link's origin is DERIVED from `location`, not hardcoded.**
- **The invitation message keeps its explanatory text**, and **ends on the case number.**
- **`j.html` carries NO `og:image`.**
- **No real-world trademark or police insignia in the art.**
- **Cases cap at 50 clues.**
- **The shared case number carries a thin space**; `#join-code` is `maxlength="8"`.
- **The commendation card renders on the HUNTER's device.**
- **The commendation coin is `COIN_HERO` (ratio 1.058), not `COIN_P` (0.963).**
- **Hint coins are the SAME trophy coins.** **RANK IS A HIGH-WATER MARK.**
- **NO SEPARATE COIN FAUCET.** Earn by solving, or buy 5 for $0.99.
- **A REVEALED HINT STAYS REVEALED. THE HIDDEN HINT IS A CHEAT, NOT A REQUIREMENT.**
- **NO required hint per case.** **THE CLUE FIELD IS NOT A "DESCRIPTION."**
- **NO IN-APP PURCHASE GATE. NO INSTALL AGE CHECK. PURCHASING STAYS.** See §37.1.
- **ALL CURATED CASES MIGRATE TO 8 DIGITS.** See §38.
- **EVERY PURCHASE GOES THROUGH `requirePurchase()`. NO NATIVE `confirm()` ON A PRICED ACTION.**
- **THE CHARTER IS UNLIMITED BUILDS, NOT A QUOTA.** **Never introduce a per-case build charge.**
- **CLAUDE DOES NOT INVENT UI COPY.** **RETENTION IS 60 DAYS.**
- **THE HIDDEN-HINT FIELD IS FOLDED, BEHIND A GOLD "+tap here to add hidden hint ▾" LINE.**
- **THE PRIMARY GREEN BUTTON MUST BE VISIBLE WITHOUT SCROLLING ON EVERY SUPPORTED PHONE (§8g.1).**
- **THE CHARTER SCREEN SELLS ONLY THE CHARTER (§41.1).**
- **THE CLUE PLACEHOLDER READS "Visible short clue - 12 characters" — plain hyphen, owner copy.**
- **A VOLUME IS THREE CASES, $1.49, FOREVER. SHELF-PURE, NEVER MIXED.**
- **SINGLE CASES ARE NOT SOLD. THERE IS NO INDIVIDUAL PRICING.**
- **ONE FREE CASE PER SHELF IS STANDARD; EXTRA FREEBIES ARE ALLOWED AND UNCAPPED — AND FREE IS PERMANENT.**
- **APPEND-ONLY: BUILD VOLUMES AND ADD TO THEM. NEVER EDIT OR UNPUBLISH A VOLUME.**
- **A VOLUME IS NOT SELLABLE UNTIL ALL THREE OF ITS CASES ARE LIVE.** ✅ built.
- **TEASERS CARRY NO VOLUME AND NO COUNT. THE LABEL IS `coming soon…` (lowercase, U+2026).** ✅ built.
- **THE SHELF STAMP READS `BUY VOL n` IN ARABIC; THE EYEBROW STAYS ROMAN.**
- **THE SHELF IS SORTED FREE → VOL 1 → VOL 2 → VOL 3.**
- **THE VOLUME REGISTRY MOVES TO D1 SO THE DESK CAN MINT VOLUMES (§43.3).**
- **🆕 (28) THE DIM BELONGS TO TEASERS ONLY. PAID ROWS RENDER AT FULL OPACITY.**
- **🆕 (28) THE DETAIL CARD LISTS THE VOLUME'S OTHER TWO CASES, WITH THE CURRENT CASE'S OWN
  `View sample` PILL INSIDE ITS DESCRIPTION BOX (§8y).**
- **🆕 (28) THE HOME CREDENTIALS BLOCK IS AT 75 % (§8z).**
- **🆕 (28) THE SITE BACKGROUND IS THE APP'S REAL PARCHMENT TEXTURE — the owner kept it after being
  told it measures darker than the flat colour.**
- **🆕 (28) THE PUBLIC CONTACT ADDRESS IS `info@scavengerandhunt.com`.**

---

## §11 — EDIT-SAFETY & BATTERY PROTOCOL
- **Battery before every ship** (recreate the ~20-line agents; suites vanish between sessions — §32):
  - **Agent A** — `node --check` on the extracted largest `<script>` block.
  - **Agent B** — every `on*=` handler resolves. **Known false positives:**
    `if`/`for`/`while`/`setTimeout`/`setInterval`/`return`/`switch`/`catch`/`event`/**`function`**,
    and the four method hits **`blur`, `replace`, `scrollTo`, `stopPropagation`**.
  - **Agent D** — tag balance. **🔴 MEASURE THE DELTA AGAINST THE PREVIOUS BUILD, NOT AGAINST A
    RECORDED ABSOLUTE BASELINE.** The old baseline (`button −1`, `span −1`) **does not reproduce**
    with a plain `<tag\b` / `</tag>` regex, which gives 0/0. **Every delta must be explainable.**
    *(Session 28: ALL ZERO on every build, including the plaque swap in 28f.)*
  - **Hygiene** — zero `console.log`, zero duplicate base64, `http://` audit.
- **Render check:** headless Playwright at **390×844 and 320×568**, deviceScaleFactor 2.
  **FOR ANYTHING THAT CHANGES MODAL HEIGHT, ADD 375×667 AND 430×932 — see §8g.1.**
  **Playwright is NOT preinstalled — `npm i -g playwright && npx playwright install chromium`, ~1 min.**
  Import by full path: `/home/claude/.npm-global/lib/node_modules/playwright/index.mjs`.
- **⚠ SERVE OVER HTTP, AND RESTART THE SERVER EACH TURN.**
  `(setsid python3 -m http.server 8901 --directory serve >/tmp/s1.log 2>&1 </dev/null &)` then `sleep 4`.
  **`ERR_CONNECTION_REFUSED` means the server died, not that the code broke.** *(Hit three times in 26,
  three in 27, **five in 28**.)* **Guard with `pgrep -f 8901 >/dev/null || (start it)` — and see §5 on
  never `pkill`-ing a pattern that matches your own shell.**
  **`file://` cannot test the cards** — copy `og-card.jpeg` and `award-card.jpeg` into the serve dir.
  **TIP: run a SECOND server on another port pointed at the previous build** to answer "did I cause
  this?" with data rather than memory. **Used to great effect in 28e (§8z).**

### 🔴 §11.R — **NO SHUTTER WITHOUT A CLEAN AUDIT**

**THE FAILURE THAT FORCED THIS.** Session 27 delivered a Curator's Desk screenshot with **two
full-screen overlays on top of it**. The cleanup step was skipped, and even when run, `curpass-ov` had
never been in the cleanup list. The owner caught it.

**🔴 THE RULE — the list is best-effort; THE AUDIT IS THE GATE.**

1. **Before every capture, run an UNFILTERED sweep** of `body *` for any `fixed`/`absolute` element
   that is visible and whose rect **intersects the target**, excluding the target's own subtree.
   **NO z-index floor. NO size floor.**
2. **If the sweep is non-empty, DO NOT CAPTURE.** Add the offender, re-clean, re-audit.
3. **Run the cleanup TWICE with a short gap.** `#scrollhint-ov` **re-shows itself within ~900 ms of
   boot**, so a single clean at load is not enough.
4. **When capturing an overlay deliberately, exempt it BY ID** rather than skipping the audit.
5. **🆕 (28) WHEN THE AUDIT FLAGS SOMETHING GENUINELY *BEHIND* THE TARGET, PROVE IT WITH Z-INDEX
   BEFORE EXEMPTING IT.** The cold-case backdrop `cold-ov` z500 sits under `colddetail-ov` z510 —
   **read both computed z-indexes and compare, do not assume.**

**Known cleanup list:** `scrollhint-ov`, `curpass-ov`, `ov-name`, `record-ov`, `ov-commend`,
`ov-coins`, `ov-buy`, `ov-loupe`, `tour-sign`, `tour-down`, **`commish-card`**, **`commish-ov`**,
**`commish-seal`**, plus `.overlay.open` and both toasts.
**🆕 (28) `commish-card` (z498) WAS ADDED — it was found sitting over the cold shelf by the audit.**

**⚠ WHY THIS BITES CLAUDE SPECIFICALLY: the `view` tool returns blank images in this sandbox
(sessions 20–28). Claude cannot look at its own screenshots.** Every visual claim is a measurement,
never an observation. **The audit is the only thing standing in for eyes.**

- **⚠ MEASURE TOASTS/ANIMATIONS AT A SETTLED MOMENT (~2200 ms+)** — except when measuring *first paint*,
  where you **poll at 50 ms**.
- **⚠ A CLASS IS NOT A PIXEL, AND A MECHANISM IS NOT A PATH.** Drive the real entry point.
- **⚠ VERIFY GEOMETRY BY MEASUREMENT, NOT BY EYE.**
- **⚠ STATE PLAINLY WHEN A DELIVERABLE WAS VERIFIED BY MEASUREMENT RATHER THAN BY EYE**, and deliver
  the artefact. **AND SAY SO WHEN THE OWNER FINDS A VISUAL FAULT.**

### 🔴 §11d — TEST-HARNESS RULES. WRITTEN s57, AFTER THE HARNESS FAKED A BUG FOR MANY BUILDS.

**Delivered as rules and applied VERBATIM. Do not paraphrase or compress these.** The incident that
produced them is §89 — the harness's own stub called `fetch(null)` on itself, and Check 4 could not
see the resulting 404 because it only asserted "no page errors".

```
## Test-harness rule - make the failure visible, and don't let the stub fake it

Two independent failures let a `GET /null 404` fire on every boot for many builds
with the battery staying green. Both are general; both are now rules.

### 1. A `page.evaluate(string)` stub must NOT end on a function-valued expression

`page.evaluate(str)` returns the string's **completion value**, and Playwright
serialises that value **by value**. When the completion value is a *function*,
Playwright **invokes it** - passing `null` as the argument.

So a stub whose last statement is an assignment like:

    window.fetch = async (u, o) => { ... return _f(u, o); };

leaves the completion value = the fetch function -> Playwright calls `fetch(null)`
-> `"null"` resolves against the origin -> `GET /null` 404. The stub fetched itself;
the app was never involved.

**Rules:**
- End every `evaluate`d stub string on a **primitive** (`true;`, `0;`, `void 0;`),
  or wrap the mutations in a named function and call it separately
  (`window.__stub = () => {...};` then `evaluate("window.__stub()")`) so the
  completion value is `undefined`. (behaviour.py already does the wrapper form -
  copy it.)
- Never leave an assignment-to-a-function as the last statement of an `evaluate`d
  string.

### 2. "No page errors" is NOT "nothing went wrong" - assert on the network too

A failed subresource fetch is **not** a `pageerror`. A boot check that asserts only
"no page errors" is blind to any 404/500/failed request. A green tick is an exit
code, not a result; a test that cannot see the bug is a copy of the bug.

**Rules:**
- Every boot check records responses and **fails on any unexpected 404** (or 4xx/5xx
  and `requestfailed`). If the app has deliberate 404s, allow-list them explicitly;
  everything else goes red.
- Before trusting a new check, **prove it has teeth** - force the failure once and
  confirm it turns red. A check that can only return "clean" is not a check.

### 3. Attribute before you fix - isolate one variable at a time

The symptom was pinned by toggling the harness's two post-load steps (stub, gate)
independently across four runs and seeing which one reproduced it - not by reading
the app and guessing. When a symptom appears only under the full harness, split the
harness and run the cells. If neither half alone reproduces it, they interact -
report that; don't force a story.

**Rule:** never state a cause as fact until an experiment isolates it. Validate, or
label it unproven.
```

**🔴 RULE 1 HAD TWO HOMES (§1w).** `session_checks.py` was fixed when the cause was found;
**`test\\find-null.py` still ended on the same assignment** and was caught in review afterwards. A
probe carrying the defect it hunts reproduces its own artefact on every run and reads as a live bug.
Both now end on `true;` with a comment saying why it must stay. **When rule 1 is applied, grep every
`evaluate(` in `test\\` — not just the file that failed.**

### §11a — ⚠ VERIFICATION METHODS THAT GAVE FALSE ANSWERS
**Eighteen methods have now produced confident, wrong results in this project.**
1. **Colour/saturation masks over parchment.**
2. **Resizing two images to a common square before diffing** — destroyed the aspect-ratio difference
   that was the entire question, and the oblong coin shipped.
3. **Bounding boxes when two objects overlap.**
4. **Stubbing an asset from the page.** `window.PAW_INK="…"` did nothing because `PAW_INK` is a `const`
   in a closure.
5. **Measuring a gap next to a contact shadow.** **A scan window beginning where you expect the answer
   will always confirm your expectation.**
6. **Trusting that a delivered file was pushed.** **`curl` and hash-compare every repo file after any
   ship.**
7. **Reasoning about behaviour from a doc's description instead of reading the code.**
8. **A test harness that silently didn't run.** **Assert the precondition in the same result object as
   the measurement.**
9. **GREPPING THE CODE SHAPE WHEN THE FACT LIVES IN A DATA BLOB.** **Parse JSON data; grep only code.**
10. **A COLOUR MASK AGAINST AN 8px GLYPH AND A 55%-ALPHA HAIRLINE.**
11. **AN AUDIT WHOSE FILTER CAN ONLY RETURN "CLEAN."** **A check that cannot fail is not a check.**
12. **MEASURING A PNG FROM ONE BROWSER RUN WITH COORDINATES FROM ANOTHER.**
13. **CHECKING THAT AN ELEMENT *EXISTS* INSTEAD OF THAT IT IS *USABLE*.** **Presence is not
    reachability.** Assert `getBoundingClientRect().bottom <= innerHeight`.
14. **SCROLLING THE WRONG NODE AND CONCLUDING "UNREACHABLE."**
15. **SHOOTING THROUGH AN OVERLAY BECAUSE THE CLEANUP LIST WAS INCOMPLETE.** **See §11.R.**
16. **A HARNESS THAT INJECTS STATE THE APP THEN REBUILDS.** `openColdCases()` rebuilds `_coldIdx`,
    `coldCatOpen()` rebuilds it again, and **`publishCold()` calls `renderCurator()` at the end**.
    **Inject AFTER every rebuild, and always return a `precondition:` field.**
17. **🔴 NEW (28) — EDITING CSS WHEN AN INLINE STYLE FROM JS IS THE REAL SOURCE.** `.rank-stamp.home`
    `font-size` was scaled and **measured identical in both builds**, because `refreshHomeBadge()`
    sets `el.style.fontSize` from `base=30.94` with a length-based shrink. **The CSS edit was a
    no-op.** **Before changing a computed value, grep for `.style.<prop>` on that element.**
    **The A/B server (§11a(g)) is what caught it — a single-build measurement would have looked fine.**
18. **🔴 NEW (28) — ASSERTING ON THE WRONG TARGET AND CALLING IT A CODE FAULT.** The CASE FILES plaque
    click was tested against `#record-ov` and returned "not open." **`openCaseFiles()` calls
    `go("s-cases")` — it is a screen, not an overlay.** **Read the function before writing the
    assertion.** *(Caught and corrected in the same turn; nothing shipped on it.)*

**✅ WHAT WORKS:** **(a) diff the finished render against the base art** (`|S−B|.sum(2)>34`);
**(b) read the geometry out of the running page**; **(c) drive the real function and assert on its
return value**; **(d) inject the future state at runtime and drive it**;
**(e) THE DIFFERENTIAL RENDER, THE HOUSE METHOD FOR "DID THIS PAINT?"** Screenshot with the element
visible, hide **only** that element (`visibility:hidden`), screenshot again, diff.
**(f) THE MULTI-VIEWPORT ASSERTION TABLE.** Four viewports **and both states of any collapsible**.
**(g) THE A/B SERVER.** Serve the previous build on a second port and measure both in one script.
**🆕 (28) THIS IS NOW THE HOUSE METHOD FOR ANY "SCALE IT BY N%" INSTRUCTION** — print the ratio, not
the value.
**(h) THE INTRINSIC-WIDTH PROBE FOR "WILL IT FIT?"** Clone the real element, force
`position:absolute; left:-9999px; white-space:nowrap; width:auto`, read `getBoundingClientRect().width`.
**(i) THE CONSISTENCY PARSE.** Parse the registry and compare a typed value against its derived
counterpart (§41.2).
**(j) 🆕 (28) THE CENSUS.** When the owner asks "did we do X," enumerate **every** affected element and
report counts — *30 rows, 0 dimmed, minimum opacity 1.00* — rather than answering yes.
**(k) 🆕 (28) PIXEL-SAMPLING A DELIVERED RENDER.** For "is this colour right," open the PNG and read
the actual pixels. It is how the site background was found to be exactly `#EDE4D3`, and later 204
luminance.

### §11b — 🔴 TESTS MUST NEVER WRITE TO THE LIVE WORKER
`Store.set(key, val, true)` — the third argument — writes to **the production Cloudflare Worker and D1.**
Session 23 did this twice and caused a real production incident.

**THE RULES:**
1. **Never pass `shared=true` in a test.** **Stub `Store` at the top of every probe:**
   ```js
   const mem=new Map();
   Store.get=async k=>mem.get(k)??null;
   Store.set=async(k,v)=>{mem.set(k,v);return true;};
   Store.list=async()=>[]; Store.del=async()=>true;
   ```
   **✅ Sessions 24–28 stubbed on every suite and wrote nothing.**
2. **`finishBuild()` PUBLISHES.** Any test that calls it mints a real case.
   **SO DOES `publishCold()` — it writes `hunt:<code>` AND `cold:index`. Stub before driving it.**
   **🆕 (28) AND SO DOES `purgeCase()` — IT *DELETES*. NEVER DRIVE IT UNSTUBBED.**
3. **After any test session that touched `Store`, `curl` `/list` and diff against the expected key set.**
4. **Distinguish your data from the owner's before deleting.** **"Papi" and "Papi 2" are real plays on
   310401 — preserve them.**
5. **⚠ A STUB CHANGES WHAT RENDERS.** With `Store` stubbed, `.cold-meta` shows *"CASE No. 221221"* with
   **no "· 12 clues"**. **Seed the stub** — a `Store.get` that returns
   `JSON.stringify({code, tiles:new Array(12).fill({id:1})})` for any `hunt:` key is the cheapest
   seeding pattern — **before claiming anything about an async-populated line, and before capturing a
   screenshot that shows one.**
6. **SET `State.build` DIRECTLY TO TEST THE BUILDER SCREENS.** **A one-pixel PNG data URL is enough to
   drive `openCrop`.** **Set `State.captureMode="hunt"` + `State.huntTarget={id:9}` for the hunter branch.**
7. **TO TEST THE CURATOR'S DESK, SEED `mycases`.** Without it `renderCurator()` draws an empty list and
   every assertion returns a confident zero. Then `openCurator()` → `renderCurator()`, and hide
   `#curpass-ov` (§11.R).

### §11c — 🔴 NEVER INFER; VALIDATE, OR LABEL IT
**Owner instruction: *"never infer always validate we should never have this said again."***
- **Never state an unverified thing as fact.** Either validate it first, **or label it as unverified in
  the same breath — before the claim, not after being challenged.**
- **⚠ THIS APPLIES TO INHERITED DOC CLAIMS TOO** (§0.1) — **and especially to absence claims.**
- **Some things genuinely cannot be validated from the sandbox** — hardware share sheets, iMessage
  bubble counts, GitHub Pages' bandwidth terms, **the Worker's source**. For those: **say "I can't
  verify this from here" up front.**
- **⚠ WHEN THE OWNER STATES A FACT THAT IS WRONG, CORRECT IT WITH EVIDENCE IMMEDIATELY.**
  **🆕 (28) INCLUDING WHEN IT IS A FACT ABOUT THE CODE — see §45.3.**
- **⚠ AND WHEN THE OWNER CORRECTS *CLAUDE*, CHECK IT PROPERLY AND CONCEDE IN ONE LINE.**
- **⚠ 🆕 (28) AND WHEN A MEASUREMENT CONTRADICTS THE INSTRUCTION YOU WERE JUST GIVEN, SAY SO.**
  The owner asked for a lighter background; the parchment texture measures darker. **Reporting that
  is what let him make a real decision ("Keep").**

---

## 🔴 §13 — STANDING OPEN ITEMS (RE-RANKED AND RE-MEASURED, SESSION 52)

**Every item below was re-checked against `index.html` at 32i and against the live services on Aug 4
2026.** Items closed by measurement are kept, struck as CLOSED, with the evidence — they are not
deleted, because a closed item that vanishes gets re-opened by the next session.

### ✅ CLOSED SINCE THE s30 EDITION — DO NOT RE-OPEN

- **✅ 1. PUSH 29a AND `test/`. CLOSED.** Long since pushed; the repo is nine builds past it.
  **Nothing is pending push as of s52** — local == repo == Pages, `a951bf6a…`.
- **✅ 3. `CURATOR_PASS="BAKER221B"` — THE TOP SECURITY ITEM. CLOSED, BOTH HALVES.**
  Client: `CURATOR_PASS` **×0**, `BAKER221B` **×1 and only as `CURATOR_NAME`** — the public nameplate,
  explicitly commented "not a secret and not treated as one." `CURATOR_WORD` **×11**: declared
  `var CURATOR_WORD=""`, memory-only, never stored; `_curHdr()` is the single `X-Curator-Token` site
  (**×1 in the whole file**); wrong word clears it and toasts "The archivist does not recognise that
  word" — **it fails closed, as specified.** Worker: **the rotation happened** — `BAKER221B` → 403.
  **The load-bearing order in the old item was followed. Nothing here is left to do.**
- **✅ 6. THE SERVICE WORKER. CLOSED.** `sw.js` in repo, 200 on Pages. **⚠ THE HASH THAT STOOD HERE
  (`61a93b05…`, 3,435 B) WAS NEVER CORRECT — see the §0 row. It measured 3,349 B / `54127008…`, and
  as of s54 it is 5,532 B / `7a1682bd…` with the push receiver (§71).** Registered
  https-only inside a `try`, on `load`, with a swallowed `.catch()`. Its own header states the
  non-negotiables: **network-first for the document** (a 3.8 MB cache-first would pin hunters to a
  dead build), never cache the Worker, never cache a non-GET/non-200/opaque response, versioned cache.
  **It stores no hunter data.**
  - **🔴 BUT `manifest` IS STILL ×0.** The SW shipped without a web-app manifest, so there is still no
    install prompt and no home-screen identity. **This is the remainder of item 6 and it is small.**

### 🔴 STILL OPEN — RANKED

1. **🟢 INSTRUMENTATION — MOSTLY BUILT. ONE GAP.** ⚠ **The s52 re-base first recorded this as "NO
   INSTRUMENTATION" and that was WRONG — see §53.1.** What actually ships at 32i is
   **the Company Ledger (SPEC-51.4 §3)**: `function ev(name,code,tile,cat)` posting to **`/ev`** on
   the Worker, `keepalive:true`, `Content-Type: text/plain` (**CORS-safelisted on purpose, so it costs
   no preflight and adds no round trip**), `.catch()` swallowed. **It never blocks, never surfaces an
   error and never retries — offline, the count is simply lost.** Payload is event, case, clue id and
   shelf: **no name, no credential, no location.** Origin is stamped server-side from the request.
   **`EV_NAMES`, and the Worker rejects anything else:**
   `badge_issued` · `case_opened` · `case_finished` · `hint_completed` · `cold_viewed` · `case_scanned`.
   **Wired at six sites, all verified s52:** `mintCred()` → badge_issued · `joinCase()` → case_opened
   (after the expiry gate) · `finishHunt()` → case_finished · `openColdDetail()` → cold_viewed ·
   `markHintSeen()` → hint_completed · the deep-link handler → **case_scanned, deliberately fired
   before every gate, because `case_opened` only fires after five refusals and cannot answer how many
   people a poster actually reached.**
   **~~THE REMAINING GAP IS `first_find`~~ — ✅ BUILT AND LIVE, corrected s54 (§70.3, §73.4). It is
   in `EV_NAMES`, in the per-case ledger row, the totals row and the CSV. What follows is history;
   the gap it describes was closed and nobody noticed because the MONTH view never shows the
   figure — only the per-case sheet does.** The §49.3 funnel was opened / joined / first-find /
   finished. Scanned, opened and finished are covered; **there is no event on a hunter's first
   confirmed find**, so the drop-off between taking a case and getting one photograph — the single
   most diagnostic step — is invisible. **Adding it is a one-line `ev()` call plus a name in
   `EV_NAMES`, and the Worker must accept the new name or it is silently dropped.** That makes it a
   Worker-paste item, not a client-only one (item 5).
   **🔴 AND THE READ SIDE IS UNVERIFIED.** `/report` exists and is 403-gated, with three client call
   sites in the Desk ledger. **Nobody has confirmed what it returns or whether the numbers are
   sane.** Before building anything new here: **sign in at the Desk and look at the ledger.**
2. **🔴 NO BACKUP AND NO CLIENT EXPORT.** `exportAll` ×0 · `downloadBackup` ×0 · `exportCase` ×0 —
   unchanged since s29. Every case, profile and submission sits in one D1 table that `PUT` lets anyone
   overwrite. The mitigation is not auth (item 8 rules that out); it is **a periodic export**.
   **✅ THE s30 "ARCHIVE CLERK" (§51.3) — IT IS RUNNING. MEASURED s53, STATUS NO LONGER UNKNOWN.**
   The owner connected `Hunt-backups` and it was read directly. **All four setup steps were done.**
   Three snapshots on disk: `archive-2026-07-30.json` (121 B, one key), `archive-2026-08-03.json`
   (45,325 B, **749 listed keys**), `archive-2026-08-04.json` (45,758 B, **758 listed keys**), each
   `includesProfiles:true` across ten key families. **The archive half of item 2 is closed. What
   remains here is the CLIENT export — `exportAll` / `downloadBackup` / `exportCase`, still ×0.**
   **🔴 THREE DEFECTS FOUND IN THE CLERK, s53 — see §59. One was serious: the clerk was not backing
   up `SUPER-HANDOFF.md`.**
3. **🔴 THE FULL LOOP HAS NEVER RUN ON HARDWARE (§50.2).** build → share → join → photograph → verify
   → coin → rank, end to end, on two real phones. Everything verified to date is headless Chromium.
   **This is now the highest-risk item that no amount of grepping can close**, and it has been carried
   since s29 while nine builds shipped on top of it. Items 15 and 16 below are subsets of it.
4. **🔴 THE HOME PLAQUE / "CASE FILES" REQUEST — §46. STILL UNBUILT, CONFIRMED s52.**
   `btn-plaque` ×7 resolves to **three plaques on home** — `startBuild()`, `openJoin()`,
   `openColdCases()` — plus one repeat of the Build plaque in the empty-state of `#s-cases`.
   **There is no fourth plaque, and the red stamp is gone: `FIND CURRENT` ×0.** The `#s-cases` screen
   exists and is titled "Case Files", so the destination is built; **only the route from home is
   missing.** Rebuild as specified: **fourth `.btn-plaque` + the red `FIND CURRENT & OLD CASES HERE`
   stamp reinstated as its own element** (it was the silent loss of that stamp that got the s28 swap
   undone). The Case Ready copy change stands.
5. **🔴 THE WORKER SESSION — NOW TWO JOBS, ONE PASTE.** Was four; (a) the owner-delete door and
   (b) `CURATOR_WORD` are both done. **Remaining: (c) an export/backup route · (d) per-case counters.**
   **Owner pastes v2.6.1 source in, Claude hands source back** (§A.1). **⚠ The paste must be v2.6.1 —
   pasting the old v2.3 text back would silently revert the rotation-era Worker and `/report`.**
6. **🔴 §43.3 — MOVE THE VOLUME REGISTRY TO D1** so the Desk can mint Volume IV without a push.
   **Owner chose Option B. `volumeOf()` ×10 already reads the case record — half the bridge.**
   **⚠ `volumeReady()` (×2) must move with it.** *(s52 note: 32i shipped **agency licence minting** in
   the Desk — `validAgencyKey`/`AGY_KEY` ×3, `SEAT_PRICE` — so the Desk can now mint one kind of thing
   at runtime. Whoever takes this item should read that code first; the pattern may already exist.)*

7. **⚠ THE COLD DETAIL CARD AND THE SMALL-SCREEN RULE (§8g.1).** On 320 the $1.49 button sits 137 px
   below the fold; **on 375 it clears by only 3 px.** The owner accepted this knowingly, twice.
   **Cheapest fix if he changes his mind: clamp companion blurbs to one line (~62 px back).**
8. **⚠ `PUT` IS UNAUTHENTICATED.** **v2.3 did not fix it, and s52 has no evidence v2.6.1 did** and cannot without a per-user auth model.
   **Do not attempt a quick fix — it will break the app.**
9. **"pack" vs "Volume" copy sweep.** **§8v's turn-away message still says "pack" and IS LIVE.**
10. **DEAD CODE, LEFT DELIBERATELY — one cleanup pass owed (§5). RE-MEASURED s52:**
    **Still dead (definition only, zero callers):** `volumeSaving` ×1 · `volumeShort` ×1 ·
    `buyEverything` ×1. **`buyPack` ×2 = definition + one mention in a comment — still zero real
    callers.** `BUNDLE_PRICE` ×3. **⚠ `priceOf` IS NO LONGER DEAD — ×3, with two live call sites in
    the cold-detail buy path. Do not delete it.** `.stamp-link` ×5, still live. Original list:
    `.coldrow .caseno` CSS · `buyPack()` (0 callers) · `priceOf()` (only `buyPack` calls it) ·
    `volumeSaving()` (0 callers) · `volumeShort()` (0 callers) · `BUNDLE_PRICE` (×1, unrendered) ·
    `buyEverything()` (0 callers) · `grantEntitlement`'s `pack` and `everything` branches.
    **⚠ `.stamp-link` CSS is LIVE in 28e — it only became dead in the undone 28f.**
11. **`archiveCaseAsk()` still uses a native `confirm()` on a priced action** — contrary to the §39 rule.
    **RE-VERIFIED OPEN s52**: the function's own comment reads "App Store billing replaces the confirm() at release."
12. **§41.2 numeral-drift check** — add the label-vs-`volumeNo()` parse to the §32 bootstrap.
13. **No route to a volume for a non-builder (§9).** **Owner has not ruled.**
14. **The 8-digit case-number migration — §38.** **⚠ NOW ALSO TOUCHES NINE `VOLUMES[].codes` ARRAYS.**
15. **⚠ THE COMMENDATION CARD HAS NEVER RUN ON HARDWARE.** **Needs two devices or two browser profiles.**
16. **⚠ THE INVITATION MESSAGE IS UNPROVEN ON HARDWARE.**
17. **The commendation Notify button** — `email` ×0, `pushToken` ×0. **There is no address.** Owner's call.
18. **⚠ ACCESSIBILITY: `maximum-scale=1` blocks page zoom. STILL PRESENT AT 32i (×2, in the viewport meta).** iOS Safari overrides it; **Android Chrome
    honours it.** All type is `px` with **zero `em`/`rem`**. **Caveat: probably load-bearing for the
    map's `touch-action:none` pan and the loupe pinch.**
19. **⚠ UNANSWERED — build clue-tip read duration.** **3000 ms** → MOVE_TIP ~4200 ms; **2500 ms** →
    ~3700 ms; or leave it. **Carried unanswered since session 19.**
20. **⚠ git history still contains the brokerage statement.** **Owner decision owed, carried nine sessions.**
21. **⚠ `MAX_VALUE` is 2 MB and a 50-clue photo case approaches it.** A PUT over it returns 413. Untested.
22. **`/list` LIMIT 500** — **398–400 keys as of s30**; it will silently truncate at 500.
    **⚠ s52 COULD NOT RE-COUNT — the curator word is rotated and Claude does not hold it (correctly).**
    **Owner: check the key count at the Desk. If it is near 500 this is now urgent, not theoretical.**
23. **⚠ THE CREDENTIALS CREST MAY BE A REAL CLAN CREST BADGE** (`'S RIOGHAL MO DHREAM`). Unverified
    provenance. **§7 rule-adjacent. Worth checking before submission.**
24. **Face ID / WebAuthn on the Curator's Desk — §36.9.** **Sequenced AFTER the custom domain and AFTER
    §13.3.**
25. **The guardian's cipher** (§37.1) — designed, deliberately NOT built.
26. **Remaining file-size levers:** fonts ≈ 90 KB; `gWater` 238 KB; `COIN_HERO` 51 KB.
27. **River/border splices** for Mississippi, Ohio, Rio Grande — §8e recipe.
28. **Waterfront/off-river pins** — `gazAuto` centroid auto-fill → curator re-pin.
29. **Loupe follow-ups:** pinch centres on the stage not the finger midpoint.
30. **Registrar identity** (`#ov-name` vs `#scrollhint-ov`) — cleanup/dedupe. **⚠ ALSO A TEST HAZARD.**
31. **Stamp tap target** ~27–35 px tall (< 44 px comfort min).
32. **Undiffed +25 KB base** — session-9 work sits on an uploaded base never diffed.
33. **Doc-refresh debt** — **Project Instructions §9 pricing is fully superseded**, and it still
    describes a single-file repo, the old file size and pin clustering. **`Monetization-Brief.md`
    refreshed in 27; `Marketing-Brief.md` created in 28.**
34. **⚠ Move the deep link off the URL fragment** before store submission.
35. **THE WEBSITE (§44):** create the `info@` mailbox · HTTP→HTTPS redirect · lawyer review then remove
    the DRAFT banner · a 6.5″ screenshot set · Google Play's long description.
36. **Curation throughput** (§42) — one reviewer will not scale.
37. **CONTENT: 3 more Almanac cases — APRIL, JULY, AUGUST.** **Under the three-per-volume rule these
    become Almanac Volume IV** — the out-of-step growth the owner wants. **The natural next authoring task.**
38. **PROCESS — keep the handoff streak.**

**CLOSED SESSION 29:** **28e confirmed live** (hash-exact on Pages and raw) · **§45 all three
delete-path defects fixed** · **the territory deed built** — ownership transfer, mandatory tick,
reset-on-reopen, defensive server-side-of-the-UI guard · **`Store.del()` now returns the server's
verdict** · **a persistent test suite committed** — 21 assertions, proven to catch the exact defect
that shipped · **four structural gaps identified and specced** (§49, §50) · **the website found to be
un-uploaded** — a real blocker that the session-28 doc recorded as delivered.

**CLOSED SESSION 28:** 27c confirmed live · **the teaser state built** (§8x) · **volume-not-sellable-
until-complete built** (§9 rule 6 / `volumeReady`) · **companion rows on the detail card** (§8y) ·
**the credentials block scaled to 75 %** (§8z) · **$1.49 confirmed on both stores** · **store metadata
limits verified** · **Apple org-enrolment requirements verified** · **the App Store mockup and three
real 1290×2796 screenshots** · **`Marketing-Brief.md` created** · **the public website built —
three files, brand parchment, privacy policy stating 60 days** · **three delete-path defects found**
(§45) · **two new §11a failure modes** · Worker v2.3 re-verified.

---

## §14 — HOMEWORK (owner-side, unblocks Claude)
- **🔴 NEXT: PUSH 29a AND `test/`** — https://github.com/gahensley1/Hunt/upload/main — then confirm on
  `gahensley1.github.io` that the size is **3,690,652** and the marker reads **29a**.
  **The five `test/` files go to the repo root as a folder.**
- **🔴 UPLOAD THE THREE SITE FILES (§44) — STILL NOT DONE, AND THE DOC PREVIOUSLY SAID IT WAS.**
  `site-index.html` **renamed to `index.html`**, `privacy.html`, `parch.jpg`. **The domain currently
  serves a 4,260 B placeholder and `privacy.html` 404s (§47.6).**
- **🔴 ADD THE TERRITORY CARVE-OUT TO THE PRIVACY POLICY** before it goes up — territory cases are
  sweep-exempt and permanently held, which the flat 60-day claim does not cover (§47.2, §47.6).
- **🔴 CREATE THE `info@scavengerandhunt.com` MAILBOX.** Apple checks the address resolves.
- **🟡 THE LEGAL ENTITY — SEE §50.1. NO LONGER STALLED. `Do No Harm Company LLC` WAS SUBMITTED TO
  GEORGIA at s57, after the name was cleared.** Awaiting the state. **The moment it is approved,
  START THE D-U-N-S REQUEST — it is the 30-day item and it must match the registered name EXACTLY.**
  Entity → D-U-N-S (30-day lead, exact name match) → domain/mailbox → enrolment.
- **🔴 THE TWO-PHONE PLAYTEST — SEE §50.2.** Eight steps. The core loop has never been run end to end.
- **🔴 PASTE THE WORKER SOURCE at the start of the next session** — four jobs need it (§13.2).
  dash.cloudflare.com → **Compute (Workers)** → **Workers & Pages** → **deerstalker** → **Edit Code**.
- **🔴 FIX HTTP → HTTPS REDIRECT** on scavengerandhunt.com.
- **🔴 LAWYER REVIEW OF THE PRIVACY POLICY, THEN REMOVE THE DRAFT BANNER.**
- **✅ DONE: 27c pushed and verified. ✅ DONE: `worker-v2.3.js` deployed and verified.**
  **⚠ Cloudflare secrets are WRITE-ONLY — do not ask the owner to "look at" a secret again.**
- **🔴 choose and STORE a new curator word (do not set it yet — see §13.3 sequencing).**
- **🔴 REWORK THE ALMANAC GROUPING** — **whatever it becomes must divide into threes.**
- **🔴 REPLACE THE NINE VOLUME LABELS AND THE VOLNOTE** — Claude's placeholders, labelled as such.
- **🔴 DECIDE THE APP NAME AND THE SELLER LINE (§44.4)** — 10 spare characters, and "Do No Harm Co."
  will appear publicly beneath the brand.
- **Legal entity:** register **Do No Harm Co.** as a GA LLC/corp. Georgia files online through eCorp;
  **$100 base plus a small online service charge, 3–7 business days.** *(Sources vary between $100 and
  $110 depending on filing method — confirm at georgia.gov.)*
  **⚠ THE REGISTERED NAME MUST MATCH THE D-U-N-S RECORD AND THE APPLE FORM EXACTLY** — punctuation,
  "LLC" vs "L.L.C.", the ampersand. **Pick the string once and reuse it verbatim.**
- **Domain:** ✅ **scavengerandhunt.com acquired.** **GoDaddy → GitHub Pages if the app moves:** apex
  **A** records `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`;
  **www CNAME → `gahensley1.github.io`**; then repo **Settings → Pages → Custom domain** +
  **Enforce HTTPS**. **⚠ AVOID GODADDY FORWARDING/MASKING — it breaks HTTPS and the deep link.**
  - **A custom domain moves the site to the domain ROOT**, shortening every invitation link.
    **`joinLink()` derives its origin from `location`, so no code change is needed** — but the
    **absolute `og:image` URLs in `index.html` and `j.html` still point at github.io.**
  - **⚠ NEVER give Claude GoDaddy or Cloudflare account credentials.**
- **D-U-N-S:** request one — free, **5 business days to 2 weeks**, plus up to 2 more for Apple to
  receive it. **Check the lookup tool first; have registration documents ready.**
- **Store enrollment:** Apple Developer ($99/yr) + Google Play ($25, as **Organization**).
  **✅ $1.49 is confirmed available on both — no longer an open question.**
- **Cloudflare:** confirm Worker cron `0 3 * * *` armed.
- **⚠ A LAWYER SHOULD LOOK AT THE CHILDREN'S-PRIVACY POSTURE BEFORE SUBMISSION** (§37.1).
- **Decisions owed:** Play's $0.99 US minimum; Dreams-Doc Q1 (DMO pricing); **the build clue-tip
  duration (§13.19)**; **whether to rewrite git history (§13.20)**; **whether non-builders need a route
  to a volume (§13.13)**; **whether the gold hint toggle and the `BUY VOL n` stamp read well on a real
  phone**; **whether the Roman/Arabic split reads right in his hand (§41.2)**; **the clan-crest
  question (§13.23)**.
- **Hardware testing owed:** the commendation card end-to-end and the invitation message bubble count.
- *Optional/non-blocking:* USPTO trademark (Class 9 + 41) — **file first**, then the visual/literary
  work, then the program.

---

## §32 — EFFICIENCY BOOTSTRAP (run once at session start)
- **`curl` Pages, `sha256sum`, compare to §0**, and **`curl` all eight repo files** for 200 + size +
  **Set a User-Agent on every Worker probe** (bare Python UA → 403, §A). **Check `Hunt-backups` for a
  fresh Monday snapshot** once the owner's §51.3 setup is done. Original continuation:
  **hash**. **Audit the repo file list. `curl` the Worker root (v2.3) and `/list` (403 with no token).**
  **🆕 `curl` scavengerandhunt.com and /privacy.html.**
- **Build the landmark index — `work/marks.py`.** One pass records line number, byte offset and count of
  key functions/IDs into `work/marks.json`. **Regenerate after every ship — offsets move.**
  Landmark list to include, at minimum:
  ```
  toast( toast2( _toastUnder _toastAtAdd _toastAtRow2 _tipClear _tipQueue _huntTour _huntArm
  _movePanTour _movePanArm openClue openLoupe tileEl( renderBuild( renderHunt( openTileEdit
  saveTileEdit openCrop( confirmCrop( joinCase( joinLink( joinGetPack buildShareMsg shareCase(
  saveHunterSub finishBuild genCode caseSeats listSubs chartScalePins chartGo( coldFilter(
  renderColdPins _pinsAt chartTipStack _tipPlace askName( go( stampedCard commendCard commendFacts
  rankFor openCommend shareCommend rankNeeds myRankName myCoins commCount coinBalance spendCoin
  buyCoins openCoinShop renderHintRow toggleTileHint hintSeen( isLocked ownsPack buyPack grantPack
  purchaseLicence purchaseGranted openLicence requirePurchase grantEntitlement purchaseOwned
  buyConfirm buyDecline const VOLUMES volumeById volumeOf volumeShort volumeSaving volumeNo
  volumeRank volumeReady caseTeaser bundleVolume ownsVolume grantVolume buyVolume buyEverything
  renderLicTiers BUNDLE_PRICE renderColdList openColdDetail renderKeepLine raiseComplement
  makeItYours MAP_CHART Store PAW_INK COIN_HERO COIN_PACK HUNTER_CAP SEAT_BLOCK renderCurator
  publishCold curEditCase curGeo curDiff purgeCase deleteCaseAsk archiveCaseAsk subTerrFile
  subAccept refreshHomeBadge id="buildmark" id="s-share" id="s-join" id="s-hunt" id="s-build"
  id="ov-clue" id="ov-tile" id="tile-hint" id="crop-hint" id="tile-hint-toggle"
  id="crop-hint-toggle" id="crop-cluerow" id="clue-hintrow" id="ov-coins" id="ov-buy" id="buy-go"
  id="lic-tiers" id="s-licence" id="s-receipt" id="ov-loupe" id="ov-name" id="ov-commend"
  id="record-ov" id="curator-ov" id="curator-list" id="toast" id="toast2" id="gWater"
  id="home-cred-badge" id="home-rank-stamp" id="cold-sample" _runDeepLink CURATOR_PASS
  shco:hinttip award-card.jpeg og-card.jpeg .volband{ .volband-soon{ .hint-toggle{ .hint-guide{
  .coldrow.teaser{ .coldstamp.locked{ .cd-comp{ .cold-file{ cf-wrap btn-strike stamp-link
  max-height:620px BUILTIN_INDEX=[ cvol- ccat- BUY VOL
  ```
- **Read `BUILTIN_INDEX` by PARSING, never grepping (§0.1):**
  ```python
  i=t.find('BUILTIN_INDEX='); j=t.find('];',i)
  arr=json.loads(t[i+len('BUILTIN_INDEX='):j+1])
  ```
- **RUN THE §41.2 CONSISTENCY PARSE** — for each `VOLUMES` row, compare the Roman numeral in `label`
  against `volumeNo()`'s position-within-shelf. **Nine rows, must all agree.**
- **Write `work/battery.py` once** (Agent B/D + hygiene, PASS/FAIL only). **⚠ AGENT D COMPARES DELTA
  AGAINST THE PREVIOUS BUILD, NOT AN ABSOLUTE BASELINE (§11).**
- **Write `work/probe.mjs` once** — **AUDIT before every capture (§11.R)**, **stubs `Store` (§11b)**,
  drives real functions and asserts on return values, **returns a `precondition:` field**.
- **Write `work/btn.mjs` once — THE MODAL ASSERTION TABLE (§8g.1).** Four viewports × folded/unfolded
  = **16 cells.**
- **Write `work/diff.mjs` once** — the differential render (§11a(e)).
- **🆕 Write `work/ab.mjs` once — THE A/B SERVER MEASUREMENT.** Two ports, previous build on one,
  new build on the other, **print ratios not values.** This is the tool that caught §11a #17.
- **Write `work/samp.mjs` once** — seeds a coin ledger, calls `commendCard()`, writes the returned
  `File` to disk. Copy `award-card.jpeg` and `og-card.jpeg` into the serve directory.
Then, every session: **`grep -c` each literal before editing** (**and `grep -o | wc -l` when the count
matters**); **cap every grep and `sed`**; **`timeout N` every long python heredoc**; **match
verification depth to risk**; **keep ship summaries to ~3 lines + the hash**; **encourage batching**;
**do NOT trim verification or the handoff.**

---

| `index.html` **33o — LIVE, commit `0d077334`, 20:28Z 9 Aug 2026. THE MET BADGE (§95).** | 4,188,696 B | `941d67e93a8faee2721ea8460df6a49ab414a9c0c9c5166cd14799ee269f22f2` | 🔴 **Shipped BEFORE §96 and §97 existed. Chicago and the filter fix are NOT in it.** |

| `index.html` **33p — LIVE, commit `f4ec2d35`, 21:03Z 9 Aug 2026. CHICAGO + THE FILTER FIX (§96, §97).** | 4,163,002 B | `729bffeafc61371e4062e8fae2034001acea9a3847427be14fc26830e3de153f` | 🔴 **Shipped before §98-§100 existed.** |

## 🔴 §101 — THREE BUILDMARKS SPENT MID-FLIGHT IN ONE SESSION. `33n`, `33o`, `33p`.

**Every one shipped a build that was already several revisions behind, and the mechanism was
identical each time: Claude wrote a `ship` line, work continued, and the owner ran the line in front
of him. That is correct of him and wrong of Claude.** §1y already said the ship line dies when the
build moves and that Claude must say so **in the same reply as the next edit**. Claude did not do it
once in three attempts.

| mark | commit | carried | what it missed |
|---|---|---|---|
| `33n` | `165b7400` 16:03Z | `1ac7f99e` | 8 later revisions of the stamp |
| `33o` | `0d077334` 20:28Z | `941d67e9` | Chicago, the filter fix |
| `33p` | `f4ec2d35` 21:03Z | `729bffea` | §98-§100, both stamps, the anchor fix |

**THE RULE IS NOW MECHANICAL, NOT A MATTER OF MEMORY: the moment `index.html` changes after a ship
line has been written, the next reply opens by declaring that command dead and quoting the new hash.
No exceptions, no matter how small the edit.**

## 🔴 §97 — THE COLD-CASE FILTER WAS DROPPED ON THE WAY BACK. FIXED `33p`, s58.

**Owner report: filter the archive to `chicago`, open a case, come back — the list is Savannah
again, while the search box still reads "chicago" and the chart still shows Chicago pins.**

`openColdCases()` opened with `State.coldQ=null;` unconditionally, and `coldBack()` reaches it via
`coldCatBack()`. **It clears the filter but NOT the input and NOT the pins**, so the screen showed
three views of one piece of state and only one of them had been reset. The screen looked filtered.
It was not. A player would conclude the Chicago cases had vanished, not that the filter had dropped.

**🔴 TWO BUILDMARKS WERE SPENT EARLY IN ONE SESSION — `33n` AND `33o` — BOTH BECAUSE A SHIP LINE
OUTLIVED THE BUILD IT NAMED (§1y).** `33o` shipped at 20:28Z carrying `941d67e9…`; work continued
afterwards and became `33p`. **The rule is not "one ship line at a time" but "the ship line dies the
moment the build moves" - say so out loud in the same reply as the next edit.**

**The fix keeps `State.coldQ` for as long as the query that made it is still in the box; an empty box
still clears.** Proven on the reported path: `chicago` gives 5 rows, open `606001`, `coldBack()` —
still 5 rows, same filter object, input intact. Before the patch it returned 40.

**🔴 THE LESSON: WHEN ONE PIECE OF STATE HAS THREE VIEWS, RESET ALL THREE OR NONE.** A partial reset
does not look like a bug, which is why this survived.

---

| `index.html` **34a — LIVE, commit `f6b9eed4`, 22:12Z 9 Aug 2026 (§98-§100).** | 4,172,954 B | `c6ac5c528f809095fd3f41662d52dfb1e95bd7ce6cd8c8a51bf67673240dd0a2` | **The first build of s58 that shipped as the build it named.** |

| `index.html` **34b — LIVE, commit `192e9733`, 22:23Z 9 Aug 2026. The plate 25% down, up 30px.** | 4,172,960 B | `fb6420036e1687dbbe231d0cb364991ab5cb0adaf10af6626b34bc92d4e8d844` | — |

| `index.html` **34c — LIVE, commit `4138f6e4`, 22:53Z 9 Aug 2026. The three compositing fixes (§102).** | 4,300,501 B | `6fd797e02640323b028e0ce3535b35ec6887c382b620a666681797f4f5021bb3` | 🔴 **Shipped before the wipe crop, the ordinal and the badge press. FOURTH mark spent mid-flight this session — see §101.** |

## 🔴 §102 — FOUR LAYER-FORMING PROPERTIES, INVISIBLE ON DESKTOP, WRONG ON iOS. `34c`, s58.

**Everything in this section was added by Claude for polish, looked correct in desktop Chrome, and
was WRONG on the owner's iPhone. He photographed each one; Claude could not see any of them.**

**iOS Safari rasterises layer-forming properties into their own compositing layer and backs that
layer OPAQUE.** The result is a pale rectangle where a transparent ground was intended, and a
straight-edged cut where the layer meets a clip.

| property | on | symptom |
|---|---|---|
| `mix-blend-mode:multiply` + `filter:drop-shadow` | the plate | pale box behind the stamp, straight cut |
| `text-shadow` parchment glow | the handwriting | pale patch behind the script |
| `isolation:isolate` | the fill wrapper | pale box behind the script |
| `clip-path` (the ink wipe) | the handwriting | **suspected, not yet ruled out** |

**🔴 ON THIS CARD, A LAYER-FORMING PROPERTY IS A LAST RESORT, NOT A PRECAUTION.** The blend bought
almost nothing at 93% ink; the glow and the isolation were belt-and-braces that were not needed —
`z-index:6` over the plate's `2` already settles the order.

### §103 — THE 30 DEGREES IS BAKED INTO THE ART

A rotated **square** always overhangs its bounding box — 32px at this size — and iOS clips that
rectangle. **A CIRCLE's bounding box is identical rotated or not**, so the angle was baked into the
asset and `transform` set to `none` (with `stampFlat`, a scale-only keyframe). The element's box is
now tight to the ink: 176x176, nothing to clip, and the 15px gap holds with 27px of clearance.
**The fill keeps its CSS rotation and still aligns**, because the art was square with the circle
inscribed — the tight box of the rotated circle is the same box on the same centre.

### 🔴 §104 — CLAUDE CANNOT SEE THIS CLASS OF BUG

**Every desktop measurement said the card was correct while the phone showed it broken.** Computed
styles, rects and pixel probes all agreed with Claude and all missed it. **When the owner reports a
visual fault he can see and the measurements say fine, THE MEASUREMENTS ARE ANSWERING A DIFFERENT
QUESTION — look for a compositing difference, not an arithmetic one.**

## 🟡 §108 — THE JOIN LAG. PART FIXED, THE REST MEASURED. `34d`, s58.

**Fixed:** `getMyName()` was a serial round trip waiting on the case record it does not depend on -
it now fires with the three opening reads. The local `sub:` key was **read twice** on a cold case,
and the shared `sub:` read and `checkMyReturn()` ran one after the other though both are independent
once `hid` is known - all three now go together.

**Also fixed:** `saveHunterSub()` wrote the record twice, local then shared, **one after the other** -
two round trips at the end of every join AND every find. Fired together; `durable` still reports the
LOCAL write, which is what the resume path depends on, and the cold branch awaits its local write
before returning so a reload cannot race it. Measured: 7529ms -> 6433ms synthetic, depth 7 -> 6.

**🔴 STILL OPEN.** Instrumented with a 120ms stand-in for phone latency,
one join makes **12 Store calls, 7 round trips deep**, and reads the SAME key four times and writes
it twice:

```
1109ms get sub:CODE:HID      2994ms get sub:CODE:HID (x2)
4102ms get sub:CODE:HID      5108ms set sub:CODE:HID      5990ms set sub:CODE:HID
```

The reads at 1109 and 4102 and the duplicate write come from the **resume and board-render path,
not `joinCase`** - trace `saveHunterSub()` and the board render before touching anything. **The
7.5s figure is synthetic: the shape is real, the number is not.**

---

## ✅ §100 — THE STAMP IS ANCHORED TO THE CARD. `34a`, s58.

**The plate hung off `.done-photowrap`, which is `width:208px` AND FIXED, while the thing that clips
is the card, whose width varies by device.** One offset therefore meant a different thing on every
screen: it cleared on a wide card and **sliced the stamp on a narrow one** - the owner saw it cut,
Claude measured 15px of clearance and saw nothing wrong.

`.done-photowrap` is now `position:static`, handing the containing block up to `.stamp-done`, which
IS the card. **Verified at five card widths - 307, 337, 367, 397, 457 - ink gap 15px at every one,
plate and hand aligned at every one.** Before the fix that number moved with the screen.

**`34b`: the plate went to 176px (-25%) and up 30px, and `right` WAS NOT TOUCHED - the ink edge held
at 15px on its own. THE INSCRIBED CIRCLE'S RIGHT EDGE IS THE UNROTATED BOX'S RIGHT EDGE whatever the
rotation, because a circle is invariant about its own centre.** Resize from the anchored side and the
gap keeps itself; only the rotated bounding box changes, and that corner is empty.

**🔴 A FAILED FIRST ATTEMPT IS WORTH RECORDING: Claude moved the MARKUP out of the wrapper instead.
The positioning rule is `.done-photowrap .stamp-img.done-stamp` - SCOPED TO THE WRAPPER - so the
plate lost `position:absolute`, fell into the flow as a centred image, and the handwriting stayed
behind. READ THE SELECTOR BEFORE MOVING THE ELEMENT IT MATCHES.**

**The hand is never degraded with the plate.** It is live text at `z-index:6` with
`isolation:isolate` over the stamp's `2`, so the ink lift cannot touch it. "Bolder" is an
0.8px `-webkit-text-stroke` - Delafield ships one weight. **The date is MONTH/DAY**: it read `9/8`
for 9 August, which is September the 8th to an American eye.

**⚠ `elementsFromPoint` REPORTS HIT ORDER, NOT PAINT ORDER.** The hand has `pointer-events:none`, so
it is invisible to hit testing while drawn on top. Claude quoted it as proof and was wrong.

---

## ✅ §99 — PINCH THE CHART. `34a`, s58.

**`_ptrs = new Map()` was declared in the cold-case block and never referenced anywhere.** The hook
was left and the gesture never written, so the chart only ever panned with one finger and zoomed by
the +/- buttons. **It was not lost; it never existed** - the pinch the owner remembered is the
loupe's, which has its own pointer map.

Two-pointer tracking now drives `_vb`, anchored on the midpoint. `chartApply()` already clamps width
to 0.5-1000, so pinch only sets width and origin. **`_lockScroll` is held while two fingers are down
and released when the second lifts** - without it two fingers drag the page behind the map on iOS.
Proven with synthetic PointerEvents: spread 1000 -> 333, pinch back to 1000.
**✅ CONFIRMED WITH REAL FINGERS BY THE OWNER, s58.**

---

## ✅ §98 — THE ARCHIVE OPENS ON YOUR OWN PRECINCT. `34a`, s58.

**`precinctApply()` only ever drew the banner and the map marker.** It computed the count for
"PRECINCT 60602 — 5 COLD CASES OPEN" and then rendered **the full national list underneath it** -
the bar said one thing and the list did another, the same class of fault as §97.

Opening the archive now defaults `State.coldQ` to a `near` filter on the registered zip.
**THREE GUARDS:** never override a filter the hunter set, never when a category is open, and
**never when the precinct has nothing in range** - Anchorage falls back to the full list rather than
showing an empty archive. Tested: no precinct 10 rows, `60602` 5 rows, `99501` 10 rows.

---

## ✅ §96 — FIVE CHICAGO TERRITORIES. `33p`, s58.

Built for the owner's travel week. **Codes `606001`-`606005`, all free — territories always are.
Twelve tiles each, sixty in all, and SIXTY REAL HINTS: not one placeholder.**

| code | case | territory | zip | diff |
|---|---|---|---|---|
| 606001 | The Millennium Park Enquiry | Millennium Park | 60602 | 2 |
| 606002 | The Buckingham Waterworks | Buckingham Fountain & Grant Park | 60605 | 2 |
| 606003 | The Cultural Hall Investigation | Chicago Cultural Center | 60602 | 1 |
| 606004 | The Wooded Island Affair | Wooded Island & Osaka Garden | 60637 | 2 |
| 606005 | The Pullman Enquiry | Pullman National Historical Park | 60628 | 2 |

**Owner rule: every case must sit inside a 0.25-1 mile radius, no more.** Jackson Park as a whole was
cut for this - Statue of the Republic to the Osaka Garden is 1.4 miles - and narrowed to the Wooded
Island loop, which keeps the 1893 thread since the island IS fairground.

**HOW THESE ARE BUILT, AND WHY NO WORKER ACCESS WAS NEEDED:** `BUILTIN_INDEX` entries accept
`lat/lon/city/place/zip`, and `coldIndex()` merges the built-ins into the same list the map pins draw
from — **so a baked-in case appears as a territory pin exactly like a curated Cold Case.** Modelled
on the five Savannah entries (`3104xx`). Pattern: index entry + `BUILTIN_HUNTS[code]` with
`cold:true, parAuto:true`, 12 tiles of `{id,type,emoji,clue,hint}`.

**COPY RULES USED:** no proper nouns in the clues — a detective is told what to look for, not what it
is called, which also means the clue survives a sponsor's name changing. **Hints may name streets;
that is their job.** Nothing that moves: no food carts, no rotating gallery pieces, no ice rink that
is a café in August. Pullman's Arcade Building is deliberately absent — demolished 1926, and no
detective should be sent to photograph a gap.

**🔴 UNWALKED. Sixty clues written about places Claude has only read about.** Walk one before trusting
the set.

---

## ✅ §95 — THE BADGE WEARS THE RANK. `33o`, s58.

**Owner-supplied art:** a Metropolitan Police helmet plate (VR cypher, king's crown) replaces the
clan crest at `BADGE_MAC`. Source, full-res alpha cut and the 300x420 WebP (32,828 B) are all in
`Documents\Hunt\art\`. **The white ground was cut by labelling near-white regions and keeping only
those that touch the border, plus large ones in the top 27% — the crown's arch gaps.** A plain
luminance threshold punched a hole in the medallion's specular highlight; `binary_fill_holes` filled
the crown gaps solid white. Neither is right on its own.

**The arcs now read `RETRIEVE CREDENTIALS` above and THE HUNTER'S RANK below** — so the medal is
theirs, and it re-letters itself on promotion. `credBadgeSVG(rank)` takes the rank, upper-cases it and
calls `_arcSize()` to fit the lower arc: **`ASSISTANT COMMISSIONER` is 22 characters against ~286
units and drops to 18.6px; `DETECTIVE CONSTABLE` stays at the full 19.4px.** Measured, not assumed.

**🔴 `refreshHomeBadge()` USED TO SKIP WHEN `innerHTML` WAS ALREADY SET.** That was harmless when the
badge was static; with the rank on it, **a promotion would never have reached the medal.** It now
redraws whenever `dataset.rank` differs.

**The separate `RANK` stamp under the badge is gone** — `#home-rank-stamp`, its `::before` eyebrow and
its length-based font sizing. The badge says it. **`#cred-rank` on the Credentials screen is a
different element and was left alone.**

**THE CHARTER'S CLOSE IS NOW A CIRCLE STRADDLING THE DOUBLE FRAME**, the commendation-card idiom
(`.tg-x` on `#pr-card`). `.lic-cert` already carried a double frame — 2px brass border plus a 1px
outline at 4px offset. The button moved INSIDE `.lic-cert` (which gains `position:relative`) at
`left:10px top:-17px`. **`.lic-modal` has `overflow-y:auto`, which would have clipped the overhang,
so it gains `padding-top:20px` — overflow clips at the padding box, so the circle sits in that
space.** Measured live: centre within 2px of the border, not clipped.

**Weight: +25,430 B.** The new plate is heavier than the crest it replaced.

---

## ✅ §94 — THE CASE CLOSED STAMP IS STRUCK AND SIGNED. `33n`, s58.

**Owner-supplied artwork** replaces the old CASE CLOSED wordmark on the Case Solved card: a full
round Scotland Yard / Victoria Embankment stamp with printed `DATE` and `INITIALS` rules. Source and
the alpha cut are both in `Documents\Hunt\art\` (§1v). The homepage postmark was recoloured to
match. **Two other stamped items were deliberately left alone** — `stamp-link` (CASE FILE RECORD)
and `seal-replystamp` (REPLY WAITING). The reply stamp stays slate blue **because the blue is what
distinguishes it from the postmark at a glance**; making both red would collapse two states into one.

### 🔴 94.1 THE OLD MARK WAS WIDE; THE NEW ONE IS ROUND. THE POSITION DID NOT SURVIVE THE SWAP.

The old asset was **340×235** — a wordmark. The new one is **721×720** — a circle. Dropped in at the
inherited `width:319px` the stamp grew half again as tall, **covered "Nicely done, detective." and
filled the whole card.** Caught in Chrome before shipping, not by arithmetic. **A same-scale swap is
only same-scale when the aspect ratio matches.** Final numbers, set from the owner's own mark-up on a screenshot and then trimmed 15% TWICE:
**`180px`** (`150px` under 349px), `top:-58px` `right:-187px`, `opacity:.72` — it lands across the top-right corner of the record
photo and hangs off the card edge, clear of the heading. **An intermediate 196px pass was rejected
as too small and too far left; he drew the target in yellow and that is what shipped.**

### 94.2 THE DATE AND THE INITIALS ARE WRITTEN ON, NOT BAKED IN

The date is per-case, so it cannot live in the PNG. `.done-stampfill` is a second absolutely
positioned box sharing the image's geometry and its `rotate(30deg)`, holding two spans placed on the
printed rules by percentage. `stampTheDate(code)` reads **the coin ledger entry for that case** —
the real moment it closed — and only falls back to the clock when no entry exists. Day/month, no
year, no leading zeros. Initials are `B.B.`, Bonnie's, fixed. Both are revealed left-to-right by
`inkWrite` (1.2s) after the stamp lands (`stampDown` 0.68s): date at `1.45s`, initials at `2.85s`.
**Slowed twice on owner instruction** — the first pass read as a flicker, and the writing then
started too soon after the impression. **The pause between the stamp landing and the pen starting is
the point**; it is what makes it read as a clerk signing rather than a graphic appearing.

### 🔴 94.3 A THIRD TYPEFACE — A DELIBERATE OVERRIDE OF `Branding-Guidelines.md`

`docs/Branding-Guidelines.md` said **"Never a third face."** The written marks need a hand, so
**Mrs Saint Delafield** (OFL) is embedded as `'Delafield'`, **subset to `0-9 / B .` — 2,220 B**.
**THE OWNER WAS TOLD THE RULE WAS BEING BROKEN AND APPROVED IT EXPLICITLY.** The guidelines have been
amended in the same session so a later reader does not "fix" this back. **It is a stamp-fill face
only — it must not spread to UI copy.** Claude flagged the hairline risk at small sizes; the owner
took it.

### 94.4 THE RED

Chosen from four darker candidates over FOUR passes: `#ED2939` (Imperial Red), `#B92230`
(post-office red), `#9E1B27` (carmine), and finally **`#82151F`, deep crimson — the one that
shipped.** 🔴 **THE OWNER JUDGED EVERY ONE OF THEM ON A MONITOR HE SAYS IS HARD TO READ COLOUR ON,
and his device of record is an iPHONE 15.** His words: *"my computer is a hard to read the colors so
my mistake. on the phone it is different."* **Offer the darker end of any colour range first, and
say out loud that a desktop screenshot is not the device that matters.** The local server cannot be
reached from his phone, so a colour cannot be checked there until it is live — expect colour to be
revisited AFTER a ship, and do not treat a desktop approval as final. **This is a second red in a palette whose only red was oxblood
`#8A3324`** — recorded in the guidelines. Both stamp assets carry it. Recolouring works by rebuilding
the ink as **flat colour with the grain carried in the alpha channel**; the first attempt mapped
luminance into the hue instead and the grain glowed — do not do that again.

### 🔴 94.6 THE SHIP COMMAND WENT OUT BEFORE THE LOOK WAS APPROVED — SEE §1x

The stamp moved three times: 319px inherited (covered the card), 196px (too small, too far left),
then 250px at `right:-186px` from the owner's own yellow mark-up, then ten pixels further right.
**Claude handed over `battery` and `ship` after the second of those**, on the strength of a green
STATIC and a matching hash. **The owner stopped it.** The rule that came out of it is §1x: tests are
not consent, and the `ship` line is not written until he has said yes to the appearance.

### 94.7 `+tap here to add hidden hint` GOES OXBLOOD

`.hint-toggle` was `var(--brass)` and is now `var(--oxblood)`. **One rule, both instances** —
`#crop-hint-toggle` and `#tile-hint-toggle` share it, so the Builder's crop step and the tile editor
change together. Brass is the accent/border colour; this control is a call to action on parchment
and was reading as chrome.

### 🔴 94.9 ONE RED. `--oxblood` IS NOW `#8B0000` AND THE STAMPS MATCH IT.

**Owner: "can we make the ox blood and stamp colors match and start with adobe dark red #8b0000."**
The house red was `#8A3324` and the stamps had been given their own — two reds a shade apart, which
is worse than two reds that differ on purpose. **`--oxblood` is now `#8B0000` and both stamp assets
are re-inked to the same value.** **THE SWEEP MATTERED (§1w): `#8A3324` was hard-coded in TEN places
besides the variable** — the map pin, the crosshair and its three strokes, the loupe reticle,
`.heretxt`, and twice in the commendation-card canvas. All eleven now read `#8B0000`. **Grep before
declaring a colour change done; a CSS variable is not the whole story in this file.**
**"Start with" is the owner's own word — expect this to move again, and it cannot be judged on a
desktop (§94.4).**

### 94.8 THE ORDINAL ON THE CASE SOLVED CARD

`You finished 3rd!` — the **numeral** is `1.5em`, the suffix stays `1em`. `ordinalHTML(n)` wraps
`ordinal(n)`'s own output rather than rebuilding the string, so the two can never drift; `rankEl`
moved from `textContent` to `innerHTML` for the two lines that carry it. Measured: 31.5px against
21px. **Both branches changed** — the finished line and the `Entry locked … currently Nth` line.

## 🔴 §94.10 — `33n` SHIPPED EIGHT REVISIONS EARLY, AND THE SAME BUILDMARK NAMED TWO FILES

**Found by re-hashing the live surfaces from the shell, not by being told.** Two Pages fetches
minutes apart returned different builds (`33n` on one edge, `33l` on another — a deploy in flight),
which is what prompted the check.

**The sequence:**
- **12:03 EDT** — `ship` ran. Disk held `1ac7f99e` (stamp 250px, red `#B92230`). Commit `165b7400`.
- **12:51 EDT** — `battery` ran, and recorded `4d51d5a3`. **Forty-eight minutes AFTER the ship.**
- Work continued past both. Disk reached `f5117c50`, still carrying the buildmark `33n`.

**So `33n` named two different files: the one in the repo and the one on disk.** §8i exists to stop
exactly that. The disk build was rebranded **`33o` / Lime `#7FA33C`**.

**WHAT SHIPPED IN `33n` AND WHAT DID NOT.** Live: the round stamp at 250px in `#B92230`, the written
date and initials, the recoloured postmark. **NOT live, all built after the commit:** `#82151F` then
the one-red `#8B0000` sweep, the oxblood hint toggle, `HINT_CONFIRM_MS` 6s, the stamp 15% smaller and
9px left, the beat before the handwriting, the 1.5x ordinal.

**🔴 THE CAUSE WAS CLAUDE'S, AND IT IS THE FAILURE §1x WAS WRITTEN TO PREVENT — COMMITTED AFTER
WRITING §1x.** A `ship` line was handed over three separate times while the build kept moving. **An
old `ship` command does not expire; the owner will run the one in front of him.** See §1y.

### ✅ §95.5 — THE BADGE FOLLOWS THE PLATE, NOT A CIRCLE. APPROVED s58.

**The helmet plate is photographed foreshortened.** No circle can sit parallel to it, and every
circular attempt drifted — the owner caught each one from a screenshot. **Measured from the artwork,
one ray per degree, robust Fourier fit (k<=3) with outlier rejection:**

| edge | kept | radius (units) |
|---|---|---|
| inner rim | 293/360 | **63.4 – 65.6** |
| outer / shadow edge | 270/360 | **90.4 – 95.9** |

**The band itself breathes, 27.0 to 31.8 units.** That is why the two legends reference DIFFERENT
edges — tying both to one edge is exactly what produced the drift:

- **Upper legend `RETRIEVE CREDENTIALS` = inner rim + 9.3**, constant. Sits ON its path.
- **The RANK = outer/shadow edge − 8.2**, constant. HANGS from its path — cap-tops on the line.

Against the inner rim the rank's gap to the shadow edge ran **6.3 to 11.2 units**, nearly double at
one point versus another. The owner spotted it by eye before it was measured.

`CB_RIM[]` and `CB_OUT[]` hold both curves at 3-degree steps; `_ringPath()` walks them. **A single
circle is not good enough for this plate and must not be reinstated.** Type is Playfair 800 with a
highlight layer offset 0.9 units beneath, so the letters read as struck.

### ✅ §95.7 — THE REST OF THE HOME SCREEN, s58

- **Postmark 1.2x** — `.seal-disc` 230px → 276px.
- **`send the agency a message` 1.31x** — 10px → 13.1px, letter-spacing 1.6 → 2.1 so it does not
  tighten as it grows. (Tried at 1.75x/17.5px and cut back 25% on the owner's call.)
- **The gaps above and below the badge were halved and equalised to 16px each**, from 35 above and
  29 below. Measured, not eyeballed. **🔴 `.seal-btn` carried a `margin-top` FOLLOWED BY a `margin`
  shorthand in the same rule — the shorthand silently won**, so the first attempt moved the badge and
  not the postmark. Both gaps must be measured; a screenshot would not have caught it.
- **The CASE CLOSED stamp's ink was cut to 55% coverage** — multi-scale blotch noise so it drops out
  in patches like a pad running dry, with thin ink lifting off entirely below a threshold. **The
  threshold is solved for by bisection against a target, not guessed.**
- **A `CASE FILES` brass plaque was built to replace the `CASE FILE RECORD` text image, then UNDONE
  on the owner's call.** The revert was byte-exact — the original image had been extracted to the
  scratch directory during the s58 stamps audit, so it was restored rather than rebuilt, and the hash
  returned to its previous value exactly. **Extract before you overwrite a base64 asset.**

### 🔴 §95.8 — `art/` WAS NEVER GITIGNORED, AND `ship` RUNS `git add -A`

`art/` left the tree at s56 (§88) but **was never added to `.gitignore`**, so recreating it this
session would have pushed **17 MB of source PNGs into the PUBLIC repo** — owner photographs, every
scratch preview, the diagnostic diagrams. Now ignored, with `_preview-*.html` and `_diagram-*.png`.
**The delivered artwork travels base64 inside `index.html`; `art/` is working source and belongs on
disk and in Hunt-backups only.**

### 94.5 WEIGHT

Stamp **78,036 B** WebP with alpha (the old PNG was ~24 KB), postmark **31,894 B** down from
**64,898 B**, font **2,220 B**. Net **+43,515 B** on a 4 MB file.

---

## ✅ §93 — THE HINT COIN IS EARNED, NEVER SOLD. OWNER DECISION, s57.

**Owner, verbatim: "lets jsut remove montezation of the coins,,, i would rather them buy into the
play."** And, earlier: **"i just dont want parent ire if a kid gives up and buys."**

**DECISION: coins are earned only — one per case closed. The coin shop and any purchase path come
out.** This is a monetisation decision and the full reasoning belongs in `Monetization-Brief.md`
under *Rejected, and why — do not reopen*. ⚠ **THAT FILE COULD NOT BE WRITTEN AT s57 — the bridge
returned permission denied on `docs-private\` (OneDrive lock or read-only). The paste-ready insert
is at `claude\BRIEF-INSERT-coins-s57.md` and MUST be applied**, or this decision lives only in the
public handoff and the brief still implies coins are sold.

### 🔴 93.1 THE LINE THAT MADE IT URGENT

```js
if(coinBalance()<1){ openCoinShop(); return; }
```

**The shop opened automatically when a stuck player tapped for a hint with an empty purse** —
frustration straight to a till with no step between. That is the pattern behind the kid-spending
headlines and the FTC settlements with Apple and Google. **The owner identified the risk himself,
unprompted, before any code was written.**

### 🔴 93.2 RANK WAS NEVER AT RISK — DO NOT WRITE COPY SAYING OTHERWISE

`myCoins()` is a **ledger, not a balance**: one entry per case closed, and it only grows. Rank reads
its **length**, so a spend can never demote a detective — the high-water mark is a property of the
shape, not a rule bolted on. **A draft confirmation was going to warn that spending "takes away from
your next promotion". THAT WOULD HAVE BEEN FALSE.** The true line is the reassurance the app already
shows *after* the spend — move it *before*: **"Your rank stands regardless."**

### ✅ 93.4 BUILT IN `33m`. s58.

**Owner amendment: "all the coin routes stay with the note but no buying for .99."** So the route is
**retired, not removed** — `buyCoins()`, `requirePurchase("coins", …)`, `shco:bought`,
`coinBalance()`'s arithmetic and the Worker's side all remain intact and reversible. **Nothing calls
`buyCoins()`**; the *"Five coins · $0.99"* button is out of `#ov-coins`. A long comment above the
function records why and what must never be done if it is ever wired back.

**What changed in the client:**

1. **🔴 NO TILL AT A FAILURE STATE.** `if(coinBalance()<1){ openCoinShop(); return; }` is gone. An
   empty purse now says *"Your purse is empty — a coin for every case you close."* **Verified: the
   only live `openCoinShop()` in the file is its own definition; the other two hits are the warning
   comments.**
2. **The spend is confirmed.** Two-state button in place — first tap arms it and relabels to *"Tap
   again to spend 1 coin · you hold N · your rank stands regardless"*, disarming itself after
   `HINT_CONFIRM_MS` — **raised to 6s in `33n`; 4s was too quick to read (owner, s58).** **NOT a double-tap gesture: the loupe already owns double-tap for zoom
   (§90.8), and two meanings for one gesture is a collision.**
3. **The balance and the reassurance are shown BEFORE the spend**, not after. The old toast said the
   right thing at the wrong moment.
4. **A free hint now says so** — *"Consult the hint — on the house."* Previously a free hint and a
   paid one wore identical button text, so a player could not tell whether they were spending.
5. **The purse copy** no longer offers a sale.

**STATIC clean; inline handlers 113 → 112, the one removed being the sale button.**

### 93.3 THE BUILD — done in `33m`, kept for the record

1. **Hint path:** replace the `openCoinShop()` call with *"Your purse is empty — a coin for every
   case closed."* No till at the moment of failure, ever.
2. **`coinBalance()`** becomes earned − spent. **Keep READING `shco:bought`** so any existing value
   still counts — the code comment says purchases were preview-only, so no real money is involved,
   but do not strand a balance.
3. **`#ov-coins`** keeps the purse display, loses the purchase controls.
4. **The confirmation (§93.2 wording), and free hints labelled as free** — currently a free hint and
   a paid one wear the same button text, so a player cannot tell whether they are spending.
5. **Removes a consumable IAP from the store track entirely** — the heaviest compliance category
   there is, gone for nothing lost.

---

## ✅ §92 — `ship` NOW REFUSES THINGS. THREE GATES, TWO PROVEN TO BITE. s57.

**The finding this rests on: every rule enforced by code held today; every rule that was only prose
was broken at least once.** Agent D stopped Claude twice and would not be talked round. `battery`
never lied. Meanwhile a log was read from the wrong end, the wrong build was shipped, and §0 was
left stale twice — all covered by written rules that had been read that morning. **So the rules that
matter were moved into the script.**

| gate | refuses when | the s57 failure it answers |
|---|---|---|
| **1** | `index.html`'s hash is absent from `HANDOFF.md` | the wrong build shipped **and** §0 left stale — one check, both faults |
| **2** | `index.html` changed but the buildmark did not | §8i, enforced instead of remembered |
| **3** | the battery last passed on a **different** build | 33e, 33f and 33g all shipped untested |

`ship /force "..."` overrides all three; **the message must say why.**

**GATE 3 NEEDS A STAMP.** `battery.cmd` now writes `test\.last-battery` containing the hash of the
`index.html` it passed on — **only on a full pass with no argument**, since `battery some.html`
skips SESSION and must not leave a stamp claiming the shelf build was tested. The stamp is
**gitignored**: machine-local evidence, not a source of record, and it must not travel between
clones.

### 92.1 THEY WERE TESTED, NOT ASSUMED (§11d: prove it has teeth)

- **GATE 1 — PROVEN.** A comment was appended to `index.html` so its hash (`152b16c8…`) appeared
  nowhere in `HANDOFF.md`. `ship` refused, named the reason, and **never reached the Y/N prompt**.
  The file was restored to the shipped bytes immediately after and re-hashed to confirm.
- **GATE 3 — PROVEN.** The stamp was doctored to all zeros while `index.html` stood at
  `2f9cd80f…`. `ship` refused, printed **both** hashes side by side, and named the three builds the
  gate exists to prevent. Stamp restored and re-verified.
- **GATE 2 — PROVEN, AND ISOLATED.** A comment was added to `index.html`, **its new hash was written
  into `HANDOFF.md` and into the battery stamp on purpose**, so gates 1 and 3 both passed and gate 2
  was the only thing that could refuse. It did, on an unbumped `33l`. All three files were reverted
  and re-hashed afterwards.

**ALL THREE GATES HAVE NOW BEEN SEEN TO REFUSE, each isolated so that only the gate under test could
fire.** That is the §11d standard — a check that has only ever returned "clean" is not a check — and
it is the first time in this project that the *refusal* path of anything has been exercised
deliberately rather than discovered by accident.

**⚠ WHEN TESTING, DO NOT PASTE THE REFUSAL TEXT BACK INTO `cmd`.** It tries to run each line as a
command and sprays "is not recognized as an internal or external command". Harmless, but it reads
like a second failure and is not one.

### ⚠ 92.2 THE SCRIPT WAS WRITTEN BLIND

**Claude cannot execute `cmd.exe`.** Every line of `ship.cmd`'s gate logic was written without being
run once. **The pre-s57 script is kept at `claude\ship-s55-backup.cmd`** — if `ship` misbehaves,
copy it back over `ship.cmd` and carry on. A script that refuses wrongly is worse than one that
never refuses.

**⚠ AND A FIRST-RUN CONFUSION, RECORDED:** the first test expected a gate-3 refusal and got a clean
ship. **The gate was right and the expectation was stale** — the owner had run `battery` in between,
so the stamp legitimately matched. `33l` went live under the commit message "gate test", which is a
poor record; §0 and §91 carry the real one.

---

## ✅ §91 — A ZIP IS A MAIL ROUTE, NOT A NEIGHBOURHOOD. THE ZIP BAND. `33l`, s57.

**Owner, s57: "when i type in the zip 31405 it says showing one and there are several pins on the
screen … technically yes one in this zip but the zip code areas are small."**

**THE DEFECT WAS TWO VIEWS OF ONE QUERY DISAGREEING.** `chartGoZip` frames the chart at a viewBox
width of `1.5`, which covers far more ground than a ZIP polygon, while `coldFilter`'s `zip5` arm
string-matched `e.zip`. Both were correct; they answered different questions. The map showed five
pins and the list said one.

### 91.1 WHY NO METRO TABLE — THE REASONING, SO IT IS NOT RE-OPENED

A CBSA crosswalk is the "correct" answer and was rejected deliberately: **~100 KB on an already
4 MB file, definitions that move every few years, and nothing at all to say about the many ZIPs
inside no CBSA.** ZIP3 was rejected too — it is a mail-sorting hierarchy, not a geography (Atlanta
spans 300, 301, 302, 303, 305, 306, 311; one rural prefix bundles unrelated towns).

**AN EXPAND-UNTIL-YOU-FIND-ENOUGH RADIUS *IS* THE METRO AWARENESS.** ZIP area is inversely
proportional to density, so a ladder that stops when it has enough self-tunes: sub-mile in
Manhattan, single digits in Savannah, tens of miles in thin country. **No data shipped, no
definitions to maintain, no coverage gaps.**

### 91.2 WHAT WAS ALREADY THERE

Nothing new had to be invented, which is why this was cheap:
- **`GAZ5` is the full US gazetteer** — 33,791 ZIPs at 0.01° (±~0.8 km), so any typed ZIP resolves.
- **`coldNear(e,q)`** already did radius filtering with the cos-latitude correction.
- **A `near` mode** already existed in `coldFilter`. `zip5` simply never used any of it.

### 91.3 THE BAND

`ZIP_LADDER = [3,6,12,25,50]`, `ZIP_TARGET = 8`. New `zipnear` mode matches **exact ZIP OR within
the band**. `zipBand()` mirrors `coldFilter`'s category step (`!e.cat`) **so the chip's figures and
the list can never disagree** — the fault this section exists to fix.

**THE EXACT COUNT IS THE HEADLINE AND IS NEVER LOST** (owner's choice): `SHOWING 3 IN ZIP 31401 ·
2 MORE WITHIN 8 MILES`. A merged list would discard the one figure a player can walk to. When the
band is empty the nearest is named anyway — `NEXT NEAREST 716 MILES` — so a thin region is never a
dead end. Inside a band the list sorts exact-ZIP first, then strictly by distance.

### 🔴 91.4 THE NOTE REPORTED THE RUNG, NOT THE DISTANCE — CAUGHT BY COMPUTING IT

First cut announced **"5 MORE WITHIN 50 MILES"** for five cases all inside six. **With 35 cases on
the shelf the ladder rarely reaches `ZIP_TARGET`, so it lands on the last rung and reported the
radius SEARCHED rather than the radius that CONTAINS them.** True, and useless. `say` is now the
farthest case actually in the band, rounded up. Verified against the real `BUILTIN_INDEX`:

```
SHOWING 3 IN ZIP 31401 · 2 MORE WITHIN 8 MILES
SHOWING 0 IN ZIP 31405 · 5 MORE WITHIN 9 MILES
SHOWING 0 IN ZIP 10001 · NEXT NEAREST 716 MILES
```

**This was found by running the ladder over the real data in the sandbox, not in a browser** — the
cheapest verification available and it caught a copy defect no screenshot would have.

### 🔴 91.5 AGENT D DRIFT: `ZIP_LADDER` — AND THE RIGHT WAY TO CLEAR IT

`agents.py` Agent D balances **TAGS**, and a `<` immediately followed by an identifier reads to it
as an opening tag. `for(var i=0;i<ZIP_LADDER.length;i++)` scored as drift. **`baseline.json` is a
list of exactly these false hits and it was NOT grown** — the battery's own banner forbids it. The
loop became `.some()` instead.

**⚠ IT FAILED A SECOND TIME BECAUSE THE FIX'S COMMENT SPELLED THE PATTERN OUT IN PROSE.** Agent D
reads the file, not the syntax tree. **Do not write the offending form into a comment either.**
`baseline.json` closed the session at `5acde1a5…`, untouched.

### ⚠ 91.6 WHAT WAS NOT DONE

- **THE CHART STILL FRAMES A FIXED `w=1.5`, NOT THE BAND.** The chip now explains the extra pins,
  which resolves the confusion — but the map and the list are still sized by different rules.
  **Framing the chart to the band would close it properly** and is the obvious next move.
- **No per-card distance.** "4 MORE WITHIN 6 MILES" carries it in aggregate; a distance on each
  card is a visual change and was not asked for.
- **NOT SEEN IN A BROWSER.** Chrome froze twice earlier (§90.10). Arithmetic verified in-sandbox.

---

## ✅ §90 — THE SURVEYOR'S PLAN. A TERRITORY MAY CARRY A MAP. `33h` + Worker v2.6.13, s57.

**Owner, s57: "i want to be able to add a map to the territories before we publish… there will be a
button on the case if there is a map so one could click to see the map as a pop up it should have an
x in the upper left hand to x out." And: "not every case will have it. only selected cases."**

### 🔴 90.1 THE MAP MAKER IS GONE — §1v, AND IT COST THIS FEATURE A REBUILD

A map maker was built in an earlier session and produced the sample plan. **It is not in
`index.html` (zero hits for `surveyor`, `OpenStreetMap`, or any map builder), not on disk, not in
the handoff, and not in project knowledge.** It existed only in a chat. **§1v in its purest form,
and this is the second time the rule has been proved this session.** Only the output image survives.
**Decision taken: the curator UPLOADS a finished image; the app does not make maps.** No map
library, no tile fetch, nothing added to a 4 MB file.

### 90.2 HOW IT WORKS

- **Storage: `map:CODE`, one key, via the existing generic `/kv/{key}`.** No new route, no schema
  change. `MAX_VALUE` is 2 MB; the client downscales the longest edge to 1200px and re-encodes at
  the app's existing `0.72` JPEG, landing far inside.
- **`hasMap` rides the `cold:index` entry**, so a shelf card knows a plan exists **without fetching
  the picture**. Only selected cases carry it, so drawing a card costs no extra request.
- **The picture is written ONLY when the Amendment is filed**, in the same action that sets the
  flag, so the two can never disagree and an abandoned upload leaves nothing behind.
- **The card gains a `View plan` pill** beside `View sample`, rendered only when the flag is set.
- **The popup is `#ov-plan`** — the standard `.modal`, with **the ✕ UPPER-LEFT by the owner's
  instruction**, not the usual right.

### 🔴 90.3 WORKER v2.6.13 — A HOLE THAT WAS ALREADY OPEN

**PUT on `/kv/` was gated for exactly two things: `cold:index` and `push:`. EVERYTHING ELSE WAS
OPEN.** So any hunter holding a case code could have written that case's `map:` key — and, before
this feature, any other key too. v2.6.13 refuses PUT and DELETE on `map:` without the curator token.
**GET stays open deliberately: a hunter must be able to look at the plan, and a street plan carries
nothing private.** Verified from outside, four ways: root reads `(v2.6.13)`; ungated PUT returns
**403** *"the archivist shakes his head"*; the follow-up GET returns **404**, proving nothing was
written; and a control PUT to a non-`map:` key still returns **200**, proving the gate is specific
and not a blanket lock.

**⚠ THE WIDER HOLE IS STILL OPEN AND IS NOT THIS SECTION'S TO CLOSE.** Ungated PUT on every other
key remains. Recorded here because the control test proved it; **§80 should carry it.**

### 90.4 `openCrop()` WAS NOT REUSED — AND THE PLAN SAID IT WOULD BE

The plan claimed the upload could borrow `openCrop()`. **Reading it showed that was wrong:** it is
wired to the clue-capture flow (`crop-cluerow`, `crop-clue`, `State.captureMode`,
`State.huntTarget`) and sits on the hunt path. Borrowing it would have put clue fields on a map
upload and risked the most-used screen in the app. **The plan was corrected before code was
written, not after.**

### 🔴 90.5 THE Z-INDEX BAND COMMENT HAD EXPIRED — AND THREE LAYOUT DEFECTS FOUND BY MEASURING

**The CSS comment naming "515-519" as the free band is out of date: all five are taken, and 519
already shares three overlays.** `#ov-plan` sits at **521** — above `#colddetail-ov` (510) and
`#cred-ov` (520) so it paints over the archive that opens it, below `.toast` (620) so a toast still
surfaces, clear of `#ov-loupe` (700). **NEXT FREE: 522.** The comment is corrected in place.

Three faults were then found **by measuring in Chrome, none of them visible by reading the code**:

1. **🔴 NO `max-height`. At a 449px-tall viewport the modal stood 787px with its top at −169 — THE
   CLOSE BUTTON WAS OFF-SCREEN AND THE OVERLAY COULD NOT BE LEFT.** A landscape phone would have
   trapped the user. Capped at `90vh`.
2. **`max-height:100%` DOES NOT CONSTRAIN inside an auto-height flex parent** — a 705px image sat
   in a 380px card and scrolled instead of fitting. **`vh` resolves against the viewport and always
   bites.**
3. **The card did not hug the plan** — 714px of parchment around a 337px map. `width:fit-content`.

**Final measured state:** card 337×362 around a 337×337 plan, fits the viewport, X at 9,9, no
scroll.

### ✅ 90.12 THE OWNER TESTED IT. IT WORKS. (s57 close)

**Owner, s57: "map works!" and then "I TESTED THE MAP ITS GOOD THE REPORTS LOOK GOOD."**

**THE WRITE PATH IS PROVEN BY USE** — attach a plan in the Desk, file the Amendment, the `map:CODE`
key is written under the curator token, the `hasMap` flag lands on the `cold:index` entry, the
**VIEW MAP** pill appears on the shelf card, the popup opens, and tap-to-magnify works through the
loupe. **None of that had ever been executed end to end before this; every claim in §90 up to now
was static analysis, measurement or reasoning.** The reports were checked at the same time and read
correctly.

**🟢 ASKED, AND THE ANSWER WAS "IPHONE".** So this is the first feature in the project's history
verified **on the target device** rather than in headless Chromium or on a desktop. It also means
the loupe's pinch-and-drag has now been driven by real touch, not synthesised events — something no
test in the battery can do. *(§90.6 below is superseded on the round-trip and the pixels, and
stands on everything else.)*

### ⚠ 90.6 WHAT IS NOT PROVEN

- **THE SCREENSHOT AND THE RECTS DISAGREE AND IT WAS NOT RESOLVED.** `getBoundingClientRect` reports
  a 337px card centred in a 1024px viewport; the capture shows it starting at x≈500 and running off
  the right edge. No transform, no zoom, `devicePixelRatio` 1.875, capture 1045px for a 1024px
  viewport. **Trust the numbers, not the picture — and do not quote the picture as verification.**
- **✅ SUPERSEDED — THE UPLOAD ROUND-TRIP RAN AND WORKED (§90.12).** *(the original line:)* Writing
  a `map:` key needs the curator token, which Claude must never hold (§A.1), so the first real save
  at the Desk was the test.
- **NOT SEEN ON THE PHONE.** The owner is on an iPhone 15; every route Claude has is desktop Chrome.
- **✅ SUPERSEDED IN `33i` — SEE §90.7. The publish page now has it too.** *(the 33h line, for the
  record:)* Only the TERRITORIES editor got the control. The submissions (`sb`) and publish (`p`)
  editors did not.

### 🔴 90.7 THE PLAN ON THE PUBLISH PAGE — AND A BUG IT EXPOSED. `33i`, s57.

**Owner, s57: "i need the Attach a surveyor's plan also on this publish page."** The same control,
the same held-until-filed behaviour, written by `publishCold()` instead of `saveTerrInfo()`.

**🔴 AND ADDING IT FOUND A REAL BUG IN THE PUBLISH PATH.** `saveTerrInfo()` builds its index entry
with `Object.assign({}, prev, …)` — it MERGES. **`publishCold()` builds `entry` FRESH, from a
literal.** So every field not named in that literal is dropped on re-publish. With `hasMap` added,
**re-publishing a case that already had a plan would have silently cleared the flag: the `View
plan` pill would vanish while the picture sat in the store, orphaned.** Fixed by reading
`idx[i]` into `_prevP` and carrying the flag through.

**⚠ THE SAME SHAPE MAY BITE AGAIN.** `publishCold()`'s literal is the only place in the Desk that
rebuilds an index entry from scratch rather than merging. **Any future field added to a `cold:index`
entry must be added THERE TOO, or re-publishing will erase it.** This one was caught only because
the new field happened to be added in the same session; a later field would not be.

**Buildmark `33i` / Cobalt `#3B6BA5`** — §8i's letters wrapped after `h` Rust.

### ✅ 90.8 TAP THE MAP TO MAGNIFY — NO NEW ZOOM CODE. `33j`, s57.

**Owner, s57: "map works! can the map be zoomed in on?"** — the first confirmation that the WRITE
path works end to end, and the answer to the second half was already in the file.

**`openLoupe()` ALREADY DOES PINCH, DRAG AND DOUBLE-TAP** for clue photos. It takes any object with
a `.src`, and `safeImgSrc()` accepts a `data:image/(png|jpe?g|webp|gif|bmp);base64,…` URI — which is
exactly what a map is. **So the map rides it: six lines, no zoom library, no gesture handling, no
new state.** The image gets `cursor:zoom-in` and an `onclick` that calls
`openLoupe({src:d})`.

**THE LAYERING WORKS BY LUCK OF AN EARLIER FIX, AND IS WORTH KNOWING.** `#ov-loupe` is **700** and
is explicitly NOT an `.overlay` — the §79-era z-index comment says so. `#ov-plan` is **521**. So the
loupe paints over the map card that summoned it and its own `#loupe-x` stays reachable. Had the map
card been given a number above 700 this would have failed silently.

**⚠ NOT VERIFIED IN A BROWSER.** Chrome froze twice while trying (stubbing `Store` after boot leaves
the app's in-flight reads hanging — see 90.10). STATIC clean and the battery green on `33j`, but
**the zoom itself has been reasoned about, not watched.** The owner has it on the phone, which is
the surface that matters: a 337px street plan is unreadable, which is why he asked.

### ✅ 90.11 THE CAPTION TELLS YOU IT ZOOMS — AND THE PINS STOP JUMPING. `33k`, s57.

**Two owner asks, both from the phone.**

**(a) THE CAPTION. Owner copy, applied verbatim: `TAP MAP TO ZOOM IN & PAN`.** *(He first gave
`(TAP MAP TO BE ABLE TO ZOOM IN & PAN)` and shortened it himself; the shorter line is the one that
shipped.)* **His condition was "IT NEEDS TO FIT ON ONE LINE."**

**🔴 AND THE FIRST ATTEMPT DID NOT, WHILE APPEARING TO.** At 11px the longer wording ran **359px
inside a 337px card** — `nowrap` pushed it past the card edge, where `overflow:hidden` would have
clipped both ends. **`scrollWidth === clientWidth` REPORTED CLEAN AND WAS WRONG: the element had
already overflowed its PARENT, so it was measuring itself against itself.** The honest test is
`cap.width <= modal.width`. §11a, again: a check that can only say "fine".

Final, measured: **11px, one line, 342px cap in a 342px card, not clipped**; at a 320px phone the
line runs 121px inside a 289px content box. **IF THE WORDING CHANGES, RE-MEASURE — a longer line
clips silently rather than wrapping.**

**(b) THE PINS — THREE TIERS, ARRIVED AT IN TWO PASSES, AND THE SECOND PASS IS THE LESSON.**

`pinBoost` was `_vb.w<=0.5 ? 2.0 : _ramp` — 2.0x on the FINAL zoom step alone, so the pins **jumped**
on the last press. First fix: widen the threshold so the two steps beneath max also got 2.0. **The
owner looked at it and said "this is too large" — three consecutive steps of full-size pins swamped
the chart.** Correct diagnosis, wrong remedy: the jump was real, but flattening it upward traded one
fault for another.

**HIS OWN SUGGESTION IS WHAT SHIPPED: a median tier.** The two steps below max take the midpoint
between the ramp and 2.0, so the pins grow as a progression rather than a step.

```
pinBoost = _vb.w<=0.5 ? 2.0
         : _vb.w<=2.5 ? (_ramp+2.0)/2
         : _ramp;
```

`chartZoomIn` divides the viewBox width by 2.2 and floors at 0.5, so the ladder and the resulting
boosts are:

| viewBox `w` | 4.009 | 1.822 | 0.828 | 0.500 |
|---|---|---|---|---|
| `_ramp` | 0.816 | 0.886 | 0.955 | 1.000 |
| **pinBoost** | **0.816** | **1.443** | **1.478** | **2.000** |

**DO NOT re-round the 2.5 without re-deriving that ladder — 4.009 must stay outside it.** The code
comment carries the same warning and the history, so the next session does not re-flatten it.

**⚠ ARITHMETIC VERIFIED, APPEARANCE NOT.** The boosts above were computed, not watched. **The
owner's screenshots are the check, and they are what caught the first attempt** — which is the
argument for showing him pixels before shipping a visual change, not after.

### 🔴 90.9 THE WRONG BUILD WENT LIVE, AND THE PROOF BLOCK SAID SO

**`ship` committed the PRE-rename `33i` (`eb5f9652…`, `View plan` ×4) and it was recorded as done.**
The rename was on disk; the commit was not. **`ship`'s proof block PRINTS THE COMMITTED
`index.html` HASH — the evidence was on screen and neither of us read it**, because the ask had
been "paste me Local/Origin" and that is all that was read.

**THE RULE: READ ALL OF `ship`'s PROOF BLOCK — the hash and the buildmark, not just Local vs
Origin.** Local == Origin only proves the push matched the commit; it says nothing about WHICH
BUILD was committed. This is §77.11 in a second costume: the tool told the truth and the wrong line
was read.

### ⚠ 90.10 STUBBING `Store` AFTER BOOT FREEZES THE PAGE — TWICE IN ONE SESSION

Replacing `Store.get`/`Store.base` from the console **after** the app has booted froze the renderer
twice, each time killing the tab and costing a reload. **The app's own in-flight reads are already
awaiting the real `Store`; swapping it mid-flight strands them.** `session_checks.py` avoids this by
stubbing at a controlled point in `boot()`, 1100ms after `goto`. **From the console: stub via
`add_init_script`-equivalent BEFORE load, or force `Store.base=()=>null` as the very first statement
after `DOMContentLoaded` — never mid-session.**

---

## ✅ §89 — `GET /null 404` ON BOOT. RESOLVED — IT WAS THE HARNESS, NOT THE APP. (s57)

**THE APP WAS NEVER AT FAULT. The premise that "the app is building a URL from a `null`" is struck.**
The `/null` was the test harness's own Store/fetch stub calling `fetch(null)` on itself when
`page.evaluate()` serialised it. The app makes no such request. Proven by experiment, not inferred.

**THE EXPERIMENT THAT SETTLED IT.** `find-null.py` was extended to take a mode argument
(`A`/`B`/`C`/`D`) toggling `boot()`'s two post-`goto` steps — the Store stub and `gate()`
(`credFiled()`) — independently. Run against a local server logging every request:

| | stub | gate | result |
|---|---|---|---|
| A | no  | no  | 1 request, **no `/null`** |
| B | no  | **yes** | 1 request, **no `/null`** |
| C | **yes** | no  | **REPRODUCES `/null`** |
| D | yes | yes | reproduces `/null` |

**Cell C fired and cell B did not** — so the **stub owns it** and `credFiled()`/the gate is innocent.
The confirmation in the battery log: the old `session_checks.py` printed **exactly five** `/null`
404s per run — **one per `boot()` call** (5 boots), not two per viewport and nothing to do with the
gate.

**THE MECHANISM, PROVEN.** `boot()` does `await pg.evaluate(STUB)` where `STUB` is a multi-statement
string. A `page.evaluate(string)` returns the string's **completion value**, and here the last
statement is `window.fetch = async (u,o) => {…}` — an **assignment whose value is the newly-assigned
fetch function.** Playwright serialises an `evaluate()` result *by value*, and **when that value is a
function it INVOKES it** — with `null` as the argument. That call is literally `window.fetch(null)` →
`"null"` resolves against the page origin → `GET /null` → 404. Reproduced in isolation with a
three-line stub (function completion value throws `fetch(null)`; a primitive completion value does
not). CDP `Network.requestWillBeSent` initiator, verbatim — note the deepest frame is `evaluate`,
never an app function:

```
--- CDP initiator ---
  type: script
    window.fetch  @ line 9  col 61      <- the stub's fetch wrapper
    window.fetch  @ line 13 col 9       <- the probe's trace wrapper
    evaluate      @ line 317 col 17     <- Playwright UtilityScript.evaluate
    (anonymous)   @ line 0  col 43
```

**THE FIX — BOTH HALVES (§1w).**
1. **The stub (root cause).** `session_checks.py`'s `STUB` now ends on a terminal primitive
   (`true;`) so `evaluate()`'s completion value is no longer the fetch function. The `/null` is gone:
   a full boot now makes exactly one request (`index.html` 200) and nothing else. Commented in place
   so it is not undone.
2. **The blind check (§11a — "the test that passes for the wrong reason").** Check 4 asserted only
   *"boots with no page errors,"* and **a failed subresource fetch is not a page error**, so a 404
   scrolled past under a green tick. `boot()` now records every 404 response, and Check 4 fails on
   any unexpected one (the app makes no deliberate 404, so any 404 is unexpected). **Proven to have
   teeth**: with a real missing subresource the check returns non-empty and goes red — it is not an
   audit that can only return "clean" (§11a #11). SESSION is now **21/21** (was 19/19; +2).

**STATE:** battery green on `33g`, all three suites — STATIC clean · BEHAVIOUR 59/59 · **SESSION
21/21** · Agent D drift NONE. **No `index.html` byte changed** — this was a test-only correction, so
no visual output moved. `find-null.py` keeps the four-cell mode and stands as the record of the
mechanism. **⚠ s57 review: `find-null.py` itself still ended on the offending assignment — the
SECOND COPY of the defect (§1w). Fixed with the same terminal primitive. The general rules are
§11d.**

---

## ✅ §88 — THE REPO WAS SLIMMED. 22 MB OF IT WAS NEVER SERVED. s56.

**THE OWNER, LOOKING AT THE GITHUB FILE LIST:** *"does all this need to live here"* — followed by
*"whatever is best as long as u have it locally."* It did not.

### 88.1 WHAT THE SITE ACTUALLY NEEDS — ELEVEN THINGS, MEASURED NOT ASSUMED
`index.html` · `sw.js` · `manifest.webmanifest` · `j.html` · `og-card.jpeg` · `award-card.jpeg` ·
`icons/` (180, 192, 512 and the maskable pair) · `.nojekyll`.
**`sw.js` PRECACHES ONLY SIX PATHS** — `./`, `./index.html`, `./j.html`, `./award-card.jpeg`,
`./og-card.jpeg`, `./icons/icon-192.png`. That list is the shortest honest answer to "what is the app".

### 88.2 WHAT LEFT, AND WHERE IT WENT
**Moved to `_to_delete\s56-repo-slim\` — ON DISK, gitignored, NOT deleted:**
`_preview/` **19 MB** (scratch HTML from old design passes) · `art/` **2.8 MB** (source art: the Bonnie
source, the seals, icon-C) · `hunt-icon-v5.png` · the **root** `behaviour.py`, byte-identical to
`test/behaviour.py` and carried as a known duplicate since s52.
**22 MB out of a repo whose app is 4 MB.** `art/` is source material and is kept deliberately — it
simply has no business in a PUBLIC WEB repo.

### 🔴 88.3 A NEAR-MISS, RECORDED BECAUSE IT WOULD HAVE READ AS PROOF
The first reference check reported **`art` referenced 567 times** and Claude nearly stopped there.
**It was matching the substring** — `start`, `part`, `apart`. Re-run against the PATH form
(`"art/`, `'art/`, `(art/`) and against each filename individually, the true count is **zero**.
**A grep for a short word is not a grep for a path.** The same class as §0.1's `paid:` error:
querying the wrong shape and believing the number that came back.

### 88.4 WHAT STAYS, AND THE DECISION STILL OWED
`HANDOFF*.md`, `docs/`, `claude/`, `test/`, `ship.cmd`, `battery.cmd` all stay. None are served; they
are the build record. **The question about them is not size, it is that THE REPO IS PUBLIC** — the
three handoffs are world-readable and describe the Worker's routes, the retention rules and the open
security items. **No secret is in them (re-checked s56).** `Marketing-Brief.md` and
`Monetization-Brief.md` were correctly NEVER committed — pricing and positioning are not public.
**§80 item 9's decision stands open: keep the handoffs public, or move them to `Hunt-backups`.**

---

## ✅ §87 — THE BYTE-ORDER MARK. EVERY CSV HAS BEEN WRONG SINCE THE FIRST ONE. `33g` + Worker v2.6.12, s56.

**HOW IT WAS FOUND:** the owner opened the emailed annual report and asked what was in the sheet —
its title row read **`THE CASE â€” THE YEAR`**. He was not reporting a bug; he was asking a question,
and §1's rule held — **measure and answer, do not assume a change was requested.** The answer was a
defect older than the feature he was looking at.

### 87.1 THE CAUSE, AND WHY `charset=utf-8` NEVER SAVED IT
**Excel opens a `.csv` with no byte-order mark as Windows-1252.** The em dash is UTF-8
`E2 80 94`; read as cp1252 those three bytes are `â€”`. **The `charset=utf-8` on the MIME type does not
reach Excel** — by the time the file is on disk the header is gone, and a `.csv` has no other way to
declare its encoding. **Only the BOM does.** Every em dash, guillemet and `№` in every report has been
arriving mangled since the first CSV shipped; nobody noticed because nobody had opened one in Excel.

### 87.2 THE SAME DEFECT HAD TWO HOMES (§1w)
**Worker `v2.6.12`** — one helper, `csvBytes(s)`, prepending `\uFEFF`, wired into **all three**
attachment sites (`sendYear`, `sendCaseSheet`, `sendLedger`). One helper and not three inline copies,
deliberately: a fourth copy of the same string is how they drift.
**Client `33g`** — the two `Take a copy` `Blob` constructors, which download rather than email and
were the half a Worker fix would have left broken.
**Fixing only the one the owner could see would have left the other, and he would have found it.**

### 87.3 WHAT WAS VERIFIED
Worker root reads `(v2.6.12)`; `/list` with no token still **403** — the lock was not disturbed.
Pages serves `ec6f2966…` / 4,052,031 B / `33g` with **both** BOM sites present, counted in the
FETCHED bytes rather than inferred from the hash. `node --check` clean on both files.
**Raw was still serving `33f` at the time and that is normal (§0) — Pages is authoritative.**

### ⚠ 87.4 TWO THINGS RECORDED
- **THE BATTERY IS STILL GREEN ONLY ON `33d`.** 33e, 33f and 33g have all shipped untested.
  This is now three builds of drift and it should be closed before the next one.
- **`33g` WAS PUSHED THROUGH THE GITHUB WEB PAGE, NOT `ship`.** So the owner's **local clone is
  behind origin** (`4b7432a5` local, `9cd34d4d` origin). **`git pull` before the next `ship`** or the
  push is rejected. *(Claude cannot run git from the sandbox at all — §77 — so this is his to do.)*

---

## ✅ §86 — THE ANNUAL REPORT REACHED THE DESK. `33f`, s56.

**OWNER, s56, VERBATIM:** *"on the case sheet i think we need a yearly report button and a earlier
later with month scroll like the ledger this needs to be on each case sheet."*

**SHIPPED: `33f` / Magenta `#A8478F` — 4,051,223 B / `437fdc409f3e163831a062994da151638c985cc166f7fdcc599d50e401c90fc8`,
commit `b7e348e7`. Disk == raw == Pages, hash-verified.** Client only; Worker v2.6.11 was already
answering `?year=` and was not touched.

### 86.1 THE SECOND HALF OF HIS ASK WAS ALREADY THERE — AND THAT IS WHY HE COULD NOT SEE IT
The case sheet has had working month arrows since 33b (`ledg-sprev` / `ledg-snext`). What it did
NOT have was **the month's name anywhere in the nav** — the centre read `CASE No. 112211`, so a
reader could scroll four months and never learn which one he was on. **He read a missing LABEL as a
missing FEATURE, and he was right to: an unlabelled control is not a control.**
**33f: two rows.** Row one is the case number; row two is the Ledger's own
`‹ Earlier · August 2026 · Later ›`, verbatim, so both screens scroll identically. The bare-guillemet
`.ledg-arrow` buttons went with the labels that replaced them; **the CSS rule is left in place** —
unrequested deletions are how a later session finds a class it cannot explain (§5).

### 86.2 THE COPY IS THE OWNER'S. CLAUDE'S PLACEHOLDER WAS NOT SHIPPED.
§84.6 proposed `The whole year 2026 ›` and flagged it as unapproved. It was put to him with two
alternatives; **he chose `Annual report ›`**, and that is what is in the file, on both screens.
Layout was also offered as three options before a pixel moved (the aesthetics rule), and the
two-row nav is the one he picked.

### 86.3 WHAT THE YEAR VIEWS SHOW — AND THE HEADING THAT KEEPS THEM HONEST
`loadYear(year, fromMonth)` (the company) and `loadCaseYear(code, year, fromMonth)` (one case).
Both carry `‹ 2025 · 2026 · 2027 ›`, a month-by-month table with **every month drawn, quiet ones
included**, and `‹ The month` back to exactly where the reader came from.
**🔴 THE §84.3 FIGURES ARE PRINTED UNDER THEIR OWN HEADING, `ALL-TIME — NOT THIS YEAR`, AND NEVER
INSIDE THE YEAR'S TABLE.** Badges issued, hunters and first finds carry no date in the record;
summing them per year would be inventing data. A case year that crosses the 400-day fold prints the
Worker's own `foldNote` — **a month reading zero because the record was folded is not the same as
nothing happening.**

### 86.4 `fromMonth` — A BUG CAUGHT BEFORE IT SHIPPED, RECORDED BECAUSE THE CAUSE RECURS
The first cut had both year views return via `State.ledgMonth`. **`State.ledgMonth` is set by
`loadLedger` and by nothing else** — `loadCaseSheet` never writes it — so a case sheet's year would
have returned to whatever month the LEDGER last showed, which is usually not the month the reader
left. The month is now **carried in as an argument**. *(The general fault: reading shared state to
recover a value the caller already had.)*

### 86.5 `email report` POSTS WHAT IS ON SCREEN
`_wireLedgEmail(month, code, year)`. **`year` is appended only when the caller passes one**, so both
month callers are byte-identical in behaviour to 33e. The Worker tests `?year=` before `?month=`
(§84.2) and still validates `month`, so the month stays on the query as a valid value and is simply
not the one used. **Requires v2.6.11**, which is deployed.

### ⚠ 86.6 WHAT IS NOT DONE
- **✅ CLOSED s57 — THE BATTERY IS GREEN ON `33g`, WHICH COVERS 33e, 33f AND 33g (§82.3).**
  *(the s56 line, for the record:)* **THE BATTERY.** §82's tick is still **33d**. 33e and now 33f
  have both shipped untested. `node --check` was clean on the single script block, and that is all
  that was run.
- **`ship`'s `git add -A` SWEPT 33f INTO THE s55 DOCS COMMIT.** The log message for `b7e348e7`
  reads `s55: docs rescued, .gitignore, ship.cmd…` and says nothing about the annual report.
  The code is correct; **the history misnames it.** Anyone bisecting on the message will miss it.
- **NO CSV FOR A YEAR.** `Take a copy` is on the month's case sheet only. Not requested — not built.
- **NOTHING HAS BEEN SEEN ON A PHONE**, as with every build since s29 (§80 item 1).

---

## ✅ §84 — THE YEAR. **CLOSED s56 — THE DESK UI SHIPPED IN `33f`. SEE §86.** (written s55 close)

**OWNER, s55, VERBATIM:** *"on the report side i need to be able to sort by year like i will need an
annual report per case and over all and when 2027 rolls around start fresh."*

**✅ SERVER: `worker-v2_6_11.js` 97,885 B /
`7dacce07977efdc466af0fbf5b59b04e02e678204403024a5ba38bdf890fce74` — DEPLOYED AND VERIFIED,
root reads `(v2.6.11)`.** It also carries v2.6.10 (the CSV header block, `Aug 1` day labels, and the
`d.day` bug — see §84.4). `node --check` clean.
**🔴 CLIENT: NOT BUILT. There is no way to reach a year from the Desk yet.** The routes are additive,
so 33e is unaffected and nothing is broken — the feature is simply unreachable until the UI lands.

### 84.1 ✅ "START FRESH IN 2027" NEEDED NO WORK, AND A RESET WOULD BE A BUG
**Every counter is already year-stamped** — `mo:YYYY-MM:event` and `ct:CODE:YYYY-MM-DD:event`. **A
year is a FILTER, not a reset.** Nothing is archived, zeroed or rolled over at midnight on New Year's
Eve, and **nothing should be: a reset would destroy the year-on-year comparison the annual report
exists to make.** Do not add one, and do not accept a request for one without reading this line back.

### 84.2 THE ROUTES — ALL CURATOR-LOCKED, `?year=` BEATS `?month=`
```
GET  /report?year=2026                      -> annual(env, year)      the company
GET  /report?code=112211&year=2026           -> caseYear(env, code, year)  one case
POST /report-email?year=2026[&code=112211]   -> sendYear(env, rep)     either, by post
```
**`?year=` is tested BEFORE `?month=` deliberately** — a caller sending both gets the year it asked
for, not silently the month. **A malformed year is a 400, never a quiet fallback to the month.**
`yearOK` verified: `2026` true; `26`, `20x6`, `2026-08` all false.

### 🔴 84.3 WHERE EVERY FIGURE COMES FROM — AND THE THREE THAT CANNOT BE YEARLY AT ALL
- **THE COMPANY YEAR IS EXACT AND STAYS EXACT FOREVER.** `mo:` rows are true monthly deltas **and
  are in the sweep's permanent set**, so the year is twelve reads and never degrades.
- **A CASE's YEAR COMES FROM ITS DAILY ROWS**, which are true daily deltas — **but they are folded
  after `DAILY_KEEP_DAYS = 400`.** So a case year is exact only while those days survive. Every
  case-year payload therefore carries **`foldedBefore`** (the cutoff date) and **`complete`**, and the
  email prints a note naming the date. **A month reading zero because the record was folded is NOT
  the same as nothing happening, and the report must never let a reader confuse the two.**
- **🔴 `joined`, `first_find`, the state tally and the geography CANNOT BE SPLIT BY YEAR.**
  `seen:`, `seenf:`, `st:` and `geo:` rows **carry no date whatsoever** — all-time by construction.
  They are printed under their own heading, **`ALL-TIME — NOT THIS YEAR`**, never inside the year's
  table. **Two traps recorded so nobody repeats them:** summing them per year would be **inventing
  data**; and summing a sealed month's per-case `joined` across twelve months would **double-count
  catastrophically, because that field is cumulative-to-date, not a monthly delta.** If a yearly
  hunter count is ever genuinely wanted it needs **a dated key written at the time** — a future build,
  never a query over what exists.

### 84.4 🔴 A BUG SHIPPED IN v2.6.9 AND FIXED IN v2.6.10 — THE SAME MISTAKE AS §79.4
The case CSV's first column arrived **empty in every row**. `caseCsv` read **`d.day`**; `caseSheet()`
populates **`date`**. **Claude guessed the key instead of reading the shape** — the identical error to
hand-typing the month label, twice in one session. **`out.days` entries are
`{date, scanned, opened, finished, hints}`.** `scanned` was also being dropped and is now a column.
**READ THE SHAPE. THE FILE IS RIGHT THERE.**

### 84.5 HOW IT WAS VERIFIED WITHOUT A DATABASE — AND THE ONE TEST THAT PROVED THE FILTER
The real functions were imported into **node** against a **stub D1** that translates SQL `LIKE` to a
regex. **`export default` was rewritten to `const __handler =` rather than truncated** — the first
attempt cut the file at `export default` and deleted every function under test, which are defined
BELOW it.
**THE TEST THAT MATTERS: a planted `ct:112211:2025-12-30:case_opened = 99`.** The 2026 case year
returns **9** (2+1+1+1+4), **not 108** — so December 2025 does not leak into 2026. Company 2026
totalled `badge_issued 27`, `cold_viewed 32`, `case_opened 62` from an August and a September row.
**Sample CSVs were written and handed to the owner to open in Excel.** `csvDay('nonsense')` returns
the input rather than `undefined`.

### 🔴 84.6 WHAT IS LEFT — THE CLIENT, AND THE IDIOM ALREADY DECIDED
The app already has the pattern: the case sheet's **`‹ The whole month`**. One level up:
**Ledger (a month) → a line under the month row reading `The whole year 2026 ›` → the annual view,
where the arrows become `‹ 2025 · 2026 · 2027 ›` and `‹ The month` returns.** Identical on a case
sheet, so a year is one tap from wherever the reader stands, and **`email report` posts whatever is on
screen** — month or year — through the same `_wireLedgEmail` (§83.2), which will need a `year`
argument alongside `code`.
**✅ s56: BUILT, AND THE COPY WAS PUT TO THE OWNER RATHER THAN SHIPPED.** He chose **`Annual report ›`** — Claude's `The whole year 2026 ›` placeholder was NOT used. See §86.

---

## 🔴 §109 — SESSION 58 CLOSE. READ THIS BEFORE §80.

**WHAT IS LIVE:** 🔴 **CORRECTED s59 — `34e` IS LIVE, NOT `34d`.** Commit `f35b49de`; `34e` was
pushed after this section was written, so it read stale from the moment it was saved. **4,302,603 B /
`2adb51cf74344de5eb02f155f8b932cec661492d106f8478f69772bd39039357`** — disk == origin == Pages == raw,
re-hashed s59 from the shell. Worker **v2.6.13**. `34e` is the join-lag work only — no pixels.
**`34e` / Verdigris IS SPENT. NEXT MARK `34f` / Magenta `#A8478F`.**

**NOTHING IS ON DISK UNSHIPPED, AND THE BATTERY DID RUN.** §109 said Gate 3 held `d4ab9a79`; that is
also stale — `test\.last-battery` reads
`2adb51cf74344de5eb02f155f8b932cec661492d106f8478f69772bd39039357`, which IS `34e`, so a full
three-suite battery passed on the shipped build. STATIC re-run green in the sandbox s59.

### WHAT SHIPPED TODAY, IN ORDER
`33m` the hint coin · `33n` the CASE CLOSED stamp · `33o` the Met badge, one red `#8B0000`, the
1.5x ordinal · `33p` five Chicago territories + the cold-filter fix · `34a` precinct default, chart
pinch, the stamp anchor · `34b` the plate 25% smaller · `34c` the iOS compositing fixes ·
`34d` the wipe crop, the 1.95em ordinal, the badge press.

### 🔴 THE SESSION'S OWN LESSON — SIX MARKS SPENT MID-FLIGHT
`33n`, `33o`, `33p`, `34c` all shipped builds that were already behind, plus `34d` shipping while
`34e` sat on disk. **Every one had the same cause: Claude wrote a `ship` line, kept editing, and did
not declare the old command dead.** §1x and §1y say exactly what to do and were written DURING this
session. **`ship`'s three gates caught what discipline did not — Gate 1 on a stale §0, Gate 2 on an
unbumped buildmark, Gate 3 on a stale battery. TRUST THE GATES; THEY ARE THE ONLY THING THAT WORKED.**

### 🔴 OPEN, IN ORDER OF WHAT IT COSTS TO LEAVE IT
1. **`docs/Branding-Guidelines.md` IS STALE AND DUPLICATED IN THE PUBLIC REPO.** The file is LOCKED
   on the owner's disk — Claude's writes fail `PermissionError`, and `del` fails silently (OneDrive
   or an open editor). `Branding-Guidelines-s58.md` sits beside it carrying a banner saying it
   supersedes. **Two public documents disagree about the house red and the type rule.** Five ships
   have gone out with this unresolved. Clear the lock, `del`, `ren`.
2. **PUSH CANNOT WORK ON iOS UNTIL THE APP IS INSTALLED TO THE HOME SCREEN** (§80.1). The `push`
   handler in `sw.js` is correct and fires with the app closed; `new Notification()` (5 sites) only
   works on screen. **The install flow has still never been exercised.** This gates the whole
   notification feature and no client change touches it.
3. **THE JOIN IS STILL 12 STORE CALLS, 6 ROUND TRIPS DEEP** (§108). Half fixed in `34e`. The same
   `sub:` key is still read four times; the reads at 1109ms and 4102ms come from the resume and
   board-render path, not `joinCase`. Trace `saveHunterSub()` and the board render.
4. **THE SIXTY CHICAGO CLUES ARE UNWALKED** (§96). `Chicago-Cold-Cases-plan.html` at the repo root
   is the field document — a page per hunt, all twelve finds with hints, a plate for a photograph.
   **Wikimedia Commons rate-limited (429) from the sandbox, so no pictures could be sourced.**
5. **THE PHONE PREVIEW.** The owner had to SHIP TO SEE every visual change today. `serve.ps1` binds
   to localhost; if it bound to `0.0.0.0` the iPhone could load a build over wifi before it went
   near the repo. **This is the single change that would most improve the next session** (§104).

### ✅ CONFIRMED BY THE OWNER THIS SESSION
Chart pinch works with real fingers (§99). The handwriting crop is fixed (§106).

---

## 🔴 §80 — THE OPEN-TASK REGISTER, RE-AUDITED AT s55 CLOSE. THIS SUPERSEDES §65's ORDER.

Every line below was checked against the document and, where measurable, against the live services
at s55 close. **§65 was the s53 ordering; four of its ten items have since closed and it still reads
as current. Use THIS list.**

**GIT AND SURFACES: CLEAN.** `local == origin == 58f24c38`. `index.html` **33d** 4,037,229 B /
`6f3d5f62…` identical on disk, raw and Pages. Worker **v2.6.7**. Site and `/privacy.html` both 200.

### ✅ CLOSED SINCE §65 WAS WRITTEN — DO NOT RE-RAISE THESE
1. **The notification card** — built s54, 32r (§66).
2. **`TASK-live-roster`** — built s54, 32t (§68).
3. **Read `/report` once** — done s54, and it found the take-rate defect (§73).
4. **The take-rate defect** — fixed in Worker 2.6.6, and **2.6.7 is live**, so it is deployed (§73.2).
5. **`first_find`** — was already built; struck s54 (§70.3).
6. **Client export** — struck s54 with reasoning: nothing promises it (§75.4).
7. **THE EMAILED LEDGER — ✅ FULLY CLOSED s55, BOTH HALVES.** Client 32y/33a/33b, on the Ledger AND
   the case sheets (§79); **Worker v2.6.8 deployed and the send confirmed working by the owner
   (§81).** Open since §64.4. **The remaining unknown is the 3am cron, not the send.**
8. **§85.2, the ledger meta row** — closed by deleting the sentence (§78).
9. **🆕 `candidate-32m.html` and `_candidate-32m.html`** — **BOTH 404 ON RAW. THEY ARE ALREADY GONE.**
   §0's table still carries a red row ordering their deletion. **That row is stale — strike it.**
10. **`privacy.html` to GoDaddy** — `scavengerandhunt.com/privacy.html` returns **200**. Done.

### 🆕 §80.1 THE FILE AUDIT AT s55 CLOSE — WHAT THE SPLIT TURNED UP

**🔴 THE FOUR "OTHER CANONICAL DOCS" WERE NOT ON DISK AT ALL.** `Marketing-Brief.md`,
`Monetization-Brief.md`, `Privacy-Policy-DRAFT.md`, `Branding-Guidelines.md` and
`SPEC-SERVICE-WORKER.md` existed **only in the claude.ai project knowledge** — read-only, outside
git, one copy, invisible to `curl` and to any future session that did not happen to be given the
project. **§1v in its purest form, and it had been true since s27/s28 without anyone noticing.**
**Claude's own s55 instruction block carried the same five names forward WITHOUT CHECKING THEY
EXISTED** — the identical error §77.9 was written to condemn, committed in the act of fixing it.
**✅ NOW COPIED TO `docs/`:** Marketing-Brief 19,652 B · Monetization-Brief 13,849 B ·
Privacy-Policy-DRAFT 12,489 B · Branding-Guidelines 3,079 B · SPEC-SERVICE-WORKER 6,839 B.
**⚠ NOT YET COMMITTED — an owner decision is owed first: see the note on the two commercial briefs
below.** The instruction block's paths become true only once they are committed; until then it names
files a fresh clone will not have.

**🔴 THE PROJECT KNOWLEDGE HOLDS TWO DEAD HANDOFFS, AND BOTH ARE NOW DOUBLY DEAD.**
`SUPER-HANDOFF.md` (312,895 B) and `SUPERHANDOFF.md` (76,521 B) are both there. The instruction
"there is one copy and never another" has been violated the whole time, and after the s55 split
**neither file exists in the repo at all.** **DELETE BOTH FROM PROJECT KNOWLEDGE and upload
`HANDOFF.md` in their place.** *(Only `HANDOFF.md` — the other two are reference and history and do
not belong in a context window.)*
It also holds `worker-v2_5_0/2_6_0/2_6_1.js`, all superseded; the live Worker is **v2.6.11**.

**⚠ NINE WORKER SOURCES WERE SITTING AT THE ROOT.** Seven are now staged at
`_to_delete\old-worker-sources\` (2.6.3 → 2.6.9). **Kept: `worker-v2_6_11.js` (live) and
`worker-v2_6_10.js` (one back).** All are untracked and must stay untracked — **the repo is public
and the Worker source must never be committed.**

**✅ ALL THREE CLOSED s56 — SEE §88.** The root `behaviour.py`, `_preview/` and
`hunt-icon-v5.png` are out of the repo tree and kept on disk at `_to_delete\s56-repo-slim\`.

### 🔴 OPEN, IN ORDER OF WHAT IT COSTS TO LEAVE IT
0. **✅ CLOSED s56 — THE YEAR'S DESK UI SHIPPED IN `33f` (§86). DO NOT RE-RAISE.** *(the original entry, for the record:)* **THE YEAR'S DESK UI (§84.6).** The Worker is deployed and answers `?year=`; **there is no way
   to reach a year from the app.** The idiom is decided and the copy needs approving. **This is the
   first thing to build next session** — it is half-finished work, which is the worst kind to leave.
   **⚠ AND THE BATTERY HAS NOT RUN ON 33e** (§82's tick was 33d).
1. **🟡 THE PHONE — PARTLY DONE AT LAST, s57. Carried since s29.** **The owner ran the app on his
   iPhone and exercised the surveyor's map end to end there** — the Desk upload, the shelf pill, the
   popup, pinch-zoom by real touch — **and the reports too (§90.12).** After nineteen-plus builds of
   "it has never been on a phone", it has.
   **🔴 BUT THE ITEM DOES NOT CLOSE, AND THE DIFFERENCE MATTERS.** Running in mobile Safari is not
   the same as being installed. **STILL UNTESTED:** the **install / home-screen standalone mode**
   (never seen), the **notification card**, **web push**, the **live roster**, and the **full hunt
   loop across two devices** (§50.2).
   **✅ THE LEDGER EMAIL IS OFF THIS LIST — CONFIRMED RECEIVED (owner, s57): "IT SENDS AND WAS
   RECIEVED."** The send was confirmed at s55 (§81); **arrival in the inbox is now confirmed too.**
   The only unknown left on that feature is the 3am cron, which has never fired on its own (§59.3).
   **🔴 THE APP HAS NO INSTALL AFFORDANCE AT ALL — MEASURED s57: `Add to Home` ×0,
   `beforeinstallprompt` ×0, `display-mode: standalone` ×0, `navigator.standalone` ×0.** The
   manifest is complete (`display:standalone`, six icons, theme colour) and **has never once been
   exercised.** **ON iOS APPLE PROVIDES NO PROGRAMMATIC PROMPT** — installing is Share → Add to Home
   Screen by hand, so the "install prompt" has to be the app's OWN instruction card, shown only when
   it detects it is not standalone.
   **🔴 WEB PUSH ON iOS REQUIRES THE HOME-SCREEN INSTALL (Apple, iOS 16.4+).** The notification card
   and push are therefore **not broken — they are UNREACHABLE from a Safari tab**, and no amount of
   testing in one will move them. Standalone also changes the layout: no browser chrome means a
   taller viewport and real safe-area insets, which `--safe-b` and the rotate gate were written for
   and have never met.
   **NEXT BUILD, SMALL AND HIGH-LEVERAGE:** detect standalone with
   `navigator.standalone || matchMedia('(display-mode: standalone)').matches`; when false on iOS,
   show a Victorian instruction card. Then Share → Add to Home Screen, open from the icon, confirm
   it launches standalone — **and the notification card, push and the roster all become testable for
   the first time.**
2. **🟡 THE LEGAL ENTITY (§50.1) — MOVED s57. `Do No Harm Company LLC` IS SUBMITTED TO GEORGIA,
   after the name came back cleared.** Step 1 of four is in the state's hands; nothing else on the
   store track can start until it is approved. **THE NEXT ACTION IS THE OWNER'S AND IT IS TIME-
   CRITICAL: the D-U-N-S request the day approval lands.** Thirty-day lead, and the name must match
   the registered entity EXACTLY — a mismatch restarts the wait, so it cannot be typed from memory.
   **RECORD THE REGISTERED NAME VERBATIM IN §50.1 THE MOMENT IT IS APPROVED**, including whether
   Georgia issues it as `Do No Harm Company LLC`, `Do No Harm Company, LLC` or otherwise — the
   comma is not cosmetic when an exact match is the requirement.
3. **✅ THE BATTERY IS GREEN ON `33g` — s57, ALL THREE SUITES. STATIC clean · SESSION 21/21 ·
   `BATTERY PASSED` (the aggregate exit code, so all three children returned 0).** The blocker was
   never the build: **Chromium had never been downloaded after a Playwright update**, so
   `behaviour.py` and `session_checks.py` both died on `chromium.launch()` before running a check.
   One command cleared it — `python -m playwright install chromium` (§82.3). **33e, 33f and 33g are
   now covered:** STATIC clean, **BEHAVIOUR 59/59**, **SESSION 21/21** (was 19/19 — §89 added two
   "no unexpected 404" checks to Check 4 at s57), Agent D drift NONE,
   nothing rebaselined — the same results as 33d, counted and not merely exit-coded. *(the s55 entry, for the record:)* Run in **Claude Code** by the owner: STATIC clean,
   BEHAVIOUR 59/59, session checks 19/19, Agent D drift NONE, hygiene clean, nothing rebaselined
   (§82). **THE STANDING ARRANGEMENT: Claude cannot run it (§77.2) — CLAUDE CODE IS THE ROUTE.
   Ask for it before every ship, with `PYTHONUTF8=1` (§82.1).**
4. **✅ CLOSED s57 — THE BLOCK IS PASTED.** `claude/PROJECT-INSTRUCTIONS-s57.md`, datestamped
   `2026-08-08 20:13 EDT · session 57 · live build 33k`. Open since s55 and the cheapest thing on
   the list the whole time. **It now names the three canonical files, the real `docs/` paths, the
   `docs-private\` gitignore caveat, §77.12's opening checklist, `ship`'s gates and the rotate-gate
   rule.** ⚠ **IT CARRIES A STALENESS TEST: if §0's live build is more than a few ahead of the one
   named in the block's footer, say so at the top of the session and offer a fresh one.** The s55
   block ran two builds stale for two sessions because nothing in it *looked* wrong.
   *(the original entry, for the record:)* **PASTE THE PROJECT-INSTRUCTION BLOCK** from
   `claude/PROJECT-INSTRUCTIONS-s55.md`. Until then every session is sent to a filename that does
   not exist and to a `§16` that was never written (§77.9).
5. **Cloudflare Workers Paid ($5/mo)** — a stated pre-event blocker. Free caps CPU at 10ms/request,
   which can break `slim=1` on a large case (§69.1).
6. **THE CASE FILES PLAQUE (§13.4 / §46)** — cheap, high value, still not done. Fourth
   `.btn-plaque` **plus** the red stamp as its own element. **Do not re-apply 28f blindly.**
7. **The Monday cron has never fired** — eleven runs, all manual (§59.3). And **the empty-snapshot
   gate still passes a one-key file as a good backup** — a backup that cannot be trusted is not one.
8. **REPLACE THE PROJECT-KNOWLEDGE HANDOFF** each session, or the next one opens stale.
9. **THE OWNER-ONLY DECISIONS (§14):** the nine volume labels · the app name and seller line ·
   clue-tip duration (open since s19) · the clan crest · the Almanac regrouping · a non-builder route
   to a volume · **whether `SUPER-HANDOFF.md` stays in the public repo.**
10. **Cloudflare Pages migration** — three arguments for it now (§70.5 item 6). Not urgent.

11. **🔴 UNGATED `PUT` ON EVERY OTHER `/kv/` KEY (found s57, §90.3).** PUT is curator-gated for
   `cold:index`, `push:` and now `map:`. **Everything else is open to anyone who can reach the
   Worker** — proven, not inferred: a control `PUT /kv/zztest:s57` returned **200**. A hunter
   holding a case code can write keys for that case; the blast radius has not been mapped. **Rank
   it against §13's security list before the next Worker version, and decide deliberately whether
   it is acceptable — it may well be, since a builder must write their own case. What is not
   acceptable is not having decided.**

### ⚠ SMALL, RECORDED, NOT URGENT
- **`behaviour.py` STILL EXISTS TWICE** — repo root and `test/`, both 18,003 B, byte-identical. The
  root copy is the accident. **Delete it on the next push that touches anything.**
- **✅ s56: MEASURED AGAIN AFTER THE SLIM — **EIGHTEEN**, LISTED FROM `api.github.com`: `.gitattributes` · `.gitignore` · `.nojekyll` · `HANDOFF.md` · `HANDOFF-SPEC.md` · `HANDOFF-HISTORY.md` · `award-card.jpeg` · `battery.cmd` · `claude/` · `docs/` · `icons/` · `index.html` · `j.html` · `manifest.webmanifest` · `og-card.jpeg` · `ship.cmd` · `sw.js` · `test/` (§88). **AUDIT IT EVERY SESSION.** *(the s55 line, for the record:)* **§0's "THE REPO IS TEN TOP-LEVEL ENTRIES" IS WRONG AGAIN. MEASURED s55: FIFTEEN** —
  `.gitattributes` · `.nojekyll` · `SUPER-HANDOFF.md` · `_preview/` · `art/` · `award-card.jpeg` ·
  `behaviour.py` · `hunt-icon-v5.png` · `icons/` · `index.html` · `j.html` ·
  `manifest.webmanifest` · `og-card.jpeg` · `sw.js` · `test/`. It went 5 → 10 → 15 with a doc entry
  only twice. **Audit it every session; it changes without ceremony.**
- **`_preview/` is in the PUBLIC repo** and is scratch. Safe to delete wholesale.
- **`hunt-icon-v5.png` is unreferenced.** Harmless.
- **A per-case email route (v2.6.8)** would need writing and deploying if a single-case send is ever
  wanted (§79.1). **Not requested — do not build it speculatively.**
- **The Ledger nav's month is 7.9px right of card centre** (§78) — measured, shown to the owner,
  deliberately not changed.

---

## 🔴 §77 — THE TOOLING FACTS. READ THIS BEFORE YOU TRY TO MEASURE ANYTHING. (s55)

**Owner's instruction, s55: "concrete everything we have relearned here and put it somewhere you do
not forget it."** This section is that place. It is here, in the canonical document, because a fact
that lives in a chat is gone (§1v) and a fact in a side file is not read. **Every item below was
established by measurement in session 55, most of them after wasting time on the alternative.**

### ✅ 77.0 TWO SCRIPTS EXIST NOW. USE THEM INSTEAD OF PASTING COMMANDS. (s55)

Both at the repo root, CRLF, written because s55 spent a dozen exchanges pasting the same commands
and twice got the shell wrong.

- **`ship "s56: 33f - what changed"`** — the whole push. Shows what is about to go, asks Y/N, stages
  **honouring `.gitignore`** so the Worker sources and `docs-private\` cannot slip in, commits,
  pushes, then **prints local HEAD, origin HEAD, the `index.html` SHA-256 and the buildmark.**
  **⚠ IT DOES NOT PROVE PAGES.** Claude must still hash Pages and probe the Worker before anything is
  recorded as live (§2f). A bare `ship` with no message dates one.
- **`battery`** — the pre-ship battery with **`PYTHONUTF8=1` already set** (§82.1), installing
  playwright/Chromium if absent and warning if `node` is off PATH. **`battery some.html`** tests a
  candidate build.
- **🔴 `.gitignore` EXISTS AT LAST**, and it is what makes `ship`'s `git add -A` safe:
  `worker-v2_*.js` · `docs-private/` · `_to_delete/`. **Before s55 the nine Worker sources sitting at
  the root were untracked by luck, not by rule.**
- **⚠ A MISTAKE MADE WHILE WRITING THEM, LOGGED:** Claude appended `docs-private/` to
  **`.gitattributes`**, which is not the file for exclusions and governs line-ending normalisation.
  Reverted; `.gitattributes` is back to its original 672 B with only `*.cmd text eol=crlf` added.
  **`.gitignore` excludes, `.gitattributes` normalises. They are not interchangeable.**

### 77.1 ✅ THERE IS A LOCAL WEB SERVER. IT IS THE ANSWER TO ALMOST EVERYTHING.

**🔴 s57 — THE PRECONDITION THIS HEADING OMITS: IT IS THE ANSWER ONLY WHEN A BROWSER IS
PAIRED.** The server runs on the OWNER'S machine. **Claude's shell is a separate Linux VM with no
route to it** — `localhost:8000`, `127.0.0.1`, `host.docker.internal` and `172.17.0.1` were all
tried at s57 and all four time out. The server measures nothing by itself; the only thing that can
reach it is a browser ON his machine, i.e. **the Chrome extension, which must be CONNECTED.**
**CHECK `list_connected_browsers` FIRST** — at s57 it returned `[]` while the session was being
told "you have chrome" and "you have port 8000", both true and neither sufficient. Server ✅ plus
extension ❌ is still zero. Ask for the extension by name, not for the server.

**`C:\Users\tony\Documents\Hunt-backups\serve.ps1` serves the live working copy of the repo at
`http://localhost:8000/`.** The owner runs it in a `cmd` window; it logs every request with a status
and a byte count. **VERIFIED s55: `http://localhost:8000/index.html` returned buildmark `32z` — the
real current on-disk build, not a stale copy.**

**🔴 THIS IS THE PRIMARY MEASUREMENT ROUTE. USE IT FIRST, ALWAYS.** Load it in the Claude-in-Chrome
extension and the true build is in a real browser, with real fonts, real CSS and a real DOM, before
anything is pushed. It removes the entire class of problem this document has been fighting for three
sessions: **measuring a build you cannot open.**
**ASK THE OWNER TO START IT AT THE TOP OF EVERY SESSION THAT WILL TOUCH LAYOUT.**
**⚠ Confirm the buildmark it serves before trusting it.** In one s55 log the served `index.html` was
4,009,521 B and 4,010,286 B — **builds `32p` and `32q`** — because those requests were for
`_preview/` copies. **A server on the right port can still hand you the wrong file. Check the mark.**

### 77.2 🔴 WHAT CANNOT MEASURE, AND STOP RE-TRYING IT

- **NO BROWSER IN THE SANDBOX. AT ALL.** `pip install playwright` works and
  `playwright install chromium` downloads 115 MB, then the binary dies on
  **`libXdamage.so.1: cannot open shared object file`**. `playwright install-deps` and `apt-get`
  both fail — **no root, no dpkg lock, and `sudo` is not available.** There is no workaround.
  **DO NOT SPEND ANOTHER MINUTE ON THIS.** ~4 minutes and a 115 MB download were spent proving it.
  **🔴 s57 CORRECTION — THIS IS HALF THE BATTERY, NOT ALL OF IT, AND THE OVERSTATEMENT COST
  THREE SESSIONS OF NOT TRYING.** `test/agents.py` (STATIC — Agents A, B, D and hygiene) needs
  **only `node`, which the sandbox HAS at `/usr/bin/node`.** Claude ran it on `33g` in-sandbox and
  it passed, matching the owner's machine line for line. **RUN STATIC IN THE SANDBOX BEFORE ASKING
  FOR ANYTHING** — it catches drift, unresolved handlers and hygiene for free.
  **What genuinely cannot run here is the BROWSER half** — `behaviour.py` and `session_checks.py`,
  both of which `import playwright.async_api` and launch Chromium. Those two, and only those two,
  need the owner's machine. A build with STATIC green and the browser half unrun ships labelled
  **"BEHAVIOUR and SESSION not run"** — which is a different claim from "battery not run."
- **`file:///C:/...` DOES NOT WORK THROUGH THE CHROME EXTENSION.** `navigate` **silently prefixes
  `https://`**, reports *"Navigated to https://file:///C:/..."* as a success, and the tab never
  leaves `chrome://newtab`. The failure only surfaces on the next call, as
  *"Cannot access a chrome:// URL."* **A NAVIGATION THAT REPORTS SUCCESS IS NOT A NAVIGATION —
  read `location.href` back before you believe it.** This is why 77.1 matters: `http://localhost`
  works where `file://` cannot.
- **`resize_window` DID NOT CHANGE `window.innerWidth`** (stayed 1536 after a 390×844 call).
  **To measure a phone layout, force the container's width in CSS instead** — see 77.3.

### 77.3 🔴 HOW TO MEASURE A PHONE LAYOUT IN THIS APP, EXACTLY

**Measured geometry of the curator overlay, s55 — write these numbers down, they are load-bearing:**
`#curator-ov` has **18px** padding each side · `.tov-card` is `max-width:420px` with **16px** padding
each side. **So at a 390px viewport: card = 354px, and the CONTENT WIDTH IS 322px.**

**🔴 AND THE TRAP THAT ATE A ROUND TRIP: `#curator-list` LIVES INSIDE `#curator-ov.hidden`, SO EVERY
`getBoundingClientRect()` RETURNS 0.** Not an error — a clean, confident set of zeros that reads
exactly like a real measurement, including a cheerful `sameLine:true` (0 == 0). **This is the §11a
class in its purest form. A ZERO IS NOT A MEASUREMENT.** Assert a non-zero width before believing
any rect. The same thing happened a second time later in the session and the zeros were spotted only
because the numbers were implausible.

**THE ROUTE THAT WORKS:** either unhide `#curator-ov` and force `width:390px` on it, or append a
`position:fixed` `.tov-card` of width 354px with 16px padding to `<body>` at a high `z-index`.

### 🔴 77.3a THE ROTATE GATE — IT WILL EAT YOUR FIRST SCREENSHOT EVERY SINGLE TIME

**Owner, s55: "remember and concrete this too — when you render it shows this unless you fix it."**

Open the app in a desktop browser window and you do not get the app. You get **`#ov-rotate`** — a
full-screen `position:fixed;inset:0;z-index:99999` panel reading *"The Agency conducts its business
in portrait only. Kindly right your device before continuing the investigation."* **It is triggered
by `@media (orientation: landscape) and (max-height: 500px)`**, which a normal desktop window
satisfies, so **every screenshot is that panel until it is dealt with.** This cost a wasted
screenshot in s55 and it will cost one every session that does not read this.

**🔴 THE FIX IS ONE LINE, AND IT IS THE APP'S OWN ESCAPE HATCH — NOT A HACK:**

```js
document.documentElement.classList.add('rotlock-off');
```

`html.rotlock-off #ov-rotate{display:none!important}` already exists in the stylesheet. **In the UI
the same switch is the full stop in "Scavenger & Hunt Co." on that panel** — `.rl-dot`, which calls
`toggleRotLock()`. **Do not delete either; they are deliberate.**

**RUN THAT LINE FIRST, BEFORE ANY SCREENSHOT OR RENDER, EVERY TIME.** Two alternatives, both worse:
make the window taller than 500px, or use a `position:fixed` probe card at a higher `z-index` —
**a probe card renders over the gate, which is why the s55 option screenshots worked while the
earlier full-page one did not.** The one-liner is cleaner: it shows the *real* app, not a probe.

### ⚠ 77.3b CLAUDE'S `Edit` TOOL ESCAPES NON-ASCII INTO `\uXXXX` IN THIS FILE

An em dash, `§`, `‹`, `›` or `⚠` typed into an `index.html` edit **lands on disk as the literal
seven characters `—`**, not the character. **Verified s55** — the 32z and 33a code comments both
carry it. **Harmless in a JS comment, and harmless inside a JS string literal** (`"—"` still
renders as the dash). **🔴 BUT IT WOULD BREAK CSS** — `content:"—"` is not the same thing — and
it makes greps for the character fail. **Write code comments in plain ASCII, and if a non-ASCII
character must reach a CSS or HTML literal, verify the bytes after the edit.**

### 77.4 ⚠ THE MEASUREMENT THAT LOOKS LIKE A MEASUREMENT BUT ISN'T

When `.meta` is `flex:1 1 auto`, **`scrollWidth` reports the FLEXED width, not the intrinsic one** —
five different candidate sentences all reported exactly 252px. **To get the true width of a string,
measure a `position:absolute;visibility:hidden;white-space:nowrap` clone of the same class.** The
pass/fail was sound; the number was not, and it must never be quoted as an intrinsic width.

### 77.5 THE OWNER'S SHELL IS `cmd.exe`, NOT PowerShell

`Remove-Item`, `Get-FileHash` and `(Get-Item x).Length` all failed. **Send `cmd`: `cd /d`, `del`,
`certutil -hashfile <file> SHA256`, `findstr /c:"..."`, `type`.** **ONE COMMAND PER LINE** — a
verification block pasted onto the end of a `git push` line produced
`git: 'push(Get-FileHash' is not a git command`, which cost a round trip and looked like a git fault.

### 77.6 🔴 GIT: READ THE REFS, DO NOT INTERPRET THE MESSAGES

**`git add` + `git commit` printing "nothing added to commit" DOES NOT MEAN THE EDITS ARE MISSING.**
In s55 it meant they were **already committed** by an earlier command in the same window, and Claude
told the owner his file had not been written — **a wrong and alarming claim, from a message that was
merely ambiguous.** The refs said it plainly the whole time: `refs/heads/main` had advanced,
`refs/remotes/origin/main` had not.
**ALWAYS READ `.git/refs/heads/main` AND `.git/refs/remotes/origin/main` AS PLAIN FILES FIRST.
`local != origin` means "committed, not pushed" and nothing else.**
**AND `git push` REPORTING SUCCESS IN THE OWNER'S WINDOW IS NOT PROOF THE THING YOU CARE ABOUT WENT.**
In s55 a push succeeded while the handoff commit stayed local — **`origin/main` was one commit
behind and GitHub's copy of the handoff was 320,426 B against 322,949 B on disk.** Fetch and compare.
**⚠ SCREENSHOTS OF A TERMINAL MAY BE SCROLLBACK.** One pasted screenshot showed
`5c254ff..c749c87` and `318503c` — **session-52/53 pushes** — while the session was discussing today's.
**Check the SHAs against the refs before reading a screenshot as current.**

### 77.7 ✅ WHAT DOES WORK IN THE SANDBOX, AND WHAT THE BRIDGE COSTS

- **`curl` WORKS.** §30's "Cowork's sandbox no longer fetches URLs" is **not universally true** —
  raw, Pages, the Worker and the site were all fetched and hashed directly, in one command, in
  seconds. **TRY `curl` FIRST: it is far cheaper than the extension for hashing a surface.**
  **Hash all three surfaces in ONE command and say the result out loud** (§0).
- **The Worker root probe MUST carry `?cb=<timestamp>` and a User-Agent.** With the buster it read
  **`(v2.6.7)`**.
- **Claude's host-path `Edit` writes DO reach the owner's real folder** — proven: the edits appeared
  in his working tree and were committed from it. **Do not doubt this again.**
- **THE BRIDGE CANNOT DELETE.** `touch` succeeds; `rm` returns **`Operation not permitted`**.
  **Test it once with a throwaway file if the mode is ever in doubt — but a probe file you cannot
  delete becomes litter in a PUBLIC repo.** `_deltest` had to be cleaned up by the owner.
  **Prefer reading `.git/refs` to prove the mode; it costs nothing and leaves nothing behind.**
- **THEREFORE: NEVER RUN `git` FROM THE SANDBOX, not even `git status`** — it writes
  `.git/index.lock`, which the bridge cannot remove, stranding a lock that blocks the owner.

### 🔴 77.9 THE PROJECT-INSTRUCTION BLOCK SENDS EVERY SESSION TO TWO THINGS THAT DO NOT EXIST

**This wasted the first move of s55 and it will waste the first move of every session until the
owner edits the instruction block. 🔴 OWNER ACTION: fix these two strings in the project
instructions.**

1. **THE PATH IS WRONG.** The block says the canonical document is **`claude/SUPERHANDOFF.md`** and
   stresses "note the path: it lives under `claude/`, not at the root." **BOTH HALVES ARE FALSE.**
   The file is **`SUPER-HANDOFF.md` — AT THE REPO ROOT, WITH A HYPHEN.** `claude/SUPERHANDOFF.md`
   does not exist; `wc` on it returns *"No such file or directory."* `claude/` holds eleven briefs
   and no handoff. **There is still only one handoff — the instruction just names it wrongly.**
2. **`§16` DOES NOT EXIST.** The block says to read "§0, §13 and §16 before doing anything." **There
   is no §16 in this document.** Read **§0, §13, §65 and §77** instead — §65 is the ranked backlog
   the header points to, and §77 is the tooling.

**✅ THE REPLACEMENT BLOCK IS WRITTEN AND ON DISK: `claude/PROJECT-INSTRUCTIONS-s55.md`.** It holds
the full paste-ready text plus a numbered list of what changed and why. **⚠ `claude/` IS NOT IN GIT**
(§69) — the laptop disk and `Hunt-backups` are its only durable copies. **If a future session finds
the instruction block still naming `claude/SUPERHANDOFF.md` or `§16`, the owner has not pasted it
yet: point him at that file rather than re-deriving it.**

**THE GENERAL LESSON, AND IT IS THE §0.2 CLASS ONE LEVEL UP:** the instruction block is a document
too, **and it is the one document that cannot be corrected from inside the repo.** It goes stale
exactly like §0 did, it reads with total authority because it arrives before anything else, and
**Claude cannot fix it — only the owner can.** **When the instructions and the disk disagree, THE
DISK WINS, and say so out loud rather than hunting for the file the instructions promised.**

### 🔴 77.12 THE FIRST FOUR CALLS OF EVERY SESSION. DO THESE BEFORE ASKING THE OWNER FOR ANYTHING. (s57)

**Owner, s57: "how can i make sure you know you have powershell and chrome access next time we start
a chat and also you access the folder."** He should not have to. Three of the four are Claude's to
do unprompted, and s57 wasted the top of the session asking for two of them.

**1. MOUNT THE FOLDER YOURSELF. DO NOT ASK.** `request_cowork_directory` takes a PATH:
`C:\Users\tony\Documents\Hunt`. It mounts on approval with no folder-picker and no hunting.
**s57 opened by telling him to "Add folder" — wrong, and he had to say so.** Add
`C:\Users\tony\Documents\Hunt-backups` too if the work touches the archive, the clerk or
`serve.ps1`. Access does NOT persist between sessions; re-mounting is one call, not a request.

**2. CHECK CHROME WITH `list_connected_browsers`. NEVER ASSUME EITHER WAY.** It returns `[]` when
the extension is not paired and a device record when it is. **s57 was told "you have chrome" while
it returned `[]` — the statement was true and the extension still was not connected.** If it is
empty, ask for the EXTENSION by name; do not ask for the browser, the server or the port.
🔴 **AND THE SERVER IS NOT A SUBSTITUTE.** `serve.ps1` runs on HIS machine. Claude's shell is a
separate Linux VM: `localhost:8000`, `127.0.0.1:8000`, `host.docker.internal:8000` and
`172.17.0.1:8000` were all tried at s57 and all four time out. **Server ✅ + extension ❌ is zero.**

**3. RUN STATIC IN THE SANDBOX.** `PYTHONUTF8=1 python3 test/agents.py index.html` needs only
`node`, which the sandbox has. Free drift, handler and hygiene check before the owner lifts a
finger (§77.2). Only BEHAVIOUR and SESSION need his machine.

**4. HASH THE THREE SURFACES AND PROBE THE WORKER**, per §0 and the block. `curl` works in-sandbox.

**🔴 5. KILL THE ROTATE GATE AS THE FIRST LINE OF EVERY SINGLE `javascript_tool` CALL, AND PROVE IT
OFF.** Owner, s57, twice: *"you have portrait lock on you keep doing even though its a rule"* and
*"make sure you pull the landscape mode off as a rule."* **It is not enough to do it once per
session — a reload, a navigate or a fresh tab restores it, and s57 lost tabs to exactly that.**

```
document.documentElement.classList.add('rotlock-off');
try{ localStorage.setItem('shco:rotlock','off'); }catch(e){}
```

**AND ASSERT IT, do not assume the class took:** `#ov-rotate` must compute `display:none` AND
`rotlock-off` must be on `documentElement`. Report the boolean in the same result as the
measurement, every time — a screenshot of the portrait panel wastes a round trip and reads, to him,
like the rule being ignored.

**THE SHELL: `cmd.exe`, NOT PowerShell** (§77.5) — `cd /d`, `del`, `certutil -hashfile`, `findstr`,
`type`. **THE ONE EXCEPTION IS `serve.ps1`**, which is launched THROUGH PowerShell from `cmd`:
`powershell -ExecutionPolicy Bypass -File C:\Users\tony\Documents\Hunt-backups\serve.ps1`.
That is not "he uses PowerShell" — it is one command that invokes it.

### 🔴 77.11 A PARTIAL READ OF A LOG IS NOT A MEASUREMENT (s57)

**`python test\\run.py > file 2>&1` PUTS THE PARENT'S OUTPUT AT THE BOTTOM AND THE CHILDREN'S AT
THE TOP.** Redirected, Python block-buffers the parent and flushes it at exit, while each
subprocess writes straight through. **The file reads back inside out.**

**What it cost:** s57 was handed the last five lines of such a file — three suite headers and
`BATTERY FAILED`, with nothing between them — and concluded that **every suite had failed silently
and the harness was broken.** It had not and it was not. The suite output was sitting at the top of
the same file, and the real cause was one line: **Chromium was never downloaded after a Playwright
update.** Three round trips were spent on a diagnosis drawn from the wrong end of a log.

**THE RULE: READ THE WHOLE FILE, OR SAY THAT YOU HAVE NOT.** This is §11a in a new coat — output
that reads exactly like a clean result while being an artefact of how it was captured. **Fixed at
source:** every parent `print` in `test\\run.py` is now `say()` with `flush=True`, so the order is
true whether redirected or not. **The fix does not retire the rule** — any other tool's log can do
the same thing.

### ⚠ 77.10 SMALL ONES, LOGGED SO THEY ARE NOT REDISCOVERED

- **The extension's `zoom` screenshot action timed out** — *"CDP sendCommand Page.captureScreenshot
  timed out after 30000ms"* — on a page where a plain `screenshot` worked immediately afterwards.
  **Prefer a plain `screenshot`; do not retry `zoom`.**
- **`Hunt-backups` was NOT connected this session.** Folder access does not persist. **Ask for both
  folders at the top if the work will touch the archive, the clerk or `serve.ps1`.**
- **`sudo` does not exist in the sandbox** — the error text even suggests adjusting a container
  flag. There is no route to root. Nothing that needs `apt-get` will ever work.
- **🔴 DO NOT RAISE `j.html` AS DRIFT. IT IS CRLF, NOT A DIFFERENCE.** A file-by-file disk-vs-GitHub
  hash sweep at s55 close reported `j.html` mismatched — **disk 1,419 B, GitHub 1,386 B, exactly 33
  bytes across 33 lines.** That is **CRLF on the owner's disk against LF in the repo**, normalised by
  `.gitattributes` on check-in. **The content is identical and git reports the file clean.**
  **A whole-file hash comparison is the wrong tool for text files here** — it will flag every
  CRLF file forever. Compare `git`'s own view, or compare after `tr -d '\r'`. The nine binary and
  LF-normalised files all matched exactly.

### 77.8 THE TWO STANDING RULES FROM THIS SESSION

Both are recorded in full at **§85.6** and are repeated here in one line each because they are the
two the owner asked twice for: **(1) push permission is granted standing — do not ask again, but
still hash before recording "pushed."** **(2) When Claude cannot execute something, the paste-ready
`cmd` block ships in the SAME reply as the blocker, unprompted, with a verification block whose
expected values are stated up front.**

---
