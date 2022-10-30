#!/usr/bin/python3
"""Defines the save_to__json_file function"""
import json


def save_to_json_file(my_obj, filename):
    """"Writes an Object to a text file, using a JSON representation."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
