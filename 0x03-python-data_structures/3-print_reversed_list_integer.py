#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return
    text = ""
    for e in reversed(my_list[:]):
        text += "{:d}\n".format(e)
    print(text, end="")
