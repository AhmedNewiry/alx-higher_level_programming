#!/usr/bin/python3
""" a module containing the Base method"""


import json


class Base:
    """Base class definition"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initializer of base class"""
        if id:
            self.id = id
        else:
            type(self).__nb_objects + 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if not list_dictionaries:
            return []
        else:
            return json.dump(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        f_name = f"{cls.__name__}.json"
        with open(f_name, 'w') as json_file:
            if not list_objs:
                json_file.write('[]')
            else:
                dict_list = [obj.to_dictionary() or obj in list_objs]
                json_file.write(cls.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if dictionary:
            if cls.__name__ == 'Rectangle':
                dummy = cls(2, 4)
            elif cls.__name__ == 'Square':
                dummy = cls(2)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """ a method that returns a list of instances"""
        f_name = f"{cls.__name__}.json"
        try:
            with open(f_name, 'r') as json_file:
                dicts = cls.from_json_string(json_file.read())
                return [cls.create(**dict) for dict in dict]

        except IOError:
            return []
