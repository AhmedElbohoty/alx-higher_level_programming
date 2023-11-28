#!/usr/bin/python3

def uppercase(c):
    '''Prints a string in uppercase followed by a new line.
    '''
    for s in c:
        char = s if not islower(s) else chr(ord(s) - 32)
        print("{}".format(char), end="")
    print("")


def islower(c):
    '''checks for lowercase character

    Returns True if c is lowercase, else returns False
    '''
    code = ord(c)
    if code >= 97 and code <= 122:
        return True
    return False
