#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    '''Prints all integers of a list, in reverse order.
    '''

    start = len(my_list) - 1
    end = -1
    for i in range(start, end, -1):
        print("{:d}".format(my_list[i]))
