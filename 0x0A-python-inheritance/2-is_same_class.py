#!/usr/bin/python3
'''Check if the object is exactly an instance of the specified class

Functions:
    is_same_class
'''


def is_same_class(obj, a_class):
    '''Check if the object is exactly an instance of the specified class

    Args:
        obj (any)
        a_classs (class type)

    Returns:
        - True if the object is exactly an instance of the specified class
        - Else, returns False
    '''

    if type(obj) == a_class:
        return True

    return False
