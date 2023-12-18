#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    '''Prints the first x elements of a list and only integers.
    '''
    c = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except IndexError as ex:
            raise ex
        except (TypeError, ValueError):
            pass
        else:
            c += 1
    print("")
    return c
