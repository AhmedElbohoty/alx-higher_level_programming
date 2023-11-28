#!/usr/bin/python3

def fizzbuzz():
    '''Prints the numbers from 1 to 100 separated by a space.

    For multiples of three print Fizz
    For multiples of five print Buzz
    For multiples of three and five print FizzBuzz
    '''

    for i in range(1, 101):
        res = i
        if i % 5 == 0 and i % 3 == 0:
            res = "FizzBuzz"
        elif i % 3 == 0:
            res = "Fizz"
        elif i % 5 == 0:
            res = "Buzz"

        print("{}".format(res), end=" ")
