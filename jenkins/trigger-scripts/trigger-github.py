import os
import requests
import json
import sys

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

OWNER = "Latha-107"
REPO = "testing-load"
WORKFLOW_FILE = "build.yml"   # .github/workflows/build.yml
BRANCH = "main"

if not GITHUB_TOKEN:
    print("ERROR: GITHUB_TOKEN not found")
    sys.exit(1)

url = f"https://api.github.com/repos/{OWNER}/{REPO}/actions/workflows/{WORKFLOW_FILE}/dispatches"

headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

payload = {
    "ref": BRANCH
}

response = requests.post(url, headers=headers, json=payload)

print("GitHub Status Code:", response.status_code)
print("GitHub Response:", response.text)
