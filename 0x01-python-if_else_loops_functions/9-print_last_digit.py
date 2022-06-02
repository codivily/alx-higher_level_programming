#!/usr/bin/python3
def print_last_digit(number):
    digit = repr(number)[-1]
    ord_digit = ord(digit)
    if ord_digit >= ord('0') and ord_digit <= ord('9'):
        print("{:c}".format(ord_digit), end="")
    else:
        raise Exception("Invalid number")
    return (digit)
