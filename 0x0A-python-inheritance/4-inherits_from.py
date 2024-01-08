#!/usr/bin/python3
'''Check if the object is an instance of a class that inherited
(directly or indirectly) from the specified class

Functions:
    inherits_from
'''


def inherits_from(obj, a_class):
    '''Check if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
        obj (any).
        a_classs (class type).

    Returns:
        - True: if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class.
        - False: else.
    '''
    if type(obj) == a_class:
        return False
    if issubclass(type(obj), a_class):
        return True
    return False
