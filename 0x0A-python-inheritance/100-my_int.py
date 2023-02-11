#!/usr/bin/python3
"""a module for MyInt class"""


class MyInt(int):
    """a subclass for int class"""

    def __eq__(self, num):
        """inverts == behavior"""
        return self.real != num

    def __ne__(self, num):
        """inverts != behavior"""
        return self.real == num