import os
import requests
import json
import sys
from requests.auth import HTTPBasicAuth

BITBUCKET_USERNAME = os.getenv("BITBUCKET_USERNAME")
BITBUCKET_APP_PASSWORD = os.getenv("BITBUCKET_APP_PASSWORD")

WORKSPACE = "your-workspace"
REPO_SLUG = "your-repo"
BRANCH = "main"

if not BITBUCKET_USERNAME or not BITBUCKET_APP_PASSWORD:
    print("ERROR: Bitbucket credentials not found")
    sys.exit(1)

url = f"https://api.bitbucket.org/2.0/repositories/{WORKSPACE}/{REPO_SLUG}/pipelines/"

payload = {
    "target": {
        "type": "pipeline_ref_target",
        "ref_type": "branch",
        "ref_name": BRANCH
    }
}

response = requests.post(
    url,
    auth=HTTPBasicAuth(BITBUCKET_USERNAME, BITBUCKET_APP_PASSWORD),
    headers={"Content-Type": "application/json"},
    data=json.dumps(payload)
)

print("Bitbucket Status Code:", response.status_code)
print("Bitbucket Response:", response.text)
