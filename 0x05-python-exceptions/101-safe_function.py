#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    '''Executes a function safely.
    '''
    res = None
    try:
        res = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)

    return res
