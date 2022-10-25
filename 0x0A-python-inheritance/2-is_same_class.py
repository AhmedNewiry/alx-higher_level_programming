#!/usr/bin/python3
"""This module contains the is_same_class function"""


def is_same_class(obj, a_class):
    """Return true if obj is the exact class a_class, otherwise false
    """
    return (type(obj) == a_class)
