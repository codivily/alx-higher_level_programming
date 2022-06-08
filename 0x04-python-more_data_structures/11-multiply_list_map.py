#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    return [my_list[0] * number] + (my_list if not my_list else multiply_list_map(my_list[1:], number))
