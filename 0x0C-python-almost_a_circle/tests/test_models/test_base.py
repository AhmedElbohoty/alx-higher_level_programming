#!/usr/bin/python3
'''Unit tests for Base'''
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    '''Unit tests for Base'''

    def test_nb_objects_private(self):
        '''Check if nb_objects is private class attribute.'''
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_base_init_args(self):
        '''Check if Base works with args'''
        b = Base(12)
        self.assertEqual(b.id, 12)
        b = Base(4)
        self.assertEqual(b.id, 4)

    def test_base_init_no_args(self):
        '''Check if Base works with args'''
        b = Base()
        self.assertEqual(b.id, 1)
        b = Base(4)
        self.assertEqual(b.id, 4)
        b = Base()
        self.assertEqual(b.id, 2)


if __name__ == "__main__":
    unittest.main()
