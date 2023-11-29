#!/usr/bin/python3

def print_tebahpla():
    '''Prints the ASCII alphabet, in reverse order.

    alternating lowercase and uppercase
    '''
    for i in range(122, 96, -1):
        if i % 2 == 0:
            print("{}".format(chr(i)), end="")
        else:
            print("{}".format(chr(i - 32)), end="")


print_tebahpla()
