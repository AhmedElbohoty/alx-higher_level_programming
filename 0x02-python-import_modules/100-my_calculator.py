#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ != "__main__":
    exit()

args = sys.argv

if len(args) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)

a = int(args[1])
operator = args[2]
b = int(args[3])

if operator not in "+-*/":
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)

res = 0
if operator == "+":
    res = add(a, b)
elif operator == "-":
    res = sub(a, b)
elif operator == "*":
    res = mul(a, b)
elif operator == "/":
    res = div(a, b)

print("{:d} {:s} {:d} = {:d}".format(a, operator, b, res))
