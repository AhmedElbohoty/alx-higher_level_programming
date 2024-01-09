#!/usr/bin/python3
'''class MyInt that inherits from int'''


class MyInt(int):
    '''Class MyInt that inherits from int'''

    def __eq__(self, value):
        '''Reverse equal method'''
        return self.real != value

    def __ne__(self, value):
        '''Reverse not equal method'''
        return self.real == value
