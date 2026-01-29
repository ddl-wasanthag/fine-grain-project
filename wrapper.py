import argparse
import requests
import os

parser = argparse.ArgumentParser()
parser.add_argument("--branch", required=True)
args = parser.parse_args()

DOMINO_API_HOST = "https://sbx.domino.novartis.net"
DOMINO_API_KEY = os.environ["DOMINO_USER_API_KEY"]

PROJECT_ID = "69534743f94ca329e099e42b"
ENVIRONMENT_ID = "6862e3ab18cd5d5cbd36a1fd"

url = f"{DOMINO_API_HOST}/api/jobs/v1/jobs"

payload = {
"projectId": PROJECT_ID,
"runCommand": "python output_text.py",
"environmentId": ENVIRONMENT_ID,
"mainRepoGitRef": {
"refType": "branches",
"value": args.branch
}
}

headers = {
"X-Domino-Api-Key": DOMINO_API_KEY,
"Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

if not response.ok:
print("Status:", response.status_code)
print("Body:", response.text)
response.raise_for_status()
