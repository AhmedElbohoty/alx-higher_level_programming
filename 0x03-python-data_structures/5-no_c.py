#!/usr/bin/python3

def no_c(my_string):
    '''Removes all characters c and C from a string
    '''
    res = ""
    for char in my_string:
        if char != "c" and char != "C":
            res += char

    return res
