#!/usr/bin/python3
""" a Python script that fetches
	https://alx-intranet.hbtn.io/status
"""
from urllib import request
if __name__ == "__main__":
	url = "https://alx-intranet.hbtn.io/status"
	with request.urlopen(url) as res:
		print("Body response:")
		result = res.read()
		print(f"\t- type: {type(result)}")
		print(f"\t- content: {result}")
		print(f"\t- utf8 content: {result.decode("UTF-8")}")
