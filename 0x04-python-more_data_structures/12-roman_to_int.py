#!/usr/bin/python3

def roman_to_int(roman_string):
    '''Converts a Roman numeral to an integer.
    '''

    if not isinstance(roman_string, str):
        return 0

    if not roman_string:
        return 0

    roman_symbols = [
        {"value": 1000, "symbol": "M"},
        {"value": 900, "symbol": "CM"},
        {"value": 500, "symbol": "D"},
        {"value": 400, "symbol": "CD"},
        {"value": 100, "symbol": "C"},
        {"value": 90, "symbol": "XC"},
        {"value": 50, "symbol": "L"},
        {"value": 40, "symbol": "XL"},
        {"value": 10, "symbol": "X"},
        {"value": 9, "symbol": "IX"},
        {"value": 5, "symbol": "V"},
        {"value": 4, "symbol": "IV"},
        {"value": 1, "symbol": "I"},
        ]

    string = roman_string
    res = 0
    for c in roman_symbols:
        if not string:
            break

        if not string.startswith(c["symbol"]):
            continue

        while string.startswith(c['symbol']):
            string = string[len(c["symbol"]):]
            res += c["value"]

    return res
