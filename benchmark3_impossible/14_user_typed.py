# Secret is typed in by a human at runtime and never written to disk anywhere.
# Scanning every file in the project forever will never find it, because it
# simply never existed as a file.
api_key = input("Please paste your Stripe key: ")
