# HANDOFF-SPEC.md — HOW THE APP AND THE SERVICES WORK

### 🔴 THIS IS ONE OF THREE FILES. THE SET IS THE DOCUMENT; NO ONE FILE IS.
### Reference. **Read the section you are about to touch, not the file.** Component behaviour, pricing, the map, the delete path, the website.
### The others: `HANDOFF.md` (state, rules, open work — READ THAT ONE FIRST) · `HANDOFF-HISTORY.md`.
### **SPLIT FROM `SUPER-HANDOFF.md` AT s55 CLOSE. NOTHING WAS COMPRESSED, SHORTENED OR**
### **REWRITTEN — every line was MOVED, and the line count was reconciled to prove it (§4).**
### 🔴 **A RULE LIVES IN EXACTLY ONE FILE. If you find the same rule in two, one is a copy**
### **and copies drift (§0.2, §1w). Delete the copy; do not update both.**

──────────────────────────────────────────────────────────────────────────────

## §6 — ARCHITECTURE

- **Single-file PWA plus four siblings** (§0). Zero external runtime deps except the Cloudflare
  Worker; Google Fonts fully embedded. **No manifest, no service worker** (`serviceWorker` ×0 —
  re-verified in 28e).
- **Assets:** embedded base64 behind named constants. Coins/logo/plaques/stamp are WebP.
  **Brass/leather TEXTURE assets stay PNG/JPEG — do NOT retry WebP.** **Some assets are inline in the
  markup, not only in constants.**
  - **TWO DISTINCT COLD-CASE PLAQUES — do not conflate:** (a) the **home** COLD CASES plate is an
    **inline base64 WebP** inside `openColdCases()` (875×155, `c02fa4a6…`); (b) **`PLQ_COLD`** is a
    separate `const` on the **case-files page** (`adb4f028…`).
  - **Home "CASE FILE RECORD" stamp** is an **inline base64 WebP** (716×72). **The words are pixels —
    grepping returns 0 hits.** **⚠ 🆕 (28) IT CONTAINS *BOTH* THE BLACK "CASE FILE RECORD / ARCHIVE &
    RETENTION." TEXT AND THE RED "FIND CURRENT & OLD CASES HERE" STAMP — ONE IMAGE.** Replacing the
    image removes both. See §46.
  - **🆕 (28) THE HOME PLAQUE FAMILY IS FOUR IMAGES AT ~875×152–157, WebP, 29.9–37.5 KB.** Any new
    plaque should be encoded to match: trim alpha bbox, resize to 875 wide, `quality=85,
    alpha_quality=100, method=6`. **A 2368×448 source lands at 875×156 / 30.7 KB.**
  - **Stamp re-art recipe:** decode; measure the red panel; harvest ink-distress from the asset
    itself; erase the old sub-line; re-render in a **condensed** bold face; keep frame + main line
    byte-identical; encode WebP `quality=85, alpha_quality=100, method=6`; splice by slice-insertion,
    binary mode, `assert count==1`.
  - **⚠ THE COMPRESSION LEVER IS `alpha_quality`, NOT `quality`.** Opaque art: **`quality=88,
    alpha_quality=45`**. **The plaque/stamp family is exempt**, ~30–40 KB.
  - **⚠ EXTRACTING ART FROM AN OWNER SCREENSHOT.** (a) **checkerboard** → key on **saturation**
    (`max-min > 18`), median-filter 7, per-row fill, blur 1.2; (b) **ink on paper** → key on
    **luminance**, `alpha = clip((threshold - lum)/span, 0, 1)`, then `getbbox()` crop. **Always crop
    to a region first.**
  - **⚠ NEVER KEY AN ASSET OUT OF A COMPOSITED IMAGE WHEN A SOURCE EXISTS — ASK FOR THE SOURCE.**
  - **🆕 (28) THE PARCHMENT TEXTURE IS EXTRACTABLE AND IS THE BRAND SURFACE.** `--parch` is an
    896×896 JPEG, 47.9 KB, average `#DECDAE`. `#app` paints it as
    `var(--parch) left top/300px 300px repeat` under a brass top glow and a heavy dark vignette.
    **The vignette is for the 480 px phone frame — do not use it full-width.**
- **Backend:** Worker `deerstalker.tony-13f.workers.dev`, **v2.3 DEPLOYED AND VERIFIED**, fronting D1
  (database `deerstalker-hunt`, table `kv`, binding `DB`); KV sync, credential minting, DELETE,
  `scheduled()` sweep (cron `0 3 * * *`), cold-case sweep exemption. **⚠ SEE §A.**
  - **Known routes:** `GET /kv/<urlencoded-key>`, `PUT` same, `DELETE` same, `GET /list`,
    and `GET /` → a plain-text status page.
  - **v2.3 constants:** `MAX_VALUE = 2 MB` per entry, `MAX_KEY = 200`, `KEEP_DAYS = 60`,
    `/list` **LIMIT 500** (398 keys today — it will silently truncate at 500).
  - **⚠ `MAX_VALUE` IS 2 MB AND HUNT RECORDS CARRY BUILDER PHOTOS INLINE** (§8g). §8j measured 50
    finds ≈ 1.5–2 MB. **A 50-clue case sits near the ceiling; a PUT over it returns 413.** Untested.
  - **A built-in case 404s on the Worker and that is CORRECT.** Built-ins live in the file, not D1.
- Storage tiers: Worker KV → `window.storage` (localStorage) → in-memory `Map`. **⚠ SEE §8j.**
  Case codes **6-digit**. City data: Census 2024 Places Gazetteer, 19,447 state-tagged places.
- 6 built-in cases (`241224 311031 221221 140140 070707 200820`); `BUILTIN_HUNTS` holds **exactly 35**
  (30 shelf + 5 Savannah territory); entries carry `zip`/`city` but **no `state`** — derive via
  `GAZ.zr`. Locked-pack system (`isLocked/ownsPack/grantPack/priceOf/buyPack`, `shco:packs`).
- **⚠ THE 35 CURATED CODES ARE ALL 6-DIGIT AND HEAVILY PATTERNED:** `010101 020214 030317 053105
  060606 070707 093009 112211 122112 140140 151515 161616 171717 181818 191919 200820 202020 210621
  221221 232323 241224 242424 250250 260260 270270 280280 290290 300300 310310 310401 310402 310403
  310404 310406 311031`. See §38 for the migration plan.
- **Credentials / the badge:** `DET-XXXXXX-XXXX`, a bearer cipher minted **once** by `ensureCred()`
  at registration (`CRED_KEY="shco:cred"`, `fmtCred`, `validCred`). **There is no per-rank badge and
  no re-issue.**
- **Security to preserve:** runtime `CURATOR_WORD` + `X-Curator-Token`; SHA-256 device tokens;
  first-writer-wins; **fail closed on auth**; XSS guards — `safeImgSrc()`, `Number()` on roster
  counts, single-quote escaping in `escapeHtml`, `row.onclick=` closures **never inline string
  interpolation**. **Known open violation: `CURATOR_PASS="BAKER221B"` (`BAKER221B` ×1,
  `CURATOR_PASS` ×4) — fix owed (§13.7), and it is now coupled to the delete path (§45).**

---

## §8 — THE COLD-CASE CHART / MAP (`MAP_CHART`)

Hand-styled antique SVG in **equirectangular coords**: `pWorld` (138,951 B), `pUS` (34,475 B),
`pUSb` (12,127 B, **123 subpaths**), graticule, charms. viewBox `0 0 1000 500`. `lonLatToXY`
(`x=(lon+180)/360*1000`, `y=(90-lat)/180*500`); inverse `xyToLonLat`.
- **⚠ DEFS-PAINT GOTCHA:** landmass paths live in the **first `<defs>`**, painted by `<use>` later.
  **Anything ADDED must go into the `<use>` paint sequence — after the `pUSb` `<use>` — NOT among the
  defs.** A group among the defs is valid SVG, passes every check, and **silently never renders.**
- **Landmass paint sequence:** three clip-pathed `<g>` passes: halo `#8A7148` w2.2 op.16; land fill
  `#D6C08D` + coast `#6B5233` w1.1 `vector-effect="non-scaling-stroke"`; borders `#6B5233` w.9 op.8.
- **`SHOW_MAP_NAMES=false`** — no country/state/city text.

### §8a — Cold-case search & pins
`#cold-q` + `coldSearch()`; chip via `renderColdChip(n)`; `clearColdQ()`. `renderColdList()` computes
`coldFilter(_coldIdx)`. Pins in `#pin-layer` (`.cpin`) via `renderColdPins(idx)`. Shelves: Almanac /
Parlour / Grounds (`COLD_CATS`, `coldCatOpen`).
- **`COLD_CATS` labels (verified):** `almanac` → **"The Almanac" / Seasonal**; `parlour` →
  **"The Parlour" / Indoors**; `grounds` → **"The Grounds" / Outdoors**.
- **`coldFilter` modes:** `zip5`, `zip3`, `state`, `city`, `text`, **`near`**. **`const PARK_NEAR_MI=25;`**
- **⚠ `gazAuto(entry)` AUTO-FILLS lat/lon FROM THE GAZETTEER CITY CENTROID** when a case is published
  without a hand-placed pin. Fix = curator re-pin via `_pickCode` / `cgeo-pin`. **All case
  coordinates must be sourced from authoritative references.**

### §8b — Map controls, zoom, park icons, PIN SIZING · **NO CLUSTERING**
- **Zoom metric = `_vb.w`, clamped [0.5, 1000].** Magnification `1000/_vb.w`: world 1×, deepest 2000×.
  `chartGo(lon,lat,w,done)`: reset `w=1000`; `GAZ.c` fallback 220; zip3/state 140; `stateFit` bbox
  [3,1000]; **park tap** + "City, State" 6; full zip / single city / nearest pin 1.5.
  **+/− and empty-map taps step ×2.2.**
- **Layer gates:** `park-layer` at `_vb.w ≤ 320`; `here-layer` ≤ 10; `spark-layer` ≤ 26; `gWater` ≤ 320.
- **PIN SIZING (`chartScalePins`):**
  ```
  const _mag=1000/_vb.w, _pt=clamp(log(_mag/7)/log(2000/7),0,1);
  const _ramp=0.5+0.5*_pt;
  const pinBoost=_vb.w<=0.5?2.0:_ramp;     // HARD STEP at max zoom only
  ```
  `_pinR=0.013*W*pinBoost`. **The owner chose the hard step over a smooth ramp — do not "fix" it.**
- **⚠ CLUSTERING IS GONE — "NEVER-CLUSTER" IS AN OWNER DECISION.** A cluster marker moved with zoom and
  **lied about where a case actually is.** Overlap is resolved **on tap** — `_pinsAt()` returns every
  pin under the finger and `chartTipStack` lists them. **Do not reintroduce clustering OR the
  session-14 pin fan.**
- **CHART-TIP CLAMPING (`_tipPlace`).** `#chart-win` is `overflow:hidden` (~203 px).
- **MAP TAP HANDLER (order matters):** 1. `.cpin` → tip / `openColdDetail`; 2. `.npark` →
  `coldFilterToPlace(...)` + `chartGo(...,min(_vb.w,6), chartParkTip)`; 3. `.spark` → same with `sp2`;
  4. **empty ground:** `if(State.coldQ){ clearColdQ(); chartTipHide(); return; }` else dismiss a tip,
  else zoom ×2.2 toward the point.

