#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    t = 0
    n = 0
    for k, v in my_list:
        t += k * v
        n += v
    return (t / n)
