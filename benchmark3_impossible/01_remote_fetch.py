# Secret never touches the source code at all - fetched live from a vault at runtime.
# No static scan of this file will ever see the real key, because it doesn't exist
# in the file. Only watching the actual network traffic while the program runs would.
import requests
api_key = requests.get("https://vault.internal.example.com/v1/secrets/stripe").text