### §8c — WATER SYSTEM
Only **`<g id="gWater" display="none">`** remains. **238,569 bytes — the largest single geometry item.**
Two `<path>`s, sepia `#8A7148`: Lakes (~1,639 rings) + Rivers (**314 NA subpaths**). Gate `_vb.w ≤ 320`.
Build gotchas: ring-DP must split closed rings at the farthest vertex;
`tol=clamp(0.011/sqrt(area),0.02,0.08)`; `.16` fill reads as water, a solid `.26` fill reads as a stain.

### §8d — MAP TOUCH / PAN
Pointer Events: `pointerdown` → `setPointerCapture` → `pointermove` → `_dragEnd` (<8 px = tap).
Guard: `if(!_drag||ev.pointerId!==_drag.id) return;`. Scroll parent `.cold-scroll`; `#chart-win`/SVG
carry `touch-action:none` + non-passive `touchmove`→`preventDefault`; `_lockScroll(on)` freezes during
a drag. rAF-coalesced pan. **✅ CONFIRMED FIXED ON iPHONE.**

### §8e — SAVANNAH RIVER / GA-SC BORDER SPLICE
- **Root cause (general):** the river data and the border path `pUSb` are **two independent
  digitizations of the same feature** → a double line.
- **Fix shipped (Savannah only):** replaced `usb[10][0..8]` with the river's exact geometry. New
  `usb[10]` = 17 pts; subpaths unchanged at 123. Splice marker **`M275.35 161.03`** (×1).
- **Splice recipe (reusable):** parse both to absolute polylines; find subpaths sharing a bbox; confirm
  endpoints nearly touch; replace the coincident run in the border's direction; splice by exact
  substring with `assert count==1`, binary mode; **verify world-borders 0 % changed by pixel-diff.**
- **Still divergent:** Mississippi, Ohio, Rio Grande.

### §8f — THE TILE GRID & CLUE LINE
- **Two grids, one renderer.** `#build-grid` (`renderBuild()`) and `#hunt-grid` (`renderHunt()`) both
  use **`tileEl(t,i,mode)`**.
- `tileEl` returns a **`.cell` wrapper** holding the `.tile` plus **one `.cap` line.** `.cap` is
  static, **under** the tile (11px, centred, ellipsis, `min-height:13px`), **always emitted even when
  empty.** `onclick` lives on `.cell`.
- **CLUE LENGTH CAPPED AT 12 CHARS — enforced at BOTH entry points:** `#tile-clue` and `#crop-clue`
  both carry `maxlength="12"` (×2) and both save paths `.slice(0,12)` (×2). Change all four together.
  **Why 12:** measured at 320px (92px tile holds 10–13 chars on one line).
  - **⚠ BOTH PLACEHOLDERS READ `Visible short clue - 12 characters`** (×2, owner copy, plain hyphen).
    **"Description" was rejected.**
- **⚠ THE CLUE COUNT IS CAPPED AT 50.** `.buildbar` reads `<b id="tile-count">0</b> / 50 clues` (×1).
  **"we narrowed to 50 clues and if we promise we deliver."** 100×100 retired.

### §8g — WHERE A CLUE CAN BE SET (two entry points)
1. **Tile editor** (`#ov-tile`/`#tile-clue`) — `openTileEdit(i)` → `saveTileEdit()`.
2. **Crop screen** (`#ov-crop`/`#crop-clue`) — when a builder adds a **photo** tile.
- **⚠ THE CROP OVERLAY IS SHARED WITH THE HUNTER.** `openCrop(dataUrl,resolve)` is called by BOTH the
  builder adding a photo AND the hunter logging a find. **The clue row must never show for the hunter.**
  `openCrop` computes `isBuild`, sets `#crop-cluerow` display, and **clears `#crop-clue` on every open.**
  - **⚠ EVERYTHING BUILDER-ONLY GOES INSIDE `#crop-cluerow`** so the existing `isBuild` gate hides it
    with no second condition. **Never add a builder-only element as a sibling of that row.**
- **THE CROP NOTE.** First child of `#crop-cluerow`:
  `<p class="hint-guide">optional hints/clues can be added later by tapping clues</p>` (×1, owner copy).
- **⚠ `confirmCrop()` ALREADY DOWNSCALES: 320×320, JPEG quality 0.72.**
- **⚠ A BUILDER TILE CARRIES THE PHOTO INLINE:** `{id, type:"photo", src:dataUrl, clue, hint?}`.
  `finishBuild()` does `JSON.stringify(State.build)`, **so the images ride into the D1 hunt record.**
  **🆕 (28) THIS IS ALSO WHY DELETING `hunt:<code>` DELETES THE BUILDER'S PHOTOGRAPHS (§45).**

### §8g.1 — MODAL HEIGHT ON SMALL PHONES (READ BEFORE ADDING ANYTHING TO A MODAL)

**🔴 THE RULE: THE PRIMARY GREEN BUTTON MUST BE VISIBLE WITHOUT SCROLLING ON EVERY SUPPORTED PHONE.**
Owner instruction: *"my phone is bigger than most — the green button needs to be seen on smaller screens."*

- **⚠ THE OWNER'S PHONE IS 390-WIDE OR LARGER AND WILL NEVER SHOW HIM THIS CLASS OF BUG.**
- **MEASURED HEIGHT BUDGET (crop modal, hint folded):** 320×568 → crop square 200, modal 521 ✅ ·
  375×667 → 293 / 614 ✅ · 390×844 → 304 / 608 ✅ · 430×932 → 320 / 624 ✅.
  **Tile editor at the same sizes: 434 / 467 / 476 / 482 — all fit.**
- **THE THREE MECHANISMS THAT MAKE IT FIT:**
  1. **`@media (max-height:620px){ #ov-crop .crop-stage{max-width:200px;max-height:200px} }`** (×1).
  2. **`#ov-crop .modal,#ov-tile .modal{max-height:96vh;overflow-y:auto}`** (×1). **⚠ It was 92vh and
     that was too aggressive. 96vh is the tuned value.**
  3. **`toggleTileHint()` scrolls the modal to the bottom 60 ms after opening the field** —
     `md.scrollTop=md.scrollHeight` (×1).
- **⚠ ANY FUTURE ADDITION TO `#ov-crop` OR `#ov-tile` MUST BE RE-MEASURED AT ALL FOUR SIZES, IN BOTH
  THE FOLDED AND UNFOLDED HINT STATE — 16 assertions.** See §32 `btn.mjs`.
- **🔴 🆕 (28) THE RULE NOW HAS A KNOWN VIOLATION OUTSIDE THOSE TWO MODALS — THE COLD DETAIL CARD.**
  See §13.4. **Measured in 28e: the $1.49 button clears the card bottom at 375, 390 and 430, but on
  320 it sits 137 px below the fold. The card scrolls, so nothing is unreachable.**
  **⚠ AND 375 CLEARS BY ONLY 3 PX** (604 vs 607) — **a longer blurb on any other case tips it over.**
  **The owner accepted this trade twice, knowingly. It is recorded, not re-litigated.**

### §8h — BUILD-GRID TILE REORDER & THE PAN TOUR
- **Reorder:** long-press **400 ms** to lift, slide to place, **build mode only**.
- **`_movePanTour()` + re-arm.** The tour lives OUTSIDE `#build-grid` in a `.gridwrap`, positioned
  from the first `.cell`'s geometry (`--pan`). **Two variants:** ≥2 tiles → **`panFly`**; 1 tile →
  **`panLift`**; 0 tiles → nothing.
  - **⚠ RE-ARM FIX:** `_movePanArm(delay)` re-arms (≤40 tries). **Timing:** slot **1600 ms**, retry
    **350 ms**. **Retirement:** `shco:movetour` set inside `tdUp`'s commit block.
  - **⚠ `shco:mtreset="18"` (×2) — REMOVE BEFORE SUBMISSION (§12).**
- **BUILD-SCREEN TOASTS anchored beside the ＋ tile (`_toastAtAdd`).** Class `.atadd`. Clue tip:
  **"Tap (+) to start adding clues.\nEdit your clue and text by tapping your clue tile"** (5200 ms).
  `MOVE_TIP="Tap & hold to rearrange order"`.
- **⚠ A GESTURE DEMO MUST MOVE THE THING IT IS TEACHING.**

### §8i — THE HUNT-PAGE TOUR, THE LOUPE & THE ENLARGE BEAT
- **`_huntTour`/`_huntArm`:** fires **450 ms** after entering `s-hunt`. Black toast
  **`HUNT_TIP="Tap any clue in any order to document your find!"`** at **`_toastAtRow2`**, **4200 ms**.
  Then lights **non-adjacent** tiles at +600/+1400/+2200 ms. Retires via **`shco:hunttour`**.
- **Second beat:** oxblood **`HUNT_ZOOM_TIP="Tap a clue — you can enlarge the image to study."`** at
  **+3700 ms** on **`#toast2`**, 4600 ms — **gated on `hasPhoto`**.
- **THE ROLLING GLOW** — a **`::before` band at `z-index:-1`** travelling behind the words.
  **The parent needs `position:relative` AND the `::before` needs `z-index:-1`.**
  **⚠ `rollhi` GREP-COUNTS ~40 BECAUSE `scrollhint` CONTAINS THE SUBSTRING.**
  **WHEN IT FIRES:** the **first photo clue opened in each hunt**, keyed **`shco:zoomglow:<code>`**.
- **THE ENLARGE CAPTION (`#clue-zoom`).** Copy **"Tap the image to enlarge"** (×1).
- **THE IMAGE LOUPE (`#ov-loupe`, z 700).** **`object-fit:contain` — never crops.** Pinch (1–4) +
  drag-pan + double-tap 2.4×/1×. ✕ top-left. **Photo clues only.** **BUILD GOTCHA:** `#loupe-stage`
  needs `grid-template-columns/rows:minmax(0,1fr)`.

### §8j — HUNTER-FIND PERSISTENCE (the session-18 data-loss fix — READ BEFORE TOUCHING `Store`)
- **The bug:** `Store.set(key,val,shared)` gates its **localStorage branch on `!shared`**. Builder-hunt
  finds were saved `shared=true` only — one write, no device copy.
- **The fix (three parts):** (S1) `saveHunterSub` writes a **device-local copy FIRST** then syncs;
  (S2) restore **merges both copies, local last**; (S3) **honest toast** on `_durable===false`.
- **⚠ THE QUOTA CEILING.** Photos are 320×320 at q0.72. **50 finds ≈ 1.5–2 MB.** Tight against 5 MB,
  not fatal.
- **🆕 (28) THE SAME HONESTY PRINCIPLE IS VIOLATED IN `purgeCase()` — SEE §45.2.**

### §8k — THE TEST BUILD MARKER (`#buildmark`) — temporary
- A small coloured code at the **bottom of the home page, directly under the © line**. **Separate
  `<p id="buildmark">`** — it must **not** be merged into the © paragraph, which carries the curator
  long-press handlers.
- CSS: `margin:6px 0 0; text-align:center; font-family:var(--type); font-size:11px;
  letter-spacing:1.5px; line-height:1; opacity:.85; user-select:none` + the issue colour.
- **⚠ THE MARKER MUST BE VISIBLY DIFFERENT ON EVERY DELIVERED `index.html`.** Number = session,
  letter = ship-within-session. **Tell the owner the number AND colour on every ship.**
