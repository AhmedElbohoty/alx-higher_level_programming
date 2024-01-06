#!/usr/bin/python3
def magic_string():
    magic_string.duplicate = getattr(magic_string, 'duplicate', 0) + 1
    return ", ".join(["BestSchool" for _ in range(magic_string.duplicate)])
