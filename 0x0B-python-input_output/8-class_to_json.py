#!/usr/bin/python3
'''Creates the dictionary description with simple data structure
(list, dictionary, string, integer and boolean) for
JSON serialization of an object
'''


def class_to_json(obj):
    '''Creates the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for
    JSON serialization of an object

    Args:
        obj (type): class

    Returns:
        dictionary
    '''
    return obj.__dict__
