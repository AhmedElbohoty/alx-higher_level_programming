#!/usr/bin/python3

def magic_calculation(a, b, c):
    ''' magic_calculation
    '''
    if a < b:
        return c
    elif c > b:
        return a + b

    return a * b - c
