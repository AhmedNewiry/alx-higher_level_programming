#!/usr/bin/python3
"""This module defines the from_json_string function"""
import json


def from_json_string(my_str):
    """returns an object (Python data structure)"""
    return json.loads(my_str)
