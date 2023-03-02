#!/usr/bin/python3
"""Defines a clas square"""


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
        """a property setter"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """the current square area"""
        return (self.__size * self.__size)
