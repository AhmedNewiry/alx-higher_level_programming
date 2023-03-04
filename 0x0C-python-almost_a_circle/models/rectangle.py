#!/usr/bin/python3
"""a module containing Rectangle class"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class definition"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialilzer of Rectangle method"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter method for width private instance attribute"""
        return self.__width

    @width.setter
    def width(self, val):
        """setter method for width private instance attribute"""
        if type(val) is not int:
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @property
    def height(self):
        """getter method for height private instance attribute"""
        return self.__height

    @height.setter
    def height(self, val):
        """setter method for height private instance attribute"""
        if type(val) is not int:
            raise TypeError("height must be an integer")
        if val <= 0:
            raise valError("height must be > 0")
        self.__height = val

    @property
    def x(self):
        """getter method for x private instance attribute"""
        return self.__x

    @x.setter
    def x(self, val):
        """setter method for x private instance attribute"""
        if type(val) is not int:
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @property
    def y(self):
        """getter method for y private instance attribute"""
        return self.__y

    @y.setter
    def y(self, val):
        if type(val) is not int:
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")
        """setter method for y private instance attribute"""
        self.__y = val

    def area(self):
        """returns Rectangle instance area"""
        return self.width * self.height

    def display(self):
        """prints the Rectangle instance using '#' characters"""
        if self.width == 0 or self.height == 0:
            print("")
            return
        shape = []
        for i in range(self.height):
            for x in range(self.width):
                shape.append('#')
            if i < self.height - 1:
                shape.append('\n')
        shape = ('').join(shape)
        print(shape)

    def update(self, *args, **kwargs):
        """"updates Rectangle instance"""
        if args:
            index = 0
            for arg in args:
                if index == 0:
                    self.id = arg
                elif index == 1:
                    self.width = arg
                elif index == 2:
                    self.height = arg
                elif index == 3:
                    self.x = arg
                elif index == 4:
                    self.y = arg
                index += 1

        elif kwargs:
            for key, val in kwargs.items():
                if key == 'id':
                    self.id = val
                elif key == 'width':
                    self.width = val
                elif key == 'height':
                    self.height = val
                elif key == 'x':
                    self.x = val
                elif key == 'y':
                    self.y = val

    def to_dictionary(self):
        """returns a represention of Rectangle instance as dict"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """prints the string representaion of
        a Rectangle instance when printed"""
        return """[Rectangle] ({self.id}) {self.x}/{self.y}
                  - {self.width}/{self.height}"""
