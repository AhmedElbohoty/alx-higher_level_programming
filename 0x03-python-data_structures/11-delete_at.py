#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    '''Deletes the item at a specific position in a list
    '''
    if idx < 0:
        return my_list

    if idx >= len(my_list):
        return my_list

    arr = []
    for i, x in enumerate(my_list):
        if i != idx:
            arr.append(x)

    return arr
