#!/usr/bin/python3
"""list 10 commits (from the most recent to oldest) of
   the repository "rails" by the user "rails"""""
import requests
from sys import argv
if __name__ == "__main__":
    request = "https://api.github.com/repos/{}/{}/commits".format(
        argv[2], argv[1])
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"}
    res = requests.get(request, headers=headers)
    res = res.json()
    try:
        target_res = res[:10]
        for item in target_res:
            print(
                "{}: {}".format(
                    item["sha"],
                    item.get("commit").get("author").get("name")))
    except IndexError:
        pass
