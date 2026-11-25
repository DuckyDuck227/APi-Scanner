# API Scanner

A security scanner for vibe-coded apps (built with Lovable, Bolt, Cursor, Supabase, Firebase, etc.).
It looks for API keys and secrets accidentally left in code, checks Supabase RLS policies, and more.

**Status: 🚧 Work in progress — not production-ready yet.**

## Why this exists

AI coding tools ship fast, but they often leave the same kinds of security gaps behind
(exposed API keys, database rules left wide open, no rate limiting). This project is me
building a scanner that catches those specific, known patterns — and testing it honestly
against a benchmark of planted secrets, instead of just assuming it works.

## What it can do right now

- Searches for API keys using known provider patterns (Stripe, OpenAI, Google/Firebase, AWS, GitHub, Slack, Private Keys)
- Two scan modes: a live website (give it a URL) or a local folder
- Comes with its own benchmark folder of 11 known test leaks, so the detection rate is measured, not guessed

## What worked

- The core approach (pattern list + regex, checked line by line) works and is easy to extend.
- Found 6 of 11 planted secrets correctly on the first full benchmark run (Stripe, AWS, Google/Firebase, GitHub, Slack, and a private key block), across different file types (.js, .env, .json, .yml, .md, .sql).
- Correctly ignored most decoy/placeholder values.

## What didn't work (yet)

**Detection rate: 6/11 = 55%** on the benchmark — here's exactly why:
- An OpenAI key regex that was too strict missed the newer `sk-proj-...` format.
- No generic check for secrets stored in suspiciously-named variables (e.g. `session_secret = "..."`) that don't match a known provider format.
- The pattern list is still incomplete — npm tokens, for example, aren't covered yet.
- One false positive: a placeholder value (`sk-xxxx...`) got flagged as if it were real.

This is intentional and public — a secret scanner that silently claims 100% accuracy is lying to you. 55% is the honest current number, and the gaps above are exactly what's being worked on next.

## Planned next

- Fix the known regex gaps and extend provider coverage
- Add a generic secret check (based on variable names, not just known formats)
- Add entropy-based detection for unknown/custom secrets
- Verify found keys against the real provider API (is it still live?)
- Scan git history too, not just the current file state

## Changelog

- **2026-11-25** — First working scanner (URL + folder scan modes). Benchmark built. Measured 55% detection rate and documented why.
