import argparse
import base64
import json
import os
import re
import sys

import requests


GITHUB_REPO_PATTERN = re.compile(
    r"https://github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)"
)


def make_headers(token):
    headers = {"Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"token {token}"
    return headers


def github_get_json(url, token):
    response = requests.get(url, headers=make_headers(token), timeout=20)
    try:
        payload = response.json()
    except ValueError:
        payload = None
    return response, payload


def extract_repo(value):
    candidate = value.strip().rstrip("/")
    if candidate.startswith("https://github.com/"):
        match = GITHUB_REPO_PATTERN.search(candidate)
        if match:
            return match.group(1).lower()
        return None

    if candidate.count("/") == 1 and " " not in candidate:
        return candidate.lower()
    return None


def repo_from_issue_content(issue_content):
    lines = issue_content.splitlines()

    for line in lines:
        if line.startswith("Repo URL:"):
            repo = extract_repo(line.split("Repo URL:", 1)[1])
            if repo:
                return repo

    for line in lines:
        repo = extract_repo(line)
        if repo:
            return repo

    return None


def validate_local_plugin_json(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            json.load(f)
    except FileNotFoundError:
        print(f"ERROR: Local file not found: {path}")
        return False
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON in {path}: {e}")
        return False
    except OSError as e:
        print(f"ERROR: Could not read {path}: {e}")
        return False

    print(f"OK: Local JSON is valid: {path}")
    return True


def validate_remote_repo(repo, token):
    project_url = f"https://api.github.com/repos/{repo}"
    latest_release_url = f"{project_url}/releases/latest"

    release_response, release_data = github_get_json(latest_release_url, token)
    if release_response.status_code == 401:
        print("ERROR: Bad credentials, check access token.")
        return False
    if release_response.status_code == 404:
        print(
            "ERROR: Could not get release information. "
            "Likely the repo has tags but no associated release, or the repo is private."
        )
        return False
    if not release_response.ok:
        print(
            f"ERROR: Failed to fetch release data ({release_response.status_code}) from {latest_release_url}"
        )
        return False
    if not isinstance(release_data, dict):
        print(f"ERROR: Failed to parse release data JSON from {latest_release_url}")
        return False

    tag = release_data.get("tag_name")
    if not tag:
        print("ERROR: Latest release did not contain a tag_name.")
        return False

    plugin_json_url = f"{project_url}/contents/plugin.json?ref={tag}"
    plugin_response, plugin_data = github_get_json(plugin_json_url, token)
    if plugin_response.status_code == 404:
        print(f"ERROR: plugin.json not found for release tag '{tag}'.")
        return False
    if not plugin_response.ok:
        print(
            f"ERROR: Failed to fetch plugin.json ({plugin_response.status_code}) from {plugin_json_url}"
        )
        return False
    if not isinstance(plugin_data, dict):
        print(f"ERROR: Failed to parse plugin.json metadata from {plugin_json_url}")
        return False

    encoded_content = plugin_data.get("content")
    if not encoded_content:
        print(
            f"ERROR: plugin.json metadata did not include file content at {plugin_json_url}"
        )
        return False

    try:
        decoded = base64.b64decode(encoded_content.replace("\n", ""), validate=True)
        json.loads(decoded)
    except (ValueError, json.JSONDecodeError) as e:
        print(f"ERROR: plugin.json in {repo} at tag '{tag}' is not valid JSON: {e}")
        return False

    print(f"OK: Remote plugin.json is valid for {repo} at tag '{tag}'.")
    return True


def parse_args():
    parser = argparse.ArgumentParser(
        description="Validate plugin.json from GitHub issue content, repo URL, or a local file."
    )
    parser.add_argument(
        "legacy_token",
        nargs="?",
        help="GitHub token (legacy positional argument, kept for CI compatibility).",
    )
    parser.add_argument("--token", help="GitHub token. Optional for public repos.")
    parser.add_argument(
        "--issue-content", help="Issue body text containing a repo URL."
    )
    parser.add_argument(
        "--issue-content-file",
        help="Path to a file containing issue body text.",
    )
    parser.add_argument(
        "--repo-url",
        help="Repository URL or owner/repo string to validate directly.",
    )
    parser.add_argument(
        "--plugin-json",
        help="Path to a local plugin.json file to validate directly.",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    token = args.token or args.legacy_token or os.environ.get("GITHUB_TOKEN")

    issue_content = args.issue_content
    if not issue_content and args.issue_content_file:
        try:
            with open(args.issue_content_file, "r", encoding="utf-8") as f:
                issue_content = f.read()
        except OSError as e:
            print(f"ERROR: Failed to read --issue-content-file: {e}")
            return 1

    if not issue_content:
        issue_content = os.environ.get("ISSUE_CONTENT")

    checks_run = 0
    failures = 0

    if args.plugin_json:
        checks_run += 1
        if not validate_local_plugin_json(args.plugin_json):
            failures += 1

    repo = None
    if args.repo_url:
        repo = extract_repo(args.repo_url)
        if not repo:
            print(
                "ERROR: Could not parse --repo-url. Use https://github.com/owner/repo or owner/repo."
            )
            return 1
    elif issue_content:
        repo = repo_from_issue_content(issue_content)
        if not repo:
            print("ERROR: Could not find a GitHub repo URL in issue content.")
            return 1

    if repo:
        checks_run += 1
        if not validate_remote_repo(repo, token):
            failures += 1

    if checks_run == 0:
        print(
            "ERROR: Nothing to validate. Provide --plugin-json, --repo-url, --issue-content, "
            "--issue-content-file, or set ISSUE_CONTENT."
        )
        return 1

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
