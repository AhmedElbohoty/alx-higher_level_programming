#!/usr/bin/python3

def weight_average(my_list=[]):
    '''Returns the weighted average of all integers tuple (<score>, <weight>).
    '''

    if len(my_list) == 0:
        return 0

    s = 0
    w = 0
    for t in my_list:
        a, b = t
        s += a * b
        w += b

    return s / w
