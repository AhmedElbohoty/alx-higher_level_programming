#!/usr/bin/python3
'''Create Square class that inherits from Rectangle
'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Square class that inherits from Rectangle
    '''

    def __init__(self, size):
        '''Init a square.

        Args:
            size (int): The square size.
        '''
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size
