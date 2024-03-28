#!/usr/bin/python3
'''Write a function that finds a peak in a list of unsorted integers.'''


def find_peak(list_of_integers):
    '''Finds a peak in a list of unsorted integers.

    Args:
        list_of_integers (arr): list of unsorted integers
    '''
    ints = list_of_integers

    if not ints:
        return None
    if len(ints) == 0:
        return None

    left = 0
    right = len(ints) - 1

    while left < right:
        mid = left + (right - left) // 2

        if ints[mid] > ints[mid - 1] and ints[mid] > ints[mid + 1]:
            return ints[mid]

        if ints[mid - 1] > ints[mid + 1]:
            right = mid
            continue

        left = mid + 1

    return ints[left]
