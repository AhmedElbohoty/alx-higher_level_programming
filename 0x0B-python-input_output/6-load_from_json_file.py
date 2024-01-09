#!/usr/bin/python3
'''Creates an Object from a “JSON file”
'''
import json


def load_from_json_file(filename):
    '''Creates an Object from a “JSON file”

    Args:
        filename (str): the JSON filename
    '''

    if not filename:
        return

    with open(filename, 'r', encoding='utf-8') as file_obj:
        content = file_obj.read()
        return json.loads(content)
