# Secret is derived from a master password using a slow key-derivation function
# (PBKDF2/Argon2). Even with the salt and algorithm fully visible, deriving the
# actual key back would take real computing time per guess and still requires
# knowing the master password, which is never stored anywhere.
import hashlib
master_password = get_password_from_secure_prompt()  # never written down
salt = b"\x9f\x2a\x11\xcc"
api_key = hashlib.pbkdf2_hmac("sha256", master_password.encode(), salt, 200000).hex()
