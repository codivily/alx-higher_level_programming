#!/usr/bin/python3
def uppercase(str):
    orda = ord('a')
    ordA = ord('A')
    ordz = ord('z')
    for c in str:
        c = ord(c)
        print('{:c}'.format(ordA + c - orda if (c >= orda and c <= ordz)
                            else c), end='')
    print('\n')
