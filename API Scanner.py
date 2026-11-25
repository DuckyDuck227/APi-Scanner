import requests
import os
import re
import math
import base64

# Ask for a website URL to scan live (separate feature from the folder scan below)
domain = input("Type in your Domain. ")

# Request URL Domain and save

# Auto-add https:// if the user forgot it, so requests.get() doesn't fail
if not domain.startswith("http"):
    domain = "https://" + domain

answerdomain = requests.get(domain)

# Known API key formats: (provider name, regex pattern to match that provider's key)
api_key_patterns = [
    ("Stripe live", r"sk_live_[0-9a-zA-Z]{24,}"),
    ("Stripe test", r"sk_test_[0-9a-zA-Z]{24,}"),
    ("OpenAI", r"sk-[A-Za-z0-9-]{20,}"),
    ("Google/Firebase", r"AIza[0-9A-Za-z_\-]{35}"),
    ("AWS Access Key", r"AKIA[0-9A-Z]{16}"),
    ("GitHub Token", r"ghp_[A-Za-z0-9]{36}"),
    ("Slack Token", r"xox[baprs]-[0-9A-Za-z-]{10,}"),
    ("Private Key", r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    ("npm Token", r"npm_[A-Za-z0-9]{36}"),
]

# Catches secrets with no known provider format: any "key/secret/password/token" variable
# assigned a quoted value, e.g. session_secret = "..."
generic_pattern = r"(key|secret|password|token)\s*(=|:)\s*[\"']([^\"']+)[\"']"

# Catches base64-encoded secrets: quoted strings made only of base64 characters
base64_pattern = r"[\"']([A-Za-z0-9+/]{16,}={0,2})[\"']"

half_pattern = r'["\'](sk_live_|sk_test_|sk-|AKIA|ghp_|npm_|xoxb-|AIza)["\']'


def calculate_entropy(text):
    # Shannon entropy: how random a string looks. High = likely a real secret,
    # low = likely a placeholder like "xxxxxxxx".
    entropy = 0
    for char in set(text):
        probability = text.count(char) / len(text)
        entropy = entropy - probability * math.log2(probability)
    return entropy


folder_to_scan = input("Which folder should I check? ")

for folder_path, subfolders, filenames in os.walk(folder_to_scan):
    for name in filenames:
        path = folder_path + "/" + name
        with open(path) as file:
            for line in file:
                # Check 1: known provider patterns (Stripe, AWS, GitHub, etc.)
                # Only OpenAI needs the entropy check too, since its format is loose
                # enough to also match placeholder text like "sk-xxxx...xxxx"
                for provider_name, pattern in api_key_patterns:
                    match = re.search(pattern, line)
                    if match and (provider_name != "OpenAI" or calculate_entropy(match.group(0)) > 4.0):
                        print(path, line)

                # Check 2: generic secret-looking variable, not tied to any provider
                match = re.search(generic_pattern, line)
                if match and calculate_entropy(match.group(3)) > 4.0:
                    print(path, line)

                # Check 3: base64-encoded secrets - decode first, then re-check
                # against the same known patterns
                candidates = re.findall(base64_pattern, line)
                for candidate in candidates:
                    try:
                        decoded = base64.b64decode(candidate).decode()
                    except Exception:
                        continue

                    for provider_name, pattern in api_key_patterns:
                        if re.search(pattern, decoded):
                            print(path, "decoded:", decoded)
                if re.search(half_pattern, line):
                      print(path, "possible splitted key:", line)
