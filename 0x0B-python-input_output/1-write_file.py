#!/usr/bin/python3
'''Writes a string to a text file (UTF8) and
returns the number of characters written
'''


def write_file(filename="", text=""):
    '''Writes a string to a text file (UTF8) and
    returns the number of characters written

    Args:
        filename (str optional): the file name
        text (str optional): the text to be written in file

    Returns:
        int: the number of characters written
    '''

    if not filename:
        return

    with open(filename, 'w', encoding='utf-8') as file_obj:
        count = file_obj.write(text)
        return count
