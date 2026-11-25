# Secret is stored inside a compiled/binary resource file (imagine an .exe, a
# compiled .pyc, or an embedded binary blob), not in any text file at all.
# A text-based line-by-line scanner cannot even open this as readable text.
with open("app_resources.bin", "rb") as f:
    blob = f.read()
api_key = blob[128:168].decode()
