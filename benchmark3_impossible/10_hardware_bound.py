# Secret is decrypted using a key tied to this specific machine's hardware
# (TPM chip / secure enclave). The encrypted blob is useless without that exact
# hardware - no scanner, and not even a human with the source code, can recover
# the real key without the physical device it was bound to.
encrypted_blob = b"\x8f\x3a\x7c\x12\x9e\x44\xbb\x02"
real_key = hardware_tpm.decrypt(encrypted_blob)  # only works on the original machine
