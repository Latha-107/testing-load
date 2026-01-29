import os
import requests
import sys

GITLAB_TOKEN = os.getenv("GITLAB_TOKEN")

PROJECT_ID = "12345678"   # numeric project ID
BRANCH = "main"

if not GITLAB_TOKEN:
    print("ERROR: GITLAB_TOKEN not found")
    sys.exit(1)

url = f"https://gitlab.com/api/v4/projects/{PROJECT_ID}/pipeline"

headers = {
    "PRIVATE-TOKEN": GITLAB_TOKEN
}

data = {
    "ref": BRANCH
}

response = requests.post(url, headers=headers, data=data)

print("GitLab Status Code:", response.status_code)
print("GitLab Response:", response.text)
