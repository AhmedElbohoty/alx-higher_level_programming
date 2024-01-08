#!/usr/bin/python3
'''Create a class MyList that inherits from list.

Functions:
    print_sorted
'''


class MyList(list):
    '''Class that inherits from list
    '''

    def print_sorted(self):
        '''Prints the list, but sorted (ascending sort).
        '''
        lst = self.copy()
        lst.sort()
        print(lst)
