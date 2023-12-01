#!/usr/bin/python3
""" a Python script that takes in a URL,
    sends a request to the URL
    and displaysthe body of the
    response (decoded in utf-8).
"""
import sys
from urllib import request, error


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with request.urlopen(url) as r:
            print(r.read().decode('utf8'))
    except error.HTTPError as err:
        print(f"Error code: {err.code}")
