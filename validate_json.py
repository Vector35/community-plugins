import os
import sys
import requests

token = sys.argv[1]

def getfile(url):
    return requests.get(url, headers={'Authorization': f'token {token}'})

encoded_issue_content = os.environ.get('ISSUE_CONTENT')
if encoded_issue_content:
    issue_content = base64.b64decode(encoded_issue_content).decode('utf-8')
else:
    print("No issue environment variable.")
    sys.exit(-1)

issue_content = os.environ.get("ISSUE_CONTENT")

if issue_content.startswith("Please add my plugin to the repository."):
    lines = issue_content.split("\n")
    for line in lines:
        if line.startswith("Repo name:"):
            repo = line.split(" ")[-1]
            if repo.startswith("https://github"):
                repo = repo[19:] # strip off beginning of URL if it exists
            repo = repo.strip("/") #normalize path
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
                print("\n\nFailed to load valid release data json from {latestRelease}")
                sys.exit(-1)
            try:
                tag = releaseData['tag_name']
                pluginjsonurl = f"{projectUrl}/contents/plugin.json?ref={tag}"
                content = getfile(pluginjson).json()['content']
            except:
                print("\n\nFailed to parse valid plugin.json from https://github.com/{repo}/blob/master/plugin.json")
                sys.exit(-1)
