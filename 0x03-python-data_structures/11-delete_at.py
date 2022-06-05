#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list is None or idx is None or idx < 0 or idx >= len(my_list):
        return (my_list)
    r = []
    for i in range(0, len(my_list)):
        if i != idx:
            r.append(my_list[i])
    return (r)
