#!/usr/bin/python3
import dis

def magic_calculation(a, b):
    '''magic_calculation
    '''
    from magic_calculation_102 import add as add, sub as sub
    
    if a < b:
        c = add(a, b)
    else:
        return sub(a, b)

dis.dis(magic_calculation)