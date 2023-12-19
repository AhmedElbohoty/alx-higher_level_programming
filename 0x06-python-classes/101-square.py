#!/usr/bin/python3
"""Create a class Square"""


class Square:
    """Used to create a square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """Create new instance

        Args:
            size: size of one side of square

        Attributes:
            size: size of one side of square
        """
        self.__size = size
        self.__position = position

    def area(self):
        """Returns the square area
        """
        return self.__size * self.__size

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

    @property
    def position(self):
        """Get the position of square
        """
        return self.__position

    @position.setter
    def position(self, pos):
        """Position setter.

        Args:
            pos (tuple): position of the square.

        Raises:
            TypeError: position must be a tuple of 2 positive integers
        """
        if not isinstance(pos, tuple) or len(pos) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(pos[0], int) or pos[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(pos[1], int) or pos[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = pos

    def my_print(self):
        """Prints in stdout the square with the character #.
        """
        size = self.__size
        pos = self.__position
        if size == 0:
            print("")
        else:
            for a in range(pos[1]):
                print()
            for b in range(size):
                for c in range(pos[0]):
                    print(' ', end='')
                for d in range(size):
                    print('#', end='')
                print()

    def __str__(self):
        """Prints in stdout the square with the character #.
        """
        res = ""
        size = self.__size
        pos = self.__position

        if size == 0:
            return res
        for y in range(pos[1]):
            res += '\n'
        for i in range(size):
            for x in range(pos[0]):
                res += ' '
            for j in range(size):
                res += '#'
            res += '\n'
        return res[: - 1]
