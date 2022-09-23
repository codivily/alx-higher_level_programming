#!/usr/bin/python3
"""A module for the find_peak function"""


def find_peak(list_of_integers):
    """Finds a peak in alist of unsorted integers"""
    if not list_of_integers:
        return None
    x = 1
    stop = len(list_of_integers) - 1
    while x < stop:
        left = list_of_integers[x - 1]
        peak = list_of_integers[x]
        right = list_of_integers[x + 1]

        if left < peak and right < peak:
            return peak
        x += 1

    return peak
