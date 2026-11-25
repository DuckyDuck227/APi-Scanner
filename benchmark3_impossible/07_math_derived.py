# Secret is rebuilt character by character from a formula based on position.
# There's no string, no prefix, no recognizable pattern anywhere - just numbers
# and arithmetic that only make sense once you run them.
def build_char(i):
    base = (i * 7 + 3) % 26
    return chr(base + 97)

real_key = "".join(build_char(i) for i in range(20))
