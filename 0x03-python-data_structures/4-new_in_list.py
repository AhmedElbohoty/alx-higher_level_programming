#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    '''Replaces an element in a list at a specific position
       without modifying the original list (like in C).
    '''
    arr = []
    for i in my_list:
        arr.append(i)

    if idx < 0:
        return arr

    if idx >= len(arr):
        return arr

    my_list[idx] = element

    return arr
