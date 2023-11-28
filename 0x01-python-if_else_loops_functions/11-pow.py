#!/usr/bin/python3

def pow(a, b):
    '''Computes a to the power of b and return the value.
    '''

    if b == 0:
        return 1

    sign = -1 if b < 0 else 1
    res = 1
    b = abs(b)
    while b != 0:
        res *= a
        b -= 1

    if sign < 0:
        return 1 / res
    return res
