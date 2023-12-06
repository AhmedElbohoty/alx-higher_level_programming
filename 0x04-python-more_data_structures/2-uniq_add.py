#!/usr/bin/python3

def uniq_add(my_list=[]):
    '''Adds all unique integers in a list (only once for each integer).
    '''
    res = 0
    dup = []
    for num in my_list:
        if num in dup:
            continue
        dup.append(num)
        res += num

    return res
