#!/usr/bin/pyhton3
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
        if type(width) is not int:
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
        if type(width) is not int:
            raise TypeError('with must be an integer')
        if width < 0:
            raise ValueError('with must be >= 0')
        self.__width = value

    def area(self):
        """ a method that returns the rectangle area"""
        if  self.__height == 0 or self.__width == 0:
            return 0
        return self.__height * self.__width


    def perimeter(self):
        """a method the returns the rectangle perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """ a magic method that prints the
            rectangle dimensions in # chars
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        shape = []
        for i in range(self.__height):
            for x in range(self.__width):
                shape.append('#')
            if i < self.__height - 1:
                shape.append('\n')
        shape = shape.join('')
        return shape

    def __repr__(self):
        """returns a string representation that can
           be re-evaluated using eval function
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)