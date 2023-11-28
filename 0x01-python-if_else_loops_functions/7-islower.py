#!/usr/bin/python3

def islower(c):
    '''checks for lowercase character

    Returns True if c is lowercase, else returns False
    '''
    code = ord(c)
    if code >= 97 and code <= 122:
        return True
    return False
