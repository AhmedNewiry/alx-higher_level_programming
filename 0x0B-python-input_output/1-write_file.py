#!/usr/bin/python3
"""Defines the write_file function"""


def write_file(filename="", text=""):
    """Writes a string to a text file
    Return:
        The number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
