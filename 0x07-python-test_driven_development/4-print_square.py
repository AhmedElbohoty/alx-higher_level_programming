#!/usr/bin/python3
'''Module for printing a square with the character #

Functions:
    print_square
'''


def print_square(size):
    '''Prints a square with the character #.

    Args:
        size (int):is the size length of the square

     Raises:
        TypeError: if size is not an integer.
                   'size must be an integer'
        ValueError: if size is less than 0
                    'size must be >= 0'

    Returns:
        None
    '''
    if not isinstance(size, int):
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    for _ in range(size):
        for __ in range(size):
            print('#', end='')
        print('')


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
