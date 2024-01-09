#!/usr/bin/python3
'''Reads a text file (UTF8) and prints it to stdout'''


def read_file(filename=""):
    '''Reads a text file (UTF8) and prints it to stdout

    Args:
        filename (str optional): the file name
    '''

    if not filename:
        return

    with open(filename, 'r', encoding="utf-8") as file_obj:
        content = file_obj.read()
        print(content, end='')
