#!/usr/bin/python3
"""add funtion module."""


def add_integer(a, b=98):
    """ a function that adds two integers
        Args: a (int): the first integer
              b (int): the second integer
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return (a + b)
