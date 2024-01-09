#!/usr/bin/python3
'''Inserts a line of text to a file, after each line
   containing a specific string
'''


def append_after(filename='', search_string='', new_string=''):
    '''Inserts a line of text to a file, after each line
    containing a specific string.

    Args:
        filename (str): The file name.
        search_string (str): The string to search in line.
        new_string (str): The string to append.
    '''
    text = ''
    with open(filename, 'w+', encoding='utf-8') as file_obj:
        for line in file_obj:
            text += line
            if search_string in line:
                text += new_string

        file_obj.write(text)
