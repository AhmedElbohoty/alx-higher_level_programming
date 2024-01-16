#!/usr/bin/python3
'''Create Square class that inherits from Rectangle
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Square class that inherits from Rectangle
    '''

    def __init__(self, size, x=0, y=0, id=None):
        '''Intialize Square

        Args:
            size (int): The square size.
            x (int, optional): The square x position - default is 0.
            y (int, optional): The square y position - default is 0.
            id (int, optional): default is None.
        '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Return the representation of a square.'''
        id = self.id
        width = self.width
        x = self.x
        y = self.y
        cls_name = str(self.__class__.__name__)
        text = '[{}] ({}) {}/{} - {}'.format(
            cls_name, id, x, y, width)
        return text

    @property
    def size(self):
        """Get the one side size of square
        """
        return self.width

    @size.setter
    def size(self, size):
        """Size setter

        Args:
            size (int): size of one side.
        """
        self.validate_integer('width', size)
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        '''Assigns an argument to each attribute

        Args:
            *args (tuple): the tuple of arguments.
            **kwargs (dict): the dictionary of arguments.
        '''
        attrs = ['id', 'size', 'x', 'y']
        if args:
            for idx, value in enumerate(args):
                if idx == 1:
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, attrs[idx], value)
        elif kwargs:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        '''Returns the dictionary representation of a Square.

        Returns:
            dict: square attributes.
        '''
        id = self.id
        size = self.width
        x = self.x
        y = self.y
        return {'id': id, 'size': size, 'x': x, 'y': y}
