#!/usr/bin/python3
'''Get the list of available attributes and methods of an object

Functions:
    lookup(obj)
'''


def lookup(obj):
    '''Get the list of available attributes and methods of an object

    Args:
        obj (obj)
    '''
    return dir(obj)
