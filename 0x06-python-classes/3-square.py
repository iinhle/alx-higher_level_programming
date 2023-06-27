#!/usr/bin/python3
"""Defines a class Square"""

class Square:
    """Represnts a square"""

    def __init__(self, size=0):
        """Initializes a new square

        Args:
            size (int): Size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        elif size < 0:
            raise ValueError("Size must be >= 0")
        self.__size = size

    def area(self):
        """Returns Current area of the square."""
        return (self.__size * self.__size)
