#!/usr/bin/python3
"""a module containing add_attribure function"""


def add_attribute(obj, attr, value):
    """Add a new attribute to an object if possible"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
