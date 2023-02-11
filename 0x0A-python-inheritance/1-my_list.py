#!/usr/bin/python3
"""Mylist class module"""


class MyList(list):
    """inherits List class"""

    def __init__(self):
        """intitialize class instances"""
        super().__init__()

    def print_sorted(self):
        """prints the list ordered in an ascending manner"""
        print(sorted(self))
