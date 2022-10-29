#!/usr/bin/python3
"""Contains the read_file function"""


def read_file(filename=""):
    """Prints a text file to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
