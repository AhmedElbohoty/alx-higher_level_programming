#!/usr/bin/python3
'''BaseGeometry'''


class BaseGeometry():
    '''BaseGeometry class'''

    def area(self):
        '''Public instance method - Not implemented.'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Validate the value

        Args:
            name (str): the name
            value (int): integer greater than 0

        Raises:
            - TypeError: if value is not an integer
                         ('<name> must be an integer')
            - ValueError: if value is less or equal to 0
                          ('<name> must be greater than 0')
        '''
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/7-base_geometry.txt")
