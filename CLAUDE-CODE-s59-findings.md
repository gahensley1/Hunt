# s59 findings — the cold-case archive (§97/§98): a latent "three views of one state" defect

**Session:** s59, Claude Code, tests only. **Build under test:** `34e` — 4,302,603 B /
`2adb51cf74344de5eb02f155f8b932cec661492d106f8478f69772bd39039357`, commit `f35b49de`, Worker
`v2.6.13`. Disk == origin == Pages == raw (as handed over).

**Nothing was shipped, bumped, pushed, rebaselined, and `index.html` was not touched.** The only
file changed is `test/behaviour.py` (one new test appended). The defect lives in `index.html` and
its fix is recommended below for the owner to apply — I did not, per the session's constraints.

---

## 1. Battery baseline (34e, before my change)

Full three-suite battery, green, matching the owner's word:

```
STATIC     Agent A ok · Agent B 112 handlers, unresolved NONE · Agent D drift NONE · buildmark 34e
BEHAVIOUR  59/59
SESSION    21/21
```

## 2. What I chose to break, and why

Two options were offered. I took **(b) the cold-case filter and map pins (§97)** over (a) the
join-lag Store-call count (§108). Reason: §108 is a documented, accepted *performance* concern;
the cold archive is a *correctness* area where the same class of fault — one piece of state rendered
three ways, and the renderings disagreeing — has already bitten four times (§97 filter drop, §98
precinct list, §91 zip band, §90.11 caption). That is where a player-visible wrong number lives.

## 3. The invariant under test

`openColdCases()` defaults `State.coldQ` to a **near** filter on the hunter's registered precinct
(§98). Three surfaces then all claim to describe "cases near your precinct", and must agree:

| # | surface | drawn by | how it counts |
|---|---------|----------|----------------|
| 1 | `#precinct-bar` "PRECINCT z — N COLD CASES OPEN" | `precinctApply()` | a lat/lon **box**: `|Δlat|≤0.5 && |Δlon|≤0.65` |
| 2 | `#cold-filterbar` chip "SHOWING n IN PRECINCT z" | `renderColdChip()` | `coldFilter()` length |
| 3 | `#cold-list` rows | `renderColdList()` | `coldFilter()` near-mode = `coldNear()`, a **25-mi radius** |

## 4. The defect

**`precinctApply()` counts by a bounding box; the chip and the list count by a radius. They are
different geometries, so they disagree for any case in the 25–34-mile ring.**

The two lines, verbatim from `index.html`:

```js
// precinctApply()  — the banner (a BOX, ~34 mi half-extent, and it ignores e.cat):
const n = idx.filter(e => e.lat!=null
        && Math.abs(e.lat-g.ll[0])<=0.5 && Math.abs(e.lon-g.ll[1])<=0.65).length;

// coldNear()  — the list/chip near-mode (a 25-mi RADIUS; q.mi = PARK_NEAR_MI = 25):
return Math.sqrt(dx*dx+dy*dy) <= q.mi;
```

`±0.5°` latitude ≈ ±34.5 mi and `±0.65°` longitude ≈ ±33–38 mi (latitude-dependent), so the banner's
box reaches ~9 miles further than the list's 25-mi radius. A case in that ring is **counted by the
banner but excluded by the list.**

