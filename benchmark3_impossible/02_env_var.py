# Secret is injected by the hosting platform (Heroku, Docker, GitHub Actions secrets, etc.)
# as an environment variable. The value is set OUTSIDE this file entirely - it never
# exists in any file you could scan.
import os
api_key = os.environ["STRIPE_API_KEY"]
