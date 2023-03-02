#!/usr/bin/python3
"""a module containing Rectangle class"""


class Rectangle:
    """a class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """initializes instances of Rectangle class"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """getter of with property"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter of with property"""
        if not isinstance(width, int):
            raise TypeError('with must be an integer')
        if width < 0:
            raise ValueError('with must be >= 0')
        self.__width = value

    @property
    def height(self):
        """getter of height property"""
        return self.__width

    @height.setter
    def height(self, value):
        """setter for height property"""
        if not isinstance(width, int):
            raise TypeError('with must be an integer')
        if width < 0:
            raise ValueError('with must be >= 0')
        self.__width = value
