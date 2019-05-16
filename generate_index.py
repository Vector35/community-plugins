#!/usr/bin/env python3
import pygit2
import sys
import os
import json
import argparse
import base64
import requests

ghUrl = "https://github.com/"
pluginsDirectory = "plugins"
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

def getPluginJson(sm):
    if not sm.url.startswith(ghUrl):
        print("Not a github url {}".format(sm.url))
        return None

    userAndProject = sm.url[len(ghUrl):]
    if userAndProject.endswith(".git"):
        userAndProject = userAndProject[:-4]
    if userAndProject.endswith("/"):
        userAndProject = userAndProject[:-1]

    packageUrl = "https://raw.githubusercontent.com/{userAndProject}/{commit}/plugin.json".format(userAndProject=userAndProject, commit=sm.head_id)
    try:
        response = getfile(packageUrl)
    except requests.exceptions.HTTPError:
        print(" Unable get get url")
        return None

    data = response.json()["plugin"]

    projectData = None
    projectUrl = "https://api.github.com/repos/{userAndProject}".format(userAndProject=userAndProject)
    try:
        projectData = getfile(projectUrl)
    except requests.exceptions.HTTPError:
        print(" Unable get get url {}".format(projectUrl))
        return None
    data["projectUrl"] = projectUrl
    data["projectData"] = projectData.json()
    # sm.url if not sm.url.endswith('.git') else sm.url[:-4]
    data["authorUrl"] = '/'.join(sm.url.split('/')[:4])
    data["packageUrl"] = "https://github.com/{userAndProject}/archive/{commit}.zip".format(userAndProject=userAndProject, commit=sm.head_id)
    # data["readmeUrl"] = "https://raw.githubusercontent.com/{userAndProject}/{commit}/{readme}".format(userAndProject=userAndProject, commit=sm.head_id, readme=data["readme"])
    data["commit"] = str(sm.head_id)
    data["path"] = sm.path[len(pluginsDirectory) + 1:]
    if isinstance(data["api"], str):
        data["api"] = [data["api"]]
    if "minimumBinaryNinjaVersion" not in data or not isinstance(data["minimumBinaryNinjaVersion"], int):
        data["minimumBinaryNinjaVersion"] = 0
    if "platforms" not in data:
        data["platforms"] = []
    if "installinstructions" not in data:
        data["installinstructions"] = {}

    # TODO: Support Submodules!
    #   Need to recursively checkout the project, check for submodules and record packageUrls for each
    #   data["submodules"] = getPackageSubmodules(sm)
    return data

def main():
    parser = argparse.ArgumentParser(description="Produce 'plugins.json' for plugin repository.")
    parser.add_argument("-i", "--initialize", action="store_true", default=False,
        help="For first time running the command against the old format")
    parser.add_argument("-r", "--readme", action="store_true", default=False,
        help="Generate README.md")
    parser.add_argument("username")
    parser.add_argument("token")
    args = parser.parse_args(sys.argv[1:])
    global user
    global token
    user = args.username
    token = args.token

    basedir = os.path.join(os.path.dirname(os.path.realpath(__file__)))
    pluginjson = os.path.join(basedir, "plugins.json")

    repo = pygit2.Repository(".")

    # People are dumb and don't follow the spec for plugin.json files also our initial spec sucked so they can't be blamed
    allPlugins = {}
    directories = list(os.walk(os.path.join(basedir, pluginsDirectory)))[0][1]
    for i, smpath in enumerate(directories):
        printProgressBar(i, len(directories), prefix="Collecting Plugin JSON files:")
        fullsmpath = os.path.join(pluginsDirectory, smpath)
        sm = repo.lookup_submodule(fullsmpath)
        jsonData = getPluginJson(sm)
        allPlugins[pluginsDirectory + "/" + smpath] = jsonData
    printProgressBar(len(directories), len(directories), prefix="Collecting Plugin JSON files:")

    oldPlugins = {}
    if os.path.exists(pluginjson):
        with open(pluginjson) as pluginsFile:
            data = json.load(pluginsFile)
            for i, plugin in enumerate(data):
                for path, data in allPlugins.items():
                    if path == (pluginsDirectory + "/" + plugin["path"]):
                        oldPlugins[pluginsDirectory + "/" + plugin["path"]] = plugin

    newPlugins = []
    updatedPlugins = []
    allSubmodules = repo.listall_submodules()
    for i, submoduleStr in enumerate(allSubmodules):
        printProgressBar(i, len(allSubmodules), prefix="Updating plugins.json:")
        sm = repo.lookup_submodule(submoduleStr)
        pluginIsNew = (sm.name not in oldPlugins)
        pluginIsUpdated = False

        if args.initialize:
            pluginIsNew = True
        if not pluginIsNew:
            pluginIsUpdated = oldPlugins[sm.name]["commit-hash"] != str(sm.head_id)
        if (pluginIsUpdated or pluginIsNew):
            # A new plugin was added or a plugin's commit has changed pull its plugin.json file
            # Plugin has been updated record its new information
            pluginInfo = allPlugins[sm.path]
            if pluginInfo is None:
                print("Error failed to fetch: {}".format(sm.name))
            else:
                if pluginIsNew:
                    newPlugins.append(pluginInfo)
                elif pluginIsUpdated:
                    updatedPlugins.append(pluginInfo)
                oldPlugins[sm.name] = pluginInfo
    printProgressBar(len(allSubmodules), len(allSubmodules), prefix="Updating plugins.json:")

    print("{} New Plugins:".format(len(newPlugins)))
    for i, plugin in enumerate(newPlugins):
        print("\t{} {}".format(i, plugin["name"]))
    print("{} Updated Plugins:".format(len(updatedPlugins)))
    for i, plugin in enumerate(updatedPlugins):
        print("\t{} {}".format(i, plugin["name"]))
    print("Writing {}".format(pluginjson))
    with open(pluginjson, "w") as pluginsFile:
        json.dump(list(oldPlugins.values()), pluginsFile, indent="    ")

    if args.readme:
        with open(os.path.join(pluginsDirectory, "README.md"), "w", encoding="utf-8") as readme:
            readme.write(u"# Binary Ninja Plugins\n\n")
            readme.write(u"| PluginName | Author | License | Type | Description |\n")
            readme.write(u"|------------|--------|---------|----------|-------------|\n")

            for plugin in oldPlugins:
                readme.write(u"|[{name}]({url})|[{author}]({authorlink})|[{license}]({plugin}/LICENSE)|{plugintype}|{description}|\n".format(name = data['name'],
                    url=plugin["url"],
                    plugin=plugin["name"],
                    author=plugin["author"],
                    authorlink=plugin["url"],
                    license=plugin['license']['name'],
                    plugintype=', '.join(sorted(plugin['type'])),
                    description=plugin['description']))
            readme.write(u"\n\n")
if __name__ == "__main__":
    main()
