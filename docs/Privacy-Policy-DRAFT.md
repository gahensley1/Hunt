# Privacy Policy — The Deerstalker (DRAFT)
## Scavenger & Hunt Co. · Do No Harm Company, Savannah, Georgia

*Session-40 revision: THE COMPANY LEDGER IS LIVE. Worker v2.4.1 was deployed this
session, so the paragraph that had been held pending at the foot of this document has been
moved into What We Collect and widened — the ledger counts more than the two events the
original sentence described. A matching line was added to How Long We Keep It, because the
counts are aggregates and are kept indefinitely. Counsel now has three things to review, not
two. The wording below is Claude's draft and awaits owner rewording.*

*Session-38 revision: the photograph retention block is RESOLVED — the owner ruled, and the
paragraph now sits under What We Collect. Two consent checkpoints are live in the app and are
described there. Only counsel review and the public URL remain before publication.*

*Session-34 rewrite. Supersedes the previous edition entirely, which was wrong on four counts:
it stated a flat 90-day retention (the real figure is layered — see below), it twice used the
term for undercover play that was retired from the lexicon, it claimed undercover play never
reaches the server (it does, when the undercover agent joins a hunt), and it stated a two-year
case retirement that has no support in the code. Every retention figure below was read out of live `index.html` 29g and Worker v2.3.3
this session.*

*Before publishing: host at the custom domain, resolve the three PENDING blocks, and have counsel
review — this is a working draft, not legal advice.*

**Effective date:** [DATE]

---

## The Short Version

The Deerstalker is designed to know as little about you as possible. We never ask for your real
name, email address, or phone number. There are no ads, no analytics trackers, and no sale of
data. Game records are pseudonymous, and they delete themselves on a schedule — a case you set
is kept for 90 days from the day you set it, and any loose record untouched for 60 days is swept
away by an automated nightly process.

## What We Collect

**If you play as a registered detective:**

- A **detective name you invent** — a pseudonym. We never ask for or verify your real name.
- A **cipher** we issue (`DET-XXXXXX-XXXX`) that acts as your credential.
- **Game records:** hunts you have built or joined, clue-completion submissions (including
  photographs you attach as proof of a find), finish times, and trophy coins earned.

**If you play as an Undercover Agent:**

An Undercover Agent has no detective name and no cipher, and nothing about them is stored under
a name or a credential. What that does and does not mean, stated plainly:

- **If you never join a hunt, nothing leaves your device.** Browsing the app, reading the Cold
  Case Files, and looking at the map are entirely local.
- **If you join someone's hunt, your finds do reach our server** — they have to, because that is
  how the person who set the hunt sees them and marks them verified. Those records are filed
  against an anonymous device identifier, not against you: no name, no cipher, no contact detail.
  Correspondence you send arrives with no return address, and the app tells the setter as much.

**Counting how the agency's cases are used.** Our server records certain events as they
happen: when the app first issues you a credential, when a case in the Cold Case Files is
looked at, and when a case is joined, finished, or a hint is revealed. Two of these — the
first issue of a credential, and the joining of a case — also carry the approximate city
they came from, as reported by our hosting provider. Nothing finer than a city is ever
recorded, your device is never asked for its location, and no permission prompt is shown.
These are counts of events, not of people: no name, no cipher and no contact detail is
attached to any of them, and they cannot be traced back to a person or joined to a game
record.

We do **not** collect: real names, email addresses, phone numbers, contacts, precise location
tracking, advertising identifiers, or device fingerprints.

Photographs you attach to clue submissions are shared only with the setter of that hunt, for
review. Take them of the objects you found, not of people.

**Cases filed for territory are permanent, and so are the photographs attached to them.** A case
you file for consideration as a Cold Case passes into the permanent record of Scavenger & Hunt Co.
It is kept, along with its clue photographs and its hunters' submissions, for as long as it remains
published in the Cold Case Files, rather than being deleted on the schedule above. You are told
this before you file, and filing is a deliberate act taken twice — once when you tick the box on
the build screen, and again when you confirm on the filing form. Your credentials and particulars
remain your own. If a case is later retired from the archive, it returns to the normal deletion
timing above.

> **PENDING — counsel review only.** The owner ruling behind the paragraph above is settled
> (session 38) and the two consent checkpoints are live in the app. Counsel should confirm the
> wording before publication; no further owner decision is owed.

## How We Use It

Solely to run the game: syncing your credentials and trophies across your devices, showing your
submissions to the setter of a hunt you joined, and showing rankings and finish notifications to
that hunt's participants. Nothing else. No advertising, no profiling, no third-party marketing.

## Where It Lives

Game records are stored with **Cloudflare** (Workers and D1 database), our infrastructure
provider. Cloudflare stores the pseudonymous game data described above on our behalf and does not
use it for its own purposes. Data is transmitted over HTTPS.

**Typography.** All fonts used in the app (Playfair Display, Special Elite) are bundled directly
inside the app itself. We do not load fonts from Google Fonts or any other third-party font
service — nothing about your visit is disclosed to a font provider, and the app works fully
offline.

