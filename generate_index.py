#!/usr/bin/env python3
import sys
import os
import json
import argparse
import base64
import requests
from dateutil import parser
import base64
import re
from datetime import datetime

ghUrl = "https://github.com/"
user = None
token = None

def printProgressBar(iteration, total, prefix = '', length = 80, fill = '█'):
    filledLength = int(length * iteration // total)
    bar = (fill * filledLength) + ('-' * (length - filledLength))
    percent = 100 * (iteration / float(total))
    fmt = "\r{prefix} |{bar}| {percent:.1f}%".format(prefix=prefix, bar=bar, percent=percent)
    sys.stdout.write(fmt)
    # Print New Line on Complete
    if iteration == total:
        print()

def getfile(url):
    return requests.get(url, auth=requests.auth.HTTPBasicAuth(user, token))

def getPluginJson(plugin):
    if "site" in plugin:
        print("We only currently support github projects")
        return

    site = "https://github.com/"
    apisite = "https://api.github.com/repos/"
    jsonUrl = "{}{}/contents/plugin.json?ref={}"
    userAndProject = plugin["name"]
    userName = plugin["name"].split("/")[0]
    releasesUrl = "{}{}/releases/tags".format(apisite, userAndProject)
    tagsUrl = "{}{}/tags".format(apisite, userAndProject)

    releaseData = None
    try:
        releases = "{}/{}".format(releasesUrl, plugin["tag"])
        releaseData = getfile(releases).json()
        if "message" in releaseData and releaseData["message"] == "Not Found":
            print("\n\nERROR: {}, Couldn't get release information. Likely the user created a tag but no associated release.\n".format(plugin['name']))
            return None
    except requests.exceptions.HTTPError:
        print(" Unable get get url {}".format(releases))
        return None

    commit = None
    zipUrl = None
    # Lookup the tag url and find the associated commit
    try:
        tagData = getfile(tagsUrl).json()
        for tag in tagData:
            if tag["name"] == plugin["tag"]:
                commit = tag["commit"]["sha"]
                zipUrl = tag["zipball_url"]
                break
        if commit is None:
            print("Unable to associate tag {} with a commit for plugin {}".format(plugin["tag"], plugin["name"]))
            return None
    except requests.exceptions.HTTPError:
        print(" Unable get get url {}".format(tagsUrl))
        return None

    projectData = None
    try:
        projectData = getfile(apisite + userAndProject).json()
    except requests.exceptions.HTTPError:
        print(" Unable get get url {}".format(apisite + userAndProject))
        return None

    data = None
    try:
        jsonDataUrl = jsonUrl.format(apisite, userAndProject, plugin["tag"])
        content = getfile(jsonDataUrl).json()['content']
        data = json.loads(base64.b64decode(content))
        if "plugin" in data:
            # Using old style json
            data = data["plugin"]
    except requests.exceptions.HTTPError:
        print(" Unable get get url")
        return None

    # Additional fields required for internal use
    data["lastUpdated"] = int(parser.parse(releaseData["published_at"]).timestamp())
    data["projectUrl"] = site + userAndProject
    data["projectData"] = projectData
    data["authorUrl"] = site + userName
    data["packageUrl"] = zipUrl

    # Replace the fwd slash with _ and then strip all non (alpha, numeric, _ )
    data["path"] = re.sub("[^a-zA-Z0-9_]", "", re.sub("/", "_", projectData["full_name"]))
    data["commit"] = commit

    # TODO: Consider adding license info directly from the repository's json data (would need to test unlicensed plugins)
    # data["license"] = {"name" : data["license"]["name"], "text": getfile(data["license"]["url"])}

    if isinstance(data["api"], str):
        data["api"] = [data["api"]]
    if "minimumBinaryNinjaVersion" not in data or not isinstance(data["minimumBinaryNinjaVersion"], int):
        data["minimumBinaryNinjaVersion"] = 0
    if "platforms" not in data:
        data["platforms"] = []
    if "installinstructions" not in data:
        data["installinstructions"] = {}
    return data

def main():
    parser = argparse.ArgumentParser(description="Produce 'plugins.json' for plugin repository.")
    parser.add_argument("-i", "--initialize", action="store_true", default=False,
        help="For first time running the command against the old format")
    parser.add_argument("-r", "--readme", action="store_true", default=False,
        help="Generate README.md")
    parser.add_argument("-l", "--listing", action="store", default="listing.json")
    parser.add_argument("username")
    parser.add_argument("token")
    args = parser.parse_args(sys.argv[1:])
    global user
    global token
    user = args.username
    token = args.token

    basedir = os.path.join(os.path.dirname(os.path.realpath(__file__)))
    pluginjson = os.path.join(basedir, "plugins.json")

    allPlugins = {}
    listing = json.load(open(args.listing, "r", encoding="utf-8"))
    for i, plugin in enumerate(listing):
        printProgressBar(i, len(plugin), prefix="Collecting Plugin JSON files:")
        jsonData = getPluginJson(plugin)
        if jsonData is None:
            return
        allPlugins[plugin["name"]] = jsonData
    printProgressBar(len(plugin), len(plugin), prefix="Collecting Plugin JSON files:")

    oldPlugins = {}
    if os.path.exists(pluginjson):
        with open(pluginjson) as pluginsFile:
            for i, plugin in enumerate(json.load(pluginsFile)):
                oldPlugins[plugin["projectData"]["full_name"]] = plugin["lastUpdated"]

    newPlugins = []
    updatedPlugins = []
    for i, (name, pluginData) in enumerate(allPlugins.items()):
        # printProgressBar(i, len(allPlugins), prefix="Updating plugins.json:")
        pluginIsNew = False
        pluginIsUpdated = False
        if name not in oldPlugins:
            pluginIsNew = True
        else:
            if name not in oldPlugins:
                pluginIsUpdated = True
            else:
                pluginIsUpdated = pluginData["lastUpdated"] > oldPlugins[name]

        if pluginIsUpdated or pluginIsNew:
            if pluginIsNew:
                newPlugins.append(name)
            elif pluginIsUpdated:
                updatedPlugins.append(name)

    printProgressBar(len(allPlugins), len(allPlugins), prefix="Updating plugins.json:       ")
    allPluginsList = []
    for name, plugin in allPlugins.items():
        allPluginsList.append(plugin)

    print("{} New Plugins:".format(len(newPlugins)))
    for plugin in newPlugins:
        print("\t- {}".format(plugin))
    print("{} Updated Plugins:".format(len(updatedPlugins)))
    for plugin in updatedPlugins:
        print("\t- {}".format(plugin))
    print("Writing {}".format(pluginjson))
    with open(pluginjson, "w") as pluginsFile:
        json.dump(allPluginsList, pluginsFile, indent="    ")

    if args.readme:
        info = ""
        if os.path.exists("INFO"):
            info = open("INFO", encoding="utf-8").read() + u"\n"
        with open("README.md", "w", encoding="utf-8") as readme:
            readme.write(info)
            readme.write(u"# Binary Ninja Plugins\n\n")
            readme.write(u"| PluginName | Author | Last Updated | License | Type | Description |\n")
            readme.write(u"|------------|--------|--------------|---------|----------|-------------|\n")

            for plugin in allPlugins.values():
                readme.write(u"|[{name}]({projectUrl})|[{author}]({authorUrl})|{lastUpdated}|{license}|{plugintype}|{description}|\n".format(name = plugin['name'],
                    projectUrl=plugin["projectUrl"],
                    plugin=plugin["name"],
                    author=plugin["author"],
                    authorUrl=plugin["authorUrl"],
                    lastUpdated=datetime.fromtimestamp(plugin["lastUpdated"]).date(),
                    license=plugin['license']['name'],
                    plugintype=', '.join(sorted(plugin['type'])),
                    description=plugin['description']))
if __name__ == "__main__":
    main()