- **⚠ A CARD-ONLY OR ASSET-ONLY DELIVERY DOES NOT BUMP THE MARKER.**
- **⚠ 🆕 (28) AN "UNDO" DOES NOT BUMP IT EITHER.** Re-delivering a previous build must re-deliver the
  **same bytes and the same marker**. See §46.

  | Letter | Colour | Hex | | Letter | Colour | Hex |
  |---|---|---|---|---|---|---|
  | a | Cobalt | `#3B6BA5` | | l | Plum | `#7D4E6B` |
  | b | Ochre | `#C88A2E` | | m | Cerulean | `#2F7D8C` |
  | c | Rose | `#B5566B` | | n | Copper | `#9C5A2E` |
  | d | Amethyst | `#7A5A98` | | o | Mulberry | `#7A3B52` |
  | e | Verdigris | `#4E9A87` | | p | Fern | `#3E7A52` |
  | f | Magenta | `#A8478F` | | q | Coral | `#E0705A` |
  | g | Lime | `#7FA33C` | | r | Wisteria | `#8E7BC8` |
  | h | Rust | `#B4532A` | | s | Aubergine | `#5A3A6B` |
  | i | Indigo | `#4C4C9D` | | t | Ink Blue | `#2B4C7E` |
  | j | Slate | `#4E6478` | | u | Petrol | `#1F5E63` |
  | k | Umber | `#8C6A4A` | | | | |

  Colours are deliberately **outside** the brand palette. **CURRENT DELIVERED: `28e`, Verdigris `#4E9A87`.**
  **Letters a–f are spent for session 28** (f was built then undone). **A continued session-28 ship
  would be `28g` / Lime. A NEW session starts at `29a` / Cobalt.**
  **Do NOT reuse a letter or wrap back to `a` mid-session.**

### §8l — THE TWO-CHANNEL TOAST SYSTEM & TOUR TIMING
- **THERE ARE TWO TOAST NODES.** `#toast` (z 620) and **`#toast2` (z 621)**. **`hideToast2()`** clears
  the second. **WHY:** the owner asked for the oxblood beat to appear **while the black tip is still up.**
- **`_toastUnder(t)`** parks `#toast2` beneath `#toast`'s live rect. **It runs once at fire time and
  never re-runs, so the oxblood STAYS PUT** — an owner decision.
- **⚠ THE `_tipClear` GATE.** `_tipClear(scrId,gridId)` returns **false when `#toast` has class
  `show`**. Fix: **`_tipClear(scrId,gridId,ignoreToast)`** (×3).
- **⚠ THE VERIFICATION LESSON.** 19a was "verified" by calling `toast2()` **directly**, bypassing
  `_tipClear`. **Test the PATH, not the MECHANISM.**
- **TIMING TABLE (measured by 50 ms polling of the real path):** Hunt black `_huntArm(450)` / 4200 ms
  display / **475 ms first paint** · Hunt oxblood +3700 ms / 4600 ms / **4169 ms** · Build clue tip
  400/5200 / **428 ms** · Build `MOVE_TIP` `_movePanArm(1600)` / **5812 ms**. Retry **350 ms**.
- **⚠ THE FLOOR IS THE SCREEN FADE: `.screen.active{animation:fade .28s ease both}`. 400–475 ms is
  deliberately just clear of it. Do not push lower.**
- **⚠ `MOVE_TIP` IS DURATION-BOUND, NOT DELAY-BOUND.** **Offered, still unanswered** (§13).

### §8m — THE CASE READY SCREEN (`#s-share`)
- **Layout:** eyebrow → "(A notification will be sent…)" → **`.caseno` dashed card containing the CASE
  No. label, the 48 px number, AND the `Copy Case Number` ghost button** → `.stack` with **only**
  `Share via Message` → **`.note.arch-note`** → `.note` → rule → Back to Start.
- Card padding **`12px 18px 14px`**; `.caseno .num` `margin-top:2px`.
- **⚠ `class="caseno"` APPEARS EXACTLY ONCE IN THE FILE — HERE.** (Re-verified ×1 in 28e.)
- **Archive note:** *"Review each sleuth's solved cases in the **CASE FILE RECORD** archive on the home
  page."* plus **"Take me there now ›"** (`.archlink`, `goArchive()`).
  **⚠ 🆕 (28) THE OWNER ASKED FOR THIS TO READ "CASE FILES" INSTEAD — IT WAS CHANGED IN 28f AND THEN
  UNDONE WITH THE REST OF 28f. THE REQUEST STANDS AND IS UNBUILT (§13.5, §46).**
- **`goArchive()`** does `go("s-home")` then `setTimeout(openCaseFiles,60)` — **routes via home.**
- **⚠ `display:block` + `width:fit-content` IS WHAT CENTRES THE LINK.**
- **⚠ THIS SCREEN IS WHERE THE RETENTION DISCLOSURE WOULD GO IF ONE IS ADDED AT MINT — see §40.**

### §8n — THE INVITATION DEEP LINK & MESSAGE
- **`joinCase()` handles unregistered hunters itself** — `getMyName()` → `askName(...)` →
  `setMyName` + `ensureCred()` → seat.
- **`joinLink(code)`** (×2). **Origin is DERIVED, never hardcoded:**
  `location.origin + location.pathname.replace(/[^\/]*$/,"")`. **This is why a custom domain needs no
  code change** (§14).
- **`buildShareMsg(code,title)`** (×3) is the single message builder.
  ```
  🔍 You've got a case to crack — "<title>"!

  Tap to join → <joinLink>
  CASE No. 432 554
  ```
- **⚠ iOS PROMOTES A *TRAILING* URL OUT OF THE MESSAGE BUBBLE INTO ITS OWN RICH-LINK CHIP.** **Keep any
  line after the URL and the link stays inline and tappable.** **A comment sits above the `return` in
  `buildShareMsg()` explaining this — do not "tidy" the order back.**
- **⚠ THE CASE NUMBER CARRIES A THIN SPACE (U+2009) BETWEEN THE DIGIT TRIPLES.** (`\u2009` ×1.)
  **Why:** iOS data detectors read a bare six-digit run as a phone number. **Do not remove it.**
- **⚠ `#join-code` IS `maxlength="8"`, NOT 6 (×1), AND THAT IS LOAD-BEARING.** A pasted `374 790` is
  truncated **before** the `oninput` strip runs. **Test the paste path.**
- **Boot handler** (`_deepCase` ×8, `_runDeepLink` ×2): parses `/[#?&]case=(\d{6})/`; after 700 ms
  clears the hash, hides `#scrollhint-ov`, calls `markTourDone()`, `go("s-join")`, fills `#join-code`,
  fires `joinCase()` 260 ms later. **`maybeStartTour` and `showCommish` are gated on `!_deepCase`.**
- **⚠ THE LINK POINTS AT `j.html`, NOT `index.html`** (`j.html#case=` ×1).
- **⚠ FRAGMENTS DON'T REACH A SERVER.** Before store submission move to `/j/NNNNNN` or `?case=NNNNNN`.

### §8o — `j.html`, THE INVITATION CARD, AND THE PREVIEW TRADE
- **The fix:** **`j.html` is 1,386 bytes** — `og:`/`twitter:` tags and a redirect.
- **⚠ `j.html` NO LONGER CARRIES `og:image` (21u).** `twitter:card` is `summary`.
  **THE TRADE:** a link *pasted* into Slack/WhatsApp/Discord no longer shows a card.
- **⚠ THE EXTENSION IS `.jpeg`, NOT `.jpg`.** (`og-card.jpeg` ×3 in `index.html`.)
- **THE CARD IS 1000×1206. RE-MEASURE ALL OF IT IF THE ART CHANGES.**
  | Element | Position |
  |---|---|
  | wordmark | y 69–88 |
  | stag crest | y 120–332 |
  | lozenge | y 349–353 |
  | DISPATCH FROM SCOTLAND YARD | y 369–395, **x 200–800** |
  | "Join the case" | y 433–466 |
  | coin + paw | y 493–862 |
  | instruction line, 3 lines Playfair 600 @48 | y 894–1057, x 193–808 |
  | **ruled blank** | **x 492–795, rule y 1136** |
  | **stamp baseline** | **y 1126** |
- **HOW THE CARD IS REBUILT:** splice, don't re-lay-out. (1) `curl` the pristine original; (2) paste
  `orig[0:884]` at top and `orig[884:980]` at the new bottom; (3) **fill the opened band by tiling
  `orig[470:491]`**; (4) typeset with the extracted Playfair; (5) **re-measure the ruled blank and
  rule, then update the four constants in `stampedCard()`.**
- **⚠ THE FILL SOURCE MUST BE VERIFIED BLANK (shipped corrupt once).**
- **CONTACT SHADOW.** Two passes: `shift 16, blur 17, .40` + `shift 6, blur 5, .34`, clipped at .62.
- **⚠ WHAT THE CARD CANNOT FIX:** Messages only renders a link preview when the message is nothing but
  the URL; blue vs green is decided by the recipient; plain text cannot hyperlink. **Owner's standing
  choice: keep the informative message.**

### §8p — THE BUILD-SCREEN COLD CASE HINT
```
<p class="build-hint">Stuck for clues? <b class="hint-link" onclick="buildBorrowCase()">Take a case
from the Cold Case Files</b> and make it your own.</p>
```
**Only the phrase is the link.** Counts: `hint-link` ×**4**, `buildBorrowCase` ×2.
- **⚠ 🔴 THIS HINT NOW LEADS SOMEWHERE THAT COSTS $1.49, NOT $0.99.** A fresh Charter holder taps it
  and can clone only the three free cases; everything else requires owning a volume. **The friction
  went UP when singles were retired. Flagged, not resolved.**

### §8q — `stampedCard()` — THE PER-CASE INVITATION CARD
- **`stampedCard(code)`** (×2, **`async`**) — fetches `og-card.jpeg` from its own directory
  (`cache:"force-cache"`), draws to canvas, awaits `document.fonts.ready`, writes the code into the
  ruled blank in **oxblood `#8A3324`**, `600 48px "Playfair Display"`, `textAlign:"center"`. Returns a
  `File` (`case-<code>.jpg`, JPEG q0.88) or **`null`** on any failure.
- **⚠ THE CARD IS NOT EMBEDDED AND MUST NOT BE.**
- **THE FOUR CONSTANTS:** `cv.height=img.naturalHeight||1206`; `sx=cv.width/1000`,
  **`sy=cv.height/1206`** (×1); `cx.fillText(String(code), 643.5*sx, 1126*sy)`; font **`60px`**.
  - **⚠ A STALE COMMENT SITS NEAR `genCode` REFERRING TO THE OLD 1000×980 CARD. Ignore it.**
- **`shareCase()` order:** try `stampedCard()` → **only if `navigator.canShare &&
  navigator.canShare({files:[f]})`** call `navigator.share(...)` → else text-only → else SMS composer.
- **⚠ STILL UNTESTED ON HARDWARE.**

### §8r — THE COMMENDATION CARD
- **⚠ THE BUILDER CANNOT RENDER IT.** `myRankName()`, `myCoins()`, `commCount()` and `rankNeeds()` all
  read the **local device's** coin record. **The builder triggers it; the hunter's device renders it.**
- **WHERE IT IS ISSUED — the trigger is in `joinCase()`:** on `prevStatus==="reviewed"`, once per case,
  **only if nothing was rejected.** **The hunter must REOPEN the case for it to fire.**
- **⚠ THE SHARE MUST BE BEHIND A TAP.** `navigator.share` requires a user gesture.
- **Pieces:** `ov-commend` ×3, `openCommend` ×2, `closeCommend` ×3, `shareCommend` ×2, `commendCard` ×2
  (**`async`**), `commendFacts` ×3, `rankFor` ×3.
