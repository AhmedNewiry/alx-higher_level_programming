#!/usr/bin/python3
""" a Python script that takes
    in a URL,sends a request to the
    URL and displaysthe value of the variable
    X-Request-Id in the response header
"""
import sys
import requests

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    headers = r.headers
    print(headers["X-Request-Id"])
