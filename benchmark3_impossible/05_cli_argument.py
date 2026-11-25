# Secret is passed in when the program starts (e.g. `python app.py --key=sk_live_xxx`),
# typed by a human or injected by a deploy script. Never written anywhere in the code.
import sys
api_key = sys.argv[1]
