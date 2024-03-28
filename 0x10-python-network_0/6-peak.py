#!/usr/bin/python3
'''Write a function that finds a peak in a list of unsorted integers.'''


def find_peak(list_of_integers):
    '''Finds a peak in a list of unsorted integers.

    Args:
        list_of_integers (arr): list of unsorted integers
    '''

    if not list_of_integers:
        return None

    res = None

    for integer in list_of_integers:
        if res is None or res < integer:
            res = integer

    return res
