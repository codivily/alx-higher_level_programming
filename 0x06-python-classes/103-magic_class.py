#!/usr/bin/python3
"""The MagicClass module"""
import math


class MagicClass:
    """The MagicClass for circle"""

    def __init__(self, radius=0):
        """Initialize the radius"""
        if type(radius) not in [int, float]:
            raise TypeError('raise must be a number')
        self.__radius = radius

    def area(self):
        """Return the area of the circle"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Return the circumference of the circle"""
        return 2 * math.pi * self.__radius
