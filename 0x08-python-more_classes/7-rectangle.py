#!/usr/bin/python3
'''Defines a rectangle
'''


class Rectangle:
    '''Defines a rectangle.

    Class Attributes:
        number_of_instances: number of rectangles
    '''

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        '''
        Args:
            width (int, optional): width of rectangle.
            height (int, optional): height of rectangle.
        '''
        Rectangle.validate_width(width)
        Rectangle.validate_height(height)
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        '''Print the rectangle with the character #

        Note:
            if width or height equals zero return empty string
        '''
        if self.__width == 0 or self.__height == 0:
            return ''

        message = ''
        for i in range(self.__height):
            for _ in range(self.__width):
                message += Rectangle.print_symbol
            if i != self.height - 1:
                message += '\n'
        return message

    def __repr__(self):
        '''Create representation for Rectangle'''
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

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
        '''
        Rectangle.validate_width(value)
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
        '''
        Rectangle.validate_height(value)
        self.__height = value

    def area(self):
        '''Return the area of rectangle
        '''
        return self.__width * self.__height

    def perimeter(self):
        '''Return the perimeter of rectangle

        Note:
            if width or height is equal to 0, perimeter is equal to 0
        '''
        if self.__width == 0:
            return 0

        if self.__height == 0:
            return 0

        return 2 * (self.__width + self.__height)

    @staticmethod
    def validate_width(width):
        '''Validate rectangle width
        Raises:
            1- TypeError: if width is not integer.
            2- ValueError: if width is less than 0.
        '''
        if not isinstance(width, int):
            raise TypeError('width must be an integer')

        if width < 0:
            raise ValueError('width must be >= 0')

    @staticmethod
    def validate_height(height):
        '''Validate rectangle height
        Raises:
            1- TypeError: if height is not integer.
            2- ValueError: if height is less than 0.
        '''
        if not isinstance(height, int):
            raise TypeError('height must be an integer')

        if height < 0:
            raise ValueError('height must be >= 0')
