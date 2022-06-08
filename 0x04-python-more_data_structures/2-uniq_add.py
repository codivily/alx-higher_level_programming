#!/usr/bin/python3
def uniq_add(my_list=[]):
    r = 0
    for e in set(my_list):
        r += e
    return r
