#!/usr/bin/python3
import dis

def magic_calculation(a, b):
    '''magic_calculation
    '''
    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)
        for n in range(4, 6):
            c = add(c, n)
        return c
    else:
        return sub(a, b)

dis.dis(magic_calculation)