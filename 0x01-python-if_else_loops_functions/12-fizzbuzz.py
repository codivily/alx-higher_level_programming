#!/usr/bin/python3
def fizzbuzz():
    for n in range(1, 101):
        mod3 = (n % 3 == 0)
        mod5 = (n % 5 == 0)
        if mod3 or mod5:
            if mod3:
                print("Fizz", end="")
            if mod5:
                print("Buzz", end="")
        else:
            print(n, end="")
        print(" ", end="")