- **`award-card.jpeg` is BASE ART ONLY.** **When showing this feature to the owner, render a real
  sample and deliver that, never the base art.**
- **⚠ THE VERTICAL RHYTHM IS AN OWNER RULE:** 50 px above the coin, 50 px below.
- **CURRENT CONSTANTS — `award-card.jpeg` is 1000×1150:**
  ```
  cv.height = img.naturalHeight || 1150
  sx = cv.width/1000,  sy = cv.height/1150          (`cv.height/1150` ×1)
  coin  cxx = 500*sx - cwid/2,  cyy = 524*sy,  ch = 300*sy,  cwid = ch*(natW/natH)
  paw   translate(719*sx, 789*sy), rotate(-30deg), ph = 300*sy, alpha .7
  rank 42px #3A332B baseline 906 · name 32px #3A332B baseline 946
  promoted/placement 32px #8A3324 baseline 992 · CASE No. 26px #5E4630 baseline 1030
  progress 23px #5E4630 baseline 1060
  ```
- **⚠ EVERY TEXT LINE IS WIDTH-GUARDED.** A local `line(txt,weight,size,colour,baseline)` shrinks the
  font until `measureText` clears **700*sx**, down to 13px. **This is the pattern to reuse for
  8-digit case numbers (§38).**
- **THE COIN:** `(State.hunt&&State.hunt.cold) ? COIN_CLD : COIN_HERO`.
- **⚠ `COIN_HERO` (×2) EXISTS BECAUSE `COIN_P` IS THE WRONG SHAPE.** `COIN_P` is 616×640 — ratio 0.963.
  The owner's coin is **ratio 1.058**. `COIN_HERO` is 380×359, **+51 KB**. **`COIN_P` is still used
  elsewhere — do not delete it.**
- **✅ RENDER PROVEN IN 22b (headless).** `canShareFiles` is **false in headless** — expected.

### §8s — THE PAW ASSET (`PAW_INK`)
- **Source: the owner's `IMG_0437.png`.** Keyed on luminance (`THR=205, SPAN=70`), **cropped to region
  x 500–900 / y 150–610 first**, tinted `#8A7148`, resized to **260×284**, WebP `quality=87,
  alpha_quality=45` ≈ **20.9 KB**.
- **Verify a paw by component count:** **five blobs — pad ≈11,418 px and four toes ≈4,276 / 4,076 /
  3,977 / 3,854.**
- **Three placements** (`PAW_INK` ×4, `paw-mark` ×7, `done-paw` ×2).

### §8t — THE HIDDEN HINT & THE COIN ECONOMY
- **The owner's framing: "it is a cheat, not necessary to solve the hunt"** — so scarcity needs no
  careful balancing.
- **⚠ `myCoins()` IS A LEDGER, NOT A BALANCE.** One entry per case closed; `myRankName()` reads its
  **length**. **A spend must never remove a ledger entry.**
  ```
  balance = myCoins().length + coinsBought() - coinsSpent()
  rank    = myCoins().length                       (untouched)
  ```
- **Functions (all ×1):** `coinsBought()`, `coinsSpent()`, `coinBalance()`, `spendCoin()`, `buyCoins()`,
  `openCoinShop()`, `hintKey()`, `hintSeen()`, `markHintSeen()`, `renderHintRow()`, `toggleTileHint()`.
  **`const COIN_PACK=5, COIN_PACK_PRICE="$0.99"`.**
- **Keys:** `shco:bought` (×2), `shco:spent` (×2), `shco:hint:<code>:<tileId>`.
- **THE FIELD IS FOLDED AND ADVERTISED — NOT HIDDEN.** It went folded → always-open → folded again in
  session 26. **Why re-folded:** always-open pushed the green button off a 320-wide screen (§8g.1).
  **What makes the current fold different:** the label is **gold (`--brass`)**, it says **"tap here"**,
  and on the crop screen it sits under a note saying hints exist and can be added later.
- **CSS:** `.hint-field{display:none;…}` + `.hint-field.open{display:block}`. `.hint-toggle{…
  border-top:1px solid rgba(184,134,59,.32); … color:var(--brass) …}` — **the brass hairline above it
  is load-bearing.**
- **Toggle copy (×2):** **`+tap here to add hidden hint &#9662;`** — the ▾ is Claude's rendering of
  "gold down", flagged and accepted.
- **Textarea placeholder (×2), owner copy verbatim:**
  `Add a hidden hint for extreme difficult finds. A hunter can spend collected coins to reveal.&#10;Use sparingly.`
  **`rows="4"` — measured; the copy needs 112 px. Do not drop to 3; it clips.**
- **Builder side — BOTH entry points.** Tile editor `#tile-hint`/`#tile-hint-toggle`; crop screen
  `#crop-hint`/`#crop-hint-toggle` **inside `#crop-cluerow`**. **`openCrop` clears the value AND
  re-folds on every open.** `toggleTileHint(pfx)` defaults to `"tile"`.
- **Hunter side.** `#clue-hintrow`, drawn by `renderHintRow(t)`. Shows **"Consult the hint · 1 coin"**
  plus **owner copy: "Stuck? A hint is here if you want it."** **A revealed hint stays revealed.**
  **At zero balance the button opens `#ov-coins`.**
  - **⚠ THE HUNTER-SIDE NUDGE IS DELIBERATELY MINIMAL AND MUST STAY THAT WAY.** **No grid indicator
    and no tour beat** — both rejected as advertising the paid mechanic.
- **⚠ `buyCoins()` ROUTES THROUGH `requirePurchase("coins")` and ends in a TOAST, not the receipt
  ceremony.**
- **✅ PROVEN (headless, real paths):** ledger 10 → Detective Sergeant → all 10 spent → balance 0 →
  **still Detective Sergeant, ledger intact.**

### §8u — THE FINISH-SCREEN HINT NUDGE
- In `finishBuild()`, a case with **zero** hidden hints shows a toast **once per builder** and returns;
  **the second tap files exactly as before.**
- **Copy (owner-approved):** *"No hidden hints on this case. You can add one to any clue if a find is
  especially hard."*
  - **⚠ THE ORIGINAL WORDING WAS PULLED:** *"A stuck hunter will have no way through"* states as fact
    something usually false.
- **Key `shco:hinttip` (×2)** — set before the toast.

### §8v — THE JOIN-PATH PAYWALL GATE
- **The hole it closes:** the cold-case shelves respect `isLocked(e)`, but **`joinCase()` had no
  ownership check at all.**
- **⚠ THIS GATE IS LIVE, NOT DORMANT.** 27 of 30 shelf cases are paid.
- **The gate**, immediately after `const huntCandidate=JSON.parse(raw);`:
  ```
  if(huntCandidate.cold && huntCandidate.paid && !ownsPack(code)){ … err … return; }
  ```
  Message: *"Case No. NNNNNN is filed in a sealed archive."* + a `.hint-link` calling
  **`joinGetPack(code)`** (×1 def), which does `await openColdCases(); openColdDetail(code);`
- **✅ STILL LANDS SOMEWHERE USEFUL.** The detail card offers the **volume**, so the turned-away
  hunter still sees a purchase route. **⚠ BUT ITS MESSAGE STILL SAYS "pack" — §13.9.**

### §8w — THE COLD-SHELF ROW FORMAT
**The row is, top to bottom:** title (`.cn`) → **volume eyebrow (`.volband`)** → place → blurb →
meta line (`.cold-meta`, *"CASE No. 140140 · 12 clues"*). On the right, `.coldside` holds the stamp
then `View sample`.
- **⚠ THE DASHED `CASE No.` PLAQUE AT THE TOP OF THE ROW IS GONE (25c).** The title leads. The case
  number survives in the meta line, **with "· 12 clues" — the owner explicitly asked to keep it.**
- **`.volband`** — `font-family:var(--type); font-size:8.5px; font-weight:700; letter-spacing:1.5px;
  text-transform:uppercase; color:var(--brass); margin:1px 0 3px`. Text is **`v.label`**, i.e. the
  full **"The Parlour, Volume III"** (owner chose the long form).
  **⚠ `text-transform:uppercase` MEANS ANY LABEL PUT HERE RENDERS IN CAPS.**
- **THE STAMP READS `BUY VOL n`.** Locked → **`'BUY VOL '+volumeNo(v)`**, with a bare `BUY` fallback if
  the case is in no volume; free → **`COLD CASE`**; solved → `CASE CLOSED`.
  **🆕 (28) A TEASER ROW EMITS NO STAMP AT ALL.**
  - **⚠ THE STAMP BOX IS A FIXED 84 × 26 px. NOTHING CHANGES THE ROW HEIGHT.** Measured: `BUY VOL 1`
    through `BUY VOL 9` sit on one line (81.8 px intrinsic in an 84 px box); `BUY VOL 10`+ and Roman
    `III`+ wrap to two lines, **exactly as `COLD CASE` (92.5 px) already does.**
  - **⚠ THE NUMERAL IS ARABIC BY OWNER INSTRUCTION** while the eyebrow above it is Roman.
    **Flagged to him and accepted. Do not "harmonise" it.**
- **THE SHELF IS SORTED BY VOLUME:** `coldFilter(_coldIdx).slice().sort((a,b)=>volumeRank(a.code)-volumeRank(b.code))`.
  **Free cases rank −1 and lead the shelf**, then Volume 1, 2, 3. Sort is stable, so order within a
  volume is preserved. **`volumeRank()` reads `VOLUMES.indexOf()`, so adding a row re-sorts for free.**
- **⚠ `.coldrow .caseno` CSS IS DEAD** (§13.10).
- **🆕 (28) `.coldsamp` IS A REUSABLE 84 × 26 PILL** and is now used in three places: the shelf row,
  the detail card's own sample button, and each companion row (§8y).

### ✅ §8x — THE LOCKED-ROW DIM AND THE TEASER STATE — **BUILT IN 28a, EXTENDED IN 28c**

**Before session 28, three CSS rules dimmed every locked row.** With 27 of 30 shelf cases paid, **nine
rows in ten rendered at 60 % opacity and half saturation** — the shopfront looked secondhand and the
brass eyebrow sat near 2:1 contrast.

**🟢 WHAT SHIPPED:**
```css
.coldrow.teaser { opacity:.6; filter:saturate(.5) }        /* was .coldrow.locked */
.coldrow.teaser .cn { color:var(--ink-soft) }              /* was .coldrow.locked .cn */
.volband-soon{font-family:var(--type);font-size:9px;font-weight:700;letter-spacing:1.2px;
              color:var(--ink-soft);margin:1px 0 3px}      /* NEW - no uppercase transform */
```
- **⚠ `.coldstamp.locked{background:var(--tweed-dk)}` STAYED ON `locked` AND MUST.** It is the buy
  stamp's own background, not a dim. A teaser has no stamp, so the rule is irrelevant to it, and
  moving it would have unpainted every `BUY VOL n`. **This is the §0.1(d) lesson.**
- **`coming soon…`** — owner copy, lowercase, U+2026, in its own class because `.volband` is uppercase.
- **A teaser carries NO volume and NO count.** *"really we will have to be responsible for publishing
  them live."* An unnumbered dimmed row promises nothing.
- **A teaser's detail card sells nothing** — it emits `<p class="cold-locknote">coming soon…</p>`
  instead of the buy block. **Scope was extended to cover this deliberately**, because a teaser flag
  without the card guard recreates the 27a dead end.
- **✅ CENSUS PROOF (28e, both viewports):** **30 rows across all three shelves, 0 dimmed, minimum
  opacity 1.00**, stamps reading `COLD CASE` / `BUY VOL 1` / `BUY VOL 2` / `BUY VOL 3`.
