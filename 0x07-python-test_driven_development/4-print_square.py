#!/usr/bin/python3
""" a module containing print square function"""


def print_square(size):
    """ a function that prints person name
    Args:
        first_name (str): person first name
        last_name (str): person last name
    Returns: None
    """
    if not type(size) is int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for x in range(size):
            print('#', end="")
        print("")
