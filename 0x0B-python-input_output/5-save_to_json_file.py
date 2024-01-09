#!/usr/bin/python3
'''Writes an Object to a text file, using a JSON representation
'''
import json


def save_to_json_file(my_obj, filename):
    '''Writes an Object to a text file, using a JSON representation

    Args:
        my_obj (any): the object to be serialized.
        filename (str): the filename
    '''

    if not filename:
        return

    with open(filename, 'w', encoding='utf-8') as file_obj:
        jsn = json.dumps(my_obj)
        file_obj.write(jsn)