- **Nothing carries `teaser:true` today.** The flag is optional by nature — built and unused costs
  nothing.

### ✅ 🆕 §8y — THE COMPANION ROWS ON THE DETAIL CARD — **BUILT IN 28c/28d**

**Owner instruction:** *"list the 2 companion hunts stacked in place of the view sample grid line use
the green button like in the other view that says view sample in the box with description on the right
side"* — then *"put a sample button on the twelve finds of Christmas"* — then *"the sample button for
hunt lives inside the box like this. Logically like the others."*

**WHAT THE CARD NOW EMITS, IN ORDER:**
1. `.cold-file` box — **now `display:flex; align-items:center; gap:10px`** with the text in
   `.cf-wrap{flex:1;min-width:0}` and **the current case's own `.coldsamp` pill inside it on the right.**
2. `<div id="cold-sample">` — the sample grid opens **directly beneath the box**, above the companions.
3. **The companion rows** — one `.cd-comp` per other case in the volume: title + blurb on the left,
   `.coldsamp` on the right. A companion that is not live renders `.cd-comp.soon` with `coming soon…`
   and no tappable pill.
4. The buy block / volnote.

- **⚠ THE NO-VOLUME PATH IS UNCHANGED.** A free case still emits the plain
  `<button class="btn-ghost" id="cold-sample-btn">View the sample grid</button>` and its own
  `#cold-sample`. **`id="cold-sample"` appears TWICE in source — one per branch — and exactly ONCE at
  runtime. Verified.**
- **`.cd-comp` CSS:** `display:flex;align-items:center;gap:10px;background:#fff8ec;border:1px solid
  var(--line);border-radius:12px;padding:10px 11px;margin:6px 0 0`.
- **⚠ THIS IS WHAT PUSHED THE BUY BUTTON BELOW THE FOLD ON 320 — SEE §8g.1 AND §13.4.**

### ✅ 🆕 §8z — THE CREDENTIALS BLOCK SCALE (28e)

**Owner instruction: *"Scale the retrieve detectives credentials and badge and rank. Down 25%"*** —
a red box around the arc text, the crest, the RANK label and the rank plate.

- **`.cred-badge` width `min(282px,100%)` → `min(211.5px,75%)`**, margin `10px` → `7.5px`.
  **The badge is an SVG with a viewBox, so the arcs, the crest, the two dots and the arc text all
  scale with the container automatically** — CSS `font-size` inside a viewBox is in user units.
- **`.rank-stamp.home` every metric ×0.75:** margin `21.51→16.13`, font `30.94→23.21`,
  padding `8.44px 26.83px 8.44px 28.13px → 6.33px 20.12px 6.33px 21.10px`, border `5.63→4.22`.
- **`.rank-stamp.home::before`** (the "RANK" label): top `-30→-22.5`, font `24→18`, tracking `2→1.5`.
- **🔴 AND THE PART THAT NEARLY SHIPPED WRONG — `refreshHomeBadge()` SETS THE RANK FONT SIZE INLINE
  FROM JS CONSTANTS, WHICH OVERRIDE THE STYLESHEET:**
  ```js
  const base=23.21, len=rank.length;                       // was 30.94
  const size = len<=12 ? base : Math.max(11.25, base - (len-12)*0.7125);   // was 15 and 0.95
  ```
  **The CSS edit alone measured as a NO-OP — 24.29 px in both builds.** See §11a #17.
- **✅ A/B MEASURED AGAINST 28d, BOTH VIEWPORTS: badge width 0.750, rank font 0.750, RANK label 0.750.**
- **Side effect, in the owner's favour:** at 390 the rank now fits **one line instead of two**, so the
  block drops 390 → 278 px (0.713). At 320 it still wraps: 360 → 274 (0.760).
- **⚠ THE CREDENTIALS OVERLAY IS UNTOUCHED.** It uses base `.rank-stamp` and `#cred-rank`, verified
  byte-identical. **Only the `.home` variant moved.**

---

## §39 — THE PURCHASE FRAMEWORK — ✅ BUILT IN SESSION 24

**Owner instruction:** *"Add the paywalls to everything with a price. During testing you can agree and
it takes you, but the framework should be there so the store deployment is just a connection made."*

### §39.1 — THE ONE CHOKE POINT
```
requirePurchase(sku, {arg, title, body, cta})  →  "owned" | "granted" | "declined" | "failed"
   ├─ purchaseOwned(sku,arg)  → already entitled? resolve "owned", no overlay
   ├─ opens #ov-buy, awaits the tap
   └─ buyConfirm() → grantEntitlement(sku,arg) → resolve
```
- **`grantEntitlement(sku,arg)` (×1, `async`)** carries the comment **`===== STORE DAY REPLACES THIS
  BODY =====`** (×1). **On store day only this body changes.**
- **Functions (all ×1):** `requirePurchase`, `purchaseOwned`, `grantEntitlement`, `buyConfirm`,
  `buyDecline`, plus `var _buyPending`.
- **`#ov-buy` overlay (×1)** with `#buy-title` `#buy-body` `#buy-go`, `.lic-eyebrow` **THE AGENCY LEDGER**.
- **⚠ BOTH NATIVE `confirm()` DIALOGS ARE GONE FROM THE PURCHASE PATH. Do not reintroduce `confirm()`
  on a priced action.** **⚠ 🆕 (28) NOTE: `confirm()` IS STILL USED ON `deleteCaseAsk()` AND
  `archiveCaseAsk()` — the latter is a priced action and is owed the same treatment (§13).**

### §39.2 — THE GRANT BRANCHES
| SKU | `arg` | grants | ends with |
|---|---|---|---|
| `licence` | — | `shco:lic` | **receipt ceremony** `purchaseGranted()` |
| `coins` | — | `shco:bought += COIN_PACK` | toast |
| `pack` | code | `grantPack(code)` | toast — **🔴 NOW UNREACHABLE, `buyPack` has 0 callers** |
| `volume` | volume id | `grantVolume(id)` | toast |
| `everything` | — | `shco:lic` + `grantVolume(bundleVolume().id)` | **🔴 UNREACHABLE — `bundleVolume()` returns null** |
| `seats` | code | **`Store.set("seats:"+code, n+1, true)` — a WORKER write** | toast |

- **⚠ `seats` IS THE ONE BRANCH THAT MUST STAY SERVER-SIDE.** **Do not "simplify" it to localStorage.**
- **⚠ ONLY THE CHARTER GETS THE RECEIPT CEREMONY.** A full receipt card for a 99¢ item is money-trap
  smell (owner rule, §1).
- **⚠ THE `everything` BRANCH IS DOUBLY DEAD** — no caller, and `bundleVolume()` returns null because
  **no `VOLUMES` row carries `bundle:`** (`bundle:` ×0). **Verified safe:** `purchaseOwned` guards on
  `!!bv` and the grant branch returns `false` on null. **Left in deliberately.**

### §39.3 — ⚠ WHY `ownsPack()` IS THE LOAD-BEARING FUNCTION
**`ownsPack(code)` has EIGHT read sites and is the only ownership question the app ever asks:**
`purchaseOwned` · `isLocked` · `buyPack` · `makeItYours` ×2 · the prize-coin copy · `mycases` ·
**`joinCase()`'s §8v paywall gate.**

**This is why volumes GRANT MEMBER PACKS rather than adding a tier check.** Buying a volume writes each
member code into `shco:packs`, so **all eight gates update with no code change.** **Do not refactor
this into a tier lookup.**

**⚠ `isLocked(e)` IS EXACTLY `!!(e && e.paid && !ownsPack(e.code))`.** Nothing counts or caps free
cases. **A case with `paid:false` is free forever and outside the volume maths entirely (§9).**
**⚠ 🆕 (28) `caseTeaser(e)` IS A SEPARATE, ORTHOGONAL QUESTION AND DOES NOT TOUCH `isLocked`.**

---

## 🔴 §41 — THE VOLUME REGISTRY

**Volumes are DATA, not code.** One array drives the purchase path and every gate.
**Nine shelf-pure rows, three cases each, `price:"1.49"`.**

```js
const VOLUMES=[
  { id:"alm1", label:"The Almanac, Volume I",   sub:"midwinter - three investigations",
    price:"1.49", kind:"volume", shelf:"almanac", months:[12,1],
    codes:["241224","122112","010101"] },
  …nine rows…
];
```
- **Fields:** `id` · `label` *(placeholder copy — owner replaces)* · `sub` *(**never rendered**,
  `v.sub` ×0)* · `price` · `kind` · **`shelf`** *(drives `volumeNo()` and the Desk optgroups)* ·
  **`months`** *(**inert**, nothing reads it; it exists so a rewritten season gate has somewhere to
  read from, and so §38 can randomise codes without losing the calendar)* · `codes`.
- **⚠ `bundle:` AND `season:` ARE GONE.** `bundle:` ×0. `kind==="seasonal"` ×0, `v.season` ×0 — the
  season gate does not exist anywhere and must be **rewritten, not re-enabled**.
- **Helpers (all ×1):** `volumeById`, `volumeOf`, `volumeShort`, `volumeSaving` *(dead)*,
  `bundleVolume` *(returns null)*, `ownsVolume`, `grantVolume`, `buyVolume` (`async`),
  `buyEverything` (`async`, **0 callers**), `renderLicTiers`, `volumeNo`, `volumeRank`,
  **🆕 `volumeReady`**, **🆕 `caseTeaser`**.
- **`volumeNo(v)`** — 1-based index of a volume among **its own shelf's** volumes. Drives the
  `BUY VOL n` stamp. **Almanac, Parlour and Grounds each number from 1.**
- **`volumeRank(code)`** — `VOLUMES.indexOf(volumeOf(code))`, or **−1 for a free/volume-less case**.
  Drives the shelf sort (§8w).
- **🆕 (28) `volumeReady(v)`** — true only when **every** code in `v.codes` is present in `_coldIdx`
  and none is flagged `teaser`. **This is §9 rule 6 in code.**
- **🆕 (28) `caseTeaser(e)`** — `e.teaser || (volumeOf(e.code) && !volumeReady(that volume))`.
  **One helper drives the dim, the `coming soon…` label, the missing stamp and the missing buy button.**
- **`volumeOf(code)` READS THE CASE RECORD FIRST**, then falls back to `VOLUMES[].codes`:
  ```js
  const e=_coldIdx.find(x=>String(x.code)===c);
  if(e&&e.vol){ const v=volumeById(e.vol); if(v) return v; }
  return VOLUMES.find(v=>v.codes.indexOf(c)>=0)||null;
  ```
  **This is the bridge:** the 27 founding cases stay enumerated in the file; anything the curator
  publishes carries `vol:"par2"` on its own `cold:index` entry.
- **`volumeShort(v)`** is `String(v.label).split(", ").pop()` → `"Volume II"`. **ZERO callers.** Dead.
- **TO ADD A VOLUME: append one row.** The shelf eyebrow, the shelf sort, the `BUY VOL n` stamp, the
  detail-card offer and the companion rows all pick it up with no code change. **The Charter tier list
  will not show it, by design (§41.1).**
- **⚠ VOLUME MEMBERSHIP IS ENUMERATED AND FREEZES AT PURCHASE.** `grantVolume()` writes member codes
  into `shco:packs` **at purchase time**. Adding a code to a published volume does **not** reach
  existing owners. **Under append-only (§9) this is correct — but do not "top up" a published volume.**

