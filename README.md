# API Scanner

A security scanner for vibe-coded apps (built with Lovable, Bolt, Cursor, Supabase, Firebase, etc.).
It looks for API keys and secrets accidentally left in code, checks Supabase RLS policies, and more.

**Status: 🚧 Work in progress — not production-ready yet.**

## Why this exists

AI coding tools ship fast, but they often leave the same kinds of security gaps behind
(exposed API keys, database rules left wide open, no rate limiting). This project is me
building a scanner that catches those specific, known patterns — and testing it honestly
against benchmarks of planted secrets, instead of just assuming it works.

## What it can do right now

- Searches for API keys using known provider patterns (Stripe, OpenAI, Google/Firebase, AWS, GitHub, Slack, Private Keys, npm)
- A generic check for secrets with no known format (variable named "key"/"secret"/"password"/"token")
- Decodes base64-encoded secrets and re-checks the decoded value
- Flags likely split/concatenated secrets (a bare provider prefix stored alone in a string)
- Uses Shannon entropy to tell real random secrets apart from placeholder values like `sk-xxxx...xxxx`
- Two scan modes: a live website (give it a URL) or a local folder

## Three benchmarks, measured honestly

| Benchmark | Result | What it tests |
|---|---|---|
| `benchmark/` (11 cases) | **100%** (11/11), 0 false positives | Baseline: one secret per known format, one generic case, one placeholder decoy |
| `benchmark2/` (24 cases) | **67%** (16/24), 0 false positives | Harder: new provider formats not yet supported, 3-way splits, double-encoding, hex encoding, case variants, 6 decoys |
| `benchmark3_impossible/` (15 cases) | **0%** (0/15) — intentional | Cases no static text scanner can ever solve (runtime-fetched secrets, hardware-bound encryption, OAuth handshakes, binary/image storage) — included to show the honest ceiling, not a bug to fix |

## What worked today

- Fixed the OpenAI regex to accept the newer `sk-proj-...` format (was rejecting it over a stray hyphen).
- Added a generic secret check independent of provider format — catches things like `session_secret = "..."`.
- Added Shannon entropy filtering, scoped to just the OpenAI pattern and the generic check, which removed a real false positive (a placeholder matching the OpenAI format) without losing other true positives — entropy applied everywhere caused regressions, applied too narrowly it undersolves; getting the scope right took several iterations.
- Added base64 decode-then-recheck, which found a secret that was never visible as plain text in the source.
- Added a heuristic for likely split secrets (a bare known prefix stored alone in a string) — it also caught a multi-line string-concatenation case it wasn't specifically built for.
- Went from 55% → 91% → 100% on the original 11-case benchmark over the course of the day.

## What didn't work / known gaps

- `benchmark2` detection rate is 67%, not 100% — missing: 4 new provider formats (Twilio, SendGrid, Mailgun, Discord) not yet in the pattern list, double-base64 decoding (only unwraps one layer), hex-encoded secrets (only base64 is checked), and a case-sensitivity gap (lowercase `akia...` isn't matched by the AWS pattern, which only allows uppercase).
- The split-secret heuristic only flags a *possible* leak (the bare prefix), not the reconstructed full key — and could occasionally false-positive on legitimate code that happens to store a bare prefix-looking string for unrelated reasons.
- `benchmark3_impossible` confirms 15 categories of secrets no source-code scanner — not this one, not Gitleaks, not TruffleHog — can ever find by reading text: secrets fetched at runtime, injected by the platform, encrypted with hardware-bound or XOR keys, split across files only joined at runtime, stored in binary/image data, or that never exist as a fixed value at all (OAuth handshakes, challenge-response signing). Solving these would need dynamic analysis (actually running the code and watching it), a fundamentally different and much larger tool.

## Planned next

- Add the 4 missing provider patterns found by benchmark2 (Twilio, SendGrid, Mailgun, Discord)
- Make the AWS pattern (and others) case-insensitive
- Support hex-encoded secrets alongside base64
- Attempt a second base64 decode pass for double-encoded values
- Verify found keys against the real provider API (is it still live?)
- Scan git history too, not just the current file state

## Changelog

- **2026-11-23** — First working scanner (URL + folder scan modes). Benchmark built. Measured 55% detection rate and documented why.
- **2026-11-25** — Fixed OpenAI regex, added npm pattern, generic secret check, Shannon entropy filtering, base64 decode-and-recheck, and split-secret heuristic. Reached 100% on the original 11-case benchmark. Built a second, harder 24-case benchmark (67% result, gaps identified) and a third 15-case benchmark of genuinely unsolvable cases (0/15, confirmed as the expected ceiling, not a bug).
