#!/usr/bin/python3
''' function that adds a new attribute to an object if it’s possible'''


def add_attribute(obj, attribute, value):
    ''' function that adds a new attribute to an object if it’s possible.

    Args:
        obj (any): The new object.
        attribute (str): The attribute's name.
        value (any): The attribute's value.

    Raises:
        TypeError: Attribute cannot be added.
                   ('can't add new attribute')
    '''
    if not hasattr(obj, '__dict__'):
        raise TypeError('can\'t add new attribute')

    setattr(obj, attribute, value)
