ng a class."""







class Square:





    """ represents a square class."""







    def __init__(self, size = 0, position = (0, 0)):



        """ initialization a new squre:

        Args:

            size (int): the square size

        """  



        self.size = size

        self.position = position



    @property    



    def size(self):



        """ size attribue getter

        Returns: the size attribute

        """



        return self.__size

    @property    



    def position(self):



        """ position attribue getter

        Returns: the position attribute

        """



        return self.__position







    @position.setter







    def position(self, value):



        """ position attribue setter

        Args:

            value (int): the new postion value

        """

        for item in value:

            if not isinstance(item, int) and not isinstance(value, tuple) and item > 0:

                raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value        

     

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

            [print(" ", end="") for x in range(self.__position[1])]

            [print("#", end="") for y in range(self.__size)]

            print("")

        if (self.__size == 0):

            print("")