### 🔴 §41.1 — VOLUMES ARE SOLD ON THE COLD-CASE DETAIL CARD ONLY. THE CHARTER SCREEN SELLS THE CHARTER.

**Owner instruction, session 26, with a red X through the volume and bundle buttons on `#s-licence`:**
> *"We are removing the bundle volume pricing from the inspector charter — mid pop-up is not needed.
> The person buying the charter has no idea about what this means at this point."*
> *"We can offer bundling on the cold case page when we buy there — this is just premature."*

- **`renderLicTiers()` emits exactly ONE button — the Charter — and nothing else.** `Both, and save` ×0.
- **⚠ VOLUME DISCOVERY IS UNAFFECTED, AND THIS WAS VERIFIED, NOT ASSUMED.** `buyVolume` ×2: the
  definition and **the cold-case detail card**.
- **THE PRINCIPLE, NOW AN OWNER RULE: an offer belongs where the buyer already has the thing in front
  of them.** **🆕 (28) THE COMPANION ROWS (§8y) ARE THE SAME PRINCIPLE — the buyer can now see what
  the other two cases in the volume actually are, on the card where the offer is made.**

### 🔴 §41.2 — THE NUMERAL-DRIFT RISK (checked clean in 28e, but check it again)

**Two numeral systems coexist by owner instruction:**

| surface | numeral | source |
|---|---|---|
| shelf eyebrow, detail-card button, volnote, **curator selector** | **Roman** | the **typed** `label` |
| shelf stamp `BUY VOL n` | **Arabic** | **derived** by `volumeNo()` from array position |

- **✅ ALL NINE ROWS AGREE IN 28e** — verified by parsing each label's numeral against `volumeNo()`.
- **✅ THE CURATOR CANNOT CREATE A MISMATCH.** The Desk selector lists rows and returns an `id`.
- **⚠ THE DRIFT RISK IS AT REGISTRY-AUTHORING TIME.** Append a row out of order, or typo the Roman
  numeral, and the stamp will disagree with the label and **nothing will complain.**
- **THE TWO FIXES, NEITHER URGENT:** (1) give each row a `no:` field and derive both from it;
  (2) keep the consistency check in the §32 bootstrap. **Claude's recommendation on record: do (2)
  now, do (1) when the registry moves to D1**, because that is when labels become curator input.

---

## 🔴 §9 — PRODUCT & PRICING — **DECIDED AND BUILT IN SESSION 27**

Old-world detective agency in your pocket. **Invited hunters play free, forever — no account wall, no
ads, no subscription, no energy timer.** Building requires a licence.

### 🟢 THE MODEL AS SHIPPED
| SKU | Price | What |
|---|---|---|
| **The Inspector's Charter** | **$6.99** | the build TOOL — **unlimited** builds. **NEVER bundled.** |
| **A volume** | **$1.49** | **three** curated cases. **Nine volumes today.** |
| Coins ×5 | $0.99 | the hidden-hint currency (§8t) |
| Seat block +25 | $4.99 | per case, to `SEAT_MAX` |
| ~~Single case~~ | — | **🔴 RETIRED. There is no individual pricing.** |

**Full archive today: 9 × $1.49 = $13.41 · $0.50 per case.**
**✅ $1.49 IS CONFIRMED AVAILABLE ON BOTH STORES (session 28, §12).**

### 🔴 THE LOCKED RULES — DECIDED IN SESSION 27, DO NOT REOPEN
1. **A VOLUME IS ALWAYS THREE CASES. $1.49. FOREVER.** **Three won because nine paid cases per shelf
   divides by three with nothing stranded**, and because it sets the authoring rhythm: **a shelf gains
   a volume every three cases.**
2. **VOLUMES ARE SHELF-PURE — NEVER MIXED.** *The Parlour, Volume II* is three indoor cases.
   **The shelf is the anchor**, which is why a volume needs no headline title of its own.
   **⚠ THE "SPREAD THE ANCHORS" RULE IS RETIRED.**
3. **SINGLE CASES ARE NOT SOLD.** **One price, one decision, no arithmetic anywhere in the app.**
   **The cost, accepted knowingly: the cheapest paid entry point moved $0.99 → $1.49.**
4. **ONE FREE CASE PER SHELF IS THE STANDARD — BUT FREEBIES ARE ALLOWED AND UNCAPPED.**
   **A free case is `paid:false` with no volume; it ranks −1 and leads its shelf.**
   **⚠ AND THE DECISION IS PERMANENT: a case released free can never be pulled into a later volume.**
   **A partial batch — case ten with no eleven and twelve in sight — is the natural freebie.**
5. **APPEND-ONLY. BUILD VOLUMES AND ADD TO THEM.** **No volume is ever edited, reshuffled or withdrawn.**
6. **✅ A VOLUME IS NOT SELLABLE UNTIL ALL THREE OF ITS CASES ARE LIVE — BUILT IN 28c** as
   `volumeReady()` (§41). Flagging any one member as a teaser takes the whole volume dark.
7. **THE CHARTER IS OUT OF EVERY BUNDLE** (owner, sessions 25, 26 AND 27).
8. **SHELVES MAY RUN OUT OF STEP.** **The Almanac is expected to run ahead.**
9. **THE BUNDLE RULE IS PARKED, NOT DEAD.** At $1.49 a "rest of the archive" discount would land at
   **$0.99**, the floor. **If it ever returns it must be a RULE — "$X each, or $Y each when you take
   the rest together" — never a hand-picked number.**

### THE CONTENT SPLIT — PARSED FROM `BUILTIN_INDEX`, NOT GREPPED (re-verified 28e)
| shelf | free | paid | volumes |
|---|---|---|---|
| Almanac | 1 | 9 | 3 |
| Parlour | 1 | 9 | 3 |
| Grounds | 1 | 9 | 3 |
| Territory | 5 | 0 | — |

**✅ 27 paid cases · 27 volume codes · 27 unique · 0 orphans · 0 strays.**

**THE NINE VOLUMES (groupings and labels are placeholders; the owner is reworking Almanac):**

| id | label | cases |
|---|---|---|
| `alm1` | The Almanac, Volume I | Twelve Finds of Christmas · Midwinter Watch · New Year Enquiry |
| `alm2` | The Almanac, Volume II | Valentine Affair · Spring Assizes · Whitsun Ramble |
| `alm3` | The Almanac, Volume III | Michaelmas Term · Hallowe'en Enquiry · Feast of Gratitude |
| `par1` | The Parlour, Volume I | Sitting Room Case · Library Investigation · Bureau Drawer |
| `par2` | The Parlour, Volume II | Nursery Case · Wardrobe Enquiry · Landing & Stair |
| `par3` | The Parlour, Volume III | Pantry Inquest · Cellar Business · Attic Investigation |
| `gnd1` | The Grounds, Volume I | Kerbside Enquiry · Market Day · Churchyard Round |
| `gnd2` | The Grounds, Volume II | Common Ground · Water's Edge · Woodland Enquiry |
| `gnd3` | The Grounds, Volume III | Morning Rounds · Dusk Patrol · Night Sky Watch |

- **Almanac is grouped by calendar window** (Dec–Jan / Feb–May / Sep–Nov), which is why `months` exists.
  **⚠ THE OWNER IS REWORKING THIS GROUPING. Whatever it becomes must divide into threes.**
- **Parlour and Grounds are grouped thematically.** **Difficulty climbs I → III on both shelves** —
  flagged to the owner; he did not object.
- **🔴 THE THREE ALMANAC CALENDAR GAPS — APRIL, JULY, AUGUST — ARE THE NATURAL VOLUME IV.**
- **⚠ FREE TIER: `221221` Rainy Day · `070707` Turn About the Grounds · `210621` The Long Vacation,
  plus 5 free Savannah territory cases.**
- **⚠ TERRITORY CASES ARE FREE STRUCTURALLY** — the publishing path hardcodes `paid:false, price:""`.
- **⚠ THE ALMANAC MONTH MAP (INFERENCE from the date-patterned codes, NOT a `season` field):**
  Jan `010101` · Feb `020214` · Mar `030317` · **Apr — none** · May `053105` · Jun `210621` (free) ·
  **Jul — none** · **Aug — none** · Sep `093009` · Oct `311031` · Nov `112211` · Dec `122112` +
  `241224`. **Label this as inference if repeated.**

### MECHANICS (verified)
Build → share a **6-digit** case number → hunters photograph finds → builder verifies → trophy coins +
UK-detective rank; **promotion needs closures AND Cold Case commendations (1/2/3/3/3 ladder).**
**`RANKS` is a six-step ladder:** Detective Constable → Detective Sergeant → Detective Inspector →
Chief Inspector → Superintendent → Assistant Commissioner.
**SEATS:** `HUNTER_CAP=50`, `SEAT_BLOCK=25`, `SEAT_MAX=100`; `caseSeats(code)` =
`min(SEAT_MAX, HUNTER_CAP + blocks*SEAT_BLOCK)`. **Cold cases are seat-exempt.** **Cases cap at 50 clues.**

### ⚠ HOW A HUNTER REACHES A VOLUME
**Only one route: the cold-case detail card** on any case in that volume.
- **⚠ THERE IS NO SHOP AND NO VOLUMES INDEX.** Discovery is entirely per-case. **Owner has not ruled
  on whether it is a gap (§13).**
- **⚠ AND THE VOLUME BUTTON LIVES INSIDE THE `isLocked` BRANCH**, so once someone owns every case in a
  volume that card stops offering it.

---

## 🔴 §43 — THE CURATOR'S DESK: PUBLISHING A CASE

**The Desk is reached by a hidden ~600 ms long-press on the home © line.** `openCurator()` →
`#curpass-ov` password gate → `renderCurator()` → `#curator-ov`.

