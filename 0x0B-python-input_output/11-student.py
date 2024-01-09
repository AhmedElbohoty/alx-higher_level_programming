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

    def to_json(self, attrs=None):
        '''Returns a dictionary representation.

        Args:
            attrs (list of strings): the list of strings.

        Returns:
            dictionary representation.
        '''
        if type(attrs) != list:
            return self.__dict__

        ndict = {}
        for name in attrs:
            if type(name) != str:
                return self.__dict__

            if hasattr(self, name):
                ndict[name] = self.__dict__[name]

        return ndict

    def reload_from_json(self, json):
        '''Replaces all attributes of the Student instance

        Args:
            json (dict): The new attributes
        '''

        for key, value in json.items():
            setattr(self, key, value)
