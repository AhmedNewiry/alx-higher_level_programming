#!/usr/bin/python3
""" a Python script that takes your GitHub
    credentials (username and password) and
    uses the GitHub API to display your id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth
if __name__ == "__main__":
    authen = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    url = "https://api.github.com/user"
    response = requests.get(url, auth=authen)
    response = response.json()
    print(response.get("id"))
