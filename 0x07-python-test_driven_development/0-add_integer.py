#!/usr/bin/python3
'''Module for adding two integers

Functions:
    add_integer
'''


def add_integer(a, b=98):
    '''Adds 2 integers

    Args:
        1- a (int): first integer.
        2- b (int optional): second integer (default value is 98).

    Raises:
        TypeError: if a or b must be integers or floats with message
                   'a must be an integer' or 'b must be an integer'

    Returns:
        returns the result of adding a and b
    '''

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
