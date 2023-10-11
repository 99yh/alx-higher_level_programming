#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str:
        return 0
    numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M': 1000}
    num = 0
    before = 0
    for c in roman_string.upper():
        if c in numerals:
            if before < numerals[c]:
                num -= before * 2
            before = numerals[c]
            num += before
        else:
            return 0
    return num