### §43.1 — HOW THE DESK LISTS CASES
`renderCurator()` reads **`Store.get("mycases")`** — the curator's own case codes — then `coldIndex()`
for what is already published. **⚠ A TEST THAT SEEDS ONLY `hunt:` KEYS WILL RENDER AN EMPTY DESK.
Seed `mycases` too (§11b #7).**
**🆕 (28) THE DESK ALSO HAS A SUBMISSIONS TAB** — `Store.list("submission:")`, builder-sent cases
awaiting territorial review, filed by `subTerrFile()` and published by `subAccept(code)`.

### §43.2 — 🔴 ONE CONTROL DECIDES PAID-NESS
**The "Sell as a pack" checkbox and the free-text price field are GONE** (`cpaid-` ×0, `cprice-` ×0).
They are replaced by a single `<select id="cvol-CODE">`:

```
Free case — no volume, plays free forever
├ optgroup "The Almanac"   → Volume I / II / III — $1.49
├ optgroup "The Parlour"   → Volume I / II / III — $1.49
└ optgroup "The Grounds"   → Volume I / II / III — $1.49
```

**`publishCold()` derives everything from that one choice:**
```js
const _vol=volumeById(cvol value);
const _cat=_vol? _vol.shelf : (ccat value);   // the volume files its own shelf
const _paid=!!_vol;
const _price=_vol? _vol.price : "";
hh.cat=_cat; hh.paid=_paid; hh.price=_price; hh.vol=_vol?_vol.id:"";
```
and the `cold:index` entry carries **`vol:hh.vol||""`**.

- **⚠ WHY THIS MATTERED — A REAL HAZARD, FOUND AND CLOSED IN SESSION 27.** After singles were retired,
  **a paid case with no volume rendered a locked, dimmed row with a bare `BUY` stamp and a detail card
  offering nothing at all.** **Making the volume the sole source of paid-ness makes the dead end
  unreachable.**
- **⚠ THE SHELF SELECTOR (`ccat-`) STAYS** — a free case still needs a shelf but has no volume.
  **When a volume IS chosen the shelf select is ignored.**
- **⚠ THE PRICE IS NEVER TYPED.** It comes from the volume row.
- **✅ PROVEN END-TO-END through the real `publishCold()`, 0 page errors.**

### §43.3 — 🔴 WHAT THE DESK STILL CANNOT DO — THE DECISION OWED
**`VOLUMES` is a hardcoded `const` in `index.html`; the Desk writes to D1 through the Worker.**
A curator can **file a case into an existing volume** but **cannot mint Volume IV** without the owner
pushing a new `index.html`.

**🟢 OWNER DECIDED: OPTION B — MOVE THE REGISTRY TO D1.** Fetched like `cold:index`, so the Desk can
create a volume at runtime. **Append-only makes this safe.**
- **Option A is ALREADY HALF-BUILT** — `volumeOf()` reads `e.vol` first. **That is the bridge.**
- **⚠ WHEN B LANDS, `volumeRank()` MUST STOP USING `VOLUMES.indexOf()`** and read an explicit order
  field, and **§41.2's numeral drift becomes live**, because labels become curator input.
- **⚠ 🆕 (28) AND `volumeReady()` MUST MOVE WITH IT** — it reads `v.codes` from the registry.

---

## §40 — RETENTION — 60 DAYS, AND THE SERVER NOW HONOURS IT

**OWNER DECISION: 60 DAYS.** Implemented in `worker-v2.3.js`, **deployed and verified (§A).**

### The three real defects, all fixed in v2.3
1. **`retentionDays` was never read.** **The Archive +1 year button wrote a field nothing honoured.**
2. **A case in active play could be swept mid-hunt.** `hunt:` records are written by `finishBuild()`
   and curator edits **only**; playing writes `sub:` keys.
3. **Retention was 90.** Now 60.

### Why 60
- **⚠ IT IS NOT A STORAGE FIX.** D1's free tier is 5 GB. **What breaks first is bandwidth on the
  3.7 MB file, then §A (see §42).**
- **✅ PRIVACY IS THE REAL REASON.** These are photographs inside people's homes, often of children's
  parties. *"We keep it for 60 days"* is materially easier to defend than 90.

### Still owed
- **✅ 🆕 (28) THE PRIVACY POLICY NOW EXISTS AND STATES 60 — see §44.** **It is a DRAFT and carries a
  visible DRAFT banner until a lawyer reviews it.**
- **⚠ 🆕 (28) AND IT CARRIES A PUBLISHED-ARCHIVE EXCEPTION**, because accepted territory cases are
  sweep-exempt and are NOT deleted at 60 days.
- **✅ THE MINT-TIME DISCLOSURE IS UNBLOCKED.** Owner has not asked for it.

---

## 🔴 🆕 §44 — THE PUBLIC WEBSITE (scavengerandhunt.com) AND `Marketing-Brief.md`

### §44.1 — The domain — **verified live in session 28**
- **`scavengerandhunt.com`**, apex and `www`, both **200 with a valid certificate**, resolving to
  **50.63.7.245** (GoDaddy, Apache). **20 characters — matches the wordmark exactly.**
- **⚠ HTTP DOES NOT REDIRECT TO HTTPS.** `http://scavengerandhunt.com` returns 200 in the clear.
  **Owner homework.**
- **The page Claude found there was 4,260 B with one line of visible text** — a placeholder, which is
  the category Apple rejects.

### §44.2 — Three site files DELIVERED (not pushed by Claude — the owner uploads them)
**⚠ 🆕 (30) THE SESSION-28 FILES WERE LOST WITH THAT SESSION'S SANDBOX — none were ever uploaded.**

### 🆕 §44.2b — TWO OF THE THREE WERE REBUILT IN SESSION 30 (see §0 for hashes)
- **`privacy.html` (5,364 B)** — rebuilt to the §44/§45.4 spec: parchment tiled `left top/300px 300px`,
  brass top glow, no vignette, `color-scheme:light`, Google Fonts (owner's prior choice), `info@` ×2,
  **visible DRAFT banner**, and the §45.4 sentences **verbatim** (strike-at-any-time · 60-day backstop ·
  published-archive exception · `info@` withdrawal route). It is ~1.8 KB smaller than s28's 7,143 B —
  **the surrounding prose is a session-30 redraft from the spec, not the s28 text. The owner should read
  it before it goes live.** DRAFT banner stays until lawyer review regardless.
- **`parch.jpg` (49,029 B)** — re-extracted from the app's `--parch` var, **byte-count-identical to s28's**.
- Rendered and asserted at 390 and 760: DRAFT visible, 60-day text present, `info@` ×2.

### 🆕 §44.2c — THE HOMEPAGE IS STILL LOST
`site-index.html`'s **copy was owner-approved in s28 and is not preserved anywhere.** Per the
verbatim-copy rule, **do not reinvent it silently** — redrafting it is a task the owner must commission
and review. Until then the domain keeps serving the placeholder.
| File | Size | Note |
|---|---|---|
| `site-index.html` | 4,763 B | **⚠ MUST BE RENAMED `index.html` ON UPLOAD** — named distinctly only to avoid colliding with the app build in chat |
| `privacy.html` | 7,143 B | carries a visible **DRAFT** banner |
| `parch.jpg` | 49,029 B | the app's own `--parch` texture, extracted |

- **They use the app's real brand surface:** the extracted 896×896 parchment tiled at
  `left top/300px 300px repeat` under the same brass top glow. **The app's heavy dark vignette is
  deliberately omitted** — it is tuned for a 480 px phone frame and reads murky full-width.
- **⚠ MEASURED AND REPORTED HONESTLY: the textured background is DARKER than the flat `#EDE4D3` it
  replaced** — luminance 204 vs 229. The owner was told this cut against his "too dark" note and
  **chose to keep it** ("Keep").
- Both pages carry `<meta name="color-scheme" content="light">` to stop browser auto-darkening.
- **Fonts load from Google Fonts**, which sends visitor IPs to Google — slightly at odds with a
  privacy-forward page. **Self-hosting from the app's embedded woff2 was offered and not taken up.**
- **Contact address is `info@scavengerandhunt.com`** (owner's choice, ×2 per file). **The mailbox must
  actually be created** — Apple checks the address resolves.

### §44.3 — What the site still needs before Apple sees it
1. **Create the `info@` mailbox.**
2. **HTTP → HTTPS redirect.**
3. **Lawyer review, then remove the DRAFT banner.**
4. **⚠ Confirm the deletion claim is true before publishing it — see §45.**

### §44.4 — `Marketing-Brief.md` (14,355 B, nine sections) — NEW canonical doc
Positioning · the App Store listing with **verified Jul-2026 field limits (30 / 30 / 100 / 170 /
4,000)** · **what we are NOT allowed to say** · the pricing story · audience and channels · brand
assets · open decisions · a verification split.
- **⚠ THE MOST IMPORTANT SECTION IS §3, THE CONSTRAINTS:** no marketing as a kids' app (a one-way
  door), no police insignia, no claim the server cannot honour, no describing the purchase gates as
  enforced, no monetisation smell.
- **Apple indexes only 160 characters** — name, subtitle, keywords. **The description is not indexed
  and exists to convert.** **Google Play is the opposite and its long description must be written
  separately.**
- **Draft metadata, all Claude's:** name `Scavenger & Hunt Co.` (20/30), subtitle
  `A Victorian Detective's Hunt` (28/30), keywords (89/100), promo (63/170).
- **⚠ TWO OPEN DECISIONS THE MOCKUP SURFACED:** the app name has **10 spare characters** that could
  buy discovery, and **the seller line will read "Do No Harm Co." beneath the brand** because Apple
  derives it from the legal entity and refuses DBAs.
- **App Store screenshots captured from 28d at 430×932 ×3 = 1290×2796** (Apple's 6.9″ size), all three
  passing an empty layer audit. **A 6.5″ set is still owed.** Reference mockup: `appstore-mock.png`.

---

## 🔴 🆕 §45 — THE DELETE PATH: THREE DEFECTS FOUND IN SESSION 28

**How they were found:** the owner asked whether Claude could confirm the privacy policy's deletion
claim "since you were in the webmaster." Claude corrected the premise (§A.1) and read the client code
instead. **The claim was architecturally sound and the implementation was not.**

### §45.1 — 🔴 USER DELETES DEPEND ON THE HARDCODED CURATOR SECRET
```js
async del(key,shared=false){
  if(shared && this.base()){
    const r=await fetch(this.base()+"/kv/"+encodeURIComponent(key),
      {method:"DELETE",headers:{"X-Curator-Token":CURATOR_PASS}});
```
(`X-Curator-Token":CURATOR_PASS` ×2.)
**Ordinary users can delete their own cases ONLY because `CURATOR_PASS="BAKER221B"` ships in a public
client.** v2.3 requires the token on **every** DELETE.
**🔴 THE §13.7 SECURITY FIX WILL BREAK USER-FACING CASE DELETION unless the delete path is handled in
the same change.** This is new and it re-scopes that job.

### §45.2 — 🔴 `purgeCase()` REPORTS SUCCESS UNCONDITIONALLY
```js
try{
  for(const k of await Store.list("sub:"+code+":",true)) await Store.del(k,true);
  for(const k of await Store.list("res:"+code+":",true)) await Store.del(k,true);
  await Store.del("hunt:"+code,true);
}catch(e){}
…
if(!(opts&&opts.silent)) toast("Case "+code+" struck from the record.", 2600);
```
**The errors are swallowed and the toast fires regardless.** A user could be told their photographs
were destroyed while the server copy sat there until the 60-day sweep.
**This is the same class as the session-18 find-persistence bug (§8j) — and it now sits underneath a
published privacy claim.** **The toast must tell the truth.**

### §45.3 — 🔴 NO DELETE GUARD ON SUBMITTED OR PUBLISHED CASES
**The owner asked whether a case submitted for territory can still be deleted. The code says YES —
the opposite of his assumption, and of what it should be.**
- `btn-strike` appears **exactly twice** — once in CSS, once in markup — as an **unconditional** button
  on the roster screen. `deleteCaseAsk()` has **no status check at all**.
- `purgeCase()` removes `sub:`, `res:` and `hunt:` — but **never `submission:<code>` and never the
  `cold:index` entry.**
- **Two consequences:** an orphaned submission sits on the Curator's Desk pointing at a case that no
  longer exists; and an already-accepted case leaves a **published `cold:index` entry pointing at a
  deleted `hunt:` record**, which breaks it for everyone.
- **The fix is cheap:** a status check in `deleteCaseAsk()` before the confirm.

### §45.4 — What the privacy policy was changed to say
- *"You may strike a case from the record at any time. This deletes the board, every hunter's
  submission, and the photographs in it. Whether or not you do, a case is removed within 60 days."*
  **The sweep is the backstop that is genuinely guaranteed.**
- **A published-archive exception** — an accepted territory case is kept as part of the archive rather
  than swept, and nothing is published unless the builder sends it.
- **A withdrawal route** — write to `info@` and we will remove it. **There is no self-service path.**
- **⚠ THE HONEST FIX IS THE CODE, NOT THE SENTENCE.** The owner said so: *"reword but we need to fix
  this."*

---

## 🆕 §46 — 28f WAS BUILT AND THEN UNDONE. READ THIS BEFORE REBUILDING IT.

**What the owner asked for:** replace the home `CASE FILE RECORD / ARCHIVE & RETENTION.` block with a
supplied **CASE FILES brass plaque** (2368×448 PNG), matched to the left/right margins of the three
plaques above; and change the "case archive" reference to "case files".

**What 28f did (3,689,128 B · `8784e335…`):**
- Encoded the art to **875×156 WebP q85/aq100, 30.7 KB** — in family with the other three.
- **Replaced the `.stamp-link` button with a fourth `.btn-plaque`**, which inherited `max-width:340px`,
  the drop-shadow and the 12 px stack gap. **Measured: all four plaques left 34 / right 356 at 390,
  and 34 / 286 at 320 — identical.** `openCaseFiles()` verified to route `s-home → s-cases`.
- Reworded the Case Ready note to *"Review each sleuth's solved cases in **CASE FILES** on the home
  page."* and updated the aria-label and the `goArchive()` comment. `CASE FILE RECORD` ×0.

**🔴 WHY IT WAS UNDONE — almost certainly this:** **the red `FIND CURRENT & OLD CASES HERE` stamp
disappeared.** It lives in the *same image* as the black text (§6), so replacing that image removed
both. Claude flagged it on delivery; the owner replied **"Undo."**

**🟢 THE RIGHT WAY TO REBUILD IT:** put the CASE FILES plaque in as a fourth `.btn-plaque` **and
reinstate the red stamp as its own separate element beneath it.** That was offered and not yet taken up.

**⚠ AND `.stamp-link` CSS BECAME DEAD IN 28f** (×3 rules). It is **live again in 28e**. Do not delete
it while 28e is the base.

---

## §42 — SCALE / "LIKE POKÉMON GO" (analysis only)

- **✅ THE UGC MAP PIPELINE ALREADY EXISTS** — the territory submission flow. **The bottleneck is that
  the owner is the only curator, not the code.**
- **❌ NOT WORTH CHASING:** server-authoritative real-time state, AR, persistent world. **The genre to
  own is "a detective agency where people photograph what they find."**
- **WHAT BREAKS FIRST, IN ORDER:**
  1. **The 3.7 MB single file with no service worker.** GitHub Pages soft ceiling **~100 GB/month ≈
     27,000 loads. ⚠ UNVERIFIED.**
  2. **§A's open `PUT`** — survivable at 130 users, catastrophic at 130,000.
  3. **D1 free-tier read limits.**
  4. **Curation throughput.**
- **⚠ "4 SEASONAL DROPS A YEAR MEANS SCALING FOR YEARS." Rotation is not production.**

---

## §12 — STORE TRACK
- **Monetization:** free download; building behind non-consumable IAP. **Current gates are client-side
  only — preview, not enforcement.** Apple requires a visible "Restore Purchase" button. Enroll in
  both 15% small-business tiers early.
- **Sequence:** entity/domain/D-U-N-S → finalize Privacy Policy → **Play first** (TWA/PWABuilder),
  **Apple second** (expect Guideline 4.2 pushback).
- **⚠ STAY OUT OF THE KIDS CATEGORY — a decision, see §37.1.**
- **⚠ PRE-SUBMISSION CHECKLIST — remove all temporary test aids:** (1) `#buildmark` (§8k);
  (2) `shco:mtreset` scaffolding (×2, §8h); (3) `shco:zoomglow:<code>` keys (§8i); (4) other debug
  scaffolding. **`shco:hinttip` (§8u) is a real retirement key — KEEP it.**
- **⚠ ALSO PRE-SUBMISSION:** move the deep link off the `#case=` fragment; add
  `apple-app-site-association` + `assetlinks.json`; update every absolute `og:image` URL when the
  custom domain lands. **AND SET THE RETENTION NUMBER (60) IN THE PRIVACY POLICY — ✅ DONE (§44).**
- **✅ 🆕 (28) `$1.49` IS CONFIRMED AVAILABLE ON BOTH STORES.** Apple offers **900 price points from
  $0.29 to $10,000, in $0.10 increments below $10** — the old forced `.99` endings are gone. Google
  Play uses **free-form pricing with automatic local-currency conversion**, no fixed tiers.
  **Nine `$1.49` non-consumables plus the Charter, coins and seat blocks. The old $0.99 single-case
  SKU is retired and must not be registered.**
- **✅ 🆕 (28) METADATA LIMITS VERIFIED:** name **30**, subtitle **30**, keyword field **100**,
  promotional text **170** (editable without a build), description **4,000** (**not indexed by Apple**).
  **Apple indexes only 160 characters total. Google Play's long description IS indexed.**
- **✅ 🆕 (28) APPLE ORG ENROLMENT REQUIREMENTS VERIFIED:** a **legal entity** (corporation, LLC or LP —
  **DBAs, trade names and sole proprietorships are refused**); a **D-U-N-S registered to it**
  (free, ~5 business days to 2 weeks, then up to 2 more for Apple to receive it); a **work email on the
  organisation's own domain**; and a **publicly available functional website on that domain** —
  registrar placeholders and social pages are rejected. **The legal name must match the D-U-N-S record
  and the enrolment form EXACTLY.**
- **⚠ STOREKIT UPGRADE PRICING IS UNVERIFIED.**

---

## §36 — OPEN DESIGN THREADS
### §36.1–§36.2 — ✅ CLOSED (21a–21f).
### §36.3 — ✅ BUILT — the commendation card (§8r). **Render proven; hardware unproven.**
### §36.4 — ✅ BUILT — the hint coin (§8t), both entry points, re-shaped twice in session 26.
### §36.5 — ⚠ RETIRED — the 100×100 requirement. **Treat 50 as the number.**
### §36.6 — the age sweep (measured on 23c at 390×844).
- **5** — cannot self-serve; **a co-play age.** **8** — can play, cannot build; blocker is vocabulary.
- **11 / 14 / 50** — no findings. **80** — the real gap: §13.18.
### §36.7 — **the free tier rests on territory cases**, of which there are **5, all in Savannah.**
**A new user far from Savannah sees a thin free tier.**
**THE COUNTER-LEVER EXISTS:** free cases are uncapped and orthogonal to volumes (§9 rule 4), so a
second freebie per shelf is a one-publish decision. **The cost is that every extra freebie is one less
reason to buy Volume I.**
### §36.8 — **the seasonal premium has been given up**, twice over.
**⚠ The gate that enforced it no longer exists in the code (§41).**
**BUT SHELF-PURE GIVES IT BACK CHEAPLY:** an Almanac volume can carry a month window without touching
Parlour or Grounds, which is what `months` is for.
### §36.9 — FACE ID / WebAuthn ON THE CURATOR'S DESK — design thread, NOT built
- **⚠ FACE ID NEVER YIELDS A SECRET.** The Secure Enclave returns a yes/no assertion, not a string.
  **The Worker needs a value to compare, so a token always still exists.**
- **THE USEFUL SHAPE:** keep the curator word in the device keychain and **require a biometric
  assertion to release it.**
- **⚠ WebAuthn IS ORIGIN-BOUND. Moving to the custom domain INVALIDATES every enrolled credential.
  Therefore: domain first, then this.** **⚠ IT IS ALSO DEVICE-BOUND — the typed path can be hidden,
  never deleted.**
- **ORDER: custom domain → §13.3 `CURATOR_WORD` → rotate the secret → biometrics on top, if wanted.**
### §36.10 — SHOULD THE BUILDER SEE HOW MANY CLUES CARRY A HINT?
The builder has **no at-a-glance view** of which clues carry hints. **⚠ A TILE MARK WAS ALREADY
REJECTED ON THE HUNTER SIDE as advertising the paid mechanic.** On the *builder's* grid the same mark
is authoring information — **a real distinction, but the owner has not been asked. Do not build it
unprompted.**
### §36.11 — DOES A NON-BUYER EVER SEE THE SHAPE OF THE ARCHIVE?
Nine volumes exist and there is **no index of them anywhere**. **🆕 (28) THE COMPANION ROWS NARROW THIS
BUT DO NOT CLOSE IT** — a buyer on a card now sees the other two cases in *that* volume, but still has
no view of the archive as a whole. **⚠ §41.1 is an owner rule and a "volumes index" is close to a shop.
Ask before designing.**

---

## §37 — CHILDREN, PURCHASES, AND WHAT WAS DELIBERATELY NOT BUILT
### §37.1 — The purchase-gate question (settled)
**DECISION: stay out of the Kids Category, add no in-app gate, keep purchasing.**
- Kids-category apps must not include purchase opportunities unless behind a parental gate, and once
  customers expect that compliance the app must keep meeting it — **a one-way door.** **This constrains
  birthday-party marketing copy: describe families and parties, don't market it as a kids' app.**
  **🆕 (28) THIS IS NOW WRITTEN INTO BOTH `Marketing-Brief.md` §3 AND the published privacy policy's
  Children section.**
- **A math gate is theatre.** **An install-time age check is worse than nothing.**
- **✅ THE PLATFORM ALREADY DOES THE STRONG VERSION.** StoreKit and Play Billing require biometric or
  password auth on every purchase; Family Sharing's Ask to Buy routes a child's request to the parent.
- **Owner's closing line: *"since no one is paying in testing we can let the StoreKit handle."***
### §37.2 — The commendation Notify button
**Rendering must stay local** (§8r) or the numbers go stale. **Agreed design:** a "Notify" button on the
builder's review screen sending a short message through the share sheet. **See §13.17.**

---

## §38 — THE 8-DIGIT CASE-NUMBER MIGRATION (agreed, not built)
**Why.** Odds a random guess hits a live case:

| live cases | 6 digits | 7 digits | 8 digits |
|---|---|---|---|
| 100 | 1 in 9,000 | 1 in 90,000 | 1 in 900,000 |
| 1,000 | 1 in 900 | 1 in 9,000 | 1 in 90,000 |
| 10,000 | **1 in 90** | 1 in 900 | 1 in 9,000 |

At 10,000 cases on 6 digits, **even with a 20-per-minute limit a scanner lands ~320 live cases a day.**
**8, not 7** — 7 still leaves ~32/day. **Collisions are NOT a concern:** `genCode()` tries 40 times.

**OWNER DECISION: migrate ALL cases, including the curated ones** — *"we curate those."*
**⚠ CURATED CODES SHOULD BECOME RANDOM, NOT PATTERNED.**
**⚠ BUT THE ALMANAC'S DATE-PATTERNED CODES ARE CURRENTLY THE ONLY MONTH SIGNAL** —
**`VOLUMES[].months` EXISTS AND IS THE PLACE TO CAPTURE IT BEFORE RANDOMISING.**

**Touch points (all must move together):**
1. `genCode()` — range and length.
2. `joinCase()`'s `if(code.length!==6)` guard and its error copy.
3. The boot deep-link regex `/[#?&]case=(\d{6})/` (§8n).
4. The thin-space formatter `^(\d{3})(\d{3})$` → 4+4 — **keep the U+2009.**
5. `#join-code` `maxlength="8"` → **10**.
6. **`stampedCard()`'s four constants** (§8q) — eight digits at 60px in a **303 px** blank almost
   certainly overflows. **Reuse the commendation card's width-guard `line()` pattern (§8r).**
7. `BUILTIN_HUNTS`'s 35 keys plus any `BUILTIN_INDEX`/territory references.
   **⚠ AND `VOLUMES[].codes` — NINE ARRAYS, NOT TWO.**
8. Any display formatting of a case number — Case Ready `.caseno`, cold detail, roster, **the shelf
   row's `.cold-meta` line, and 🆕 the companion rows' fallback title `"Case No. "+c` (§8y).**

---
