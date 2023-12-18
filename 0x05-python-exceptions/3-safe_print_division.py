#!/usr/bin/python3
def safe_print_division(a, b):
    '''Divides 2 integers and prints the result.
    '''
    res = None
    try:
        res = a / b
    except Exception:
        pass
    finally:
        print("Inside result: {}".format(res))
