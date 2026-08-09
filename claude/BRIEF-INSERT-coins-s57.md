# Insert for `docs-private\Monetization-Brief.md` — s57

**Why this is a loose file:** the bridge could not write `docs-private\` at s57 (permission denied —
OneDrive lock or read-only attribute). Apply this by hand, then delete this file.

**Where:** in `Monetization-Brief.md`, under `## Rejected, and why — do not reopen`, immediately
before the `**Subscription.**` paragraph.

---

**Selling hint coins. Removed s57 — the owner's words: "lets jsut remove montezation of the
coins,,, i would rather them buy into the play."** Coins are earned only: one per case closed.

Why it was right to drop, beyond the tone:

- **The purchase was surfaced at the moment of failure.** `if(coinBalance()<1){ openCoinShop(); }`
  fired when a stuck player tapped for a hint with an empty purse — frustration straight to a till,
  with no step in between. **That is the pattern behind the kid-spending headlines and the FTC
  settlements with Apple and Google.** The owner spotted it unprompted: "i just dont want parent ire
  if a kid gives up and buys."
- **A consumable IAP is the heaviest compliance category there is** — a consumables SKU, receipt
  validation (already an open item), restore semantics, 15–30% off the top — for the smallest price
  point in the catalogue.
- **It could never have mattered** beside the Charter, Volumes and the Agency licence.
- **It muddled the coin.** Earn-only makes the story one sentence: *a coin for every case you close,
  spend them on hints, your rank stands either way.*

**🔴 RANK WAS NEVER AT RISK AND MUST NOT BE DESCRIBED AS IF IT WERE.** `myCoins()` is a LEDGER, not
a balance — one entry per case closed, and it only grows. Rank reads its length, so a spend cannot
demote anyone. **Any confirmation copy saying a spend costs a promotion is FALSE.** Say the
opposite: *"Your rank stands regardless."*

---

*Also update the `## Free tier` section if it implies coins can be bought, and check `## Store
track` and `## Open items` for a receipt-validation line that existed only for the coin SKU — with
consumables gone, that obligation may go with it.*
