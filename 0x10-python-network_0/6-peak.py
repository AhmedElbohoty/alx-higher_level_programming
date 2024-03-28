#!/usr/bin/python3
'''Write a function that finds a peak in a list of unsorted integers.'''


def find_peak(list_of_integers):
    '''Finds a peak in a list of unsorted integers.

    Args:
        list_of_integers (arr): list of unsorted integers
    '''
    integers = list_of_integers

    if not integers:
        return None
    if len(integers) == 0:
        return None

    left = 0
    right = len(integers) - 1

    while left < right:
        mid = left + (right - left) // 2

        if integers[mid] > integers[mid - 1] and integers[mid] > integers[mid + 1]:
            return integers[mid]

        if integers[mid - 1] > integers[mid + 1]:
            right = mid
            continue

        left = mid + 1

    return integers[left]
