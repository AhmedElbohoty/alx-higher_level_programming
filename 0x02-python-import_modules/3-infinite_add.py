#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()

index = 0
res = 0
for num in sys.argv:
    if index != 0:
        res += int(num)
    index += 1

print("{:d}".format(res))
