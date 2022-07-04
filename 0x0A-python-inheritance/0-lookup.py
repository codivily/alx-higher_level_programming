#!/usr/bin/python3
"""The ``lookup`` module"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object"""
    return obj.__dict__
