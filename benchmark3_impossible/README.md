# Impossible Benchmark (15 cases)

None of these should ever be findable by a static text/pattern scanner — not
yours, not Gitleaks, not TruffleHog, not any future version. This folder exists
to draw the real ceiling, not to be "fixed."

| # | File | Why it's unsolvable by reading text |
|---|---|---|
| 1 | `01_remote_fetch.py` | Secret fetched live from a server, never written to any file |
| 2 | `02_env_var.py` | Secret injected by the hosting platform at runtime, lives outside every file |
| 3 | `03_xor_cipher.py` | XOR-encrypted bytes look like random noise, no recoverable pattern |
| 4 | `04_database_lookup.py` | Secret lives in a database row, not in code |
| 5 | `05_cli_argument.py` | Secret typed in when the program starts, never written anywhere |
| 6 | `06_oauth_dynamic.py` | No fixed secret exists — a new token is negotiated and discarded each run |
| 7 | `07_math_derived.py` | Secret rebuilt from a formula, no string or prefix exists to match |
| 8 | `08_multi_file_split.py` + `08b_other_half.py` | Split across two unrelated-looking files, joined only at runtime |
| 9 | `09_binary_resource.py` | Secret lives inside a binary file, not readable as text at all |
| 10 | `10_hardware_bound.py` | Decryption needs the exact physical machine (TPM) it was encrypted on |
| 11 | `11_steganography.py` | Secret hidden in image pixel data |
| 12 | `12_minified_obfuscated.js` | Real obfuscator output — no clean variable/value pairs left to match |
| 13 | `13_challenge_response.py` | No reusable secret exists — only a one-time signed response |
| 14 | `14_user_typed.py` | Secret typed by a human at runtime, never saved to disk |
| 15 | `15_derived_from_password.py` | Secret derived via slow key-derivation from a password that's never stored |

**Expected result: 0 out of 15, from any scanner, forever.**

If your tool ever "finds" one of these, it's either a coincidence (false
positive on unrelated text) or this file was edited to be less extreme than
intended — these aren't meant to be solvable with better regex, more patterns,
or more entropy thresholds. They need a fundamentally different capability
(running the code, controlling the hardware, intercepting network traffic,
knowing a human-only secret) that a source-code scanner structurally cannot have.
