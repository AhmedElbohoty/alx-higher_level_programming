#!/usr/bin/python3
"""Create a class Square"""


class Square:
    """Used to create a square.
    """
    def __init__(self, size=0):
        """Create new instance

        Args:
            size: size of one side of square

        Attributes:
            size: size of one side of square
        """
        self.__size = size

    def area(self):
        """Calculate the square area
        """
        return self.__size ** 2

    @property
    def size(self):
        """Get the one side size of square
        """
        return self.__size

    @size.setter
    def size(self, size):
        """Size setter

        Args:
            size (int): size of one side.

        Raises:
            ValueError: size must be >= 0
            TypeError: size must be an integer
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
