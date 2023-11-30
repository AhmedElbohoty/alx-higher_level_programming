#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()

count = len(sys.argv) - 1
first_str = "{:d} "
if count == 1:
    first_str += "argument"
else:
    first_str += "arguments"

if count == 0:
    first_str += "."
else:
    first_str += ":"

print(first_str.format(count))

index = 0
for arg in sys.argv:
    if index != 0:
        print("{:d}: {:s}".format(index, arg))
    index += 1
