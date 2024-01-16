#!/usr/bin/python3
'''Unit tests for Base'''
import unittest
from models.base import Base
from models.square import Square


class TestBase(unittest.TestCase):
    '''Unit tests for Square'''

    def setUp(self):
        '''Reset __nb_objects'''
        Base._Base__nb_objects = 0

    def test_is_subclass(self):
        '''Test if Square is subclasses of Base'''
        self.assertTrue(issubclass(Square, Base))

    def test_class_type(self):
        '''Test Square class type'''
        self.assertEqual(str(Square),
                         "<class 'models.square.Square'>")

    def test_init_no_args(self):
        '''Create square without args'''
        msg = "__init__() missing 1 required positional argument:"
        msg += " 'size'"
        with self.assertRaises(TypeError) as err:
            Square()

        self.assertEqual(str(err.exception), msg)

    def test_invalid_width_height_args(self):
        '''Test invalid width and height'''

        msg = 'width must be > 0'
        with self.assertRaises(ValueError) as err:
            Square(0)

        self.assertEqual(str(err.exception), msg)

        msg = 'width must be an integer'
        with self.assertRaises(TypeError) as err:
            Square('1')

        self.assertEqual(str(err.exception), msg)

    def test_no_xy(self):
        '''Create square with optional x and y'''
        s = Square(1, 4)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.y, 0)

    def test_xy(self):
        '''Create square with optional x and y'''
        s = Square(1, 7)
        self.assertEqual(s.x, 7)
        self.assertEqual(s.y, 0)

        s = Square(1, 7, 9)
        self.assertEqual(s.x, 7)
        self.assertEqual(s.y, 9)

    def test_invalid_x_y_args(self):
        '''Test invalid x and y'''

        msg = 'x must be >= 0'
        with self.assertRaises(ValueError) as err:
            Square(1, -9)

        self.assertEqual(str(err.exception), msg)

        msg = 'y must be >= 0'
        with self.assertRaises(ValueError) as err:
            Square(1, 4, -9)

        self.assertEqual(str(err.exception), msg)

        msg = 'x must be an integer'
        with self.assertRaises(TypeError) as err:
            Square(1, '9')

        self.assertEqual(str(err.exception), msg)

        msg = 'y must be an integer'
        with self.assertRaises(TypeError) as err:
            Square(1, 9, '6')

        self.assertEqual(str(err.exception), msg)

    def test_area(self):
        '''Test square area'''
        s = Square(3)
        self.assertEqual(s.area(), 9)

    def test___str__(self):
        '''Test __str__ method'''
        s = Square(4, 2, 1, 12)
        msg = '[Square] (12) 2/1 - 4'
        self.assertEqual(str(s), msg)
        s = Square(5, 1)
        msg = '[Square] (1) 1/0 - 5'
        self.assertEqual(str(s), msg)

    def test_update(self):
        '''Test update method'''

        s = Square(10, 10, 10)
        msg = '[Square] (1) 10/10 - 10'
        self.assertEqual(str(s), msg)

        s.update(89, 2)
        msg = '[Square] (89) 10/10 - 2'
        self.assertEqual(str(s), msg)

        s.update(89, 3, 4, 5)
        msg = '[Square] (89) 4/5 - 3'
        self.assertEqual(str(s), msg)


if __name__ == '__main__':
    unittest.main()
