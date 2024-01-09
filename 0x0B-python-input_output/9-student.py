#!/usr/bin/python3
'''Student class'''


class Student:
    '''Class Student that defines a student props and methods
    '''

    def __init__(self, first_name, last_name, age):
        '''Init the instance.

        Args:
            first_name (str): the first name.
            last_name (int): the last name.
            age (int): the age.
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''Returns a dictionary representation.

        Returns:
            dictionary representation
        '''
        return self.__dict__
