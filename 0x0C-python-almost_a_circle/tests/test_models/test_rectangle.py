#!/usr/bin/python3
'''Unit tests for Base'''
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    '''Unit tests for Rectangle'''

    def setUp(self):
        '''Reset __nb_objects'''
        Base._Base__nb_objects = 0

    def test_is_subclass(self):
        '''Test if Rectangel is subclasses of Base'''
        self.assertTrue(issubclass(Rectangle, Base))

    def test_class_type(self):
        '''Test Rectangle class type'''
        self.assertEqual(str(Rectangle),
                         "<class 'models.rectangle.Rectangle'>")

    def test_init_no_args(self):
        '''Create rectangle without args'''
        msg = "__init__() missing 2 required positional arguments:"
        msg += " 'width' and 'height'"
        with self.assertRaises(TypeError) as err:
            Rectangle()

        self.assertEqual(str(err.exception), msg)

    def test_init_no_height_arg(self):
        '''Create rectangle without height arg'''
        msg = '__init__() missing 1 required positional argument:'
        msg += " 'height'"
        with self.assertRaises(TypeError) as err:
            Rectangle(1)

        self.assertEqual(str(err.exception), msg)

    def test_invalid_width_height_args(self):
        '''Test invalid width and height'''

        msg = 'width must be > 0'
        with self.assertRaises(ValueError) as err:
            Rectangle(0, 0)

        self.assertEqual(str(err.exception), msg)

        msg = 'height must be > 0'
        with self.assertRaises(ValueError) as err:
            Rectangle(2, 0)

        self.assertEqual(str(err.exception), msg)

        msg = 'width must be an integer'
        with self.assertRaises(TypeError) as err:
            Rectangle('1', 1)

        self.assertEqual(str(err.exception), msg)

        msg = 'height must be an integer'
        with self.assertRaises(TypeError) as err:
            Rectangle(2, '0')

        self.assertEqual(str(err.exception), msg)

    def test_no_xy(self):
        '''Create rectangle with optional x and y'''
        r = Rectangle(1, 4)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_xy(self):
        '''Create rectangle with optional x and y'''
        r = Rectangle(1, 4, 7)
        self.assertEqual(r.x, 7)
        self.assertEqual(r.y, 0)

        r = Rectangle(1, 4, 7, 9)
        self.assertEqual(r.x, 7)
        self.assertEqual(r.y, 9)

    def test_invalid_x_y_args(self):
        '''Test invalid x and y'''

        msg = 'x must be >= 0'
        with self.assertRaises(ValueError) as err:
            Rectangle(1, 1, -9)

        self.assertEqual(str(err.exception), msg)

        msg = 'y must be >= 0'
        with self.assertRaises(ValueError) as err:
            Rectangle(1, 1, 4, -9)

        self.assertEqual(str(err.exception), msg)

        msg = 'x must be an integer'
        with self.assertRaises(TypeError) as err:
            Rectangle(1, 1, '9')

        self.assertEqual(str(err.exception), msg)

        msg = 'y must be an integer'
        with self.assertRaises(TypeError) as err:
            Rectangle(1, 1, 9, '6')

        self.assertEqual(str(err.exception), msg)

    def test_area(self):
        '''Test rectangle area'''
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test___str__(self):
        '''Test __str__ method'''
        r = Rectangle(4, 6, 2, 1, 12)
        s = '[Rectangle] (12) 2/1 - 4/6'
        self.assertEqual(str(r), s)
        r = Rectangle(5, 5, 1)
        s = '[Rectangle] (1) 1/0 - 5/5'
        self.assertEqual(str(r), s)

    def test_update(self):
        '''Test update method'''

        r = Rectangle(10, 10, 10, 10)
        msg = '[Rectangle] (1) 10/10 - 10/10'
        self.assertEqual(str(r), msg)

        r.update(89, 2)
        msg = '[Rectangle] (89) 10/10 - 2/10'
        self.assertEqual(str(r), msg)

        r.update(89, 2, 3, 4, 5)
        msg = '[Rectangle] (89) 4/5 - 2/3'
        self.assertEqual(str(r), msg)


if __name__ == '__main__':
    unittest.main()
