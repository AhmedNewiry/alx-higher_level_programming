#!/usr/bin/python3



""" defining a class."""



class Square:




    """ represents a square class."""



    def __init__(self, size = 0):



        """ initialization a new squre:

        Args:

            size (int): the square size

        """  



        self.size = size



    @property    


    def size(self):


        """ size attribue getter

        Returns: the size attribute

        """



        return self.__size



    @size.setter



    def size(self, value):



        """ size attribue setter

        Args:

            value (int): the new size value

        """



        if not isinstance(value, int):



            raise TypeError("size must be an integer")



        elif value < 0:



            raise ValueError("size must be >= 0")  



        self.__size = value



    def area(self):



        """calculates the area of the square

        Return: the square area

        """



        return (self.__size) ** 2

    def my_print(self):

        """prints in stdout the square with the character #"""

        for i in range(self.__size):

            [print("#", end="") for i in range(self.__size)]

            print("")

        if (self.__size == 0):

            print("")
