#!/usr/bin/python3
def fizzbuzz():
    for n in range(1, 101):
        print("Fizz" if n % 3 == 0 else ("Buzz" if n % 5 == 0 else n), end=" ")
