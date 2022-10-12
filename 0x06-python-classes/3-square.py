#!/usr/bin/python3
""" defining a class."""

class Square:
    """ represents a square class."""
    def __init__(self, size=0):
        """ initialization a new squre:
        Args:
            size (int): the square size

        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")    
        self.__size = size
    def area(self):
        """calculates the area of the square
        Return: 
           the square area
        """

        return (self.__size) ** 2
