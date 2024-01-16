#!/usr/bin/python3
'''Create Rectangle class that inherits from Base
'''
from models.base import Base


class Rectangle(Base):
    '''Create Rectangle class that inherits from Base
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Intialize Rectangle.

        Note:
            Call the Base class with id.

        Args:
            width (int): The rectangle width.
            height (int): The rectangle height.
            x (int, optional): The rectangle x position - default is 0.
            y (int, optional): The rectangle y position - default is 0.
            id (int, optional): default is None.
        '''
        super().__init__(id)

        self.validate_integer('width', width)
        self.width = width
        self.validate_integer('height', height)
        self.height = height
        self.validate_integer('x', x, zero=False)
        self.x = x
        self.validate_integer('y', y, zero=False)
        self.y = y

    def __str__(self):
        '''Return the representation of a Rectangle.'''
        id = self.id
        width = self.width
        height = self.height
        x = self.x
        y = self.y
        cls_name = str(self.__class__.__name__)
        text = '[{}] ({}) {}/{} - {}/{}'.format(
            cls_name, id, x, y, width, height)
        return text

    @property
    def width(self):
        '''int: return the width of rectangle.
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''Set the width of rectangle.

        Args:
           width (int): width of rectangle.
        '''
        self.validate_integer('width', value)
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
           height (int): height of rectangle.
        '''
        self.validate_integer('height', value)
        self.__height = value

    @property
    def x(self):
        '''int: return the x position of rectangle.
        '''
        return self.__x

    @x.setter
    def x(self, value):
        '''Set the x position of rectangle.

        Args:
           x (int): The x position of rectangle.
        '''
        self.validate_integer('x', value, zero=False)
        self.__x = value

    @property
    def y(self):
        '''int: return the y position of rectangle.
        '''
        return self.__y

    @y.setter
    def y(self, value):
        '''Set the y position of rectangle.

        Args:
           y (int): The y position of rectangle.
        '''
        self.validate_integer('y', value, zero=False)
        self.__y = value

    def area(self):
        '''Calculate and return the area of the rectangle.'''
        return self.__width * self.__height

    def display(self):
        '''Prints in stdout the Rectangle instance with the character #.
        '''
        x = self.x
        y = self.y
        width = self.width
        height = self.height\

        for __ in range(y):
            print()
        for __ in range(height):
            for c in range(width + x):
                if c < x:
                    print(' ', end='')
                else:
                    print('#', end='')
            print('')

    def update(self, *args, **kwargs):
        '''Assigns an argument to each attribute

        Args:
            *args (tuple): the tuple of arguments.
            **kwargs (dict): the dictionary of arguments.
        '''
        attrs = ['id', 'width', 'height', 'x', 'y']
        if args:
            for idx, value in enumerate(args):
                setattr(self, attrs[idx], value)
        elif kwargs:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        '''Returns the dictionary representation of a Rectangle.

        Returns:
            dict: rectangle attributes.
        '''
        id = self.id
        width = self.width
        height = self.height
        x = self.x
        y = self.y
        return {'id': id, 'width': width, 'height': height, 'x': x, 'y': y}

    @staticmethod
    def validate_integer(name, value, zero=True):
        '''Validate input value

        Raises:
            1- TypeError: if value is not integer.
            2- ValueError: - If zero=True, value is less than or equal 0.
                           - If zero=False, value is less than 0.
        '''
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))

        if not zero and value < 0:
            raise ValueError('{} must be >= 0'.format(name))

        if zero and value <= 0:
            raise ValueError('{} must be > 0'.format(name))
