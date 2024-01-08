#!/usr/bin/python3
'''Create Rectangle class that inherits from BaseGeometry
'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Rectangle class that inherits from BaseGeometry
    '''

    def __init__(self, width, height):
        '''Intialize Rectangle.

        Args:
            width (int): The rectangle width.
            height (int): The rectangle height.
        '''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''Calculate and return the area of the rectangle.'''
        return self.__width * self.__height

    def __str__(self):
        '''Return the representation of a Rectangle.'''
        cls_name = str(self.__class__.__name__)
        width = self.__width
        height = self.__height
        text = '[{}] {}/{}'.format(cls_name, width, height)
        return text
