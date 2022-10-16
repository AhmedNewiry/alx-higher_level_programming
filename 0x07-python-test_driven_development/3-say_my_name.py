#!/usr/bin/python3
""" a module containing say_my_name fucntion"""


def say_my_name(first_name, last_name=""):
    """ a function that prints person name
    Args:
        first_name (str): person first name
        last_name (str): person last name
    Returns: None
    """

    if not type(first_name) is str:
        raise TypeError("first_name must be a string")
    if not type(last_name) is str:
        raise TypeError("last_name must be a string")
    print(f"my name is {first_name} {last_name}")
