# Secret is XOR-encrypted byte by byte. No fixed prefix, no recognizable format,
# and the result of XOR looks like pure random noise until decrypted with the
# exact same key - a scanner has no way to know which bytes to XOR or with what.
cipher_key = 173
scrambled = [214, 25, 142, 88, 201, 46, 177, 9, 233, 61, 190, 112]
real_key = "".join(chr(b ^ cipher_key) for b in scrambled)
