#!/usr/bin/python3
def print_last_digit(number):
    number = repr(number)
    number = (number[-1] if len(number) > 0 else "")
    print(number, end="")
    return (number)