**Location search data.** The Cold Case Files map's zip and city search uses a built-in dataset of
U.S. ZIP codes and place names (sourced from the U.S. Census Bureau's public Gazetteer Files) to
centre the map when you search. This data is bundled in the app itself, is entirely
one-directional — nothing you type is sent anywhere — and is not used to determine or store your
actual location.

## How Long We Keep It

Different records have different lifespans. The figures below are what the software actually does.

- **A case you set is kept for 90 days** from the day you set it. The app shows you the exact date
  on the case's own page ("Kept until…").
- **Extending a case.** Choosing "Archive" on a case adds one year to that case's life. You can
  see the new date before you confirm it.
- **A case keeps its hunters' paperwork with it.** Submissions, replies and messages belonging to
  a case that is still alive are kept as long as that case is.
- **Loose records untouched for 60 days are deleted** by an automated nightly sweep. This is the
  floor that governs anything not covered by a longer window above.
- **Published Cold Case Files holdings are retained for as long as they remain published** in the
  curated archive. Retiring a case from the archive returns it to normal deletion timing.
- **The usage counts described above are kept indefinitely.** They are running totals — a
  number of visits to a city, a number of times a case was opened — belonging to no
  particular person and to no particular record, so there is nothing in them to delete and
  a quiet month must not erase a busy one.
- **Undercover Agents who never join a hunt leave nothing to delete**, because nothing was
  collected.

Deletion is permanent. There is no backup from which a swept record is restored.

## Your Choices

- **Play with no records at all** — remain an Undercover Agent and do not join a hunt.
- **Play under a pseudonym** — a detective name you invent is never checked against your identity.
- **Walk away.** Because credentials are pseudonymous and inactive records self-delete, simply
  stopping play erases your footprint on the schedule above, with no action required from you.
- **Delete your own cases.** A builder can delete a case, its submissions and its correspondence
  from inside the app.
- **Ask us.** Write to info@scavengerandhunt.com to request deletion of records tied to your
  detective name and cipher.

## Children

The Deerstalker collects no personal information from anyone, including children. Anyone can play
as an Undercover Agent with no data collection at all.

> **PENDING — counsel.** Confirm final age-rating and COPPA language before submission. The design
> intent is that the only identifier we ever hold is a pseudonym the player invents; that posture
> should be verified, not assumed.

## Purchases

Purchases made inside the app (The Inspector's Charter, volumes, coins and seat blocks) are
processed entirely by Apple or Google. We receive confirmation that a purchase occurred — never
your payment details.

> **PENDING — activate only when it is true.** If and when Agency licence payments are taken
> through a payment processor rather than by email enquiry, this section must name that processor
> and say what it receives. As of this draft, an Agency licence enquiry is an email to
> info@scavengerandhunt.com and no processor is involved. Do not publish a processor's name before
> the route is live.

## Changes

We will post any changes to this policy at this page with a new effective date. Material changes
will be noted in the app.

## Contact

Do No Harm Company
Savannah, Georgia
info@scavengerandhunt.com
[WEBSITE URL]

---

> ## PENDING — counsel review of the Company Ledger paragraph. RESOLVED AND LIVE.
>
> The instrumentation described in `SPEC-51.4-instrumentation.md` was deployed as Worker v2.4.1
> in session 40. The paragraph it required is no longer pending: it has been moved into the body
> under **What We Collect**, and a matching retention line sits under **How Long We Keep It**.
>
> It was also **widened** against the original draft, which said only *"when the app first
> connects and when a case is joined."* The ledger records five events, not two — a credential
> being issued, a Cold Case card being looked at, a case being joined, a case being finished and
> a hint being revealed — and the narrower sentence would have understated it. Only the first
> two carry a city.
>
> **What is owed now is counsel's review of the wording, and the owner's own rewording**, not a
> decision about whether to publish it. This is the third item waiting on counsel, with the
> consent flow and the photograph paragraph.

---

### Store-Mapping Notes (delete before publishing)

- **Apple Privacy Nutrition Label:** "Data Linked to You" → none, since the pseudonym is not linked
  to an identity. Declare User Content (photographs, game data) and Identifiers (the app-issued
  cipher and the anonymous device identifier) as collected, App Functionality only, no tracking.
  The absence of any third-party SDK, font service or analytics provider is worth stating if the
  form asks about third-party services generally.
- **The usage counts are a declarable collection.** On Apple's form they fall under Product
  Interaction and Coarse Location, App Functionality only, **not linked to identity and not used
  for tracking** — there is no third-party SDK and no advertising identifier anywhere in the app.
  Coarse Location must be declared even though the client never sends it, because the server
  derives a city from the connection.
- **Google Data Safety form:** collected = user-generated content, app-issued ID, anonymous device
  ID, approximate location, app interactions; shared = with the hunt's setter only, for app functionality; encrypted in transit = yes;
  deletion path = automatic on the schedule above, plus on request, with published Cold Cases
  exempt while published.
- **Retention figure — do not simplify it.** 60 days is the Worker's floor, not the life of a case.
  `Marketing-Brief §3.3` and `Monetization-Brief` were both corrected in session 34 and now agree
  with this document and the code. This document still governs on retention wording.
- Both stores require this policy at a **public URL on the company domain** — a dependency on the
  custom-domain task.
