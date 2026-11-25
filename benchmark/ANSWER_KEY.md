# Answer Key — Secret Scanner Benchmark

Run your scanner on this folder and compare the result against this list.
**Detection rate = real leaks found ÷ 11 × 100**

## Real, findable leaks (11 total — your scanner should find these)

1. `config.js` — Stripe live key
2. `settings.py` — OpenAI key
3. `.env` — AWS Access Key
4. `app.json` — Google/Firebase key
5. `deploy.yml` — GitHub Token
6. `notes.txt` — generic `session_secret` (variable-name check, no known prefix)
7. `README.md` — Slack Token (hidden in a docs file — tests whether the scanner skips `.md` files)
8. `database.sql` — Private Key block
9. `script.ts` — npm Token

## Intentionally hard cases (2 — a normal regex scanner likely will NOT find these)

10. `split_secret.py` — Stripe key split across two variables, only joined at runtime
11. `encoded_secret.py` — AWS key base64-encoded, only decoded at runtime

## Decoy — should NOT be reported as a leak (1)

- `example.env.sample` — contains only placeholders (`YOUR_KEY_HERE`, `xxxx...`), no real key

## Scoring

- Finding all 9 "normal" cases (1-9) but neither of the 2 hard ones (10-11): **9/11 = 82%** — realistic, roughly on par with real tools from the study.
- Also flagging `example.env.sample`: that's a false positive, don't count it as a hit, but note it separately.
