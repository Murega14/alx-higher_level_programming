#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """Defines a square"""
    def __init__(self, size):
        """initializes a new square
        Args:
            size(int): the size of the new square"""
        self.__size = size

    @property
    def size(self):
        """Retrieves the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """sets the retrieved square"""
        if not isinstance(value, int):
            raise TypeError("size must be an int")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns current square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints the square in stdout"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
