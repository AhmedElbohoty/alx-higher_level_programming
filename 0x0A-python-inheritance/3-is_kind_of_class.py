#!/usr/bin/python3
'''Check if the object is an instance of, or if the object is an instance of
a class that inherited from, the specified class

Functions:
    is_kind_of_class
'''


def is_kind_of_class(obj, a_class):
    '''Check if the object is an instance of, or if the object
    is an instance of a class that inherited from, the specified class

    Args:
        obj (any)
        a_classs (class type)

    Returns:
        - True if the object is an instance of, or if the object
        is an instance of a class that inherited from, the specified class
        - Else, returns False
    '''

    if isinstance(obj, a_class):
        return True

    return False
