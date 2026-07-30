# test/ — pre-ship battery

Run before every ship. Nothing ships on a red battery.

```bash
python3 test/run.py                    # tests ./index.html
python3 test/run.py path/to/index.html # tests a candidate build
```

Requires `node` (Agent A) and Python `playwright` with Chromium
(`pip install playwright && playwright install chromium`).

## What runs

**`agents.py` — static**

| Agent | Checks |
|---|---|
| A | every inline `<script>` passes `node --check` |
| B | every `onclick="fn("` resolves to a defined function |
| D | HTML tag balance, **measured as drift from `baseline.json`** |
| Hygiene | no `console.log`, no `http://`, reports `CURATOR_PASS` and the build marker |

**`behaviour.py` — headless Chromium**

- `purgeCase()` reports honestly — returns false on a server refusal and **keeps** the case
- `deleteCaseAsk()` refuses deeded and cold cases, allows ordinary ones
- the territory deed checkbox gates the File button, resets on reopen, is tappable by its text
- both reference viewports (390×844, 320×568) boot without a page error

## Two rules that are not negotiable

**1. Tests never write to the live Worker.** Every test calls `_boot()`, which installs a
`Store` stub pointing at `https://STUB.invalid` before anything else runs. There is no path
in `behaviour.py` that reaches the network. If you add a test, call `_boot()` first.

**2. Agent D is baseline-relative on purpose.** The file carries long-standing benign
imbalances (`span -2`, `g -1`, `li -1`) plus false hits where JS comparisons like `a<b` look
like tags. Chasing them to zero is wasted effort; what matters is that a build adds none.
Regenerate the baseline **only** when you have deliberately changed markup structure:

```bash
python3 test/agents.py index.html --write-baseline
```

## Prove the suite still bites

A battery that never fails is worth nothing. Periodically re-introduce a known defect in a
scratch copy and confirm the suite goes red. The `purgeCase` failure path is the reference
case — it is the defect that actually shipped, and it survived until someone happened to
read the function.
