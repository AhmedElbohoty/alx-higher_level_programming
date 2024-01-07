#!/usr/bin/python3
'''Module for printing My name is <first name> <last name>

Functions:
    say_my_name
'''


def say_my_name(first_name, last_name=""):
    '''Prints My name is <first name> <last name>.

    Args:
        1- first_name (str): The first name
        2- last_name (str optional): The last name

    Raises:
        TypeError: if first_name is not string
                   'first_name must be a string'
        TypeError: if last_name is not string
                   'last_name must be a string'

    Returns:
        None
    '''
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')

    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    print('My name is {} {}'.format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
