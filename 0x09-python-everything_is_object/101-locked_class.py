#!/usr/bin/python3
"""This is the ``LockedClass`` module"""


class LockedClass:
    """The LockedClass"""
    def __setattr__(self, name, value):
        """Set attribute only if name == 'first_name'"""
        if type(name) is not str or name != 'first_name':
            msg = "'LockedClass' object has no attribute '{}'"
            raise AttributeError(msg.format(name))
        self.__dict__[name] = value
