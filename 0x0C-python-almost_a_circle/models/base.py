#!/usr/bin/python3
"""``Base`` class module"""


class Base:
    """Base of all classes in this project"""

    __nb_objects = 0

    def __init__(self, _id=None):
        """Sets private attributes and id fields

            Args:
                _id (int): A integer
        """
        if _id is None:
            Base.__nb_objects += 1
            self.id = Base._nb_objects
        else:
            self.id = _id
