# Answer Key — Harder Benchmark (benchmark2)

**Detection rate = secrets found ÷ 24 × 100**

## Findable with your current patterns (10)

1. `stripe.js` — Stripe live key
2. `stripe.js` — Stripe test key
3. `openai.py` — OpenAI old format
4. `openai.py` — OpenAI new `sk-proj-` format
5. `cloud.env` — AWS key
6. `cloud.env` — Firebase key
7. `ci.yml` — GitHub token
8. `ci.yml` — npm token
9. `docs.md` — Slack token
10. `docs.md` — Private key block

## New provider formats — NOT in your pattern list yet (4)

These will only be found if you add new patterns for them.

11. `notifications.py` — Twilio SID (`SK` + 32 hex chars)
12. `notifications.py` — SendGrid key (`SG.xxx.xxx`)
13. `notifications.py` — Mailgun key (`key-xxx`)
14. `notifications.py` — Discord bot token

## Generic check should catch these (4)

15. `config.py` — `db_password = "..."`
16. `config.py` — `auth_token: "..."`
17. `settings.yml` — `session_secret: "..."`
18. `settings.yml` — `admin_password: "..."`

## Harder / obfuscated cases (6) — genuinely difficult, some may be impossible with your current approach

19. `split_three.py` — Stripe key split across THREE variables (harder than the 2-way split from benchmark 1)
20. `double_encoded.py` — AWS key encoded in base64 **twice** (your current decoder only un-wraps one layer)
21. `hex_encoded.py` — GitHub token encoded as hex, not base64 (different encoding your scanner doesn't check)
22. `reversed.py` — npm token stored backwards, reversed at runtime
23. `case_variant.py` — AWS key with a lowercase prefix (`akia...` instead of `AKIA...`) — tests whether your regex is case-sensitive
24. `multiline.py` — Stripe key split across two string literals joined by Python's implicit string concatenation

## Decoys — should NOT be flagged as leaks

- `decoys.py` — a UUID (looks random, isn't a secret)
- `decoys.py` — a SHA256 hash (high entropy, isn't a secret — common false-positive source for entropy-only scanners)
- `decoys.py` — `api_secret = "none"` (low entropy, correctly ignorable)
- `decoys.py` — `pagination_token = "next_page"` (keyword "token" in the name, but not a secret)
- `env.sample` — two placeholder values (`CHANGE_ME_PLEASE`, `REPLACE_WITH_YOUR_OWN_KEY`)
- `about.md` — plain descriptive text, no secrets at all

## Scoring

- Found all 10 "current patterns" + all 4 "generic check" (14 total) with zero decoys flagged: solid baseline, matches your benchmark 1 level.
- Found the 4 new provider formats too: you extended your pattern list, 18/24 = 75%.
- Found any of the 6 harder cases: bonus — `case_variant.py` (case-insensitive regex) is the easiest of the six to actually fix. The other five need real new techniques (double-decode loop, hex decoding, string-reversal detection, N-way split detection, multi-line string joining) — some of these are open research problems for real scanners too, not just for you.
