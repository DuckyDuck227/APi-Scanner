# GitHub token stored as hex instead of base64
encoded_hex = "6768705f396d4b32704c376e5134725336745638775831795a336142356344376546396748316a"
github_token = bytes.fromhex(encoded_hex).decode()
