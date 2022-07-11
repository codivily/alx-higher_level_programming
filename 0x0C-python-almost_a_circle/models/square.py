#!/usr/bin/python3
"""``Square`` class module"""

from .rectangle import Rectangle


class Square(Rectangle):
    """A class that represent a Square"""

    def __init__(self, size, x=0, y=0, _id=None):
        """Initialize the Square's instance.

            Args:
                size (int): The size of the Square
                x (int): The x position of the Square
                y (int): The y position of the Square
                _id (any): The id of the instance object
        """
        super().__init__(size, size, x, y, _id)

    def __str__(self):
        """Returns a string representation of the Square's instance"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Returns the size of the Square"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the `width` and `height` of the Square"""
        super(Square, self).width = value
        super(Square, self).height = value

    def update(self, *args, **kwargs):
        """Update the instance's attributes"""
        attrs = ("id", "size", "x", "y")
        if args:
            len_attrs = len(attrs)
            len_args = len(args)
            if len_args > len_attrs:
                msg = "update() takes at max {} positional arguments"\
                        " but {} were given"
                raise TypeError(msg.format(len_attrs, len_args))

            for i in range(min(len(attrs), len(args))):
                k = attrs[i]
                v = args[i]
                if k == 'size':
                    setattr(self, 'width', v)
                    setattr(self, 'height', v)
                else:
                    setattr(self, k, v)
        else:
            for k in kwargs:
                if k not in attrs:
                    msg = "update() got an unexpected keyword argument '{}'"
                    raise TypeError(msg.format(k))
                v = kwargs.get(k)
                if k == 'size':
                    setattr(self, 'width', v)
                    setattr(self, 'height', v)
                else:
                    setattr(self, k, v)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        d = {}
        d['id'] = self.id
        d['size'] = self.size
        d['x'] = self.x
        d['y'] = self.y
        return d
