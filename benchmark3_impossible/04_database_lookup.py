# Secret lives in a database row, fetched at runtime. The file only contains
# a database query, never the actual secret value.
import sqlite3
conn = sqlite3.connect("secrets.db")
api_key = conn.execute("SELECT value FROM secrets WHERE name = 'stripe_key'").fetchone()[0]
