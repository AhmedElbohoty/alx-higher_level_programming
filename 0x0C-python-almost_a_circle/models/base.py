#!/usr/bin/python3
'''Base Class:

The “base” class of all other classes in this project
'''
from json import dumps, loads
from os.path import isfile
import csv


class Base():
    '''The “base” class of all other classes in this project'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Manage id attribute in all future classes and
        to avoid duplicating ids

        - If id is not None, assign the public instance
          attribute id with this argument value.
        - Otherwise, increment __nb_objects and assign the
          new value to the public instance attribute id

        Args:
            1- id (int, optional): default is None.
        '''
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @classmethod
    def save_to_file(cls, list_objs):
        '''Writes an Object to a text file, using a JSON representation

        Args:
            list_objs (any): the object to be serialized.

        Steps:
            1- If list_objs is None, save empty list.
            2- Convert every instance into dictionary.
            3- Writes JSON representation to file.
        '''
        if list_objs is None:
            list_objs = []

        list_objs = [obj.to_dictionary() for obj in list_objs]

        filename = '{}.json'.format(cls.__name__)
        with open(filename, 'w', encoding='utf-8') as file_obj:
            file_obj.write(cls.to_json_string(list_objs))

    @classmethod
    def create(cls, **dictionary):
        '''Create an instance from dictionary

        Args:
            dictionary (dict): instance attributes.

        Steps:
            1- Get class name to check if it is square or rectangle.
            2- Create dummy instance.
            3- Update the instace with dictionary.

        Return:
            - instance
        '''
        name = cls.__name__
        instance = cls(1) if name == 'Square' else cls(1, 1)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        '''Create a list of instances.

        Steps:
            1- Load JSON representation from file <Class name>.json.
            2- If the file doesn’t exist, return an empty list.
            3- Writes JSON representation to file.
        '''
        name = cls.__name__
        file = '{}.json'.format(name)
        if not isfile(file):
            return []

        with open(file, 'r', encoding='utf-8') as file_obj:
            instances = []
            jsn = cls.from_json_string(file_obj.read())

            for d in jsn:
                instances.append(cls.create(**d))
            return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''Writes an Object to a csv file.

        Args:
            list_objs (any): the object.

        Steps:
            1- If list_objs is None, use empty list.
            2- Create rows.
            3- Writes rows to file.
        '''
        if list_objs is None:
            list_objs = []

        name = cls.__name__
        rows = []
        if name == 'Rectangle':
            for obj in list_objs:
                rows.append([obj.id, obj.width, obj.height, obj.x, obj.y])
        else:
            for obj in list_objs:
                rows.append([obj.id, obj.size, obj.x, obj.y])

        filename = '{}.csv'.format(name)
        with open(filename, 'w', newline='', encoding='utf-8') as file_obj:
            writer = csv.writer(file_obj)
            writer.writerows(rows)

    @classmethod
    def load_from_file_csv(cls):
        '''Loads object to csv file.'''
        ret = []

        name = cls.__name__
        filename = '{}.csv'.format(name)
        with open(filename, 'r', newline='', encoding='utf-8') as file_obj:
            reader = csv.reader(file_obj)
            for row in reader:
                row = [int(number) for number in row]
                if name == 'Rectangle':
                    id, width, height, x, y = row
                    d = {'id': id, 'width': width, 'height': height,
                         'x': x, 'y': y}
                else:
                    id, size, x, y = row
                    d = {'id': id, 'size': size,
                         'x': x, 'y': y}
                ret.append(cls.create(**d))
        return ret

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Create the JSON representation of dictionaries

        Args:
            list_dictionaries (list): list of dictionaries.

        Returns:
            str: The JSON representation of the dictionaries.
        '''
        if list_dictionaries is None:
            return '[]'
        if len(list_dictionaries) == 0:
            return '[]'
        return dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        '''Create dictionary from the JSON representation.

        Args:
            json_string (str): JSON representation of dictionary.

        Returns:
            dict: dictionary.
        '''
        if not json_string:
            return []
        return loads(json_string)
