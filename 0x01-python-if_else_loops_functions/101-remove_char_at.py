#!/usr/bin/python3

def remove_char_at(str, n):
    '''Creates a copy of the string, removing the character at the position n.
    '''

    if n < 0:
        return str
    
    if n > len(str) - 1:
        return str

    res = ""
    for c in str:
        if c == str[n]:
            continue
        res += c

    return res
