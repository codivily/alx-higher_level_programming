#!/usr/bin/python3
"""A module for the find_peak function"""


def find_peak(list_of_integers):
    """Finds a peak in alist of unsorted integers"""
    if not list_of_integers:
        return None
    stop = len(list_of_integers) - 1
    for x in range(1, stop):
        if list_of_integers[x] > list_of_integers[x - 1]:
            if list_of_integers[x] > list_of_integers[x + 1]:
                return list_of_integers[x]
    return list_of_integers[x]
