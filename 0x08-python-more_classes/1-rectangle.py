#!/usr/bin/python3
'''Defines a rectangle
'''


class Rectangle:
    '''Defines a rectangle.
    '''

    def __init__(self, width=0, height=0):
        '''
        Args:
            width (int, optional): width of rectangle.
            height (int, optional): height of rectangle.
        '''
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''int: return the width of rectangle.
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''Set the width of rectangle.

        Args:
           width (int, optional): width of rectangle.

        Raises:
            1- TypeError: if width is not integer.
            2- ValueError: if width is less than 0.
        '''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')

        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        '''int: return the height of rectangle.
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''Set the height of rectangle.

        Args:
           height (int, optional): height of rectangle.

        Raises:
            1- TypeError: if height is not integer.
            2- ValueError: if height is less than 0.
        '''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')

        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value
