#!/usr/bin/python3
class LockedClass:
    def __setattr__(self, name, value):
        if name != 'first_name':
            msg = "'LockedClass' object has no attribute '{}'"
            raise AttributeError(msg.format(name))
        self.__dict__[name] = value
