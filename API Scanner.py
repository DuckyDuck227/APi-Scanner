import requests
import os 
import re 

domain = input("Type in your Domain. ")



# Request URL Domain and save 

if not domain.startswith("http"):
  domain = "https://" + domain

answerdomain= requests.get(domain)

api_key_patterns = [
    ("Stripe live", r"sk_live_[0-9a-zA-Z]{24,}"),
    ("Stripe test", r"sk_test_[0-9a-zA-Z]{24,}"),
    ("OpenAI", r"sk-[A-Za-z0-9]{20,}"),
    ("Google/Firebase", r"AIza[0-9A-Za-z_\-]{35}"),
    ("AWS Access Key", r"AKIA[0-9A-Z]{16}"),
    ("GitHub Token", r"ghp_[A-Za-z0-9]{36}"),
    ("Slack Token", r"xox[baprs]-[0-9A-Za-z-]{10,}"),
    ("Private Key", r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
]

folder_to_scan = input("Which folder should I check? ")



for folder_path, subfolders, filenames in os.walk(folder_to_scan):
        for name in filenames:
          path = folder_path + "/" + name
          with open(path) as file:
            for line in file:
                if any(re.search(pattern, line) for provider_name, pattern in api_key_patterns):
                      print(path, line)