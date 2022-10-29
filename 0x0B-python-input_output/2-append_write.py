#!/usr/bin/python3
"""This module defines the append_write function"""


def append_write(filename="", text=""):
    """Append a string to the of a text file.

    Args:
        filename (str): the name of the file.
        text (str): the string to append to the file.

    Returns:
        The number of characterw appended.

    """
    with open(filename, "a", encoding="utf-8") as f:
         return f.write(text)
