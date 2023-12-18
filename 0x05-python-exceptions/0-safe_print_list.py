#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    '''Prints x elements of a list.
    '''
    i = 0
    while i < x:
        try:
            end = "\n" if i == x - 1 else ""
            print("{}".format(my_list[i]), end=end)
            i += 1
        except Exception:
            break

        finally:
            print("")

    return i
