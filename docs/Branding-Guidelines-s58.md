# Branding Guidelines — The Deerstalker / Scavenger & Hunt Co.

*Updated this session: terminology correction ("A Stranger" retired) and one new reusable style pattern noted. Everything else unchanged from prior consolidation.*

## Palette
**ONE RED, s58 (§94.9), owner decision: `#8B0000`.** `--oxblood` was `#8A3324` and is now
`#8B0000`; the CASE CLOSED stamp and the homepage postmark are inked to the same value. **There is
no separate stamp red.** `#ED2939`, `#B92230`, `#9E1B27` and `#82151F` were each tried and passed
over. `#8A3324` was hard-coded in ten places besides the variable — all swept.

Hunter Green `#2E4739` / Deep Hunter `#1E3128`; Bright Brass `#D8AF63` / Antique Brass `#B8863B`; warm parchment & ink; oxblood `#8B0000` for ceremony only. No pure `#FFF`/`#000`. Green is the field; brass is accent/border, never large fills. Textures as CSS vars (`--leather`, `--parch`).

## Type
Playfair Display (agency voice: titles, seals, ceremony) + Special Elite (paperwork voice: case files, clues, labels).
**"Never a third face" was overridden ONCE, deliberately, by the owner at s58 (§94):** Mrs Saint Delafield (OFL),
embedded as `'Delafield'` and subset to `0-9 / B .` (2,220 B), writes the date and initials on the CASE CLOSED
stamp. **It is a stamp-fill face only. It must not appear in UI copy.** Do not "correct" this back — it was asked
for, the rule was quoted to the owner first, and he approved it. Otherwise the two-face rule stands.

## Copy lexicon — UPDATED THIS SESSION
Credentials not Account · Cipher not Password · Case Files not Levels · Minted/Issued not Unlocked · Hunter/Detective not User · **"Undercover Agent" not "A Stranger" or "Guest"** (retired this session — "A Stranger" must not reappear anywhere in-product; the roster and all other UI now consistently say "Undercover Agent," matching the existing splash-page UNDERCOVER state terminology). Courteous, precise, faintly theatrical, no emoji/slang in-product.

## Reusable style patterns (new note this session)
- **`.lic-eyebrow` (Playfair Display, small-caps-style letter-spacing)** is now the standard treatment for "official title" labels that need to echo the splash page's brand font — used both for "SCAVENGER & HUNT CO." on the purchase popup and as the "REGISTRAR" label on the name-entry popup — confirmed as belonging on `#ov-name`, the Registrar.
- **"Join the Ranks"** is now the standing CTA label for the build-entry Registrar step (was generic "Save").
- **`.cold-scroll .cold-tag` style** (Special Elite, `letter-spacing:.12em`, centered, small caps) is the standard for search/filter hint text under a search bar — reused this session for the new "SOME TOWNS SHARE A NAME · ADD THE STATE TO BE SURE" hint on Cold Case Files.

## Motion = ceremony
Period machinery (gears, stamps, wax, sliding drawers). No confetti, bounce, or modern easing. Wheatstone-disk animation is the reference standard.

## Reserved SVG IDs — never repurpose
`wax`, `disc`, `brass`, `arcTop`, `arcBot`, `emblem`.

## Owner decisions — do NOT revisit
- Baked brass plates stay; the blank-bar + live-text redesign is permanently dead.
- One `index.html` only.
- Don't re-run WebP on brass/leather (gain confirmed negligible).
- The Inspector's Charter is a popup/overlay, not a full navigated screen (converted this session).
- Leather/parchment styling was tried on the purchase popup this session and explicitly reverted by the owner — do not reapply that treatment there without new direction.

## Registrar — resolved
**`#ov-name` is confirmed as the Registrar.** With the Purchase Receipt now decoupled from registration, the Registrar's role is unambiguous: name + precinct/zip, above a single green CTA reading **"Join the Ranks."** `#scrollhint-ov` remains the separate first-run welcome/tour dispatch card — a different thing, not the Registrar.
