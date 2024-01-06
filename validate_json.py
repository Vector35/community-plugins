import os
import sys
import requests
import base64
import json


token = sys.argv[1]

def getfile(url):
    return requests.get(url, headers={'Authorization': f'token {token}'})

issue_content = os.environ.get("ISSUE_CONTENT")

lines = issue_content.split("\n")

def validate_repo(line):
    repo = line.split(" ")[-1].lower() # handle both cases of just URL or with Repo URL: before
    repo = repo.replace("https://github.com/","").strip().strip("/") # just get the user/project portion
    projectUrl = f"https://api.github.com/repos/{repo}"
    latestRelease = f"{projectUrl}/releases/latest"
    tagsUrl = f"{projectUrl}/tags"
    try:
        releaseData = getfile(latestRelease).json()

        match releaseData.get('message'):
            case 'Not Found':
                print(f"\n\nERROR: {plugin['name']}, Couldn't get release information. Likely the user created a tag but no associated release.\n")
                sys.exit(-1)
            case 'Bad credentials':
                print("\n\nERROR: Bad credentials, check access token.\n")
                sys.exit(-1)

    except:
        print(f"\n\nFailed to load valid release data json from {latestRelease}")
        sys.exit(-1)
    try:
        tag = releaseData['tag_name']
        pluginjsonurl = f"{projectUrl}/contents/plugin.json?ref={tag}"
        content = getfile(pluginjsonurl).json()['content']
        jsoncontent = json.loads(base64.b64decode(content))
    except:
        print(f"\n\nFailed to parse valid plugin.json from https://github.com/{repo}/blob/master/plugin.json")
        sys.exit(-1)
    sys.exit(0)

for line in lines:
    if line.startswith("Repo URL:"):
        validate_repo(line)

# Failed to find a repo line, just look for the first github URL:

for line in lines:
    if line.startswith("https://github.com/"):
        validate_repo(line)