This is precisely the divergence §98 was written to remove ("the bar said one thing and the list did
another"). §98 aligned the *list* to the precinct but left `precinctApply()`'s original box geometry
in place, so the two agree only while every nearby case happens to sit inside 25 mi — which, on
shipped data, they all do.

### Two symptoms of the one root cause

- **Over-count (filter stays applied).** A precinct with ≥1 real case within 25 mi keeps the
  near-filter active. Add one case at 31 mi: the banner reads **6**, the chip and list read **5** —
  two numbers, stacked on screen, for the same precinct.
- **§98's bug, reintroduced (filter suppressed).** If the *only* nearby case is in the ring
  (nothing within 25 mi), §98's own guard — "never when the precinct has nothing in range" — sets
  `State.coldQ=null`, so the list shows the **whole national archive unfiltered**, while the banner
  still reads "PRECINCT z — 1 COLD CASE OPEN". The banner promises a nearby case the archive does
  not surface as nearby.

## 5. Isolation — one variable at a time (§11d rule 3), and a false start I caught

Driving the real `openColdCases()` against a stubbed `Store` (§11b — writes reach only the in-memory
stub, never the Worker), seeding `cold:index` with the built-ins ± one ring case, reading all three
surfaces:

| scenario | banner (box) | chip (radius) | list | agree? |
|----------|:---:|:---:|:---:|:---:|
| Chicago `60602` — shipped, 5 real within 25 mi | 5 | 5 | 5 | ✅ |
| Savannah `31401` — shipped, 5 real within 25 mi | 5 | 5 | 5 | ✅ |
| far precinct, only case at 31 mi | **1** | — (suppressed) | 11 (all) | ❌ |
| Chicago `60602` + one case at 31 mi | **6** | 5 | 5 | ❌ |

**Recorded because it is the §11d-rule-3 trap in the act:** my first probe reused one page across
scenarios and reported a Savannah divergence (banner 5, list 10). That was a **test artifact** — the
`#cold-q` input still held "60602" from the previous run, and §98's default only fires on an empty
box, so the near-default was silently skipped. The distances proved the Savannah cases are all
0.4–7.4 mi from the precinct (well inside 25 mi), so there is **no** shipped-data divergence. A fresh
page per scenario cleared it. The bug is the *geometry*, not the shipped data.

## 6. Is it player-visible today?

**No — it is latent.** Every shipped cold case (5 Savannah `3104xx`, 5 Chicago `606xxx`) sits inside
25 mi of its own precinct, so banner == list on real data (the two controls above are green). The
divergence needs a curated case 25–34 mi from some hunter's registered precinct — which is ordinary
(territories are added anywhere; a precinct is the hunter's home ZIP), so it is reachable, just not
yet present.

## 7. The check I added, and its teeth (§11d rule 2)

Appended `test_cold_precinct_views` to `test/behaviour.py`. It proves the invariant **both ways**:

- **Controls (green):** Chicago and Savannah → `banner == chip == list`. Proof the check is not
  vacuous and raises no false alarm on shipped data.
- **Defect (red, by design):** Chicago + one case 31 mi north → `banner == applied filter count`
  fails, `got=6 want=5`. That red **is the finding.**

```
Cold archive - precinct banner / filter chip / list are three views of one state (§98)
  PASS  Chicago 60602: banner == list                got=5
  PASS  Chicago 60602: chip == list                  got=5
  PASS  Savannah 31401: banner == list               got=5
  PASS  Savannah 31401: chip == list                 got=5
  FAIL  Chicago 60602 +31mi ring: banner == applied filter count  got=6 want=5
BEHAVIOUR now 64/65  (was 59/59: +5 control asserts green, +1 defect assert red)
```

STATIC and SESSION are untouched and green. I could not turn the red assertion green because the fix
is in `index.html`, which this session must not edit. It goes green the moment `precinctApply()`
counts on the same geometry as the filter.

## 8. Recommended fix (one function, for the owner — I did not apply it)

Make `precinctApply()` count with the **same predicate** the near-filter uses — a 25-mi radius, and
exclude category entries to match `coldFilter`'s base:

```js
// was: a box that also counted category cases
// const n = idx.filter(e => e.lat!=null
//         && Math.abs(e.lat-g.ll[0])<=0.5 && Math.abs(e.lon-g.ll[1])<=0.65).length;
const n = idx.filter(e => !e.cat && e.lat!=null && zipMiles(g.ll,e) <= PARK_NEAR_MI).length;
```

`zipMiles()` and `PARK_NEAR_MI` already exist and are exactly what `coldNear()` uses, so this unifies
the three views on one geometry with no new code. After the change, extend
`test_cold_precinct_views`'s ring assertion from "documents the bug" to a standing guard (it will
pass), so the class cannot regress. **The general lesson is §97's own:** when one piece of state has
three views, they must be computed from one predicate — here two of the three were, and the banner
was the third.

## 9. What I did / did not do

- **Did:** ran the battery; chose target (b); isolated and confirmed the defect against the real code
  with a stubbed Store; appended one test to `test/behaviour.py`; wrote this report.
- **Did NOT:** edit `index.html`, ship, bump the buildmark, push, rebaseline `test/baseline.json`, or
  touch the Worker. No production `Store` key was written (every seed went to the in-memory stub).
