#!/usr/bin/python3
'''Appends a string at the end of a text file (UTF8)
and returns the number of characters added
'''


def append_write(filename="", text=""):
    '''Appends a string at the end of a text file (UTF8)
    and returns the number of characters added

    Args:
        filename (str optional): the file name
        text (str optional): the text to be appended in file

    Returns:
        int: the number of appended characters
    '''
    if not filename:
        return

    with open(filename, 'a', encoding='utf-8') as file_obj:
        count = file_obj.write(text)
        return count
