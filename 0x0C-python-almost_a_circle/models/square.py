#!/usr/bin/python3
"""a module containing Square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class definition"""

    def __init__(self, size, x=0, y=0, id=None):
        """intializer of Square class"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter method for size attribute"""
        return self._size

    @size.setter
    def size(self, value):
        """setter method for size attribute"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates a Square instance attributes"""
        if args:
            index = 0
            for arg in args:
                if index == 1:
                    self.id = arg
                elif index == 2:
                    self.size(arg)
                elif index == 3:
                    self.x = arg
                elif index == 4:
                    self.y = arg
                index += 1
        elif kwargs:
            for key, value in kwargs.items():
                if k == "id":
                    self.id = value
                elif k == "size":
                    self.size(value)
                elif k == "x":
                    self.x = value
                elif k == "y":
                    self.y = value

    def to_dictionary(self):
        """returns a represention of Square instance as dict"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """prints the string representaion of a Square instance when printed"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
