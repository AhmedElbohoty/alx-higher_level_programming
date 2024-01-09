#!/usr/bin/python3
'''Create the JSON representation of an object (string)
'''
import json


def to_json_string(my_obj):
    '''Create the JSON representation of an object (string)

    Args:
        my_obj (any): the object to be serialized.

    Returns:
        str: The JSON representation of the object.
    '''
    return json.dumps(my_obj)
