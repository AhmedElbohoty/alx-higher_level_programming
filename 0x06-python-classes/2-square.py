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
        self.__size = self.__is_size_valid(size)

    def __is_size_valid(self, size):
        """Check if size is a valid square size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            return size
