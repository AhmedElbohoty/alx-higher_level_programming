#!/usr/bin/python3

def best_score(a_dictionary):
    '''Returns a key with the biggest integer value.
    '''

    if not a_dictionary:
        return None
    
    if len(a_dictionary) == 0:
        return None

    res = list(a_dictionary.keys())[0]
    for k, v in a_dictionary.items():
        if v > a_dictionary[res]:
            res = k

    return res
